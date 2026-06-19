"""Mandatory first-run account-ban-risk disclaimer.

NON-NEGOTIABLE (risk register): scraping social platforms with a real account
will likely get it PERMANENTLY banned (instaloader #2680: ban after one download).
The user must acknowledge this before any scraping UI is reachable. This dialog is
NOT a legal shield — it is informed consent.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QDialog, QDialogButtonBox, QLabel, QVBoxLayout

from ..settings import has_acknowledged_risk, set_acknowledged_risk

_DISCLAIMER = """\
<h3>Read this before you scrape anything</h3>
<p><b>Using your real social-media account with cherrybomb will very likely get it
permanently banned.</b> Platforms detect and block automated access aggressively;
a single run can be enough.</p>
<ul>
  <li>Use a <b>disposable burner account you can afford to lose</b> — never your real one.</li>
  <li>Scraping login-walled platforms may violate their Terms of Service and local law.
      <b>You are responsible</b> for how you use this tool.</li>
  <li>cherrybomb ships no accounts and makes no guarantee any scraper works at any time.</li>
</ul>
<p>This software is for ethical research, journalism and OSINT. Malicious use —
stalking, harassment, blackmail — is forbidden by the acceptable-use policy.</p>
"""


def ensure_acknowledged(parent=None) -> bool:
    """Return True if the user has (now or previously) accepted the risk.

    Shows a blocking modal on first run. Returns False if the user declines — the
    caller must then refuse to open any scraping UI.
    """
    if has_acknowledged_risk():
        return True

    dlg = QDialog(parent)
    dlg.setWindowTitle("cherrybomb — account-ban risk")
    layout = QVBoxLayout(dlg)

    label = QLabel(_DISCLAIMER)
    label.setWordWrap(True)
    label.setTextFormat(Qt.RichText)
    layout.addWidget(label)

    agree = QCheckBox("I understand the risk and will use a burner account.")
    layout.addWidget(agree)

    buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    buttons.button(QDialogButtonBox.Ok).setEnabled(False)
    agree.toggled.connect(buttons.button(QDialogButtonBox.Ok).setEnabled)
    buttons.accepted.connect(dlg.accept)
    buttons.rejected.connect(dlg.reject)
    layout.addWidget(buttons)

    if dlg.exec() == QDialog.Accepted:
        set_acknowledged_risk(True)
        return True
    return False
