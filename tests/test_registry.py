"""Registry + adapter-discovery tests. Qt-free."""

from __future__ import annotations

import pytest

from cherrybomb_engine.registry import available, create, load_adapters, register


def test_register_and_create():
    @register("dummy_test_scraper")
    class _Dummy:
        async def scrape(self, request):  # pragma: no cover
            yield

    assert "dummy_test_scraper" in available()
    inst = create("dummy_test_scraper")
    assert inst.name == "dummy_test_scraper"


def test_duplicate_registration_rejected():
    @register("dup_scraper")
    class _A:
        pass

    with pytest.raises(ValueError):

        @register("dup_scraper")
        class _B:
            pass


def test_create_unknown_raises():
    with pytest.raises(KeyError):
        create("does_not_exist")


def test_load_adapters_is_best_effort():
    # Should not raise even when optional adapter deps (praw, instaloader) are absent.
    load_adapters()
    # reddit adapter has no optional-import at module top, so it registers.
    assert "reddit" in available()
