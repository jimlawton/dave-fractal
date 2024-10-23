#!/usr/bin/env python

import argparse


def _get_args() -> argparse.Namespace:
    """Get command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bitmap_file",
        type=str,
        metavar="FILENAME",
        nargs="+",
        help="Bitmap filename",
    )
    args = parser.parse_args()
    return args


def main() -> None:
    """Main function."""
    args = _get_args()


if __name__ == "__main__":
    main()
