import argparse

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import conftest


def main(args):
    browser = args.browser
    tag = args.tag
    reruns = args.reruns
    if browser == 'chrome':
        driver_path = ChromeDriverManager().install()
    report_name = conftest.report

    pytest.main([
        '--driver={}'.format(browser),
        '--driver-path={}'.format(driver_path),
        '--reruns={}'.format(reruns),
        '-m={}'.format(tag),
        '--html={}'.format(report_name),
        '--self-contained-html'
        # '--headless'
    ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', required=True, help='specify in which browser you want to execute tests, '
                                                         'ex: --browser chrome')
    parser.add_argument('--reruns', required=False, default=0,
                        help='provide a value to rerun the failed tests those many times when it failed')
    parser.add_argument('--tag', required=False, default="",
                        help='provide this param to run specific test, ex --scenario smoke')
    main(args=parser.parse_args())
