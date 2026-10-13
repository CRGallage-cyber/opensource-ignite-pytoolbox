# pytoolbox

A small, plugin-based command-line toolbox, built as a hands-on sandbox for
learning how open-source projects actually work: forking, branching, writing
tests, and sending pull requests.

Every command lives in its own file under `pytoolbox/commands/`. The CLI
auto-discovers them, so adding a new command never requires touching shared
code.

```
$ pytoolbox list
$ pytoolbox wordcount notes.txt
$ pytoolbox dice --sides 20
$ pytoolbox password --length 16
```

This project ships with **real bugs on purpose**. See [ISSUES.md](ISSUES.md)
for the full list of bugs, features, and add-ons you can pick up, and
[CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution workflow.

## Quick start

This project is tested on Windows, macOS, and Linux — the commands below are
split by platform where they differ. Everywhere else in this repo, assume a
command works the same on all three unless noted.

**macOS / Linux (bash or zsh):**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytoolbox list
pytest
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
pytoolbox list
pytest
```

If `Activate.ps1` is blocked by PowerShell's execution policy, either run
PowerShell as the `-ExecutionPolicy Bypass` variant for this session only, or
use the Command Prompt instructions below instead.

**Windows (Command Prompt / `cmd.exe`):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
pip install -e .
pytoolbox list
pytest
```

> On Windows, `python` (not `python3`) is normally the correct command,
> assuming you installed Python from [python.org](https://www.python.org/) or
> the Microsoft Store with "Add python.exe to PATH" checked.

You can also run the toolbox without installing it as a script, on any OS:

```bash
python -m pytoolbox list
```
(use `python` instead of `python3` on Windows, as above)

## Commands

| Command     | Description                                           | Status      |
|-------------|--------------------------------------------------------|-------------|
| coinflip    | Flip a coin one or more times                          | working     |
| reverse     | Reverse a string                                        | working     |
| uuidgen     | Generate one or more UUID4 values                       | working     |
| wordcount   | Count words, lines and characters in a file             | has a bug   |
| dice        | Roll a dice with a given number of sides                | has a bug   |
| temperature | Convert Fahrenheit to Celsius                           | has a bug   |
| password    | Generate a random password of a given length             | has a bug   |
| palindrome  | Check whether a string is a palindrome                   | has a bug   |
| fizzbuzz    | Print the FizzBuzz sequence up to N                      | has a bug   |
| leapyear    | Check whether a year is a leap year                      | has a bug   |
| titlecase   | Convert a string to title case                           | has a bug   |
| filehash    | Compute the SHA-256 hash of a file                        | has a bug   |
| csv2json    | Convert a CSV file to JSON                                | has a bug   |

"Has a bug" commands run and produce output — the output is just wrong in a
specific, documented way. See [ISSUES.md](ISSUES.md) for details on each one.

## Why does `pytest` pass even though bugs exist?

Each buggy command has a correct test that is marked `xfail(strict=True)`,
pointing at the relevant issue number. That keeps CI green on `main` while
still documenting, in code, exactly what "fixed" looks like. See
[CONTRIBUTING.md](CONTRIBUTING.md) for how to work with these tests.

## Contributing

Never sent an open-source pull request before? Start with
[CONTRIBUTING.md](CONTRIBUTING.md) — it walks through fork, clone, branch,
commit, push, and PR, step by step, with command variants for Windows,
macOS, and Linux.

## Cross-platform by design

This codebase avoids anything OS-specific: all file paths use `pathlib`, no
shell commands are invoked, and there's no behavior that depends on a
particular terminal or line-ending convention. It is expected to run
identically on Windows, macOS, and Linux. If you find a place where it
doesn't, that's a bug — see [ISSUES.md](ISSUES.md) or open a new issue.
