import json
import requests
import os
import time
import aiohttp
import asyncio
import random
import logging

from logging import FileHandler
from PIL import Image

import numpy as np

print('Hello')

# Prepare logging
LOG_FILE_PATH = '/app/logs/'
log_file_name = 'tf_serving_test.log'
FORMATTER = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(funcName)s:%(lineno)d|%(message)s')

file_handler = FileHandler(LOG_FILE_PATH + log_file_name)
file_handler.setFormatter(FORMATTER)

logger = logging.getLogger('tf_serving_test')
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


# Functions to send asyncronous requests to tf-serving api
async def fetch(session, url, data, headers):
    async with session.post(url,data=data,headers=headers) as response:
        resp = await response.json()
        return resp


async def fetch_all(image_paths):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for image_path in image_paths:
            #image_np = cv2.imread(image_path).astype('uint8')
            image = Image.open(image_path)
            image_np = np.asarray(image)
            image_np = image_np.astype('uint8')
            image_np = np.expand_dims(image_np, axis=0)
            image_list = image_np.tolist()
            
            url = 'http://tf-serving:8501/v1/models/resnet:predict'
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
image_dir = '/app/test_imgs/'

# Get image paths 
files = os.listdir(image_dir)
image_paths = [image_dir + img for img in files if img.endswith('.jpg')]
image_paths.sort()


# Do testing: Send requests
# Prepare request
headers = {"content-type": "application/json"}

logger.info("Wait until server is set up.")
time.sleep(30)

# Warmup
logger.info("Started tf serving test, warming up.")
start_time = time.time()
responses = asyncio.run(fetch_all(image_paths[:3]))
logger.info(f"Warm-up: It took {time.time() - start_time}s to process {len(image_paths[:3])} images.")

# Real testing
start_time = time.time() # TODO: Replace with logging module.
responses = asyncio.run(fetch_all(image_paths))
logger.info(f"Run 1: It took {time.time() - start_time}s to process {len(image_paths)} images.")

random.shuffle(image_paths)
start_time = time.time()
responses = asyncio.run(fetch_all(image_paths))
logger.info(f"Run 2: It took {time.time() - start_time}s to process {len(image_paths)} images.")


random.shuffle(image_paths)
start_time = time.time()
responses = asyncio.run(fetch_all(image_paths))
logger.info(f"Run 3: It took {time.time() - start_time}s to process {len(image_paths)} images.")