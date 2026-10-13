import uuid

import typer
from rich.console import Console

NAME = "uuidgen"
HELP = "Generate one or more UUID4 values."

console = Console()


def _generate_one(upper: bool) -> str:
    value = str(uuid.uuid4())
    return value.upper() if upper else value


def _generate_many(count: int, upper: bool) -> list[str]:
    return [_generate_one(upper) for _ in range(count)]


def main(count: int = 1, upper: bool = False) -> None:
    if count < 1:
        console.print("[red]Error:[/red] --count must be at least 1")
        raise typer.Exit(code=1)

    for value in _generate_many(count, upper):
        console.print(value)
