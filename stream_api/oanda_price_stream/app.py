import time
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.critical("Startup")


def run():
    while True:
        logger.debug("HELLO!")
        time.sleep(5)


if __name__ == "__main__":
    run()
