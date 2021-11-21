from docutils.core import publish_parts
from markdown import markdown
from pathlib import Path
import shutil
from ssg.content import Content
import sys
from typing import List


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions: List[str] = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)


class MarkdownParser(Parser):
    extensions: List[str] = [".md", ".markdown"]

    def parse(self, path: Path, source: Path, dest: Path):
        content = Content.load(self.read(path))
