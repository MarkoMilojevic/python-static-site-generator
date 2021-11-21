from collections.abc import Mapping
import re
from yaml import load
from yaml.loader import FullLoader


class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)
