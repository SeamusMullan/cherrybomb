"""Account-safety core: kill-switch + per-account daily volume caps.

Design rule (from red-team evidence): the FIRST time a platform returns an auth /
block / checkpoint signal for an account, STOP using that account immediately. Do
not retry, do not back off and continue — a banned account is unrecoverable, and
each extra request deepens the ban. Retrying transient *network* errors is fine and
handled separately (tenacity); this module is only about platform-level account
hostility.
"""

from __future__ import annotations

# HTTP statuses that mean "this account/session is in trouble" — trip the switch.
BAN_SIGNAL_STATUSES = frozenset({401, 403, 429})


class AccountBanned(RuntimeError):
    """Raised when an account hits a ban/checkpoint signal. Terminal for that account."""

    def __init__(self, account: str, reason: str) -> None:
        self.account = account
        self.reason = reason
        super().__init__(f"account {account!r} disabled: {reason}")


class KillSwitch:
    """One per account. Once tripped, every further use raises AccountBanned.

    Adapters MUST call ``check()`` before each request and ``inspect_status()`` /
    ``trip()`` after responses. A tripped switch never un-trips for the session.
    """

    def __init__(self, account: str) -> None:
        self.account = account
        self._tripped: str | None = None

    @property
    def tripped(self) -> bool:
        return self._tripped is not None

    def check(self) -> None:
        if self._tripped is not None:
            raise AccountBanned(self.account, self._tripped)

    def trip(self, reason: str) -> None:
        if self._tripped is None:
            self._tripped = reason
        raise AccountBanned(self.account, self._tripped)

    def inspect_status(self, status_code: int) -> None:
        """Trip if a response status is a ban signal."""
        if status_code in BAN_SIGNAL_STATUSES:
            self.trip(f"HTTP {status_code} (ban/checkpoint signal)")


class VolumeCap:
    """Per-account daily request ceiling. A default, not an option.

    Caller increments per request; raises AccountBanned-style stop when exceeded so
    aggressive runs cannot quietly hammer an account into a ban.
    """

    def __init__(self, account: str, daily_limit: int = 500) -> None:
        self.account = account
        self.daily_limit = daily_limit
        self._count = 0

    def charge(self, n: int = 1) -> None:
        self._count += n
        if self._count > self.daily_limit:
            raise AccountBanned(
                self.account,
                f"daily volume cap reached ({self.daily_limit})",
            )

    @property
    def used(self) -> int:
        return self._count
