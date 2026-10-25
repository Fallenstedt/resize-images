import argparse
import os
from PIL import Image, ImageOps

# Configuration
output_dirname = 'resized'
default_max_size = 1200
extensions = ('.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff', '.bmp')


def resize_images(input_directory, max_size):
    output_directory = os.path.join(input_directory, output_dirname)
    os.makedirs(output_directory, exist_ok=True)

    for filename in sorted(os.listdir(input_directory)):
        file_path = os.path.join(input_directory, filename)
        if not os.path.isfile(file_path) or not filename.lower().endswith(extensions):
            continue

        with Image.open(file_path) as img:
            image_format = img.format
            # Apply the EXIF rotation, because the saved file has no EXIF data
            img = ImageOps.exif_transpose(img)
            img.thumbnail((max_size, max_size))

            # Save resized image in its original format
            save_path = os.path.join(output_directory, filename)
            if image_format == 'JPEG':
                img.save(save_path, 'JPEG', quality=85)
            else:
                img.save(save_path, image_format)
            print(f"Processed: {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Resize all images in the current directory into ./resized."
    )
    parser.add_argument(
        '--max-size', type=int, default=default_max_size,
        help=f"maximum length of the longest side, in pixels (default: {default_max_size})",
    )
    args = parser.parse_args()
    resize_images(os.getcwd(), args.max_size)


if __name__ == "__main__":
    main()
