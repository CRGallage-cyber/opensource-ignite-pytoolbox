import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_fizzbuzz_basic_values():
    result = runner.invoke(app, ["fizzbuzz", "--n", "5"])
    assert result.exit_code == 0
    lines = result.stdout.splitlines()
    assert lines == ["1", "2", "Fizz", "4", "Buzz"]


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #6")
def test_fizzbuzz_prints_fizzbuzz_for_multiples_of_15():
    result = runner.invoke(app, ["fizzbuzz", "--n", "15"])
    assert result.exit_code == 0
    lines = result.stdout.splitlines()
    assert lines[-1] == "FizzBuzz"
