# Issues

This file is the master list of work available on pytoolbox: real bugs, new
commands, and project improvements. It doubles as the source used by
[`scripts/create_issues.py`](scripts/create_issues.py) to create matching
GitHub issues.

## Labels

Each issue has two kinds of labels:

**Type**
- `bug` — something is implemented but behaves incorrectly
- `feature` — a new command that doesn't exist yet
- `add-on` — an improvement to the project itself (CI, docs, tooling)

**Level**
- `good first issue` — small, self-contained, great for a first PR
- `beginner` — needs a little more code reading, still approachable
- `intermediate` — touches trickier logic, shared code, or external tools

## How to claim an issue

1. Find an open issue you'd like to work on.
2. Comment on it (e.g. "I'd like to work on this") and wait to be assigned.
   This avoids duplicate work.
3. Once assigned, follow the workflow in [CONTRIBUTING.md](CONTRIBUTING.md):
   fork → branch → fix/implement → test → pull request.
4. Reference the issue number in your branch name and PR (`Closes #<n>`).

---

# Bugs

## #1 — `wordcount` miscounts words with extra whitespace

**Labels:** `bug`, `good first issue`

**Description**

`pytoolbox wordcount` is supposed to count words, lines, and characters in a
file. The word count is wrong whenever a file has multiple consecutive
spaces or blank lines.

**Steps to reproduce**

1. Create a file containing `hello   world` (three spaces between words).
2. Run `pytoolbox wordcount <file>`.

**Expected result**

`Words: 2`

**Actual result**

`Words: 4`

**Files likely to change**

- `pytoolbox/commands/wordcount.py`
- `tests/test_wordcount.py`

**Acceptance criteria**

- [ ] Word count matches the number of whitespace-separated words, regardless
      of how many spaces/newlines separate them
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_wordcount.py`
- [ ] `pytest` passes

**Hint**

Look at how the text is being split into words. Is there a built-in string
method that handles *any* run of whitespace, not just a single space?

---

## #2 — `dice` never rolls the highest value

**Labels:** `bug`, `good first issue`

**Description**

Rolling an N-sided die should be able to produce any value from 1 to N. The
highest possible value never appears.

**Steps to reproduce**

1. Run `pytoolbox dice --sides 2` many times in a row.

**Expected result**

Both `1` and `2` should appear across enough rolls.

**Actual result**

Only `1` ever appears.

**Files likely to change**

- `pytoolbox/commands/dice.py`
- `tests/test_dice.py`

**Acceptance criteria**

- [ ] A roll can produce any value from `1` to `sides`, inclusive
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_dice.py`
- [ ] `pytest` passes

**Hint**

Check the arguments passed to the random number function against what range
it's documented to produce.

---

## #3 — `temperature` conversion formula is wrong

**Labels:** `bug`, `good first issue`

**Description**

`pytoolbox temperature` converts Fahrenheit to Celsius, but the result is
incorrect for every input except where the error happens to cancel out.

**Steps to reproduce**

1. Run `pytoolbox temperature 32` (the freezing point of water).

**Expected result**

`0.00C`

**Actual result**

A different (wrong) value.

**Files likely to change**

- `pytoolbox/commands/temperature.py`
- `tests/test_temperature.py`

**Acceptance criteria**

- [ ] `pytoolbox temperature 32` prints `0.00C`
- [ ] `pytoolbox temperature 212` prints `100.00C`
- [ ] The `xfail` markers are removed from the matching tests in
      `tests/test_temperature.py`
- [ ] `pytest` passes

**Hint**

Double-check the order of operations in the formula against standard
operator precedence rules.

---

## #4 — `password` generates one character too few

**Labels:** `bug`, `good first issue`

**Description**

`pytoolbox password --length N` should generate a password of exactly `N`
characters.

**Steps to reproduce**

1. Run `pytoolbox password --length 16`.
2. Count the characters in the output.

**Expected result**

16 characters.

**Actual result**

15 characters.

**Files likely to change**

- `pytoolbox/commands/password.py`
- `tests/test_password.py`

**Acceptance criteria**

- [ ] The generated password always has exactly `length` characters
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_password.py`
- [ ] `pytest` passes

**Hint**

Look closely at the range used to build the password — off-by-one errors
often hide in `range()` or similar calls.

---

## #5 — `palindrome` is case-sensitive and punctuation-sensitive

**Labels:** `bug`, `beginner`

**Description**

A proper palindrome check should ignore letter case, spaces, and
punctuation. Right now it does a strict character-by-character comparison.

**Steps to reproduce**

1. Run `pytoolbox palindrome "Race car"`.

**Expected result**

`True`

**Actual result**

`False`

**Files likely to change**

- `pytoolbox/commands/palindrome.py`
- `tests/test_palindrome.py`

**Acceptance criteria**

- [ ] `"Race car"`, `"racecar"`, and `"A man a plan a canal Panama"` are all
      recognized as palindromes
- [ ] Clearly non-palindromic strings still return `False`
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_palindrome.py`
- [ ] `pytest` passes

**Hint**

Think about what normalization needs to happen to the string before
comparing it to its reverse.

---

## #6 — `fizzbuzz` never prints "FizzBuzz"

**Labels:** `bug`, `good first issue`

**Description**

Numbers divisible by both 3 and 5 should print `FizzBuzz`, but they currently
print `Fizz` instead.

**Steps to reproduce**

1. Run `pytoolbox fizzbuzz --n 15`.

**Expected result**

The last line printed is `FizzBuzz`.

**Actual result**

The last line printed is `Fizz`.

**Files likely to change**

- `pytoolbox/commands/fizzbuzz.py`
- `tests/test_fizzbuzz.py`

**Acceptance criteria**

- [ ] Multiples of 15 print `FizzBuzz`
- [ ] Multiples of 3 (but not 15) print `Fizz`
- [ ] Multiples of 5 (but not 15) print `Buzz`
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_fizzbuzz.py`
- [ ] `pytest` passes

**Hint**

Think about the order in which the conditions are checked, and which
condition should be checked first.

---

## #7 — `leapyear` misclassifies century years

**Labels:** `bug`, `intermediate`

**Description**

The leap year rule is more subtle than "divisible by 4": century years are
only leap years if divisible by 400. `1900` and `2100` should **not** be leap
years, but `2000` should be.

**Steps to reproduce**

1. Run `pytoolbox leapyear 1900`.

**Expected result**

`False`

**Actual result**

`True`

**Files likely to change**

- `pytoolbox/commands/leapyear.py`
- `tests/test_leapyear.py`

**Acceptance criteria**

- [ ] `2024` → `True`, `2023` → `False`
- [ ] `1900` → `False`, `2100` → `False`
- [ ] `2000` → `True`
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_leapyear.py`
- [ ] `pytest` passes

**Hint**

Look up the full Gregorian leap year rule — there are three conditions, not
one.

---

## #8 — `titlecase` mishandles apostrophes

**Labels:** `bug`, `intermediate`

**Description**

Python's built-in `str.title()` treats any non-letter character (including
`'`) as a word boundary, so `"don't stop"` becomes `"Don'T Stop"` instead of
`"Don't Stop"`.

**Steps to reproduce**

1. Run `pytoolbox titlecase "don't stop"`.

**Expected result**

`Don't Stop`

**Actual result**

`Don'T Stop`

**Files likely to change**

- `pytoolbox/commands/titlecase.py`
- `tests/test_titlecase.py`

**Acceptance criteria**

- [ ] `"don't stop"` → `"Don't Stop"`
- [ ] `"hello world"` → `"Hello World"` still works
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_titlecase.py`
- [ ] `pytest` passes

**Hint**

`str.title()` is the easy, incorrect answer here. Consider title-casing each
whitespace-separated word yourself instead.

---

## #9 — `filehash` breaks on binary files

**Labels:** `bug`, `intermediate`

**Description**

`pytoolbox filehash` is supposed to compute a SHA-256 hash of any file. It
opens files in text mode, which means it can crash on binary files and can
produce the wrong hash even for text files with non-ASCII content or
non-Unix line endings.

**Steps to reproduce**

1. Create a file containing arbitrary binary bytes (e.g. a `.png`, or any
   file with bytes that aren't valid UTF-8).
2. Run `pytoolbox filehash <file>`.

**Expected result**

The correct SHA-256 hex digest of the file's raw bytes, matching what
`sha256sum` (or Python's `hashlib.sha256` on the raw bytes) would produce.

**Actual result**

A crash (`UnicodeDecodeError`) or an incorrect hash.

**Files likely to change**

- `pytoolbox/commands/filehash.py`
- `tests/test_filehash.py`

**Acceptance criteria**

- [ ] `filehash` works correctly on arbitrary binary files
- [ ] The hash matches `hashlib.sha256(raw_bytes).hexdigest()`
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_filehash.py`
- [ ] `pytest` passes

**Hint**

Hashing should always operate on bytes, not decoded text. Check the mode
the file is opened in.

---

## #10 — `csv2json` silently drops the first data row

**Labels:** `bug`, `intermediate`

**Description**

`pytoolbox csv2json` converts a CSV file into a JSON array of objects. The
first row of actual data (right after the header) is missing from the
output.

**Steps to reproduce**

1. Create a CSV file:
   ```
   name,age
   alice,30
   bob,25
   ```
2. Run `pytoolbox csv2json <file>`.

**Expected result**

```json
[
  {"name": "alice", "age": "30"},
  {"name": "bob", "age": "25"}
]
```

**Actual result**

`alice` is missing from the output.

**Files likely to change**

- `pytoolbox/commands/csv2json.py`
- `tests/test_csv2json.py`

**Acceptance criteria**

- [ ] Every data row from the CSV appears in the JSON output, in order
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_csv2json.py`
- [ ] `pytest` passes

**Hint**

Count how many times the reader is advanced before the actual data rows are
read, versus how many times it should be.

---

## #11 — `pytoolbox list` shows commands in a random order

**Labels:** `bug`, `intermediate`

**Description**

`pytoolbox list` should show commands in a stable, predictable order
(alphabetical). Right now the order depends on filesystem/module discovery
order, which is not guaranteed to be sorted and can differ between machines.

This is the one bug in shared code (`cli.py`) rather than in an individual
command — be careful, since this file is used by every command.

**Steps to reproduce**

1. Run `pytoolbox list`.
2. Compare the order of commands shown to alphabetical order.

**Expected result**

Commands are listed alphabetically by name.

**Actual result**

Commands are listed in whatever order they were discovered on disk, which is
not guaranteed to be alphabetical.

**Files likely to change**

- `pytoolbox/cli.py`
- `tests/test_cli_list.py`

**Acceptance criteria**

- [ ] `pytoolbox list` always shows commands in alphabetical order by name,
      regardless of discovery order
- [ ] Adding a new command still requires no changes outside of
      `pytoolbox/commands/` and `tests/`
- [ ] The `xfail` marker is removed from the matching test in
      `tests/test_cli_list.py`
- [ ] `pytest` passes

**Hint**

Somewhere, the list of discovered command modules needs to be sorted by name
before it's used to build the table — and ideally before commands are even
registered, so the fix is in one place.

---

# Features

Each of these is a brand-new command. None of them exist yet. Follow the
"Adding a new command" section of [CONTRIBUTING.md](CONTRIBUTING.md): create
one file in `pytoolbox/commands/`, one test file in `tests/`, nothing else.

## #12 — Add a `base64` command

**Labels:** `feature`, `good first issue`

**Description**

Add a command that encodes or decodes text using Base64.

Example usage:
```
pytoolbox base64 "hello" --decode False
pytoolbox base64 "aGVsbG8=" --decode True
```

**Files likely to change**

- `pytoolbox/commands/base64.py` (new)
- `tests/test_base64.py` (new)

**Acceptance criteria**

- [ ] Can encode arbitrary text to Base64
- [ ] Can decode valid Base64 back to the original text
- [ ] Has tests covering both directions
- [ ] `pytest` passes

**Hint**

Python's standard library has a `base64` module — no need to implement the
algorithm yourself.

---

## #13 — Add a `roman` command (integer ↔ Roman numerals)

**Labels:** `feature`, `intermediate`

**Description**

Add a command that converts an integer to a Roman numeral, or a Roman
numeral back to an integer.

Example usage:
```
pytoolbox roman 1994
pytoolbox roman MCMXCIV --to-int True
```

**Files likely to change**

- `pytoolbox/commands/roman.py` (new)
- `tests/test_roman.py` (new)

**Acceptance criteria**

- [ ] Converts integers from 1–3999 to correct Roman numerals
- [ ] Converts valid Roman numerals back to integers
- [ ] Has tests for both directions, including edge cases like `4`, `9`,
      `40`, `90`, `400`, `900`
- [ ] `pytest` passes

**Hint**

A lookup table of value/symbol pairs, processed greedily from largest to
smallest, is the classic approach.

---

## #14 — Add a `morse` command (encode/decode)

**Labels:** `feature`, `intermediate`

**Description**

Add a command that translates text to Morse code and back.

Example usage:
```
pytoolbox morse "SOS"
pytoolbox morse "... --- ..." --decode True
```

**Files likely to change**

- `pytoolbox/commands/morse.py` (new)
- `tests/test_morse.py` (new)

**Acceptance criteria**

- [ ] Encodes letters and digits to Morse code
- [ ] Decodes Morse code back to text
- [ ] Has tests for both directions
- [ ] `pytest` passes

**Hint**

A dictionary mapping characters to Morse sequences (and its reverse for
decoding) covers most of this.

---

## #15 — Add a `slugify` command

**Labels:** `feature`, `good first issue`

**Description**

Add a command that turns a string into a URL-friendly "slug": lowercase,
spaces replaced with hyphens, punctuation stripped.

Example usage:
```
pytoolbox slugify "Hello, World!"
```
Expected output: `hello-world`

**Files likely to change**

- `pytoolbox/commands/slugify.py` (new)
- `tests/test_slugify.py` (new)

**Acceptance criteria**

- [ ] Produces lowercase, hyphen-separated slugs
- [ ] Strips punctuation
- [ ] Collapses multiple spaces/hyphens into one
- [ ] Has tests
- [ ] `pytest` passes

**Hint**

Regular expressions (`re` module) are a natural fit for stripping unwanted
characters.

---

## #16 — Add a `caesar` command (Caesar cipher)

**Labels:** `feature`, `intermediate`

**Description**

Add a command that applies a Caesar cipher shift to text.

Example usage:
```
pytoolbox caesar "hello" --shift 3
```
Expected output: `khoor`

**Files likely to change**

- `pytoolbox/commands/caesar.py` (new)
- `tests/test_caesar.py` (new)

**Acceptance criteria**

- [ ] Shifts letters by `--shift` positions, wrapping around the alphabet
- [ ] Preserves letter case
- [ ] Leaves non-letter characters unchanged
- [ ] Negative shifts work (decoding)
- [ ] Has tests
- [ ] `pytest` passes

**Hint**

The modulo operator (`%`) is what makes the alphabet wrap around correctly.

---

## #17 — Add a `hexrgb` command (hex color ↔ RGB)

**Labels:** `feature`, `good first issue`

**Description**

Add a command that converts a hex color code to RGB values, or vice versa.

Example usage:
```
pytoolbox hexrgb "#FF8800"
```
Expected output something like: `R=255 G=136 B=0`

**Files likely to change**

- `pytoolbox/commands/hexrgb.py` (new)
- `tests/test_hexrgb.py` (new)

**Acceptance criteria**

- [ ] Correctly parses hex codes with or without a leading `#`
- [ ] Produces correct R, G, B integer values
- [ ] Has tests, including edge cases like `#000000` and `#FFFFFF`
- [ ] `pytest` passes

**Hint**

`int(value, 16)` converts a hex string to an integer.

---

## #18 — Add an `agecalc` command

**Labels:** `feature`, `beginner`

**Description**

Add a command that calculates someone's age in years from a birth date.

Example usage:
```
pytoolbox agecalc 2000-01-15
```

**Files likely to change**

- `pytoolbox/commands/agecalc.py` (new)
- `tests/test_agecalc.py` (new)

**Acceptance criteria**

- [ ] Parses a date in `YYYY-MM-DD` format
- [ ] Correctly accounts for whether this year's birthday has happened yet
- [ ] Rejects clearly invalid dates with a friendly error, not a traceback
- [ ] Has tests
- [ ] `pytest` passes

**Hint**

The `datetime` module's `date` type supports comparison, which helps with
the "has the birthday happened yet this year" logic.

---

## #19 — Add a `loremipsum` command

**Labels:** `feature`, `good first issue`

**Description**

Add a command that prints N words of placeholder "lorem ipsum" text.

Example usage:
```
pytoolbox loremipsum --words 20
```

**Files likely to change**

- `pytoolbox/commands/loremipsum.py` (new)
- `tests/test_loremipsum.py` (new)

**Acceptance criteria**

- [ ] Prints exactly the requested number of words
- [ ] Works for small and large word counts (e.g. 1 and 200)
- [ ] Has tests
- [ ] `pytest` passes

**Hint**

A fixed pool of placeholder words, sampled (with repetition) to reach the
requested count, is enough — no need for an external dependency.

---

## #20 — Add a `jsonfmt` command (pretty-print JSON)

**Labels:** `feature`, `good first issue`

**Description**

Add a command that reads a JSON file and pretty-prints it with indentation.

Example usage:
```
pytoolbox jsonfmt data.json
```

**Files likely to change**

- `pytoolbox/commands/jsonfmt.py` (new)
- `tests/test_jsonfmt.py` (new)

**Acceptance criteria**

- [ ] Reads a JSON file and prints an indented, readable version
- [ ] Gives a friendly error message for invalid JSON (not a raw traceback)
- [ ] Has tests, including one for invalid JSON
- [ ] `pytest` passes

**Hint**

`json.load` plus `json.dumps(..., indent=2)` does most of the work; wrap the
parsing in a `try`/`except`.

---

## #21 — Add a `tzconvert` command (timezone conversion)

**Labels:** `feature`, `intermediate`

**Description**

Add a command that converts a time from one IANA timezone to another, using
the standard library's `zoneinfo` module (no extra dependency needed).

Example usage:
```
pytoolbox tzconvert "2024-06-01 15:00" --from-tz "America/New_York" --to-tz "Asia/Kolkata"
```

**Files likely to change**

- `pytoolbox/commands/tzconvert.py` (new)
- `tests/test_tzconvert.py` (new)

**Acceptance criteria**

- [ ] Correctly converts a naive datetime between two named timezones
- [ ] Gives a friendly error for an unknown timezone name
- [ ] Has tests
- [ ] `pytest` passes

**Hint**

`from zoneinfo import ZoneInfo` — attach a zone to the source datetime, then
call `.astimezone()` with the destination zone.

---

## #22 — Add a `unitconvert` command

**Labels:** `feature`, `beginner`

**Description**

Add a command that converts between common units: kilometers/miles,
kilograms/pounds, Celsius/Fahrenheit, etc. Pick at least two unit pairs to
support.

Example usage:
```
pytoolbox unitconvert 10 km mi
```

**Files likely to change**

- `pytoolbox/commands/unitconvert.py` (new)
- `tests/test_unitconvert.py` (new)

**Acceptance criteria**

- [ ] Supports at least two conversion pairs (e.g. km↔mi, kg↔lb)
- [ ] Gives a friendly error for an unsupported unit pair
- [ ] Has tests for each supported conversion
- [ ] `pytest` passes

**Hint**

A dictionary keyed by `(from_unit, to_unit)` mapping to a conversion factor
keeps this simple and easy to extend.

---

## #23 — Add a `bmi` command (with input validation)

**Labels:** `feature`, `beginner`

**Description**

Add a command that calculates Body Mass Index from height (meters) and
weight (kilograms), with sensible validation of the inputs.

Example usage:
```
pytoolbox bmi --height 1.75 --weight 70
```

**Files likely to change**

- `pytoolbox/commands/bmi.py` (new)
- `tests/test_bmi.py` (new)

**Acceptance criteria**

- [ ] Computes BMI correctly (`weight / height^2`)
- [ ] Rejects zero or negative height/weight with a friendly error, not a
      crash
- [ ] Has tests, including for invalid input
- [ ] `pytest` passes

**Hint**

Validate inputs before doing the division, and use `typer.Exit` or similar
for a clean early exit on bad input.

---

## #24 — Add a `countdown` command (with a progress bar)

**Labels:** `feature`, `intermediate`

**Description**

Add a command that counts down from N seconds, showing a live progress bar
using `rich`.

Example usage:
```
pytoolbox countdown --seconds 10
```

**Files likely to change**

- `pytoolbox/commands/countdown.py` (new)
- `tests/test_countdown.py` (new)

**Acceptance criteria**

- [ ] Counts down for the requested number of seconds
- [ ] Shows a `rich` progress bar while counting down
- [ ] Has a test that doesn't require the test suite to actually wait the
      full duration (e.g. test with a very small number of seconds, or test
      the underlying logic directly)
- [ ] `pytest` passes

**Hint**

`rich.progress.track` or `rich.progress.Progress` can drive both the timing
and the bar.

---

# Add-ons

## #25 — Add a `--version` flag to the main app

**Labels:** `add-on`, `good first issue`

**Description**

Running `pytoolbox --version` should print the installed version and exit,
instead of currently doing nothing meaningful.

**Files likely to change**

- `pytoolbox/cli.py`

**Acceptance criteria**

- [ ] `pytoolbox --version` prints the version from `pytoolbox.__version__`
- [ ] Has a test
- [ ] `pytest` passes

**Hint**

Typer supports an eager callback option for flags like `--version`.

---

## #26 — Add a `--json` output option to `list`

**Labels:** `add-on`, `intermediate`

**Description**

`pytoolbox list --json` should print the command list as a JSON array
instead of a rich table, so it can be used by scripts/tools.

**Files likely to change**

- `pytoolbox/cli.py`

**Acceptance criteria**

- [ ] `pytoolbox list --json` prints valid JSON with name/help for each
      command
- [ ] `pytoolbox list` (no flag) still prints the rich table as before
- [ ] Has a test that parses the JSON output
- [ ] `pytest` passes

**Hint**

Keep this additive — branch on the flag inside the existing `list` command
rather than creating a second command.

---

## #27 — Add `ruff` linting to CI

**Labels:** `add-on`, `beginner`

**Description**

Add `ruff` as a dev dependency and run it in CI so style/lint issues are
caught automatically on every PR.

**Files likely to change**

- `requirements.txt`
- `pyproject.toml`
- `.github/workflows/ci.yml`

**Acceptance criteria**

- [ ] `ruff` is added as a dev dependency
- [ ] A reasonable `ruff` configuration is added to `pyproject.toml`
- [ ] CI runs `ruff check .` and fails the build on lint errors
- [ ] The existing codebase passes (or lint config is adjusted sensibly)

**Hint**

Start with ruff's default rule set before adding stricter rules — a wall of
unrelated lint errors on day one isn't the goal.

---

## #28 — Add test coverage reporting with `pytest-cov`

**Labels:** `add-on`, `beginner`

**Description**

Add `pytest-cov` so contributors can see which lines are covered by tests,
and show a coverage summary in CI.

**Files likely to change**

- `requirements.txt`
- `.github/workflows/ci.yml`

**Acceptance criteria**

- [ ] `pytest-cov` is added as a dev dependency
- [ ] CI runs `pytest --cov=pytoolbox` and prints a coverage summary
- [ ] README mentions how to run coverage locally

**Hint**

`pip install pytest-cov` then `pytest --cov=pytoolbox --cov-report=term-missing`.

---

## #29 — Add a CI matrix for multiple Python versions and OSes

**Labels:** `add-on`, `intermediate`

**Description**

CI currently only runs on Ubuntu with Python 3.11. Expand it to a matrix
covering Python 3.10, 3.11, and 3.12, on both Ubuntu and Windows, so
cross-platform/cross-version regressions are caught.

**Files likely to change**

- `.github/workflows/ci.yml`

**Acceptance criteria**

- [ ] CI matrix includes Python 3.10, 3.11, 3.12
- [ ] CI matrix includes `ubuntu-latest` and `windows-latest`
- [ ] All matrix jobs pass
- [ ] Total CI time stays reasonable (jobs run in parallel)

**Hint**

GitHub Actions' `strategy.matrix` is designed exactly for this; `os` and
`python-version` become matrix axes.

---

## #30 — Improve the README with a GIF/screenshot section and commands table

**Labels:** `add-on`, `good first issue`

**Description**

The README would be more inviting with a short section showing what the
tool actually looks like in a terminal (a GIF or screenshot), in addition to
the existing commands table.

**Files likely to change**

- `README.md`

**Acceptance criteria**

- [ ] README has a "Demo" section with a placeholder for a GIF/screenshot
      and instructions on how to record one (e.g. using `asciinema` or a
      terminal recorder of choice)
- [ ] Commands table stays accurate and up to date
- [ ] Markdown renders correctly on GitHub

**Hint**

You don't need to actually produce a perfect recording — a clear placeholder
and instructions are enough for this issue.

---

## #31 — Friendly error messages for missing files

**Labels:** `add-on`, `intermediate`

**Description**

Commands that take a file path (`wordcount`, `filehash`, `csv2json`) crash
with a raw Python traceback if the file doesn't exist. They should print a
short, friendly error message instead.

**Steps to reproduce**

1. Run `pytoolbox wordcount does-not-exist.txt`.

**Expected result**

A short message like `Error: file not found: does-not-exist.txt` and a
non-zero exit code — no traceback.

**Actual result**

A full Python traceback (`FileNotFoundError`).

**Files likely to change**

- `pytoolbox/commands/wordcount.py`
- `pytoolbox/commands/filehash.py`
- `pytoolbox/commands/csv2json.py`
- Possibly a small shared helper, if one doesn't conflict with how the
  plugin system discovers commands

**Acceptance criteria**

- [ ] Missing files produce a short, friendly message, not a traceback
- [ ] The command exits with a non-zero exit code
- [ ] Has tests for the missing-file case in each affected command
- [ ] `pytest` passes

**Hint**

Typer raises a clean, typed exit (`typer.Exit`) nicely — catch the
`FileNotFoundError` (or check `Path.exists()` first) and print with `rich`
before exiting.
