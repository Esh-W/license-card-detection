"""Shared image loading, annotation, and output-saving interfaces."""

from __future__ import annotations

from pathlib import Path

import numpy as np


def load_image(path: str | Path) -> np.ndarray:
    """Load an image from disk.

    Args:
        path: Path to an image file.

    Returns:
        The loaded image as a NumPy array.
    """
    raise NotImplementedError


def draw_box(img: np.ndarray, points: np.ndarray) -> np.ndarray:
    """Draw a polygon or bounding box on a copy of an image.

    Args:
        img: Input image.
        points: Polygon or bounding-box coordinates.

    Returns:
        An annotated image.
    """
    raise NotImplementedError


def save_image(img: np.ndarray, path: str | Path) -> None:
    """Save an image to disk.

    Args:
        img: Image to save.
        path: Destination path.
    """
    raise NotImplementedError

