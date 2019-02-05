from src.UrlLoader import UrlLoader
from src.WebPageReader import WebPageReader
from src.FileWriter import FileWriter

import time
import logging as logger

# basic logging to file
logger.basicConfig(
    filename="logs/base.log",
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


class Base:
    __page_urls = None

    def __init__(self):
        self.url_loader = UrlLoader()
        self.page_reader = WebPageReader()
        self.writer = FileWriter()

    def read_web_pages(self):
        self.__load_web_pages()
        self.__crawl_pages()

    def __load_web_pages(self):
        self.__page_urls = self.url_loader.get_urls()

    def __crawl_pages(self):
        for attribute in self.__page_urls:
            start_time = time.time()
            web_page_doc = self.page_reader.read_page(self.__page_urls[attribute])
            self.__save_page(attribute, web_page_doc)
            end_time = time.time()

            logger.info("Time to fetch: " + attribute + " - " + str(end_time - start_time) + " milli-secs")

    def __save_page(self, file_name, page):
        self.writer.write_to_file(file_name, page)


'''
    Main Method
'''
if __name__ == '__main__':
    Base().read_web_pages()
