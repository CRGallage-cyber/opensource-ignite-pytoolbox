import typer
from rich.console import Console

NAME = "leapyear"
HELP = "Check whether a year is a leap year."

console = Console()

MIN_SUPPORTED_YEAR = 1


def _is_leap(year: int) -> bool:
    return year % 4 == 0


def _days_in_year(is_leap: bool) -> int:
    return 366 if is_leap else 365


def main(year: int, verbose: bool = False) -> None:
    if year < MIN_SUPPORTED_YEAR:
        console.print("[red]Error:[/red] year must be a positive integer")
        raise typer.Exit(code=1)

    is_leap = _is_leap(year)
    console.print(is_leap)

    if verbose:
        console.print(f"{year} has {_days_in_year(is_leap)} days")
