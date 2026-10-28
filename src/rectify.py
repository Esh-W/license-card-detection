"""Order card corners and prepare perspective-corrected images."""

from __future__ import annotations

import numpy as np


def order_corners(pts: np.ndarray) -> np.ndarray:
    """Order four corners as top-left, top-right, bottom-right, bottom-left.

    Args:
        pts: Four unordered ``(x, y)`` corner coordinates.

    Returns:
        The corners in a consistent clockwise order.

    Raises:
        NotImplementedError: Corner ordering is not implemented yet.
    """
    raise NotImplementedError


def rectify(
    img: np.ndarray,
    corners: np.ndarray,
    size: tuple[int, int] = (1012, 638),
) -> np.ndarray:
    """Apply a perspective transform to a detected licence card.

    Args:
        img: Input image containing the card.
        corners: Four card-corner coordinates.
        size: Output ``(width, height)`` in pixels.

    Returns:
        A perspective-corrected card image.

    Raises:
        NotImplementedError: Rectification is not implemented yet.
    """
    raise NotImplementedError

