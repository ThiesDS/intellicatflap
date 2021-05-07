import json
import requests
from utils import load_image


def detect_cat(image_path):

  image_np = load_image(image_path)

  # Create json structure for request
  data = json.dumps({"signature_name": "serving_default", "instances": image_np.tolist()})

  # Send request
  json_response = requests.post(url, data=data, headers=headers)

  # Cat: 0; No Cat: 1
  cat_probability = json.loads(json_response.text)['predictions'][0][0]

  return cat_probability