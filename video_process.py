import cv2
import random
ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'


def convet(pix):
    # import math
    # return math.ceil((len(ASCII_CHARS) - 1) * pix / 255)
    return pix // 25

def pixels_to_ascii(frame):
    ascii_str = ''
    for row in frame:
        ascii_str+='data:'
        for pixel_value in row:
            ascii_str += ASCII_CHARS[::-1][convet(pixel_value)]
        ascii_str += '\n'
    return ascii_str.strip()


def grayify(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_frame

def contrastify(frame):
    return cv2.equalizeHist(frame)

def invert_pixels(frame):
    return 255 - frame


def process_bin_image(frame):
    resized_frame = resize_image(frame)
    gray_frame = grayify(resized_frame)
    contrasted = contrastify(gray_frame)
    inverted = invert_pixels(contrasted)
    ascii_art = pixels_to_ascii(inverted)
    return ascii_art


def resize_image(frame, new_width=100):
    (original_height, original_width, _) = frame.shape
    aspect_ratio = original_width / float(original_height)
    new_height = int(new_width / aspect_ratio)
    new_frame = cv2.resize(frame, (new_width, new_height))
    return new_frame


def generate_stream(video=None):
    if not video:
        name = f"./videos/test-vid{random.randint(1, 7)}.mp4"
        print(name)
    # name = './videos/test-vid3.mp4'
    video_capture = cv2.VideoCapture(name)
    while video_capture.isOpened():
        success, frame = video_capture.read()
        if not success:
            break
        processed_frame = process_bin_image(frame)
        yield f"{processed_frame}\n\n"

    video_capture.release()
