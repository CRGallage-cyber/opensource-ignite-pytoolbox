import importlib
import pkgutil

import typer
from rich.console import Console
from rich.table import Table

from pytoolbox import commands

app = typer.Typer(help="pytoolbox: a plugin-based command-line toolbox.")
console = Console()

_loaded_commands = []


def _discover_commands():
    discovered = []
    for module_info in pkgutil.iter_modules(commands.__path__):
        if module_info.name.startswith("_"):
            continue
        module = importlib.import_module(f"pytoolbox.commands.{module_info.name}")
        if not hasattr(module, "NAME") or not hasattr(module, "main"):
            continue
        discovered.append(module)
    return discovered


def _register_commands():
    for module in _discover_commands():
        app.command(name=module.NAME, help=getattr(module, "HELP", ""))(module.main)
        _loaded_commands.append(module)


_register_commands()


@app.command(name="list")
def list_commands():
    """List all available commands."""
    table = Table(title="pytoolbox commands")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")

    for module in _loaded_commands:
        table.add_row(module.NAME, getattr(module, "HELP", ""))

    console.print(table)
