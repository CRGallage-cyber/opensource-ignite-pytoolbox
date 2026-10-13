import random

import typer
from rich.console import Console

NAME = "coinflip"
HELP = "Flip a coin one or more times."

console = Console()

_SIDES = ["heads", "tails"]


def _flip_once() -> str:
    return random.choice(_SIDES)


def _flip_many(times: int) -> list[str]:
    return [_flip_once() for _ in range(times)]


def _summarize(results: list[str]) -> str:
    heads = results.count("heads")
    tails = results.count("tails")
    return f"{heads} heads, {tails} tails"


def main(times: int = 1, summary: bool = False) -> None:
    if times < 1:
        console.print("[red]Error:[/red] --times must be at least 1")
        raise typer.Exit(code=1)

    results = _flip_many(times)
    for result in results:
        console.print(result)

    if summary and times > 1:
        console.print(f"[dim]{_summarize(results)}[/dim]")
