"""Typed result models.

Scraper output shapes drift constantly as platforms change their responses, so
these models are deliberately PERMISSIVE: unknown fields are kept (``extra="allow"``)
rather than rejected. A strict schema gate over scraper output would red-flag every
legitimate anti-bot-driven change — see the risk register.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Record(BaseModel):
    """One collected item (a post, profile, comment, hit, ...).

    ``platform`` + ``kind`` + ``id`` identify it; ``data`` holds the raw normalized
    fields. Exporters flatten ``data`` into columns/rows.
    """

    model_config = ConfigDict(extra="allow")

    platform: str
    kind: str = "item"
    id: str
    url: str | None = None
    collected_at: datetime | None = None
    data: dict = Field(default_factory=dict)


class ScrapeRequest(BaseModel):
    """A unit of work handed to an adapter."""

    model_config = ConfigDict(extra="allow")

    platform: str
    target: str  # username / URL / query — adapter-defined
    limit: int | None = None
    options: dict = Field(default_factory=dict)
