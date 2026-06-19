# cherrybomb

A cross-platform desktop application for data collection from social-media platforms
and other OSINT sources.

cherrybomb is intended for ethical hackers, data scientists, machine-learning
engineers, researchers and journalists who need large amounts of public data from
social platforms. The makers and contributors do **not** condone malicious or violent
use. Using tools like cherrybomb for exploitation, blackmail, threatening, stalking or
similar is forbidden — see [`ACCEPTABLE_USE.md`](ACCEPTABLE_USE.md).

> ⚠️ **Account-ban warning.** Scraping social platforms with a real account will very
> likely get it **permanently banned** — often after a single run. **Use a disposable
> burner account you can afford to lose.** Scraping login-walled platforms may also
> violate their Terms of Service and your local law; you are responsible for your use.
> See [`LEGAL.md`](LEGAL.md). cherrybomb ships no accounts and guarantees no scraper
> works at any given time.

## Status

Early development, mid-rewrite. The original C++/WebView prototype has been replaced
(see below). Expect breakage; nothing is stable yet.

## Tech stack

cherrybomb is a **single-language Python** application:

- **GUI** — [PySide6](https://doc.qt.io/qtforpython/) (Qt 6 Widgets). Native rendering,
  **no webview** — chosen for low memory and mature data-visualization primitives
  (`QTableView`, `QGraphicsView`, `QtCharts`). The webview prototype was dropped.
- **Engine** — a GUI-agnostic Python scraping package (`cherrybomb_engine`) that also
  runs headless (`python -m cherrybomb_engine`) and powers a CI breakage canary. The
  GUI and the scrapers are the **same language**, so contributing a scraper never
  means touching GUI code.
- **Builds** — heavy per-OS packaging (PyInstaller, signing, notarization) runs in
  **GitHub Actions CI**, not on dev machines.

Why the change from C++/WebView? The owner's constraints are: develop on WSL2 but
build elsewhere, ship a low-memory **native** (non-webview) cross-platform GUI, and
work in the language where the OSINT ecosystem actually lives. PySide6 satisfies all
three; the saucer/webview C++ prototype satisfied none.

### Platform support (ship order)

| Platform | Status |
|----------|--------|
| Reddit | Phase 1 — official API (PRAW). Low ban risk. The plumbing de-risker. |
| Instagram | Phase 2 — **best-effort, account-at-risk.** The single v1 anti-bot platform. |
| Twitter/X | Post-v1 — **best-effort, frequently broken.** Maintainer-owned (no abandoned OSS lib). Official paid API supported. |
| Username enumeration (sherlock-style) | Post-v1. |

## Architecture

```
src/
  cherrybomb/            PySide6 GUI (imports the engine in-process; no scraping logic)
    gui/                   main window, views, mandatory first-run risk disclaimer
  cherrybomb_engine/     GUI-agnostic engine (ZERO Qt imports)
    registry.py            @register extension point — add a platform in one file
    net/                   shared anti-bot + SAFETY core (kill-switch, volume caps, rate limit)
    adapters/              one module per platform (reddit, instagram, twitter, enum)
    __main__.py            headless CLI (same adapters the GUI uses)
spikes/                  Phase-0 throwaway feasibility gates (A: data-viz, B: anti-bot, C: packaging)
packaging/               per-OS PyInstaller recipes (filled in Phase 1+)
.github/workflows/       smoke-test (GUI boots headless), build-release, canary
```

## Development setup

Develop on Linux/WSL2; you do **not** build here.

```sh
python3.12 -m venv .venv && . .venv/bin/activate
pip install -e ".[gui,reddit,dev]"

ruff check . && pytest -q          # lint + Qt-free engine tests
python -m cherrybomb_engine list   # headless: list scrapers
cherrybomb                         # GUI (needs a display — see scripts/dev-gui.md)
```

GUI preview under WSLg: see [`scripts/dev-gui.md`](scripts/dev-gui.md).

## Contributing

The extension point is `cherrybomb_engine/adapters/`: add one module with a class
decorated `@register("name")` implementing the `Scraper` protocol. No GUI changes
needed. A contributor cookbook lands with Phase 3. PRs welcome — by contributing you
agree your scraper respects the acceptable-use policy.

## Documentation

Engine and GUI documented with Doxygen (Python via filter); built and hosted from
`docs/`. (To be wired up.)
