import shutil
from collections.abc import Iterator
from pathlib import Path

import pytest

from src.file_utils import create_file, read_file


@pytest.fixture
def temp_dir() -> Iterator[Path]:
    p = Path("temp")
    p.mkdir(exist_ok=True)
    yield p
    shutil.rmtree(p)

    # Более элегантное решение:
    # with tempfile.TemporaryDirectory() as tmpdir:
    #     yield Path(tmpdir)


def test_create_and_read_file(temp_dir: Path) -> None:
    content = "Hello, pytest!"
    path = temp_dir / "test.txt"

    create_file(path, content)

    assert path.exists()
    assert read_file(path) == content
