"""GATE C — packaging + relocated-browser launch spike (throwaway).

Question: does a PyInstaller-frozen app resolve its per-OS resource paths AND
actually LAUNCH a relocated browser on a clean/minimal machine, on every OS×ARCH?

This is the load-bearing pillar for IG/X: PyInstaller does NOT collect the per-user
Playwright browser cache, the path differs across .app / AppImage-squashfs /
Program Files, and several of those dirs are non-writable. So the mechanism is:
  PLAYWRIGHT_BROWSERS_PATH -> a WRITABLE platformdirs cache (set at runtime), and
  for the FULL build a PyInstaller runtime hook repoints it before any browser call.

This script has two modes:
  --self-test   : verify writable-path resolution + (if installed) launch a browser
                  and load about:blank. Exits non-zero on failure. CI runs this
                  inside the frozen onedir on a MINIMAL distro container.
  (default)     : print the plan.

In Phase 0 the browser launch is best-effort: if patchright/playwright is not
installed (lean build), the path-resolution half must still pass.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _writable(path: Path) -> bool:
    try:
        path.mkdir(parents=True, exist_ok=True)
        probe = path / ".write_probe"
        probe.write_text("ok")
        probe.unlink()
        return True
    except OSError:
        return False


def self_test() -> int:
    # 1) resolve a writable browser cache via the same code the app uses.
    try:
        # Works when run from the installed package; falls back for raw spike runs.
        from cherrybomb_engine.paths import browser_cache_dir

        cache = browser_cache_dir()
    except ImportError:
        from platformdirs import user_cache_dir

        cache = Path(user_cache_dir("cherrybomb", False)) / "browsers"
        cache.mkdir(parents=True, exist_ok=True)

    print(f"GATE C: browser cache dir = {cache}")
    if not _writable(cache):
        print("GATE C: FAIL — browser cache dir is not writable")
        return 1

    # 2) point Playwright/Patchright at it and try a real launch.
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = str(cache)
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("GATE C: PASS (path-resolution only; no browser lib in this build)")
        return 0

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("about:blank")
            title = page.title()
            browser.close()
        print(f"GATE C: PASS — launched relocated Chromium, loaded page (title={title!r})")
        return 0
    except Exception as exc:  # noqa: BLE001 — spike wants the raw failure surfaced
        print(f"GATE C: FAIL — browser launch error: {exc}")
        return 1


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--self-test" in argv:
        return self_test()
    print(__doc__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
