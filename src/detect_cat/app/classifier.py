import json
import requests
from utils import load_image
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def detect_cat(image_path: str, url: str) -> float:
    """Get probability for a given image containing a cat

    Args:
        image_path: The path to a given image
        url: The url to a Tensorflow server
    Returns:
        Probability that a given image contains a cat
    """

    image_np = load_image(image_path)

    # Create json structure for request
    data = json.dumps({"signature_name": "serving_default", "instances": image_np.tolist()})

    # Send request
    with requests.Session() as session:
        retry_adapter = requests.adapters.HTTPAdapter(
            max_retries=Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        )
        session.mount("http://", retry_adapter)

        json_response = session.post(url, data=data)

    # Cat: 0; No Cat: 1
    cat_probability = json.loads(json_response.text)["predictions"][0][0]

    # Reverse: Cat 1; No Cat: 0
    cat_probability = 1 - cat_probability

    return cat_probability
