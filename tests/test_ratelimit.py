"""Token-bucket rate limiter tests. Qt-free, no real sleeps of consequence."""

from __future__ import annotations

import asyncio
import time

from cherrybomb_engine.net.ratelimit import TokenBucket


def test_burst_then_throttle():
    async def run() -> float:
        # 50 tokens/sec, capacity 5: first 5 immediate, 6th waits ~1/50s.
        bucket = TokenBucket(rate=50, capacity=5)
        for _ in range(5):
            await bucket.acquire()
        t0 = time.perf_counter()
        await bucket.acquire()  # must wait for a token to refill
        return time.perf_counter() - t0

    waited = asyncio.run(run())
    assert waited >= 1 / 50 * 0.5  # allow scheduler slop, but it did throttle
