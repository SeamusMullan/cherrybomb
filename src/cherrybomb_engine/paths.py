"""Per-OS path resolution. NEVER hardcode paths.

Program Files and read-only AppImage squashfs mounts are non-writable, so the
browser cache and runtime state MUST live in a writable user dir. platformdirs
gives the correct location on every OS.
"""

from __future__ import annotations

from pathlib import Path

from platformdirs import PlatformDirs

_dirs = PlatformDirs(appname="cherrybomb", appauthor=False)


def data_dir() -> Path:
    p = Path(_dirs.user_data_dir)
    p.mkdir(parents=True, exist_ok=True)
    return p


def cache_dir() -> Path:
    p = Path(_dirs.user_cache_dir)
    p.mkdir(parents=True, exist_ok=True)
    return p


def browser_cache_dir() -> Path:
    """Writable location Playwright/Patchright browsers are relocated to.

    Wired to PLAYWRIGHT_BROWSERS_PATH at runtime in the packaged FULL build.
    """
    p = cache_dir() / "browsers"
    p.mkdir(parents=True, exist_ok=True)
    return p
