import time
import base64
import cv2
import numpy as np

from os import path
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, render_template, request, Response


frontend_path = 'static'

app = Flask(__name__, template_folder=frontend_path)

from video import video_to_ascii

ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'


from io import BytesIO
import numpy as np
import math

def convet(pix):
    # return math.ceil((len(ASCII_CHARS) - 1) * pix / 255)
    return pix // 25
    # return pix // 21

def pixels_to_ascii(frame):
    """Map each pixel in the OpenCV frame to an ASCII char."""
    ascii_str = ''
    for row in frame:
        ascii_str+='data:'
        for pixel_value in row:
            ascii_str += ASCII_CHARS[::-1][convet(pixel_value)]
        ascii_str += '\n'
    return ascii_str.strip()


def grayify(frame):
    """Convert the OpenCV frame to grayscale."""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_frame

def contrastify(frame):
    return cv2.equalizeHist(frame)

def invert_pixels(frame):
    return 255 - frame


def process_bin_image(frame):
    """Process the OpenCV frame and generate ASCII art from it."""
    # Resize the frame
    resized_frame = resize_image(frame)

    # Convert the frame to grayscale
    gray_frame = grayify(resized_frame)

    contrasted = contrastify(gray_frame)
    inverted = invert_pixels(contrasted)

    # Convert grayscale frame to ASCII art
    ascii_art = pixels_to_ascii(inverted)
    return ascii_art


def resize_image(frame, new_width=200):
    """Resize the OpenCV frame to the given width and adjust the height to maintain the aspect ratio."""
    (original_height, original_width, _) = frame.shape
    aspect_ratio = original_width / float(original_height)
    new_height = int(new_width / aspect_ratio)
    new_frame = cv2.resize(frame, (new_width, new_height))
    return new_frame

def generate_stream():
    video_capture = cv2.VideoCapture('test-vid3.mp4')

    while video_capture.isOpened():
        success, frame = video_capture.read()

        if not success:
            break

        # Process the frame using process_bin_image and convert it to a binary string
        processed_frame = process_bin_image(frame)
        yield f"{processed_frame}\n\n"

    video_capture.release()



@app.route('/')
def index():
    return render_template('template.html')

@app.route('/stream')
def stream():
    return Response(generate_stream(), content_type='text/event-stream')


if __name__ == "__main__":
    app.run(debug=True)
