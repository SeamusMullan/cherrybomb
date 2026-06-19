# Packaging

Per-OS release recipes. **Heavy builds run in CI only** (`.github/workflows/build-release.yml`),
never on the dev box.

Lands in Phase 1+:

- `cherrybomb.spec` — PyInstaller **onedir** freeze of the PySide6 app + engine, with a
  runtime hook that repoints `PLAYWRIGHT_BROWSERS_PATH` to a writable platformdirs cache
  (the FULL, browser-bundled flavor; the LEAN flavor is HTTP-only and fetches the browser
  on first launch).
- **Two artifact flavors:** LEAN (HTTP-only, small) and FULL (browser bundled / first-launch
  fetch). A per-OS **size-budget gate** in CI fails the build if an artifact exceeds its
  ceiling. `pyarrow`/Parquet is an optional extra, never base.
- **Windows:** NSIS/MSI + Authenticode signing + a VirusTotal/Defender scan gate (PyInstaller
  bootloaders that spawn interpreters + a browser are AV-flagged otherwise).
- **macOS:** `.app` with hardened-runtime **deep**-signing of every nested Mach-O (interpreter,
  dylibs, Chromium) + notarization.
- **Linux:** AppImage/Flatpak (Flatpak preferred for the browser-bundled case) + `.deb`.
  **Never** ship a silent `--no-sandbox` for a credential-handling tool. Clean-machine smoke
  tests run in a **minimal distro container** (debian-slim/fedora), not ubuntu-with-dev-libs.
