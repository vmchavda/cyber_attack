import pytest
from BrowserManager import Browser
import logging

@pytest.fixture(scope="function")
def setup():
    Browser.create_new_driver(Browser.CHROME)
    Browser.get_driver().maximize_window()
    Browser.get_driver().get('https://mystifying-beaver-ee03b5.netlify.app/')
    logging.info('Navigating url')
    yield
    Browser.shutdown()