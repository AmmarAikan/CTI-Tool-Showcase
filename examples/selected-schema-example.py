"""Reduced CTI schema example for technical demonstration.

This is not the complete CTI-Tool implementation.
Copyright © 2026 CTI-Tool Project Contributors. All Rights Reserved.
"""

from dataclasses import asdict, dataclass, field
from typing import Literal


PipelineName = Literal["external", "internal"]


@dataclass(frozen=True, slots=True)
class Indicator:
    value: str
    type: str
    confidence: float
    extractor: str


@dataclass(slots=True)
class CTIObject:
    source_id: str
    source_type: str
    source_pipeline: PipelineName
    title: str
    classification_label: str | None = None
    indicators: list[Indicator] = field(default_factory=list)
    processing_status: str = "collected"

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
