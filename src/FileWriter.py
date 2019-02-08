import logging as logger


class FileWriter:
    __file_path = "D:/Fella/ExtractedPages/"

    def write_to_file(self, file_name, content):
        path = self.__file_path + file_name + ".html"

        logger.info("Writing to file: " + path)
        file = None
        try:
            file = open(path, 'wb')
            file.write(content)
        except IOError:
            logger.error("Error writing to file: " + file_name, IOError)
        finally:
            if file is not None:
                file.close()
