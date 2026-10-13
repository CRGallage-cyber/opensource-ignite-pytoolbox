import typer
from rich.console import Console

NAME = "reverse"
HELP = "Reverse a string."

console = Console()


def _reverse_text(text: str) -> str:
    return text[::-1]


def _reverse_words(text: str) -> str:
    return " ".join(reversed(text.split(" ")))


def main(text: str, words: bool = False) -> None:
    if text == "":
        console.print("[red]Error:[/red] text must not be empty")
        raise typer.Exit(code=1)

    result = _reverse_words(text) if words else _reverse_text(text)
    console.print(result)
