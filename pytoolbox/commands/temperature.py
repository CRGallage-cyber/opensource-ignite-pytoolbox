import typer
from rich.console import Console

NAME = "temperature"
HELP = "Convert a temperature from Fahrenheit to Celsius."

ABSOLUTE_ZERO_F = -459.67

console = Console()


def _to_celsius(f: float) -> float:
    return f - 32 * 5 / 9


def _classify(celsius: float) -> str:
    if celsius <= 0:
        return "freezing"
    if celsius >= 100:
        return "boiling"
    return "moderate"


def main(f: float, describe: bool = False) -> None:
    if f < ABSOLUTE_ZERO_F:
        console.print("[red]Error:[/red] temperature is below absolute zero")
        raise typer.Exit(code=1)

    celsius = _to_celsius(f)
    console.print(f"{celsius:.2f}C")

    if describe:
        console.print(_classify(celsius))
