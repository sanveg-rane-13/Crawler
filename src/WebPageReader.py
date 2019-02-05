import urllib.request as reader
import logging as logger


class WebPageReader:
    def read_page(self, url):
        self.__pass_self()
        logger.info("Reading URL: " + url)

        parsed_page = None
        converted_page = None

        try:
            url_page = reader.Request(url);
            response = reader.urlopen(url_page)
            parsed_page = response.read()
        except reader.error.URLError:
            logger.ERROR("Error parsing URL")
        except reader.error.HTTPError:
            logger.ERROR("Error reading page")

        # if parsed_page is not None:
        #     try:
        #         converted_page = parsed_page.decode('utf-8')
        #     except UnicodeDecodeError:
        #         logger.error("Error converting page to string")

        return parsed_page

    def __pass_self(self):
        return
