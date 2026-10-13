import csv
import json
from pathlib import Path

import typer
from rich.console import Console

NAME = "csv2json"
HELP = "Convert a CSV file to JSON."

console = Console()


def _read_rows(path: Path) -> tuple[list[str], list[dict]]:
    with open(path, newline="") as f:
        reader = csv.reader(f)
        headers = next(reader)
        next(reader)

        rows = [dict(zip(headers, row, strict=False)) for row in reader]

    return headers, rows


def _to_json(rows: list[dict], indent: int) -> str:
    return json.dumps(rows, indent=indent)


def main(path: Path, indent: int = 2) -> None:
    if indent < 0:
        console.print("[red]Error:[/red] --indent must not be negative")
        raise typer.Exit(code=1)

    _headers, rows = _read_rows(path)
    console.print(_to_json(rows, indent))
