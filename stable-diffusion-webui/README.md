## Lagrange Mars Testnet Base Space

### Table of Content

* [Introduction](#introduction)
* [How to Fork the Base Space and Rename it](#how-to-fork-the-base-space-and-rename-it)
* [How to Add More Models (optional)](#how-to-add-more-models)
* [How to Get Your Space Running](#how-to-get-your-space-running)
  * [Deploy the Stable Diffusion Web UI (Automatic1111)](#step1-deploy-the-stable-diffusion-web-ui-automatic-111)
  * [Install LoRA Extensions](#step-2-install-a-lora-model-into-automatic1111)
  * [Set Up LoRA Models](#step-3-set-up-lora-models)
* [Reference](#reference)

### Introduction
Space Link: https://lagrangedao.org/spaces/0x231fe9090f4d45413474BDE53a1a0A3Bd5C0ef03/Stable-Diffusion-Base-LoRA/files


This tutorial guides you on how to complete[ Task 2: Space Builder Task](https://github.com/lagrangedao/community/blob/main/Mars-Testnet/Lagrange-Mars-Testnet-Campaign.md), to fork and run a `Stable Diffusion Space`. It covers the deployment of Stable-diffusion in Lagrange Space, adding LoRA models to `Automatic1111` for image generation, and further customizing your Space with additional models.

#### What is Stable Diffusion
Stable Diffusion is a state-of-the-art text-to-image model that generates an image from text.

#### What is Lagrange Space
Lagrange Space is a simple way to host ML demo apps on Lagrange.

#### What is LoRA
LoRA (Low-Rank Adaptation) is a training technique for fine-tuning Stable Diffusion models. and LoRA models are specific versions of the Stable Diffusion model that have undergone fine-tuning.

#### What is `Automatic111`
Stable Diffusion web UI (`AUTOMATIC1111` or A1111 for short) is the de facto GUI for advanced users.

### How to Fork the Base Space and Rename it

1\. Visit \[[https://lagrangedao.org/spaces](https://lagrangedao.org/spaces)] and log in to your account

2\. Visit the[ Stable Diffusion Base Space](https://lagrangedao.org/spaces/0x6091b2f5678952cAfbf02755D78973EBff302e11/Stable-Diffusion-Base-LoRA/card), and click on the **`Fork`** button to create a duplicate of the Base Space.

<figure><img src="https://lh4.googleusercontent.com/UJnbM8oLVJXDjWZZkxQ7fDCek29pVJVBGxoAmvMUyhRzzX-z_WtvKNWKwzYH3xxQZjlwI9UV5Tl3hV_DjFsf6h9zRaxy6EACBGTbtvwDK2P47l8KcTDISitGLMZUdY2gy3Q7NtKejlP3Hdzhoy9xm-M" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh6.googleusercontent.com/oRy_T_MNTSJ6bqGTJtiHK_Pw-tzBLhY3r6e1UFzPxxxxD1bh5OImd22rOktVH0Cs1iO-CW1B1-a6J8JYn0GvSy_sZn1PWvuIpNg5yHGTpTI3pgWzxh9Zrm4q2eL-iyW2AAYlgOA29FZR1LN4CGw9t3c" alt=""><figcaption></figcaption></figure>

3\. Click on the **`Just Fork, choose config later`**
<figure><img src="https://lh5.googleusercontent.com/S2daQ_7aiKXdAxCogyBDELByzC282gzCATDRIa9vhx_0xYT8nrqYhAvu5kAvbrE5s-O1kYqzZ1jZYG9pnFYxqK8k-FfD1KFuAMh5g9GJ1GjbYtP5NxueHVCP3QUA3DO25DqUo-jSA63e6hPaJjKizzU" alt=""><figcaption></figcaption></figure>

In your forked Space, click the **`Settings`** button and scroll down to the Rename section to rename your Space.

<figure><img src="https://lh4.googleusercontent.com/cdSKmw-kdgN5Zlm2mQ05GiCantlI8hbbfc1Ahc5cp6DcU6Fw4dMlftmYWJCskoq6tAl7oB5sXuUm549WhQ9EcIHxt6RLVcnTVwt-228mqOKEZ5KDiXmZintlNr3CeUKLzw5lTksOslWfjwwRFE7Mb1U" alt=""><figcaption></figcaption></figure>

### How to Add More Models

If you prefer to utilize the default LoRA models provided by Base Space, you can proceed directly to the section on How to Get Your Space Running.

However, if the available models do not precisely align with your image preferences, you have the option to enhance your Stable Diffusion Space by **_adding more models by following the below steps_**.

1\. Find models you liked from[ Civitai](https://civitai.com/?query=lora) and[ Hugging Face](https://huggingface.co/models?search=lora), and get the downloading link of the model.

2\. Go to **`Files and versions`** and Update the Dockerfile , you need to replace the `<model_download_link>` and `<your_model_name>`, then add the below command to the Dockerfile:

```
# Command Example
RUN wget <model_download_link> -O /stable-diffusion-webui/models/Lora/<your_model_name>
```

<img width="1337" alt="image" src="https://github.com/Normalnoise/models/assets/102578774/d6d8d3a2-31f6-44b1-b918-ecaa24a3abf3">


<img width="1297" alt="image" src="https://github.com/Normalnoise/models/assets/102578774/2a04348c-9937-416a-94b9-3efc5443e130">


### How to Run Your Space

To set up your Stable Diffusion Space for generating images from textual descriptions, you must

 - (1) deploy the Stable Diffusion Web UI, a user-friendly interface that facilitates interaction with the model. Additionally,
 - (2) installing LoRA extensions enhances the Web UI's capabilities, enabling support for LoRA models.
 - (3) installing the actual LoRA models to enable image generation.

#### **Step1: Deploy the Stable Diffusion web UI (Automatic 111)**

1\. Click on **`Settings`** and select your preferred hardware meeting the below requirements:

 -  At least one GPU
 -  At least 4 vCPUs
 -  Minimum 50GB SSD storage
 -  Minimum 32GB memory
 -  Minimum 50MB bandwidth
 -  Here are the GPUs we recommend:
    -  T4, RTX 4090, 3090Ti, 3090, 3080Ti, 3080, 3060Ti, 2060, 2070, 2080, 2080Ti, A100, H100

**Ensure you choose hardware with at least one GPU**; without it, Stable Diffusion Space won't function.

And proceed with the payment.

<figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh3.googleusercontent.com/ur12FW4N4N9oFzS5J5nO55B5wZMb9wHtVV6kvkC5oHumsfut9B9cDmDvSlabaezsQ9HN_7ebG9s4wwAlOHsRmB-X2laTri9PAf5228lLlCAOAexnb_LE_UXW6MXfyhryuSlZbNApJwtjwxXiU1LoKOI" alt=""><figcaption></figcaption></figure>

2\. After payment confirmation, observe the status tag of your Space. It will transition from `Waiting for Transaction` to "Deploying," and finally to `Running` once the Stable Diffusion web UI is successfully deployed on your Space.

<figure><img src="https://lh3.googleusercontent.com/GynEwa-x3Vg008tyW70OlJ11Du-WbouUPAfRhH1WKODaXMIxS6-8RsrVoXxRxgRkQMrPORtnnIkRL2W2usMpMVZNb8V6b5KMeesy_TYVsJm4lu4ikYwThdw4kie1uZWER_6VMdsxdIO5E7aCLchRTmE" alt=""><figcaption></figcaption></figure>

After a few minutes, you can access the Stable Diffusion web UI in the **`App`** tab of your Space.


#### **Step 2: Install a LoRA Model Into Automatic1111**

Before using LoRA models in your Stable Diffusion Web UI, you need to install the LoRA extension.

1\. Click on the **`App`** tab to Launch the Stable Diffusion Web UI in the space.

<figure><img src="https://lh3.googleusercontent.com/bv9DMnddVoAL2FaT_iw1_Izp87oy4GbpG5hjnFuICcjm62YrmND_WqicTYocsGmS-hYeht1j6d0FjhE0x_qD3su3OOsGJz8rnlkgj3F8xoOBqEbox-mEhv4upEzaQkU2RlnTTkKzPkZ5Yxw4hxI6FHU" alt=""><figcaption></figcaption></figure>

2\. Open the **`Extensions`** tab, click on **`Install from URL`**, and copy the following link:

```
https://github.com/kohya-ss/sd-webui-additional-networks.git
```

And Click the **`Install`** button.

<figure><img src="https://lh6.googleusercontent.com/8KNP0TXzh5EBUFjrAVPmClMgxMG1VDEI_MzoY36EBuhY5jD4KzDmChiq9QVVn8slZZxc2LfmoHcw6s0Akij5KuJvL9Y2HZ7ZgtRO-M4_x5rVaH6Vzc6dUHImD7ys7lGrkUu2gIU6t-cy66LuJwp-Mv4" alt=""><figcaption></figcaption></figure>

3\. To verify if the installation was successful, switch to the **`Installed`** tab. and Click on the **`Apply and restart UI`** button.

<figure><img src="https://lh3.googleusercontent.com/D34PMjWXZjDEz9mtIKJCLu6vkoUgJGsHN7Fh0FdUA30vQAIaCbI8_Q-sYh1E3qjkZRJsLjBBDo16S9diY8TMUIr_GfcBRcdOa89jTiBS0W7m9eSCX5_Zvub8Q_tnQLdiAZBQG7C7uWLq_W3GROkmFpo" alt=""><figcaption></figcaption></figure>

4\. Open the **`Settings`** tab and switch to the **`Additional Networks`** tab, paste `stable-diffusion-webui/models/Lora` in the input field of `Extra paths to scan for LoRA models` and then click **`Apply settings`**.

<figure><img src="https://lh4.googleusercontent.com/ABPxubNgvGpLUgdYM0DHN3ub-h34hu0g8hLt0rdQmsujA6oDtTjt64zVPq-uVMrYGUiD6EzLcBbWV-4xgPz8CUdRNVgPowpzD87tn_NvTshfZQZZJ90q50R2bQx1FyKe2r5Kpq4MeFb5AKHjRVXc_O0" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh4.googleusercontent.com/5dVz0nAVDWgvQ7qOrPWSycUBAifZQyiyFV9fb6vV5rWrE-iNYoaLsSYx4zZIqQYTQLjzGh06yftmn_SDJujpTEUuRlaZYXFoqSOuZlqRd0-gYe-OsMg0Z6O7hpB_nHKvQWAjY0BqU8PV6Qim2Km34PI" alt=""><figcaption></figcaption></figure>

#### **Step 3: Set Up LoRA Models**

Although the LoRA Extension has been installed successfully, it's not enough to start generating images. You need to install your actual LoRA Models to the specified folder as well.

1\. Click the **`App`** tab in your Space to access the launched Stable Diffusion Web UI.

2\. Choose your desired checkpoint model from the preloaded options (e.g., "chilloutmix-Ni.safetensors" or "V1-5-pruned-emaononly.safetensors").

3\. Click on the **`txt2img`** tab and select the icon of **`Additional Networks`** under the **`Generate" button`**, then choose `LoRA`.

<figure><img src="https://lh4.googleusercontent.com/Tj_whyH8mY6b6-7zJOtw_irYoeVvmhicN6bAOSx3aPqIdU5AoPgj8SBPuEOpCdZAX8TGseIcHrhPhQ2PN0fpLh30-0S5j_v28hboBekLahFy0Rf7sOIQLwXfK5DeAHoJuqZsiekRjL3FFhSIO_cKkuI" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh3.googleusercontent.com/Ogy4r3jdsUesmBVJjhLhHCohS9Dcfdrs1SgSjVGLijQMHKw7fqkd5dktzRsY8F0L7HXUDdwrFoE28BybVt17wY1AWw8fFASmJqd_b1xjcgVGBXacoSYa9OclZwGlqbLBVxiokTF-JtYNcVz-Ty-SRo0" alt=""><figcaption></figcaption></figure>

Several LoRA models will be displayed. Select the one you want to use.

4\. Each LoRA model has a "Trigger Word." Ensure your prompts include the specific LoRA's trigger word, which is usually added automatically(**Click the Model**).

For example, if you **Click** "KsmRm," it will show `<lora:KsmRm:1>`.

<figure><img src="https://lh5.googleusercontent.com/NAOTPoZIGGKbOPQHxBtNqTaC6Fvmz68ABYKqsO5YcHQwWkSA2yDn_sQONgfbX6n4UgTtYScNG9RzPnlqFqkjBFD5i2WgfEBFR6JLKeAwmu6sOJ_uhR5qur8d00WZsiCyrCzis5IbFBiHxex1fnT_Snk" alt=""><figcaption></figcaption></figure>

5\. Add the text or description for the image you want to create after the LoRA's trigger words.

<figure><img src="https://lh5.googleusercontent.com/Cie6sBdryTVvu1e9MkwmTy66IDwHBACV5lEZAdJtF3pSOpSglFZC7CZD0Ad4UVhFN5x3QBvCZ-3fU9QidnzqOIVIoFxB6fd6MShrZqFPeYKv5HIbDoqbHtlMieffdYZyjK_YsCfkbQ8ZS_rUJhS7vN8" alt=""><figcaption></figcaption></figure>


**Congratulations!** 🎉🎉🎉 

An image has been generated from your forked Stable Diffusion Space using a LoRA model.

#### NOTES

If you have not previously added any models and now wish to include additional ones, please Click on **`Redeploy`** after following the steps outlined in [How to Add More Models](#how-to-add-more-models).


<figure><img src="https://lh3.googleusercontent.com/2yhRhnPCKsAX82qvk4N4tF9gVZ7CnjYLUIsrjeweTC5PCjoOY-9PE6ofpVzzYMO-_iX2eJ3xr2KJ-ScRaqOZ45n1aA8gH8s7B2wcR_aNBOuUJAJsLUi7nyPoypE8VCiKyYbg1Hm9akXFJARkqqB2Ls0" alt=""><figcaption></figcaption></figure>

Once the redeployment is complete(almost 10 minutes), continue by following the guidance provided in Install LoRA Extensions and Set Up LoRA Models once more to ensure the successful integration of your newly added models and guarantee their effective functioning within your Space.

### Reference

* Special thanks to[ AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui.git) for the support.
* [Stable Diffusion: What Are LoRA Models and How to Use Them?](https://softwarekeep.com/help-center/how-to-use-stable-diffusion-lora-models)
* [What are LoRA models and how to use them in AUTOMATIC1111](https://stable-diffusion-art.com/lora/)
