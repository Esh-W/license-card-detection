"""OCR adapter and licence-card field extraction interfaces."""

from __future__ import annotations

from typing import TypeAlias

import numpy as np

OCRResult: TypeAlias = tuple[np.ndarray, str, float]


def run_ocr(img: np.ndarray) -> list[OCRResult]:
    """Run the configured OCR engine on an image.

    Args:
        img: Image prepared for OCR.

    Returns:
        OCR detections as ``(bbox, text, confidence)`` tuples.
    """
    raise NotImplementedError


def extract_fields(results: list[OCRResult]) -> dict[str, str]:
    """Map OCR detections to the project's licence-card fields.

    Args:
        results: OCR detections returned by :func:`run_ocr`.

    Returns:
        A mapping of field names to extracted text.
    """
    raise NotImplementedError

