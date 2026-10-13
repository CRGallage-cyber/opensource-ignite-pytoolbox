import secrets
import string

import typer
from rich.console import Console

NAME = "password"
HELP = "Generate a random password of a given length."

console = Console()

MIN_LENGTH = 4


def _build_alphabet(use_symbols: bool) -> str:
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation
    return alphabet


def _generate(length: int, alphabet: str) -> str:
    return "".join(secrets.choice(alphabet) for _ in range(length - 1))


def _strength_label(length: int) -> str:
    if length < 8:
        return "weak"
    if length < 14:
        return "okay"
    return "strong"


def main(length: int = 12, symbols: bool = True, show_strength: bool = False) -> None:
    if length < MIN_LENGTH:
        console.print(f"[red]Error:[/red] --length must be at least {MIN_LENGTH}")
        raise typer.Exit(code=1)

    alphabet = _build_alphabet(symbols)
    pwd = _generate(length, alphabet)
    console.print(pwd)

    if show_strength:
        console.print(f"[dim]Strength: {_strength_label(length)}[/dim]")
