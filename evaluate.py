"""Evaluation metric interfaces for card detection and OCR experiments."""

from __future__ import annotations

from typing import Mapping, Sequence

import numpy as np


def intersection_over_union(
    predicted: np.ndarray,
    target: np.ndarray,
) -> float:
    """Compute bounding-box or mask intersection over union.

    Args:
        predicted: Predicted region.
        target: Ground-truth region.

    Returns:
        IoU score in the range from zero to one.
    """
    raise NotImplementedError


def corner_error(predicted: np.ndarray, target: np.ndarray) -> float:
    """Compute geometric error between predicted and target corners.

    Args:
        predicted: Predicted corner coordinates.
        target: Ground-truth corner coordinates.

    Returns:
        Corner error in pixels.
    """
    raise NotImplementedError


def character_error_rate(reference: str, hypothesis: str) -> float:
    """Compute character error rate for an OCR prediction.

    Args:
        reference: Ground-truth transcription.
        hypothesis: Predicted transcription.

    Returns:
        Character error rate.
    """
    raise NotImplementedError


def word_error_rate(reference: str, hypothesis: str) -> float:
    """Compute word error rate for an OCR prediction.

    Args:
        reference: Ground-truth transcription.
        hypothesis: Predicted transcription.

    Returns:
        Word error rate.
    """
    raise NotImplementedError


def field_accuracy(
    references: Mapping[str, str],
    predictions: Mapping[str, str],
) -> float:
    """Compute exact-match accuracy across named card fields.

    Args:
        references: Ground-truth field values.
        predictions: Predicted field values.

    Returns:
        Fraction of reference fields predicted exactly.
    """
    raise NotImplementedError


def evaluate_dataset(
    predictions: Sequence[Mapping[str, object]],
    references: Sequence[Mapping[str, object]],
) -> Mapping[str, float]:
    """Aggregate all planned metrics over a dataset.

    Args:
        predictions: Per-image predicted values.
        references: Per-image ground-truth values.

    Returns:
        A mapping of metric names to aggregate scores.
    """
    raise NotImplementedError

