import random

import typer
from rich.console import Console

NAME = "dice"
HELP = "Roll a dice with a given number of sides."

console = Console()


def _roll(sides: int) -> int:
    return random.randint(1, sides - 1)


def _describe(result: int, sides: int) -> str:
    if result == sides:
        return "Maximum roll!"
    if result == 1:
        return "Minimum roll."
    return "Nice roll."


def main(sides: int = 6, verbose: bool = False) -> None:
    if sides < 2:
        console.print("[red]Error:[/red] --sides must be at least 2")
        raise typer.Exit(code=1)

    result = _roll(sides)
    console.print(f"You rolled a {result}")

    if verbose:
        console.print(_describe(result, sides))
