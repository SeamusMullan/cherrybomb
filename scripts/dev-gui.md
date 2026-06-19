# Previewing the GUI on the WSL2 dev box

The PySide6 GUI renders with Qt's **raster backend** — no GPU required — so it works
under WSLg. You only need a display.

## Check your display

```sh
echo "DISPLAY=$DISPLAY  WAYLAND_DISPLAY=$WAYLAND_DISPLAY"
```

If both are empty (as in a bare CI-like shell), WSLg isn't wiring a display into this
shell. Options, in order of preference:

1. **Use WSLg's display** — it's normally `:0`. Export it and run:
   ```sh
   export DISPLAY=:0
   pip install -e ".[gui,dev]"
   python -m cherrybomb            # or: cherrybomb
   ```
2. **Headless smoke (no window)** — verify the app constructs without a display,
   exactly like CI does:
   ```sh
   QT_QPA_PLATFORM=offscreen python -c "import sys; from PySide6.QtWidgets import QApplication; from cherrybomb.gui.app import MainWindow; QApplication(sys.argv); MainWindow(); print('ok')"
   ```
3. **Gate A interactively** (needs a real display):
   ```sh
   DISPLAY=:0 python spikes/gate_a_dataviz.py
   ```

## Why this matters

This box is for **development**, not building. Heavy per-OS freezes (PyInstaller,
signing, notarization) run in GitHub Actions — see `.github/workflows/`. Locally you
only ever need an editable install and a display.
