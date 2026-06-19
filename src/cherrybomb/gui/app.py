"""GUI entry point.

Phase 0: boots a minimal main window behind the mandatory first-run ban-risk
disclaimer. The results grid (QTableView), job pane, settings dialogs and the
post-v1 graph/charts views land in later phases.

Rendering note: Qt's raster backend needs no GPU, so this boots under WSLg on the
dev box and under xvfb / offscreen QPA in CI — see scripts/ and CI smoke test.
"""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

from .disclaimer import ensure_acknowledged


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("cherrybomb")
        self.resize(900, 600)
        # Placeholder central widget — replaced by the results grid in Phase 1.
        self.setCentralWidget(QLabel("cherrybomb — Phase 0 skeleton"))


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("cherrybomb")
    app.setOrganizationName("cherrybomb")

    # Gate scraping UI behind informed consent. Decline => exit without opening it.
    if not ensure_acknowledged():
        return 0

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
