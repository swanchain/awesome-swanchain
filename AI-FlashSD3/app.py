import random
import spaces

import gradio as gr
import numpy as np
import torch
from diffusers import StableDiffusion3Pipeline, SD3Transformer2DModel, FlashFlowMatchEulerDiscreteScheduler
from peft import PeftModel
import os
from huggingface_hub import snapshot_download

huggingface_token = os.getenv("HUGGINFACE_TOKEN")

model_path = snapshot_download(
    repo_id="stabilityai/stable-diffusion-3-medium", 
    revision="refs/pr/26",
    repo_type="model", 
    ignore_patterns=["*.md", "*..gitattributes"],
    local_dir="stable-diffusion-3-medium",
    token=huggingface_token, # type a new token-id.
    )

device = "cuda" if torch.cuda.is_available() else "cpu"
IS_SPACE = os.environ.get("SPACE_ID", None) is not None

transformer = SD3Transformer2DModel.from_pretrained(
    model_path,
    subfolder="transformer",
    torch_dtype=torch.float16,
)
transformer = PeftModel.from_pretrained(transformer, "jasperai/flash-sd3")


if torch.cuda.is_available():
    torch.cuda.max_memory_allocated(device=device)
    pipe = StableDiffusion3Pipeline.from_pretrained(
        model_path,
        transformer=transformer,
        torch_dtype=torch.float16,
        text_encoder_3=None,
        tokenizer_3=None,
    )

    pipe = pipe.to(device)
else:
    pipe = StableDiffusion3Pipeline.from_pretrained(
        model_path,
        transformer=transformer,
        torch_dtype=torch.float16,
        text_encoder_3=None,
        tokenizer_3=None,
    )
    pipe = pipe.to(device)


pipe.scheduler = FlashFlowMatchEulerDiscreteScheduler.from_pretrained(
  model_path,
  subfolder="scheduler",
)

MAX_SEED = np.iinfo(np.int32).max
MAX_IMAGE_SIZE = 1024
NUM_INFERENCE_STEPS = 4


@spaces.GPU
def infer(prompt, seed, randomize_seed, guidance_scale, num_inference_steps, negative_prompt, progress=gr.Progress(track_tqdm=True)):
    if randomize_seed:
        seed = random.randint(0, MAX_SEED)

    generator = torch.Generator().manual_seed(seed)

    image = pipe(
        prompt=prompt,
        guidance_scale=guidance_scale,
        num_inference_steps=num_inference_steps,
        generator=generator,
        negative_prompt=negative_prompt
    ).images[0]

    return image


examples = [
    "The image showcases a freshly baked bread, possibly focaccia, with rosemary sprigs and red pepper flakes sprinkled on top. It's sliced and placed on a wire cooling rack, with a bowl of mixed peppercorns beside it.",
    'a 3D render of a wizard raccoon holding a sign saying "SD 3" with a magic wand.',
    "A panda reading a book in a lush forest.",
    "A raccoon trapped inside a glass jar full of colorful candies, the background is steamy with vivid colors",
    "Pirate ship sailing on a sea with the milky way galaxy in the sky and purple glow lights",
    "a cute cartoon fluffy rabbit pilot walking on a military aircraft carrier, 8k, cinematic",
    "A 3d render of a futuristic city with a giant robot in the middle full of neon lights, pink and blue colors",
    "A close up of an old elderly man with green eyes looking straight at the camera",
    "photo of a huge red cat with green eyes sitting on a cloud in the sky, looking at the camera"
]

css = """
#col-container {
    margin: 0 auto;
    max-width: 512px;
}
"""

if torch.cuda.is_available():
    power_device = "GPU"
else:
    power_device = "CPU"

with gr.Blocks(css=css) as demo:
    with gr.Column(elem_id="col-container"):
        gr.Markdown(
            f"""
        # ⚡ Flash Diffusion: FlashSD3 ⚡
        This is an interactive demo of [Flash Diffusion](https://gojasper.github.io/flash-diffusion-project/), a diffusion distillation method proposed in [Flash Diffusion: Accelerating Any Conditional
        Diffusion Model for Few Steps Image Generation](http://arxiv.org/abs/2406.02347) *by Clément Chadebec, Onur Tasar, Eyal Benaroche and Benjamin Aubin* from Jasper Research.
        [This model](https://huggingface.co/jasperai/flash-sd3) is a **90.4M** LoRA distilled version of [SD3](https://huggingface.co/stabilityai/stable-diffusion-3-medium) model that is able to generate 1024x1024 images in **4 to 8 steps**.
        Results can be compared with the teacher model [here](https://huggingface.co/spaces/stabilityai/stable-diffusion-3-medium).
        Currently running on {power_device}.
        """
        )
        gr.Markdown(
            "If you enjoy the space, please also promote *open-source* by giving a ⭐ to the <a href='https://github.com/gojasper/flash-diffusion' target='_blank'>Github Repo</a>. [![GitHub Stars](https://img.shields.io/github/stars/gojasper/flash-diffusion?style=social)](https://github.com/gojasper/flash-diffusion)"
        )
        gr.Markdown(
            "💡 *Hint:* We noticed that 8 steps and CFG can improve the results (text rendering in particular) for that very model. Feel free to play with those parameters."
        )

        gr.Markdown(
            "💡 *Hint:* To better appreciate the low latency of our method, run the demo locally !"
        )

        with gr.Row():
            prompt = gr.Text(
                label="Prompt",
                show_label=False,
                max_lines=1,
                placeholder="Enter your prompt",
                container=False,
            )

            run_button = gr.Button("Run", scale=0)

        result = gr.Image(label="Result", show_label=False)

        with gr.Accordion("Advanced Settings", open=False):

            negative_prompt = gr.Text(
                label="Negative prompt",
                max_lines=1,
                placeholder="Enter a negative prompt",
                value="deformed, distorted, disfigured, poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, mutated hands and fingers, disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, NSFW, bad text"
            )
            
            seed = gr.Slider(
                label="Seed",
                minimum=0,
                maximum=MAX_SEED,
                step=1,
                value=0,
            )

            randomize_seed = gr.Checkbox(label="Randomize seed", value=True)

            with gr.Row():
                
                guidance_scale = gr.Slider(
                    label="Guidance scale",
                    minimum=0.0,
                    maximum=3.0,
                    step=0.1,
                    value=1.0,
                )
                
                num_inference_steps = gr.Slider(
                    label="Number of inference steps",
                    minimum=4,
                    maximum=8,
                    step=1,
                    value=4,
                )

        examples = gr.Examples(examples=examples, inputs=[prompt], cache_examples=False)

        gr.Markdown("**Disclaimer:**")
        gr.Markdown(
            "This demo is only for research purpose. Jasper cannot be held responsible for the generation of NSFW (Not Safe For Work) content through the use of this demo. Users are solely responsible for any content they create, and it is their obligation to ensure that it adheres to appropriate and ethical standards. Jasper provides the tools, but the responsibility for their use lies with the individual user."
        )
    gr.on(
        [run_button.click, seed.change, randomize_seed.change, prompt.submit],
        fn=infer,
        inputs=[prompt, seed, randomize_seed, guidance_scale, num_inference_steps, negative_prompt],
        outputs=[result],
        # show_progress="minimal",
        #show_api=False,
        #trigger_mode="always_last",
    )

demo.queue().launch(show_api=False,server_name="0.0.0.0",server_port=9999)
