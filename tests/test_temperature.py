import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_temperature_runs():
    result = runner.invoke(app, ["temperature", "32"])
    assert result.exit_code == 0
    assert "C" in result.stdout


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #3")
def test_temperature_freezing_point():
    result = runner.invoke(app, ["temperature", "32"])
    assert result.exit_code == 0
    assert "0.00C" in result.stdout


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #3")
def test_temperature_boiling_point():
    result = runner.invoke(app, ["temperature", "212"])
    assert result.exit_code == 0
    assert "100.00C" in result.stdout
