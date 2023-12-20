import cv2
from PIL import Image, ImageDraw, ImageFont

# Define ASCII characters for different levels of shading
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Function to resize the image to a smaller size for better ASCII representation
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Function to convert a pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Function to convert each pixel to an ASCII character
def pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value // 25]
    return ascii_str


from main import process_bin_image

# Function to convert video frames to ASCII art frames
def video_to_ascii(video_path):
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        cv2.imwrite("temp_frame.png", frame)
        image = Image.open("temp_frame.png")
        yield process_bin_image(image)
        # Resize the frame
    #     image = resize_image(image, frame_width)

    #     # Convert the frame to grayscale
    #     image = grayify(image)

    #     # Convert pixels to ASCII
    #     ascii_str = pixels_to_ascii(image)

    #     # Create an ASCII image and save it
    #     ascii_image = Image.new("RGB", image.size, (255, 255, 255))
    #     d = ImageDraw.Draw(ascii_image)
    #     font = ImageFont.load_default()
    #     d.text((0, 0), ascii_str, fill=(0, 0, 0), font=font)
    #     ascii_image.save(f"{output_path}/frame_{frame_count}.png")

    #     frame_count += 1

    # video_capture.release()

if __name__ == "__main__":
    video_path = "test-vid.mp4"
    output_path = "output_frames"
    frame_width = 100
    video_to_ascii(video_path, output_path, frame_width)
