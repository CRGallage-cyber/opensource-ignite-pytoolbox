import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_leapyear_simple_true():
    result = runner.invoke(app, ["leapyear", "2024"])
    assert result.exit_code == 0
    assert "True" in result.stdout


def test_leapyear_simple_false():
    result = runner.invoke(app, ["leapyear", "2023"])
    assert result.exit_code == 0
    assert "False" in result.stdout


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #7")
def test_leapyear_century_not_divisible_by_400():
    result = runner.invoke(app, ["leapyear", "1900"])
    assert result.exit_code == 0
    assert "False" in result.stdout
