"""End-to-end licence-card pipeline interface and command-line entry point."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def process_image(
    image: np.ndarray,
    output_dir: str | Path | None = None,
) -> dict[str, object]:
    """Run detection, rectification, preprocessing, and OCR on one image.

    Args:
        image: Input image.
        output_dir: Optional directory for intermediate and final outputs.

    Returns:
        A result dictionary containing planned pipeline outputs.
    """
    raise NotImplementedError


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser for the pipeline."""
    parser = argparse.ArgumentParser(
        description="Licence card detection, rectification, and OCR pipeline."
    )
    parser.add_argument("image", type=Path, help="Path to an input image.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory for generated outputs.",
    )
    return parser


def main() -> None:
    """Parse command-line arguments and run the planned pipeline."""
    parser = build_parser()
    parser.parse_args()
    raise NotImplementedError("The pipeline has not been implemented yet.")


if __name__ == "__main__":
    main()

