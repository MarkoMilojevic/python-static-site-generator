from pathlib import Path
from typing import List


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions
