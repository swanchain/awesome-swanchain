 #!/bin/bash
wget https://huggingface.co/swl-models/chilloutmix-ni/resolve/main/chilloutmix-Ni.safetensors -P /stable-diffusion-webui/models/Stable-diffusion/ &&
##wget https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors -P /stable-diffusion-webui/models/Stable-diffusion/ &&
exec /stable-diffusion-webui/webui.sh
