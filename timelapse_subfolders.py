
import cv2
import os
from tqdm import tqdm

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory containing the JPG images (same folder as the script)
image_folder = os.path.join(script_dir)  # Update 'path/to/images/' if needed

# Traverse subfolders and collect all JPG images
images = []
for root, dirs, files in os.walk(image_folder):
    for file in files:
        if file.endswith(".jpg"):
            images.append(os.path.join(root, file))

# Sort images in alphanumeric order
images.sort()

if not images:
    print("No JPG images found in the specified directory or subfolders.")
    exit(1)

# Prompt for video resolution
resolution = input("Select video resolution:\n1) 720p\n2) 1080p\n3) 4K\n4) 8K\nEnter the number: ")

# Define the width and codec based on selected resolution
if resolution == '1':
    width = 1280
    resolution_name = '720p'
elif resolution == '2':
    width = 1920
    resolution_name = '1080p'
elif resolution == '3':
    width = 3840
    resolution_name = '4K'
elif resolution == '4':
    width = 7680
    resolution_name = '8K'
else:
    print("Invalid resolution selection. Using default 1080p.")
    width = 1920
    resolution_name = '1080p'

# Prompt for video codec
codec_choice = input("Select video codec:\n1) mp4v\n2) avc1\nEnter the number: ")

# Define the codec based on user choice
if codec_choice == '1':
    codec = 'mp4v'
elif codec_choice == '2':
    codec = 'avc1'
else:
    print("Invalid codec selection. Using default mp4v.")
    codec = 'mp4v'

# Prompt for video quality
quality = int(input("Enter video quality (0-90): "))
if quality < 0 or quality > 90:
    print("Invalid quality value. Using default value of 70.")
    quality = 70

# Prompt for frames per second (FPS) choice
fps_choice = input("Select FPS:\n1) Typical (24 FPS)\n2) 15 FPS\nEnter the number: ")

# Define FPS based on user choice
if fps_choice == '1':
    fps = 24.0
elif fps_choice == '2':
    fps = 15.0
else:
    print("Invalid FPS selection. Using default 24 FPS.")
    fps = 24.0

# Define the video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*codec)

# Read the first image to get its dimensions
first_image_path = images[0]
first_image = cv2.imread(first_image_path)
original_height, original_width, _ = first_image.shape

# Calculate proportional height based on the selected width
height = int((width / original_width) * original_height)

# Create VideoWriter object with calculated dimensions, FPS, and user-defined quality
video = cv2.VideoWriter(f'output_video_{resolution_name}_{codec}_q{quality}_fps{int(fps)}.mp4', fourcc, fps, (width, height), isColor=True)

# Iterate through images, resize, and write to video with a progress bar
with tqdm(total=len(images)) as progress_bar:
    for image_path in images:
        frame = cv2.imread(image_path)
        resized_frame = cv2.resize(frame, (width, height))
        video.write(resized_frame)
        progress_bar.update(1)

# Release the VideoWriter and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
