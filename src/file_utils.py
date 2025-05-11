from pathlib import Path


def create_file(path: Path, content: str) -> None:
    with path.open("w") as f:
        f.write(content)


def read_file(path: Path) -> str:
    return path.read_text()
