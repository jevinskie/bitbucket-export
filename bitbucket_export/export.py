import webbrowser
from pathlib import Path

from atlassian import Bitbucket
from atlassian.bitbucket import Cloud


def export_to(dir: Path, user: str, password: str):
    print(f"dir: {dir} user: {user} password: {password}")
