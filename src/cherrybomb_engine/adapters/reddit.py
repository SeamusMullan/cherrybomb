"""Reddit adapter — Phase 1, the pipeline de-risker.

Reddit has an official OAuth API (PRAW), low ban risk, clean data. Its job is to
prove the spawn -> scrape -> stream -> render -> export pipeline end-to-end. It is
EXPLICITLY NOT proof that the X/IG anti-bot thesis is tractable — that is settled by
the Phase-0 anti-bot probe (Gate B), not by Reddit working.

STATUS: skeleton. Open question before relying on it: verify PRAW's post-2023
free-tier rate caps / data-access terms are adequate for OSINT-scale use.
"""

from __future__ import annotations

from collections.abc import AsyncIterator

from ..models import Record, ScrapeRequest
from ..registry import register


@register("reddit")
class RedditScraper:
    """Official-API Reddit collector (PRAW). Filled in during Phase 1."""

    async def scrape(self, request: ScrapeRequest) -> AsyncIterator[Record]:
        # Phase 1 implementation goes here:
        #   - load praw lazily (optional dep; absent in lean build)
        #   - authenticate via stored OAuth creds
        #   - route requests through net/ TokenBucket + VolumeCap + KillSwitch
        #   - yield Record(platform="reddit", kind=..., id=..., data=...)
        raise NotImplementedError("Reddit adapter lands in Phase 1")
        yield  # pragma: no cover  (marks this an async generator)
