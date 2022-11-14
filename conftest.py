import base64
import json
import time

import pytest
import logging
from py.xml import html

from pytest import fixture

reports_path = "html_reports"
report = reports_path + "/Centime_" + str(
    time.strftime('%Y%d%m_%H:%M:%S', time.localtime(time.time()))) + ".html"


def pytest_addoption(parser):
    group = parser.getgroup('webDriver', 'webDriver')
    group.addoption('--headless',
                    action='store_true',
                    help='enable headless mode by --headless')


@fixture(scope='session')
def base_url() -> str:
    base_url = f'https://practice.automationtesting.in/my-account/'
    return base_url


@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    if pytestconfig.getoption('headless'):
        chrome_options.add_argument('headless')
        chrome_options.add_argument("--window-size=1700x1100")
    return chrome_options


def pytest_bdd_apply_tag(tag, function):
    if 'reruns' in tag:
        number = int(tag.split("=")[1])
        marker = pytest.mark.flaky(reruns=number)
        marker(function)
        return True
    if tag == 'skip':
        marker = pytest.mark.skip(reason="Current Sprint")
        marker(function)
        return True
