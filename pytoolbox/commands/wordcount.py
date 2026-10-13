from pathlib import Path

from rich.console import Console

NAME = "wordcount"
HELP = "Count words, lines and characters in a file or text."

console = Console()


def _split_words(text: str) -> list[str]:
    return text.split(" ")


def _count_lines(text: str) -> int:
    return len(text.splitlines())


def _average_word_length(words: list[str]) -> float:
    if not words:
        return 0.0
    return sum(len(word) for word in words) / len(words)


def main(path: Path) -> None:
    text = path.read_text()

    words = _split_words(text)
    line_count = _count_lines(text)
    avg_length = _average_word_length(words)

    console.print(f"Lines: {line_count}")
    console.print(f"Words: {len(words)}")
    console.print(f"Characters: {len(text)}")
    console.print(f"Average word length: {avg_length:.1f}")
