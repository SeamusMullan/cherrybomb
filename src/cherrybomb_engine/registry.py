"""ScraperRegistry — the single contributor extension point.

Adding a platform = one module in ``adapters/`` + one ``@register("name")`` decorator
on a class implementing the :class:`Scraper` protocol. The GUI and CLI both discover
adapters through this registry, so a contributor never touches GUI code to add a scraper.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Callable
from typing import Protocol, runtime_checkable

from .models import Record, ScrapeRequest


@runtime_checkable
class Scraper(Protocol):
    """Contract every platform adapter implements."""

    name: str

    def scrape(self, request: ScrapeRequest) -> AsyncIterator[Record]:
        """Yield records for ``request``. Should be cancellable and respect the
        shared net/ safety layer (rate limits, kill-switch, volume caps)."""
        ...


_REGISTRY: dict[str, type] = {}


def register(name: str) -> Callable[[type], type]:
    """Class decorator registering a scraper under ``name``."""

    def _wrap(cls: type) -> type:
        if name in _REGISTRY:
            raise ValueError(f"scraper {name!r} already registered by {_REGISTRY[name]!r}")
        cls.name = name  # type: ignore[attr-defined]
        _REGISTRY[name] = cls
        return cls

    return _wrap


def available() -> list[str]:
    """Names of all registered scrapers."""
    return sorted(_REGISTRY)


def create(name: str) -> Scraper:
    """Instantiate a registered scraper by name."""
    try:
        cls = _REGISTRY[name]
    except KeyError:
        raise KeyError(f"no scraper named {name!r}; available: {available()}") from None
    return cls()  # type: ignore[return-value]


def load_adapters() -> None:
    """Import adapter modules so their ``@register`` decorators run.

    Imports are best-effort: an adapter whose optional deps are missing (e.g. praw
    not installed in the lean build) is skipped, not fatal.
    """
    import importlib
    import pkgutil

    from . import adapters

    for mod in pkgutil.iter_modules(adapters.__path__):
        try:
            importlib.import_module(f"{adapters.__name__}.{mod.name}")
        except ImportError:
            # Optional dependency not present in this build flavor — skip.
            continue
