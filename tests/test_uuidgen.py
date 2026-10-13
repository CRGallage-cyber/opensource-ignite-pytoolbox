import uuid

from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_uuidgen_default():
    result = runner.invoke(app, ["uuidgen"])
    assert result.exit_code == 0
    value = result.stdout.strip()
    assert uuid.UUID(value).version == 4


def test_uuidgen_count():
    result = runner.invoke(app, ["uuidgen", "--count", "3"])
    assert result.exit_code == 0
    lines = [line for line in result.stdout.splitlines() if line]
    assert len(lines) == 3
    for line in lines:
        assert uuid.UUID(line).version == 4
