import hashlib
from pathlib import Path

import typer
from rich.console import Console

NAME = "filehash"
HELP = "Compute the SHA-256 hash of a file."

console = Console()

SUPPORTED_ALGORITHMS = ("sha256", "md5", "sha1")


def _read_content(path: Path) -> str:
    with open(path, "r") as f:
        return f.read()


def _hash_content(content: str, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    hasher.update(content.encode())
    return hasher.hexdigest()


def main(path: Path, algorithm: str = "sha256") -> None:
    if algorithm not in SUPPORTED_ALGORITHMS:
        console.print(f"[red]Error:[/red] unsupported algorithm {algorithm!r}")
        raise typer.Exit(code=1)

    content = _read_content(path)
    digest = _hash_content(content, algorithm)
    console.print(digest)
