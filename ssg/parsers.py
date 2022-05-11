from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions: List[str] = []


    def valid_extension(self, extension):
        return (extension in self.extensions)

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with path.open(mode='r') as file:
            return file.read_text()

    def write(self, path, dest, content, ext = ".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with full_path.open(mode='w') as file':
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        Parser.copy(path, source, dest)