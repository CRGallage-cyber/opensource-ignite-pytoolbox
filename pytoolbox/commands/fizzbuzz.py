import typer
from rich.console import Console

NAME = "fizzbuzz"
HELP = "Print the FizzBuzz sequence up to N."

console = Console()


def _value_for(i: int) -> str:
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    if i % 15 == 0:
        return "FizzBuzz"
    return str(i)


def _sequence(n: int) -> list[str]:
    return [_value_for(i) for i in range(1, n + 1)]


def main(n: int = 15) -> None:
    if n < 1:
        console.print("[red]Error:[/red] --n must be at least 1")
        raise typer.Exit(code=1)

    for value in _sequence(n):
        console.print(value)
