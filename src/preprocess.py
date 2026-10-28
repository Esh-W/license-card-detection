"""Image preprocessing stages used before licence-card OCR."""

from __future__ import annotations

import numpy as np


def to_gray(img: np.ndarray) -> np.ndarray:
    """Convert an image to grayscale.

    Args:
        img: Input colour or grayscale image.

    Returns:
        A single-channel grayscale image.
    """
    raise NotImplementedError


def denoise(img: np.ndarray) -> np.ndarray:
    """Reduce image noise while preserving text edges.

    Args:
        img: Input image.

    Returns:
        A denoised image.
    """
    raise NotImplementedError


def enhance_contrast(img: np.ndarray) -> np.ndarray:
    """Enhance local contrast using a planned CLAHE stage.

    Args:
        img: Input grayscale image.

    Returns:
        A contrast-enhanced image.
    """
    raise NotImplementedError


def binarize(img: np.ndarray) -> np.ndarray:
    """Create a binary representation suitable for OCR.

    Args:
        img: Input grayscale or enhanced image.

    Returns:
        A binary image.
    """
    raise NotImplementedError


def preprocess_for_ocr(img: np.ndarray) -> np.ndarray:
    """Run the complete planned preprocessing sequence for OCR.

    Args:
        img: Rectified card image.

    Returns:
        The preprocessed image ready for OCR.
    """
    raise NotImplementedError

