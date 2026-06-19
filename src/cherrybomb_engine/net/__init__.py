"""net/ — cross-cutting anti-bot + SAFETY plumbing shared by all adapters.

The safety core is NOT optional polish. Per the red-team's live evidence
(instaloader #2680: perma-ban after a single download), an account that keeps
scraping through a 401/403/checkpoint gets permanently banned. So the kill-switch
and per-account volume caps live here, in shared code, and every adapter routes
through them.
"""

from .ratelimit import TokenBucket
from .safety import AccountBanned, KillSwitch, VolumeCap

__all__ = ["AccountBanned", "KillSwitch", "VolumeCap", "TokenBucket"]
