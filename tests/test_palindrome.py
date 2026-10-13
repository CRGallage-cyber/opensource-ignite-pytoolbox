import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_palindrome_simple_true():
    result = runner.invoke(app, ["palindrome", "racecar"])
    assert result.exit_code == 0
    assert "True" in result.stdout


def test_palindrome_simple_false():
    result = runner.invoke(app, ["palindrome", "hello"])
    assert result.exit_code == 0
    assert "False" in result.stdout


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #5")
def test_palindrome_ignores_case_and_spaces():
    result = runner.invoke(app, ["palindrome", "Race car"])
    assert result.exit_code == 0
    assert "True" in result.stdout
