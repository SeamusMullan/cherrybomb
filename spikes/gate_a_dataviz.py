"""GATE A — Qt data-viz feasibility spike (throwaway).

Proves the README headline (interactive relationship graphs, large tables,
time-series) is tractable on mature Qt primitives. Failure here is the ONLY thing
that reopens the egui runner-up.

Three probes:
  1. QGraphicsView force-directed graph, N nodes, pan/zoom/drag, FPS measured.
  2. QTableView + QAbstractTableModel over a QSortFilterProxyModel, M rows,
     client-side sort + live filter.
  3. QtCharts zoomable time-series.

Run:  python spikes/gate_a_dataviz.py [--nodes 5000] [--rows 100000] [--bench]
With --bench it prints FPS / timing numbers and exits non-zero if below threshold,
so CI can assert the gate. Without --bench it opens interactive windows.
"""

from __future__ import annotations

import argparse
import math
import random
import sys
import time

# NOTE: throwaway spike — imports are deliberately heavy/top-level for clarity.
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QPointF,
    QSortFilterProxyModel,
    Qt,
    QTimer,
)
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsScene,
    QGraphicsView,
    QLineEdit,
    QMainWindow,
    QTableView,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

FPS_THRESHOLD = 30.0


# ---------------------------------------------------------------- graph probe
class GraphView(QGraphicsView):
    """N nodes laid out on a circle, draggable, with mouse-wheel zoom. Measures
    repaint FPS over a fixed animation burst."""

    def __init__(self, n_nodes: int) -> None:
        scene = QGraphicsScene()
        super().__init__(scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self._nodes: list[QGraphicsEllipseItem] = []
        for i in range(n_nodes):
            angle = 2 * math.pi * i / n_nodes
            r = 400 + random.random() * 400
            item = QGraphicsEllipseItem(-3, -3, 6, 6)
            item.setPos(r * math.cos(angle), r * math.sin(angle))
            item.setFlag(QGraphicsEllipseItem.ItemIsMovable)
            scene.addItem(item)
            self._nodes.append(item)
        self._frames = 0
        self._t0 = 0.0

    def wheelEvent(self, event) -> None:  # noqa: N802 (Qt override)
        factor = 1.2 if event.angleDelta().y() > 0 else 1 / 1.2
        self.scale(factor, factor)

    def benchmark(self, frames: int = 120) -> float:
        """Jitter every node `frames` times, forcing repaints; return FPS."""
        self._t0 = time.perf_counter()
        for _ in range(frames):
            for item in self._nodes:
                item.moveBy(random.uniform(-1, 1), random.uniform(-1, 1))
            self.viewport().repaint()
        dt = time.perf_counter() - self._t0
        return frames / dt if dt > 0 else float("inf")


# ---------------------------------------------------------------- table probe
class BigTableModel(QAbstractTableModel):
    """M synthetic rows x 5 cols, generated up front."""

    HEADERS = ["id", "username", "followers", "platform", "score"]

    def __init__(self, rows: int) -> None:
        super().__init__()
        plats = ["reddit", "instagram", "twitter", "mastodon"]
        self._rows = [
            (i, f"user_{i}", random.randint(0, 1_000_000), random.choice(plats), random.random())
            for i in range(rows)
        ]

    def rowCount(self, parent=QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._rows)

    def columnCount(self, parent=QModelIndex()) -> int:  # noqa: N802
        return len(self.HEADERS)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._rows[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):  # noqa: N802
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.HEADERS[section]
        return None


def build_table(rows: int) -> QWidget:
    container = QWidget()
    layout = QVBoxLayout(container)
    model = BigTableModel(rows)
    proxy = QSortFilterProxyModel()
    proxy.setSourceModel(model)
    proxy.setFilterKeyColumn(1)  # username
    proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)

    search = QLineEdit(placeholderText="filter by username…")
    search.textChanged.connect(proxy.setFilterFixedString)

    view = QTableView()
    view.setModel(proxy)
    view.setSortingEnabled(True)  # client-side sort, all columns

    layout.addWidget(search)
    layout.addWidget(view)
    return container


# ------------------------------------------------------------- timeseries probe
def build_timeseries() -> QChartView:
    series = QLineSeries()
    y = 0.0
    for x in range(2000):
        y += random.uniform(-1, 1)
        series.append(QPointF(x, y))
    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setTitle("Time-series probe (QtCharts) — wheel to zoom")
    view = QChartView(chart)
    view.setRenderHint(QPainter.Antialiasing)
    view.setRubberBand(QChartView.RectangleRubberBand)
    return view


# ----------------------------------------------------------------------- main
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--nodes", type=int, default=5000)
    ap.add_argument("--rows", type=int, default=100_000)
    ap.add_argument("--bench", action="store_true", help="headless FPS/timing assert for CI")
    args = ap.parse_args(argv)

    app = QApplication(sys.argv)

    graph = GraphView(args.nodes)

    if args.bench:
        t0 = time.perf_counter()
        table = build_table(args.rows)  # noqa: F841 (timing construction cost)
        table_build = time.perf_counter() - t0
        fps = graph.benchmark()
        print(f"GATE A bench: nodes={args.nodes} fps={fps:.1f} (threshold {FPS_THRESHOLD})")
        print(f"GATE A bench: table rows={args.rows} build={table_build * 1000:.0f}ms")
        ok = fps >= FPS_THRESHOLD
        print("GATE A:", "PASS" if ok else "FAIL")
        return 0 if ok else 1

    tabs = QTabWidget()
    tabs.addTab(graph, f"Graph ({args.nodes} nodes)")
    tabs.addTab(build_table(args.rows), f"Table ({args.rows} rows)")
    tabs.addTab(build_timeseries(), "Time-series")
    win = QMainWindow()
    win.setCentralWidget(tabs)
    win.resize(1000, 700)
    win.setWindowTitle("Gate A — Qt data-viz spike")
    win.show()
    QTimer.singleShot(0, lambda: graph.fitInView(graph.scene().itemsBoundingRect(), Qt.KeepAspectRatio))
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
