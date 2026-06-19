"""GATE B — X/IG anti-bot durability probe (throwaway, 2-week run).

THE REAL PRODUCT-VIABILITY GATE. Reddit working proves the plumbing; THIS proves the
product thesis. Question: "Can we reliably pull ONE X timeline and ONE IG profile,
once per day, for 14 days straight, without the accounts dying?"

Operational requirements (per risk register — do NOT skip):
  * BURNER accounts only — they may (will) get banned. Never real accounts.
  * RESIDENTIAL proxies — datacenter / CI IPs are auto-flagged. Required, not optional.
  * Patchright (rebrowser-patched Playwright) for the browser path; curl_cffi TLS
    impersonation for the direct path.
  * Run from NON-CI residential egress (this is why it is a local/long-running spike,
    not a CI job).

This file is the harness + run log; it deliberately does NOT hardcode endpoints or
credentials. Fill in CONFIG from a local, gitignored secrets file and run daily
(cron / Task Scheduler). It appends a JSONL outcome line per attempt so you can chart
the break/ban rate at the end of the 2 weeks and make a go/no-go call.

Pass: an honest verdict that durability is good enough to build Phase 2 on — OR a
no-go that saves months. Either outcome is a successful gate.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Outcomes accumulate here (gitignored). Chart break-rate from this at day 14.
LOG = Path(__file__).with_name("gate_b_log.jsonl")


def record(platform: str, ok: bool, detail: str) -> None:
    """Append one attempt outcome."""
    line = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "platform": platform,
        "ok": ok,
        "detail": detail,
    }
    with LOG.open("a") as f:
        f.write(json.dumps(line) + "\n")


def summarize() -> int:
    """Print break/ban rate from the accumulated log; the basis for go/no-go."""
    if not LOG.exists():
        print("GATE B: no attempts logged yet")
        return 1
    rows = [json.loads(line) for line in LOG.read_text().splitlines() if line.strip()]
    by_platform: dict[str, list[bool]] = {}
    for r in rows:
        by_platform.setdefault(r["platform"], []).append(bool(r["ok"]))
    for plat, results in by_platform.items():
        n = len(results)
        ok = sum(results)
        print(f"GATE B {plat}: {ok}/{n} successful ({100 * ok / n:.0f}%)")
    print("GATE B: review break-rate and make a documented go/no-go call.")
    return 0


# --- attempt stubs: implement against burner creds from a local secrets file ---
def attempt_x() -> None:
    """Pull one X timeline via the http-replay harness / official API / Patchright.
    Record outcome. NOT IMPLEMENTED — wire to burner creds + residential proxy."""
    raise NotImplementedError("wire to burner X session + residential proxy")


def attempt_instagram() -> None:
    """Pull one IG profile via instaloader + Patchright fallback. Record outcome.
    NOT IMPLEMENTED — wire to burner IG session + residential proxy."""
    raise NotImplementedError("wire to burner IG session + residential proxy")


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] == "summary":
        return summarize()
    print(__doc__)
    print("\nThis is a long-running operational probe, not a one-shot test.")
    print("Schedule attempt_x() + attempt_instagram() daily for 14 days, then:")
    print("    python spikes/gate_b_antibot.py summary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
