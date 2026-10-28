"""Detect licence-card boundaries and expose corner-visualisation helpers."""

from __future__ import annotations

import numpy as np


def find_card_contour(img: np.ndarray) -> np.ndarray | None:
    """Find the contour corresponding to a licence card.

    Args:
        img: Input BGR or grayscale image.

    Returns:
        The detected card contour, or ``None`` when no card is found.

    Raises:
        NotImplementedError: Detection is not implemented yet.
    """
    raise NotImplementedError


def draw_corners(img: np.ndarray, corners: np.ndarray) -> np.ndarray:
    """Draw detected card corners on a copy of an image.

    Args:
        img: Input image.
        corners: Four card-corner coordinates.

    Returns:
        An image containing the drawn corners.

    Raises:
        NotImplementedError: Drawing is not implemented yet.
    """
    raise NotImplementedError

