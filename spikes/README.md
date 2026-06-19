# Phase 0 spikes — hard exit gates

These are **throwaway feasibility probes**, not product code. Each answers one
make-or-break question cheaply, BEFORE any plumbing is built. If a gate fails, the
plan pivots (or the egui runner-up reopens) — that is the whole point of running
them first.

| Gate | Question | Spike | Pass criteria |
|------|----------|-------|---------------|
| **A** | Can Qt deliver the headline data-viz? | `gate_a_dataviz.py` | 5,000-node `QGraphicsView` force graph with pan/zoom/drag ≥30fps; 100,000-row `QTableView` with client-side sort+filter; zoomable `QtCharts` time-series. |
| **B** | Can we reliably pull X/IG for 2 weeks straight? | `gate_b_antibot.py` | Pull ONE X timeline + ONE IG profile daily for 14 days using residential proxies + Patchright + burner accounts, tracking ban/break rate. **This is the real product-viability gate.** |
| **C** | Does the frozen app launch a relocated browser on a clean machine? | `gate_c_packaging.py` + CI | PyInstaller onedir of a ping-only engine resolves per-OS paths AND actually launches a relocated Chromium on a minimal/clean container, every OS×ARCH leg. |

Run order: A and C are fast (days). B runs for 2 weeks in the background. Gates run
in parallel. Do not start Phase 1 until A and C pass and B has a go verdict.

## Running locally

GUI spikes need a display. On the WSL2 dev box, WSLg provides one; if `DISPLAY` is
empty, see `scripts/dev-gui.md`. In CI, GUI spikes run headless under `xvfb-run`
with Qt's raster backend (no GPU required).

```sh
uv sync --extra gui --extra instagram --group dev
uv run python spikes/gate_a_dataviz.py          # opens 3 windows / runs fps benchmark
uv run python spikes/gate_c_packaging.py --self-test
```
