
# This program is fairly complicated.
# It uses the BitMoji API documented at
# to download an image. Then it
# displays that image in a window.

# You need tkinter either shipped with python
# or installed from your operating system's tk package.
import tkinter

# python3 -m pip install --user pillow
import PIL
from PIL import ImageTk

# urllib and io are provided by the standard library
import urllib
from urllib import request
import io


def get_bitmoji_image(**kwargs):
  # The libmoji project documents the v3 preview API here:
  # https://github.com/matthewnau/libmoji/wiki/Understanding-Bitmoji

  # Create a map of default arguments
  api_args = {
    "scale":1,
    "gender":1,
    "style":5,
    "rotation":0,
    "beard":2212,
    "brow":1555,
    "cheek_details":1356,
    "ear":1423,
    "eye":1614,
    "eyelash":-1,
    "eye_details":1352,
    "face_lines":1366,
    "glasses":2465,
    "hair":1723,
    "hat":2495,
    "jaw":1400,
    "mouth":2338,
    "nose":1482,
    "beard_tone":8678208,
    "blush_tone":16754088,
    "brow_tone":6772090,
    "eyeshadow_tone":-1,
    "hair_tone":8637550,
    "hair_treatment_tone":10513945,
    "lipstick_tone":16740668,
    "pupil_tone":5793385,
    "skin_tone":9657655,
    "body":1,
    "face_proportion":13,
    "eye_spacing":0,
    "eye_size":2,
    "outfit":990491,
  }
  
  # Update anything given in kwargs
  # (eg if you call get_bitmoji_image(rotation=1) the face will be turned to the right slightly. )
  api_args.update(kwargs)

  # Create the URL to send to bitmoji
  bitmoji_image_url = "https://preview.bitmoji.com/avatar-builder-v3/preview/head?"
  for key, value in api_args.items():
    bitmoji_image_url = bitmoji_image_url + key + "=" + str(value) + "&"

  print(bitmoji_image_url)

  # Request bitmoji send us the image for bitmoji_image_url
  image_data = urllib.request.urlopen(bitmoji_image_url).read()
  image_data_as_stream = io.BytesIO(image_data)

  return PIL.Image.open(image_data_as_stream)



def display_image(image):
  root = tkinter.Tk()
  canvas = tkinter.Canvas(root, width=400, height=400)  
  canvas.pack()
  img = ImageTk.PhotoImage(image)
  canvas.create_image(30, 30, anchor=tkinter.NW, image=img)
  root.mainloop()  



# Finally begin executing functions
my_img = get_bitmoji_image();
display_image(my_img)

# We can modify the face...
my_img = get_bitmoji_image(beard=1639);
display_image(my_img)

# All the keys may be passed in using the kwargs synax.
# Remember to read the documentation for the image parameters,
# the code I wrote does not handle errors, so if you pass
# an unknown value for an argument the bitmoji server
# will respond with "HTTP Error 400: Bad Request" and your
# program will crash.
# A mapping of valid values is available in bitmoji_preview_valid_values.json
my_img = get_bitmoji_image(
  beard=1639,
  brow=1546,
  cheek_details=1353,
  ear=1428,
  eye=1610,
)
display_image(my_img)
