import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_titlecase_simple():
    result = runner.invoke(app, ["titlecase", "hello world"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello World"


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #8")
def test_titlecase_handles_apostrophes():
    result = runner.invoke(app, ["titlecase", "don't stop"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Don't Stop"
