import json
import requests
import os
import time
import aiohttp
import asyncio
import random

import numpy as np

# Functions to send asyncronous requests to tf-serving api
async def fetch(session, url, data, headers):
    async with session.post(url,data=data,headers=headers) as response:
        resp = await response.json()
        return resp


async def fetch_all(image_paths):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for image_path in image_paths:
            image_np = cv2.imread(image_path).astype('uint8')
            image_np = np.expand_dims(image_np, axis=0)
            image_list = image_np.tolist()
            
            url = 'http://localhost:8501/v1/models/resnet:predict'
            data = json.dumps({"signature_name": "serving_default", "instances": image_list})
            
            tasks.append(
                fetch(
                    session,
                    url,
                    data,
                    headers
                )
            )
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return responses


# Sample data for testing purposes from git repository intellicatflap_analytics
image_dir = '/intellicatflap_analytics/sample_data/calibration_sample/'

# Get image paths 
files = os.listdir(image_dir)
image_paths = [image_dir + img for img in files if img.endswith('.jpg')]
image_paths.sort()


# Do testing: Send requests
# Prepare request
headers = {"content-type": "application/json"}

# Warmup
print("Warmup") # TODO: Replace with logging module.
start_time = time.time()
responses = asyncio.run(fetch_all(image_paths[:3]))
print(f"It took {time.time() - start_time}s to process {len(image_paths[:3])} images.")

# Real testing
start_time = time.time() # TODO: Replace with logging module.
responses = asyncio.run(fetch_all(image_paths))
print(f"It took {time.time() - start_time}s to process {len(image_paths)} images.")  # TODO: Replace with logging module.


random.shuffle(image_paths)
start_time = time.time()
responses = asyncio.run(fetch_all(image_paths))
print(f"It took {time.time() - start_time}s to process {len(image_paths)} images.")  # TODO: Replace with logging module.


random.shuffle(image_paths)
start_time = time.time()
responses = asyncio.run(fetch_all(image_paths))
print(f"It took {time.time() - start_time}s to process {len(image_paths)} images.") # TODO: Replace with logging module.