from src.UrlLoader import UrlLoader
from src.WebPageReader import WebPageReader
from src.FileWriter import FileWriter

import logging as logger

logger.basicConfig(
    filename="logs/base.log",
    level=logger.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


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
            web_page_doc = self.page_reader.read_page(self.__page_urls[attribute])
            self.__save_page(attribute, web_page_doc)

    def __save_page(self, file_name, page):
        self.writer.write_to_file(file_name, page)


'''
    Main Method
'''
if __name__ == '__main__':
    base = Base()
    base.read_web_pages()
