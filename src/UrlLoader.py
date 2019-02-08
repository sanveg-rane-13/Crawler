import json
from pathlib import Path


class UrlLoader:
    __url_file_path = "../resources/urls.json"

    def get_urls(self):
        relative = Path(self.__url_file_path)
        absolute_path = relative.absolute()

        with open(absolute_path) as file:
            url_info = json.load(file)

        return url_info
