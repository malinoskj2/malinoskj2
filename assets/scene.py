import torch, sys
from diffusers import StableDiffusionXLPipeline
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
).to("cuda")
neg = "text, watermark, blurry, deformed, extra limbs, low quality, cartoon, chibi, big head"
prompts = {
 "night": "detailed pixel art illustration, high resolution 32-bit style, a young man sitting alone on the wide stone steps of a grand neoclassical european cathedral with columns and a dome, typing on a black thinkpad laptop, laptop screen glow, night, deep blue and purple sky, stars, warm lamp light, large empty sky on the left side, building on the right side, wide cinematic composition, catppuccin mocha palette, subtle dithering",
 "day": "detailed pixel art illustration, high resolution 32-bit style, a young man sitting alone on the wide stone steps of a grand neoclassical european cathedral with columns and a dome, typing on a black thinkpad laptop, bright daytime, soft pastel blue sky, a few clouds, large empty sky on the left side, building on the right side, wide cinematic composition, catppuccin latte palette, subtle dithering",
}
for name, p in prompts.items():
    for seed in [1, 2, 3, 4]:
        g = torch.Generator("cuda").manual_seed(seed)
        img = pipe(prompt=p, negative_prompt=neg, width=1536, height=640, num_inference_steps=30, guidance_scale=7, generator=g).images[0]
        img.save(f"{name}-{seed}.png")
        print("saved", name, seed, flush=True)
