import logging

LOGGER = logging.getLogger(__name__)


def test_eggs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True