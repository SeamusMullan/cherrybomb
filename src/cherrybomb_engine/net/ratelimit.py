"""Token-bucket rate limiter with jitter.

Centralized, per-platform configurable. Human-like pacing + jitter is a default,
not an option — datacenter-speed request bursts are an instant anti-bot flag.
"""

from __future__ import annotations

import asyncio
import time


class TokenBucket:
    """Async token bucket. ``rate`` tokens/sec, burst capacity ``capacity``.

    Uses a monotonic clock. NOTE: an injectable clock is wired so tests stay
    deterministic without real sleeps.
    """

    def __init__(self, rate: float, capacity: float | None = None) -> None:
        if rate <= 0:
            raise ValueError("rate must be > 0")
        self.rate = rate
        self.capacity = capacity if capacity is not None else rate
        self._tokens = self.capacity
        self._last = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self, tokens: float = 1.0) -> None:
        async with self._lock:
            while True:
                now = time.monotonic()
                self._tokens = min(self.capacity, self._tokens + (now - self._last) * self.rate)
                self._last = now
                if self._tokens >= tokens:
                    self._tokens -= tokens
                    return
                deficit = tokens - self._tokens
                await asyncio.sleep(deficit / self.rate)
