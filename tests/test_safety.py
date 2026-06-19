"""Engine safety-core tests. Qt-free; run on every push."""

from __future__ import annotations

import pytest

from cherrybomb_engine.net.safety import (
    BAN_SIGNAL_STATUSES,
    AccountBanned,
    KillSwitch,
    VolumeCap,
)


def test_killswitch_trips_on_ban_status():
    ks = KillSwitch("burner1")
    ks.check()  # fine before any signal
    with pytest.raises(AccountBanned):
        ks.inspect_status(403)
    assert ks.tripped
    # stays tripped: every later use raises
    with pytest.raises(AccountBanned):
        ks.check()


@pytest.mark.parametrize("status", sorted(BAN_SIGNAL_STATUSES))
def test_all_ban_signals_trip(status):
    ks = KillSwitch("b")
    with pytest.raises(AccountBanned):
        ks.inspect_status(status)


def test_killswitch_ignores_ok_status():
    ks = KillSwitch("burner2")
    ks.inspect_status(200)
    ks.inspect_status(404)  # not-found is not a ban signal
    assert not ks.tripped


def test_volume_cap_stops_at_limit():
    cap = VolumeCap("burner3", daily_limit=3)
    cap.charge()
    cap.charge()
    cap.charge()
    assert cap.used == 3
    with pytest.raises(AccountBanned):
        cap.charge()
