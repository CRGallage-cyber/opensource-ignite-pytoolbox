import hashlib

import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_filehash_text_file(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_bytes(b"hello world")
    expected = hashlib.sha256(b"hello world").hexdigest()
    result = runner.invoke(app, ["filehash", str(path)])
    assert result.exit_code == 0
    assert expected in result.stdout


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #9")
def test_filehash_binary_file(tmp_path):
    path = tmp_path / "data.bin"
    raw = bytes(range(256))
    path.write_bytes(raw)
    expected = hashlib.sha256(raw).hexdigest()
    result = runner.invoke(app, ["filehash", str(path)])
    assert result.exit_code == 0
    assert expected in result.stdout
