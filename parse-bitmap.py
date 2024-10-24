#!/usr/bin/env python

import argparse
import sys

from PIL import Image


def _get_args() -> argparse.Namespace:
    """Get command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bitmap_file",
        type=str,
        metavar="FILENAME",
        help="Bitmap filename",
    )
    parser.add_argument(
        "-x",
        type=int,
        metavar="X",
        help="X coordinate of the centre of the image",
    )
    parser.add_argument(
        "-y",
        type=int,
        metavar="Y",
        help="Y coordinate of the centre of the image",
    )
    args = parser.parse_args()
    return args


def main() -> None:
    """Main function."""
    args = _get_args()
    img = Image.open(args.bitmap_file)
    print(f"Format: {img.format}")
    width, height = img.size
    print(f"Width: {width}")
    print(f"Height: {height}")
    print(f"Mode: {img.mode}")
    if img.mode != "L":
        sys.exit("Error: only use greyscale images for now!")

    if args.x is not None and args.y is not None:
        centre = (args.x, args.y)
        max_side_length = min(width - args.x, height - args.y)
    else:
        centre = (width // 2, height // 2)
        max_side_length = min(width, height)
    print(f"Centre: {centre}")

    # Get the pixel value at the centre of the image
    pixel = img.getpixel(centre)
    print(f"Pixel value at centre: {pixel}")

    ratios: list[float] = []

    for length in range(3, max_side_length + 1, 2):
        box = (
            centre[0] - length // 2,
            centre[1] - length // 2,
            centre[0] + length // 2 + 1,
            centre[1] + length // 2 + 1,
        )
        print(f"Size: {length} Box: {box}")
        region = img.crop(box)
        region_data = list(region.getdata())
        print(f"Region data length: {len(region_data)}")
        print(f"Region size: {region.size}")
        # print(f"Region data: {region_data}")
        print(f"len^2: {length**2}")
        assert len(region_data) == length**2
        num_zeros = region_data.count(0)
        ratio = num_zeros / (length**2)
        ratios.append(ratio)

    print(f"Ratios: {ratios}")


if __name__ == "__main__":
    main()
