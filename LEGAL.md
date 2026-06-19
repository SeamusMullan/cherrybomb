# Legal notes

This is engineering guidance, **not legal advice.** If you operate cherrybomb at
scale or commercially, get a lawyer.

## Open questions gating release

These are unresolved and **block** shipping certain adapters publicly (see the project
plan's open questions):

1. **Login-walled adapters (Instagram `sessionid`, X cookies).** Public, unauthenticated
   scraping has some protection (e.g. *hiQ v. LinkedIn*), but supplying authenticated
   session cookies to circumvent a login wall is a different posture — potentially
   ToS breach, CFAA-contributory, and DMCA §1201 territory, with documented Meta/X
   litigation and youtube-dl-style takedown precedent. **A legal review gates the
   public Instagram release.**
2. **"Paid service" ambition.** The original README floated cherrybomb as a paid
   service. A paid service built on ToS-violating login-walled scraping is the
   highest-liability configuration. Before any X work, the paid posture must be
   reconciled — most likely pivoting paid features to **official APIs only**.
3. **Bundled dependency licenses.** Copyleft scraper libraries (e.g. gallery-dl GPLv2,
   snscrape GPL) cannot be bundled into a redistributed (possibly paid) binary without
   triggering their obligations. Such components are kept **optional and
   user-installed**, not bundled into the base artifact.

## Defenses in place

- **Per-adapter removability** — each platform is one self-contained module that can
  be deleted in response to a C&D / DMCA notice without touching the rest of the app.
- **Loud account-ban and ToS warnings** — first-run disclaimer + README.
- **No bundled accounts or credentials.**
- **Acceptable-use policy** — see [`ACCEPTABLE_USE.md`](ACCEPTABLE_USE.md).
