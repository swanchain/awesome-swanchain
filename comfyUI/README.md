# ComfyUI Space

### About ComfyUI

ComfyUI is an innovative [node-based Graphical User Interface](https://en.wikipedia.org/wiki/Node\_graph\_architecture) (GUI) designed for Stable Diffusion, a powerful AI model. ComfyUI simplifies the complex process of image generation by breaking it down into modular components known as nodes.

### About ComfyUI Space

[ComfyUI Space](https://lagrangedao.org/spaces/0x6091b2f5678952cAfbf02755D78973EBff302e11/ComfyUI/app), accessible via [Lagrange](https://lagrangedao.org/main), allows users to explore this advanced model effortlessly and create custom image generation workflows, offering numerous advantages:

**No installation required** - Access ComfyUI instantly without needing to install it locally. Lagrange provides a simple way to host ML apps for demoing and interacting with your project without local setup

**Powerful GPU Network** - Lagrange grants access to GPU computing resources, enhancing the speed and efficiency of image generation in ComfyUI.&#x20;

**Compatibility and Accessibility** - As a web-based platform, Lagrange works on Windows, Mac, Linux, and mobile. And with its powerful GPU network, You can access your ComfyUI workflows and creations from any internet-connected device

**Easy sharing** - Simply share your ComfyUI Space link for collaborators to access your workflows. Lagrange enables seamless project sharing.

### Getting Started with ComfyUI Space

#### Using the Default Workflow:

When you first access [ComfyUI Space](https://lagrangedao.org/spaces/0x6091b2f5678952cAfbf02755D78973EBff302e11/ComfyUI/app), you’ll see the default text-to-image workflow. Here's the easiest way to generate an image using ComfyUI Space:


**Step 1: Select a Model**

1. In the "Load Checkpoint" node, choose a Stable Diffusion model.
2. Click on the model name within the node to access a list of available models.
3. Select the model you want to use.

<figure><img src="https://lh7-us.googleusercontent.com/GD8WTxSfxTSeS7bd-EoC-oVNoi7-d7s44zAlyphjgmxaYn6ZB8AU5K8wnhqlbTOf4WuGQzr37OuDHlONo5wm5D_vNHYTO9phycdsNDXzoqXQN31FIrqZZ6aUPotD-cZViCKAsgn8yR486WP32CQwkUE" alt=""><figcaption></figcaption></figure>

**Step 2: Enter Prompts**

1. Find the two "CLIP Text Encode" nodes labeled "Prompt."
2. Use the top node for your primary prompt, describing what you want in the image.
3. Utilize the bottom node for a negative prompt, indicating what you DON'T want in the image.
4. Adjust keyword weights using (keyword:value) syntax for fine-tuning.

<figure><img src="https://lh7-us.googleusercontent.com/cU_vbVRO3bhtKUU413xGWmj40PTJKucqLAb4JGavSIB_AejAjKs5WS3piTM4X3EbLxaOX2PBx2pg-RenSXyBf3DV_aizmsaaVKv0wpG3egEMvvg5UiA5n5kcV1Ig2IlJOR1HYrr5kHRu-W9uXs26p98" alt=""><figcaption></figcaption></figure>

**Step 3: Generate the Image**

1. Click the "Queue Prompt" button at the top-right.
2. After a brief processing time, your first AI-generated image will appear.

![](https://lh7-us.googleusercontent.com/fJe47leDeZIut4cvsdmjaG0xOlLF\_w4dTWkiDBoIL5gUp3VXrJExqxzK79kYXFE1H4T5OfznTl405UAyYzFPO6Mty-55dsfQAYc1uODw-xg\_yYzRY-jkBzZRbVsCcEioRo\_wQzuZBzjM57GsOYsNbbI)

#### Building an Image Generation Workflow:

With ComfyUI, you are not limited to basic image generation like in AUTOMATIC1111. ComfyUI gives you extraordinary customization and control over the entire image creation process.

For example, a typical workflow involves generating an image, processing it with img2img, and upscaling. In AUTOMATIC1111, you would have to perform each step manually.

<figure><img src="https://lh7-us.googleusercontent.com/-xqLxa6qlA7v2XoxE1YCmhTiHhKsvI3IQxQn-0khi1FIiZtk6yWkMW36GFaWgdkRxH9yeNO5T-MhG1X-WZZYJgBGU0E1YFOvui5ckoYBwj7WxHeRL0u93tsC79FHTLsGb_SVYTpHA1eEOzEOewik5yw" alt=""><figcaption></figcaption></figure>

But with ComfyUI, you can streamline these into a single automated workflow with one click. ComfyUI allows you to customize and connect different processes like generation, editing, and upscaling however you want.

This makes ComfyUI perfectly suited for leveraging multi-step generation models like SDXL. SDXL uses a base model to create a noisy latent, then a specialized refiner model to denoise and sharpen the final image. With ComfyUI, you can seamlessly link these two models into one workflow.



<figure><img src="https://lh7-us.googleusercontent.com/ztHiJSwaJOZ7NUhMIuLn2D-VpYtf6N_-8ekNIeWVWmppbEXopqAfrPtEbKD0KP16eoMqueeQ8x3IJjei3qJMcAwxkqnZEYkMl9JCwl__jIKXwIF83b3AgadmSV3cq77i58HoFfuKzZhhSV4UARY8Vg4" alt=""><figcaption></figcaption></figure>

Before you can dive into creating a custom image generation workflow, it's important to first understand the basics of building a workflow in ComfyUI.

Here is **a step-by-step guide** to create a simple text-to-image workflow to gain a deeper understanding of how ComfyUI works:


**Step 1: Adding a Model**

1. Right-click and select "Add Node."
2. Choose "Loader," then "Load Checkpoint" to add your preferred model.

**Step 2: Adding Prompts**

1. To apply prompts, add "Clip Text Encode" nodes for positive and negative prompts.
2. Right-click to add nodes and search for "Clip Text Encode."

**Step 3: Sampling from the Model**

1. You need a sampler node to sample from your model.
2. Search for "Sampler" and select the advanced version for greater control.
3. Connect the model, positive prompt, negative prompt, and latent image nodes to the sampler.

**Step 4: Creating a Latent Image**

1. Set up an empty latent image node by adding "Empty Latent Image."
2. Configure the latent image size according to your needs.
3. Connect the latent image node to the sampler.

**Step 5: Auto-encoding the Image**

1. The final step involves auto-encoding the image for generation.
2. Use the auto-encoder provided in your model.

**Step 6: Preview and Save**

1. You can preview your generated image at any point in your workflow.
2. Use the preview option (note that this does not save the image).
3. To save the image, use the "Save Image" option, or add a "Save Image" node for automated saving.

**Step 7: Queuing Prompts**

1. To generate multiple images with different prompts, use the "Queue Prompt" feature.
2. This allows you to add and run multiple prompts sequentially.

### ComfyUI Nodes Explained

ComfyUI Space revolves around creating workflows by connecting different nodes. Each node is like a building block that performs a specific function within the workflow.

These nodes have three key components:

* Inputs (on the left): Where data enters the node.
* Outputs (on the right): Where data exits the node.
* Parameters (in the middle): Settings that control the behavior of the node.

Connecting nodes is as simple as dragging lines between inputs and outputs.

#### The Key Nodes in ComfyUI Space

To understand nodes, we have to understand a bit about how Stable Diffusion works. Let's take a look at the key nodes of the default workflow.

<figure><img src="https://lh7-us.googleusercontent.com/8pbPezXRN-lI4eAGlVEWVtSWZ0mbLMH_P3rFtRkal4fgZ-sinhNQqvFwRANZ4IElnjkziB6uFCfm6b-YQ9HiGxTXkmYjvGxSo3J9zf570HU1PqOeQec9EWzTThj_vjCnud3m_WFKrUz3KH62GbbxEqc" alt=""><figcaption></figcaption></figure>

**Load Checkpoint Node**

* This node allows you to select a model.
* A Stable Diffusion model consists of three main parts: MODEL, CLIP, and VAE.
* The MODEL section connects to the sampler for image generation, while CLIP preprocesses prompts.

**CLIP Text Encode Node**

* These nodes transform text prompts into embeddings.
* The top node is for the primary prompt, linked to the positive input of the KSampler node.
* The bottom node is for the negative prompt, linked to the negative input of the KSampler node.

**Empty Latent Image Node**

* This node starts the image generation process with a random image in the latent space.
* The size of the latent image is proportional to the image's pixel size.

**KSampler Node**

* KSampler is the heart of image generation in Stable Diffusion.
* Parameters in this node include Seed, Control\_after\_generation, Step, Sampler\_name, Scheduler, and Denoise.
* These parameters govern the image generation process and its quality

### Unlocking ComfyUI's Advanced Capabilities

So far we've covered the basics of building workflows in ComfyUI. Now let's look at some of its more advanced features to take your AI art to the next level:

#### Custom Nodes

One of ComfyUI's most powerful capabilities is custom nodes. These are additional nodes created by the community that let you expand what's possible in ComfyUI far beyond the default options.


The [ComfyUI Manager ](https://github.com/ltdrdata/ComfyUI-Manager)node lets you easily browse, install, and update custom nodes right within ComfyUI. Some popular custom nodes include upscalers, inpainting tools, style injectors, and more.\


<figure><img src="https://lh7-us.googleusercontent.com/hEILHlF26JUThklhxH7Rtcm3jdzvJyNVgDa1sawUOcEGoqH2XHIY0hXCgO00BClBiqfnk4j-y1KHBCFSjLwaRmP6-3U5bDDnoCMbpsjgHilZcq-BH5NbOT7pDUbWLedhAGVW7WQYyWf1vXO9q2EWgdU" alt=""><figcaption></figcaption></figure>

#### Upscaling:

ComfyUI makes it easy to upscale your final images through the workflow. You can upscale in the latent space before decoding to pixels with [Hi-Res Fix](https://stable-diffusion-art.com/automatic1111/#Hires\_fix), or use dedicated AI upscaler models with the [AI Upscaler node](https://stable-diffusion-art.com/ai-upscaler/).

Popular upscaling nodes like [SD Ultimate Upscale](https://stable-diffusion-art.com/controlnet-upscale/) are also available. You can test different upscaling methods just by wiring up a new node.

#### Inpainting:

[Inpainting](https://stable-diffusion-art.com/controlnet-upscale/) allows you to regenerate only a selected part of an image. While a bit tricky in ComfyUI, it's possible by using a mask image and the Inpainting node.

This allows seamless image editing and fixing imperfections through AI regeneration of selected areas.

#### SDXL Workflow:&#x20;

ComfyUI supports the [Stable Diffusion XL model](https://stable-diffusion-art.com/sdxl-model/), making it one of the first GUIs to do so. Users can access simple SDXL workflows and tailor them to their image generation requirements, offering flexibility and control.

<figure><img src="https://lh7-us.googleusercontent.com/WeYUwrSv2ApGEn8pmaXKkcuQf2ZHAlocG5PnvvSOE0qcTVsOHrG_tGZ-kwDfIrMoLl74RbS4KP_IQmRbrTALpofpp6AZ24P0tpVoftYfcra6dxrPnyvR6Mgw1Mj6sCRoCiq7W3apdcIC8bsSiDzcPvw" alt=""><figcaption></figcaption></figure>

#### ComfyUI Impact Pack:&#x20;

[The Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) extends ComfyUI's functionality with a collection of free custom nodes that enhance image generation. It covers various aspects, including face regeneration, advanced custom nodes, and detailed workflows. Installing the Impact Pack adds an array of additional nodes to ComfyUI, expanding its capabilities.

#### LoRA:&#x20;

[LoRA](https://stable-diffusion-art.com/lora/) is a model file designed to modify [checkpoint models](https://stable-diffusion-art.com/models/) by altering their MODEL and CLIP components while keeping the VAE intact.&#x20;

ComfyUI allows users to leverage LoRA for unique effects, including text-to-image workflows with LoRA integration or using multiple LoRAs for specific modifications.



_For more tutorials on advanced workflows, stay tuned and follow our_ [_official Medium account_](https://medium.com/@swanchain)_._&#x20;

_Happy creating with ComfyUI Space!_
