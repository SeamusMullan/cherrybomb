"""Platform adapters. One module per platform; @register makes it discoverable.

Ship order (per plan): reddit (Phase 1, low-risk plumbing de-risker) -> instagram
(Phase 2, the single v1 anti-bot platform, best-effort) -> twitter + enum (post-v1).

Each adapter is self-contained and individually removable — per-adapter removal is
the project's C&D / DMCA takedown defense.
"""
