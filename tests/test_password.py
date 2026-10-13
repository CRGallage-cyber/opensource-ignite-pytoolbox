import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_password_runs():
    result = runner.invoke(app, ["password"])
    assert result.exit_code == 0
    assert len(result.stdout.strip()) > 0


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #4")
def test_password_length():
    result = runner.invoke(app, ["password", "--length", "16"])
    assert result.exit_code == 0
    assert len(result.stdout.strip()) == 16
