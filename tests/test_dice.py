import re

import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_dice_default_in_range():
    result = runner.invoke(app, ["dice"])
    assert result.exit_code == 0
    match = re.search(r"\d+", result.stdout)
    assert match is not None
    value = int(match.group())
    assert 1 <= value <= 6


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #2")
def test_dice_can_roll_max_value():
    rolled = set()
    for _ in range(40):
        result = runner.invoke(app, ["dice", "--sides", "2"])
        match = re.search(r"\d+", result.stdout)
        rolled.add(int(match.group()))
    assert 2 in rolled
