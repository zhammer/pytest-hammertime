"""Code for the pytest-hammertime plugin."""

import pytest
import webbrowser

HAMMER_EMOJI = '\U0001f528 '
MC_HAMMER_CANT_TOUCH_THIS = 'https://www.youtube.com/watch?v=otCpCn0l4Wo&feature=youtu.be&t=14s'

def pytest_addoption(parser):
    """Turn on hammertime pytest display with --hammertime."""
    group = parser.getgroup('hammertime')
    group.addoption('--hammertime', action='store_true',
                    help='display "{}" instead of "." for passed tests'.format(HAMMER_EMOJI))
    group.addoption('--hammertime-canttouchthis', action='store_true',
                    help='celebrate on a successful test run')

def pytest_report_teststatus(report):
    """Turn '.' success char into hammer emoji."""
    if pytest.config.getoption('hammertime'):
        if report.when == 'call' and report.outcome == 'passed':
            return (report.outcome, HAMMER_EMOJI, 'PASSED')


def pytest_terminal_summary(terminalreporter, exitstatus):
    """Celebrate on a successful test run."""
    if pytest.config.getoption('hammertime_canttouchthis') and exitstatus == 0:
        terminalreporter.write_line('{} CANT TOUCH THIS {}'.format(HAMMER_EMOJI, HAMMER_EMOJI))
        webbrowser.open(MC_HAMMER_CANT_TOUCH_THIS)
