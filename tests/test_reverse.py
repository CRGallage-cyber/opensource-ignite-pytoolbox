from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_reverse_simple():
    result = runner.invoke(app, ["reverse", "hello"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "olleh"


def test_reverse_palindrome_like():
    result = runner.invoke(app, ["reverse", "abcba"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "abcba"
