from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_coinflip_default():
    result = runner.invoke(app, ["coinflip"])
    assert result.exit_code == 0
    output = result.stdout.strip()
    assert output in ("heads", "tails")


def test_coinflip_times():
    result = runner.invoke(app, ["coinflip", "--times", "5"])
    assert result.exit_code == 0
    lines = [line for line in result.stdout.splitlines() if line]
    assert len(lines) == 5
    assert all(line in ("heads", "tails") for line in lines)
