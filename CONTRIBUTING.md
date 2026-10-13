# Contributing to pytoolbox

Welcome! This guide walks through the full process of contributing, from
forking the repo to getting a pull request merged. If this is your first
open-source contribution ever, read it top to bottom before you start.

This project is used on Windows, macOS, and Linux alike. `git` commands
(`clone`, `checkout`, `add`, `commit`, `push`, ...) are identical on every
platform, so they're shown once. Steps that differ — mainly creating and
activating a virtual environment — are shown separately for each platform.

## 1. Claim an issue

Browse [ISSUES.md](ISSUES.md) (or the GitHub Issues tab if issues have been
created there). Pick one issue — comment on it saying you'd like to work on
it, and wait to be assigned before you start. This avoids two people
accidentally working on the same thing.

## 2. Fork and clone

1. Click **Fork** on GitHub to create your own copy of the repo.
2. Clone your fork locally:

   ```bash
   git clone https://github.com/<your-username>/pytoolbox.git
   cd pytoolbox
   ```

3. Add the original repo as `upstream` so you can pull in future changes:

   ```bash
   git remote add upstream https://github.com/<original-owner>/pytoolbox.git
   ```

## 3. Set up your environment

**macOS / Linux:**

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

If PowerShell refuses to run `Activate.ps1` ("running scripts is disabled on
this system"), either use Command Prompt instead (below), or run
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that
PowerShell session first.

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
pip install -e .
pytoolbox list
pytest
```

You'll know your virtual environment is active when your prompt is prefixed
with `(.venv)`, on any platform.

`pytest` should pass (some tests will show as `xfail`, which is expected —
see section 6).

## 4. Create a branch

Branch names should describe what you're doing and reference the issue
number:

- Bug fix: `fix/<issue-number>-short-name` (e.g. `fix/3-temperature-formula`)
- New feature: `feat/<issue-number>-short-name` (e.g. `feat/14-roman-numerals`)

```bash
git checkout -b fix/3-temperature-formula
```

## 5. Make your change

Keep **one change per PR**. Don't fix two unrelated bugs or add two unrelated
commands in the same branch.

### Adding a new command

Every command is a single file in `pytoolbox/commands/`. To add one:

1. Create `pytoolbox/commands/<your_command>.py` using this template:

   ```python
   from rich.console import Console

   NAME = "your_command"
   HELP = "One short sentence describing what this command does."

   console = Console()


   def main(some_argument: str) -> None:
       # Typer turns type-hinted parameters into CLI arguments/options.
       console.print(some_argument)
   ```

2. Create `tests/test_your_command.py`:

   ```python
   from typer.testing import CliRunner

   from pytoolbox.cli import app

   runner = CliRunner()


   def test_your_command_basic():
       result = runner.invoke(app, ["your_command", "hello"])
       assert result.exit_code == 0
       assert "hello" in result.stdout
   ```

3. That's it — **no other file needs to change**. The CLI auto-discovers
   every file in `pytoolbox/commands/`, which is what keeps unrelated PRs
   from conflicting with each other.

### Fixing a bug

Fix the bug in the relevant file in `pytoolbox/commands/` (or `cli.py` for
the one core bug). Then see the `xfail` rule below — you'll usually need to
remove a marker from the matching test.

## 6. The `xfail` rule

Every known bug already has a **correct** test written for it, marked like
this:

```python
@pytest.mark.xfail(strict=True, reason="See ISSUES.md #7")
def test_leapyear_century_not_divisible_by_400():
    ...
```

`xfail` means "we expect this test to fail right now, because of a known
bug." `strict=True` means: if the test *unexpectedly passes*, that's treated
as a failure too. This keeps `main` green while bugs are still open, without
hiding them.

When you fix the underlying bug:

1. The test will start passing.
2. Because of `strict=True`, that now shows up as a failure
   (`XPASS(strict)`) until you remove the `@pytest.mark.xfail(...)` line.
3. **Remove the `xfail` marker** as part of your fix. That's how the test
   suite "learns" the bug is gone. Don't delete the test itself — it's now
   your regression test.

A PR that fixes a bug but leaves the `xfail` marker in place is incomplete.

## 7. Commit messages

Use short, imperative commit messages, optionally referencing the issue:

```
Fix off-by-one in password length (#4)
Add roman numeral command (#13)
```

## 8. Push and open a pull request

```bash
git add <files you changed>
git commit -m "Fix off-by-one in password length (#4)"
git push -u origin fix/3-temperature-formula
```

Then open a PR on GitHub against the original repo's `main` branch. Fill in
the PR template, including `Closes #<issue-number>`.

## 9. Keeping your fork in sync

Before starting new work, sync your fork with upstream:

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

## 10. Your first PR: add yourself as a contributor

As a warm-up exercise, add a file `contributors/<your-github-username>.md`
following the format in [`contributors/example-user.md`](contributors/example-user.md):
your name, GitHub username, a fun fact, and your favorite Python library.
Open this as its own small PR to practice the whole flow before tackling a
real issue.

## Code style

- Use type hints on command parameters (Typer relies on them).
- Prefer `pathlib.Path` over raw string paths.
- No shell-specific code — this project must run identically on Windows,
  macOS, and Linux.
- This project uses [`ruff`](https://docs.astral.sh/ruff/) for both linting
  and formatting, enforced in CI. Before opening a PR, run:

  ```bash
  ruff check .
  ruff format pytoolbox tests scripts
  ```

  `ruff check .` must report no errors, and `ruff format` should leave your
  changed files unmodified (CI runs `ruff format --check` and will fail the
  build if formatting is off). If `ruff format` rewrites a file, just
  re-stage it and commit the formatted version.
