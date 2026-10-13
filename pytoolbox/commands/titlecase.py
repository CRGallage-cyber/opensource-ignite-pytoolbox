import typer
from rich.console import Console

NAME = "titlecase"
HELP = "Convert a string to title case."

console = Console()


def _to_title_case(text: str) -> str:
    return text.title()


def _word_count(text: str) -> int:
    return len(text.split())


def main(text: str, show_word_count: bool = False) -> None:
    if not text.strip():
        console.print("[red]Error:[/red] text must not be blank")
        raise typer.Exit(code=1)

    result = _to_title_case(text)
    console.print(result)

    if show_word_count:
        console.print(f"[dim]{_word_count(text)} word(s)[/dim]")
