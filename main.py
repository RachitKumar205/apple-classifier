import requests
from matplotlib.patches import Rectangle
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM
import transformers
import transformers.utils.logging as logging
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.transforms import Bbox

from typing import List, Optional
import numpy as np
from matplotlib import patches
from pathlib import Path
import os, sys

logging.set_verbosity(transformers.logging.CRITICAL)

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", torch_dtype=torch_dtype, trust_remote_code=True).to(device)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)

prompt = "<DENSE_REGION_CAPTION>"

url = sys.argv[1]
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=prompt, images=image, return_tensors="pt").to(device, torch_dtype)

generated_ids = model.generate(
    input_ids=inputs["input_ids"],
    pixel_values=inputs["pixel_values"],
    max_new_tokens=1024,
    num_beams=3,
    do_sample=False
)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

parsed_answer = processor.post_process_generation(generated_text, task="<DENSE_REGION_CAPTION>", image_size=(image.width, image.height))
axis = plt.gca()

#for patch in parsed_answer["<OD>"]["bboxes"]:
#    
#    print(patch) 
#    axis.add_patch(Rectangle((patch[0], patch[1]),patch[2]-patch[0],patch[3]-patch[1], facecolor="none", ec='k',lw=2))
#
#plt.imshow(image)
#plt.show()
#
#while True:
#    pass
print(parsed_answer["<DENSE_REGION_CAPTION>"]["labels"])
