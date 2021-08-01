import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    filename = logging.FileHandler('Test1.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
    filename.setFormatter(formatter)
    logger.addHandler(filename)
    logger.critical("Hi I am from info")
