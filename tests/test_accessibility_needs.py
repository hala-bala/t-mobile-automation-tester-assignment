import logging
from pathlib import Path

from automateda11y.pw.axerunner import AxeRunner
from automateda11y.pw.settings import Settings
from playwright.sync_api import Page


def json_reports_dir():
    return Path(__file__).parent.parent.__str__()

def test_accessibility_needs(page: Page):
    Settings.report_dir = json_reports_dir() + '/reports'
    page.goto("http://www.t-mobile.pl")
    data = AxeRunner(page).execute()
    for violation in data.violations:
        logging.getLogger().warning(f"Valiation: {violation.description}")
        logging.getLogger().warning("Affected nodes:")
        for node in violation.nodes:
            logging.getLogger().warning(f"HTML: {node.html}")

    assert len(data.violations) == 0, "Some violations in html"