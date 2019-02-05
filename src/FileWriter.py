from pathlib import Path
import logging as logger


class FileWriter:
    __file_path = "extractedpages/"

    def write_to_file(self, file_name, content):
        path = self.__file_path + file_name + ".txt"
        relative = Path(path)
        absolute_path = relative.absolute()

        logger.info("Writing to file: " + path)
        file = None
        try:
            file = open(absolute_path, 'wb')
            file.write(content)
        except IOError:
            logger.error("Error writing to file: " + file_name, IOError)
        finally:
            if file is not None:
                file.close()
