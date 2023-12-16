from PIL import Image
import numpy as np

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# First, we load the image
image_path = '/mnt/data/1.jpeg'
image = Image.open(image_path)

# Define the resize function
def resize_image(image, new_width=100):
    """Resize the image to the given width and adjust the height to maintain the aspect ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

# Define the grayscale function
def grayify(image):
    """Convert the image to grayscale."""
    grayscale_image = image.convert("L")
    return grayscale_image

# Define the function to create ASCII art
def pixels_to_ascii(image):
    """Map each pixel to an ASCII char."""
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

# Process the image
image = resize_image(image)
image = grayify(image)
ascii_str = pixels_to_ascii(image)

# Split the string based on width of the image
img_width = image.width
ascii_str_len = len(ascii_str)
ascii_img=""

# Split the ASCII string into lines that match the image width
for i in range(0, ascii_str_len, img_width):
    ascii_img += ascii_str[i:i+img_width] + "\n"

# Save the string to a file
with open("/mnt/data/ascii_image.txt", "w") as f:
    f.write(ascii_img)

ascii_img_path = "/mnt/data/ascii_image.txt"
ascii_img_path
