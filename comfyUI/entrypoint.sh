#!/bin/bash
wget https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt -P /ComfyUI/models/checkpoints/ &&
exec python main.py --listen "0.0.0.0" --port "8543"
