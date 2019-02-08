from src.Base import Base

import logging as logger

# basic logging to file
logger.basicConfig(
    filename="D:/Fella/Logs/Crawler.log",
    level=logger.DEBUG,
    format="%(asctime)s: %(name)-12s: %(levelname)-8s:%(message)s",
)

# set up logging to console
console = logger.StreamHandler()
console.setLevel(logger.DEBUG)
formatter = logger.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logger.getLogger('').addHandler(console)
logger = logger.getLogger(__name__)

'''
    Main Method
'''
if __name__ == '__main__':
    Base().read_web_pages()
