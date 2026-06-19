"""Headless CLI entry point (F8).

Runs the EXACT same adapters the GUI uses — no duplicated scraper logic. Used both
for headless/automated runs and by the scheduled CI canary that detects scraper
breakage before users do.

    python -m cherrybomb_engine list
    python -m cherrybomb_engine scrape <platform> <target> [--limit N]
"""

from __future__ import annotations

import argparse
import asyncio
import sys

from .models import ScrapeRequest
from .registry import available, create, load_adapters


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cherrybomb-engine", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="list registered scrapers")

    s = sub.add_parser("scrape", help="run a scraper and stream JSONL to stdout")
    s.add_argument("platform")
    s.add_argument("target")
    s.add_argument("--limit", type=int, default=None)
    return p


async def _run_scrape(platform: str, target: str, limit: int | None) -> int:
    scraper = create(platform)
    req = ScrapeRequest(platform=platform, target=target, limit=limit)
    n = 0
    async for record in scraper.scrape(req):
        sys.stdout.write(record.model_dump_json() + "\n")
        n += 1
    sys.stderr.write(f"collected {n} records\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    load_adapters()
    args = _build_parser().parse_args(argv)

    if args.cmd == "list":
        for name in available():
            print(name)
        return 0

    if args.cmd == "scrape":
        return asyncio.run(_run_scrape(args.platform, args.target, args.limit))

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
