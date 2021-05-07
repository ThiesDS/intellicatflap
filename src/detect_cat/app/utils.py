from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


def load_image(filename):
    
  # load the image
  img = load_img(filename, target_size=(224, 224))
  
  # convert to array
  img = img_to_array(img)
  
  # reshape into a single sample with 3 channels
  img = img.reshape(1, 224, 224, 3)
  
  # center pixel data
  img = img.astype('float32')
  img = img - [123.68, 116.779, 103.939]
  
  return img


def save_detections(image_path):

  # Path with name of file with detection information
  cat_detection_path = image_path.replace('.jpg','.catdetected')

  # Write empty file
  with open(cat_detection_path, "w") as file:
      file.write('')