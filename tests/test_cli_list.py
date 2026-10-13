import pkgutil

import pytest
from typer.testing import CliRunner

from pytoolbox import cli
from pytoolbox.cli import app

runner = CliRunner()


def test_list_runs_and_shows_commands():
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "wordcount" in result.stdout
    assert "coinflip" in result.stdout


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #11")
def test_list_is_alphabetically_sorted(monkeypatch):
    real_iter_modules = pkgutil.iter_modules

    def reversed_iter_modules(path):
        return list(reversed(list(real_iter_modules(path))))

    monkeypatch.setattr(cli.pkgutil, "iter_modules", reversed_iter_modules)

    names_in_order = [module.NAME for module in cli._discover_commands()]
    assert names_in_order == sorted(names_in_order)
