"""cherrybomb_engine — GUI-agnostic OSINT scraping engine.

HARD RULE: this package MUST NOT import PySide6 / Qt anything. It runs as a pure
library, as ``python -m cherrybomb_engine`` (headless, F8), and is driven by the
GUI in-process. Keeping it Qt-free is what lets the same code serve the CLI, the
GUI, and the CI canary with one implementation.
"""

__version__ = "0.0.0"
