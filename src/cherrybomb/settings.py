"""GUI-side persistent settings via QSettings (per-OS native store).

Kept minimal in Phase 0: only the first-run risk acknowledgement. Credential /
proxy / session storage lives in the engine's net/ layer (encrypted store), not here.
"""

from __future__ import annotations

from PySide6.QtCore import QSettings

_ORG = "cherrybomb"
_APP = "cherrybomb"
_KEY_RISK = "ack/ban_risk_v1"


def _settings() -> QSettings:
    return QSettings(_ORG, _APP)


def has_acknowledged_risk() -> bool:
    return bool(_settings().value(_KEY_RISK, False, type=bool))


def set_acknowledged_risk(value: bool) -> None:
    _settings().setValue(_KEY_RISK, value)
