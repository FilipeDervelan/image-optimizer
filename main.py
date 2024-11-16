import os
from PIL import Image, ImageOps


max_size = 1 * 1024 * 1024

quality = 95

img = Image.open("image.jpg")

# Adjusts the image to be vertical
img = ImageOps.exif_transpose(img)

original_size = os.path.getsize("image.jpg")

print(f"Original image size: {original_size / (1024 * 1024):.2f} MB")

while quality > 10:
    img.save("image_temp.jpg", quality=quality, optimize=True)

    file_size = os.path.getsize("image_temp.jpg")

    if file_size <= max_size:
        os.rename("image_temp.jpg", "image_output.jpg")

        print(
            f"Image saved with quality {quality}% and the size {file_size / 1024:.2f} KB"
        )

        break

    quality -= 5

if quality <= 10:
    print("Unable to reduce image below 1 MB with acceptable quality.")
