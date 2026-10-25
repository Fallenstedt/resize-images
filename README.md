# Bulk Image Resizer

This tool makes images smaller.

The `resize-images` command reads each image in the current directory. It changes the size of the image. The longest side of the new image is 1200 pixels or less. The tool keeps the aspect ratio. Then the tool writes the new image to a `resized` directory in the current directory. The new file has the same name and the same format as the original file.

The tool does not change the original files.

## System requirements

- macOS, Linux, or Windows.
- Python 3.10 or later. Python 3.14 is tested.
- The `pip` package installer. Python includes `pip`.
- `pipx` (recommended). `pipx` installs the command one time for all directories.

The installation also installs the Pillow library.

## Install the command

Use one of these two procedures.

### Procedure A: Install with pipx (recommended)

1. Install `pipx`. On macOS, use this command:

   ```sh
   brew install pipx
   pipx ensurepath
   ```

   For other systems, see <https://pipx.pypa.io>.

2. Close the terminal. Then open a new terminal.

3. Install the tool from the project directory:

   ```sh
   pipx install /path/to/bulk-image-resizer
   ```

The `resize-images` command is now available in all directories.

### Procedure B: Install in a virtual environment

1. Open a terminal in the project directory.

2. Make the virtual environment:

   ```sh
   python3 -m venv venv
   ```

3. Start the virtual environment:

   ```sh
   source venv/bin/activate
   ```

   On Windows, use this command:

   ```bat
   venv\Scripts\activate
   ```

4. Install the tool:

   ```sh
   pip install .
   ```

The `resize-images` command is available only when the virtual environment is active.

NOTE: If you move the project directory, the virtual environment stops working. Delete the `venv` directory. Then do steps 2 to 4 again.

## Run the command

1. Go to the directory that contains your images:

   ```sh
   cd ~/Pictures/my-photos
   ```

2. Run the command:

   ```sh
   resize-images
   ```

3. Get the new images from the `resized` directory.

The command shows one line for each image that it resizes:

```
Processed: photo1.jpg
```

To use a different maximum size, use the `--max-size` option. This example makes the longest side 800 pixels or less:

```sh
resize-images --max-size 800
```

To see all options, use this command:

```sh
resize-images --help
```

## Supported file types

The tool uses files that end in these extensions. Uppercase and lowercase are both correct.

- `.jpg` and `.jpeg`
- `.png`
- `.webp`
- `.tif` and `.tiff`
- `.bmp`

The tool does not use other files.

## Limits

- The tool does not use images in subdirectories.
- The tool replaces a file in `resized` if a file with the same name is there.
- The tool writes JPEG images at quality 85.
- The tool turns photos to the correct orientation. The new files do not keep the EXIF data (for example, the camera model, the date, and the GPS location).

## Remove the command

If you used Procedure A, use this command:

```sh
pipx uninstall bulk-image-resizer
```

If you used Procedure B, delete the `venv` directory.
