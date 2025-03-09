import cv2
import numpy as np

# Set the background image (use a path to your image)
background_image = "background.jpg"  # Replace with your background image path
output_video = "final_video.mp4"

# Read the background image
img = cv2.imread(background_image)

# Set the frame width, height and codec for video
frame_height, frame_width, _ = img.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, 1, (frame_width, frame_height))

# Generate 10-15 seconds of a blank video with background
for i in range(30):  # 30 frames for 30 FPS for 1 second video
    out.write(img)

# Release the video writer object
out.release()
print(f"Video saved as {output_video}")
