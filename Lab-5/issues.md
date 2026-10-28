# Lab 5 — Static Code Analysis

## File Analysed

`wildlife_sightings.py`

Line numbers in the issue table refer to the original source file unless stated otherwise.

## Before and After Results

| Tool | Before Changes | Latest After Report | Requirement Status |
|------|----------------|---------------------|--------------------|
| Pylint | 3.46/10 | 9.66/10; final newline warning remains | Score requirement met: above 9.5/10 |
| Bandit | 3 findings: 1 High, 1 Medium, 1 Low | No issues identified | Met |
| Flake8 | 6 findings | 1 finding: W292, no newline at end of file | Not yet met; final newline must be added |

## Identified Issues and Changes

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Weak MD5 hash — Bandit B324 | Security — High | 15 | Bandit flagged MD5 as a weak hash for security use. | Replaced MD5 with SHA-256. The retained six-character identifier is not an authentication token and can still have collisions. The latest Bandit report no longer flags this issue. |
| Formatted SQL query — Bandit B608 | Security — Medium | 9 | Values were inserted directly into SQL text using `.format()`, creating a possible SQL injection risk. | Replaced string formatting with SQLite `?` placeholders and passed values separately to `execute()`. The latest report no longer flags this issue. |
| Assertion used for a runtime check — Bandit B101 | Reliability — Low | 36 | The assertion could be removed when Python runs with optimisation enabled. | Replaced it with an explicit condition that raises `ValueError` if the expected species total is incorrect. The latest report no longer flags this issue. |
| Mutable default dictionary — Pylint W0102 | Bug / Reliability | 8–10 | The default dictionary was reused across calls, potentially sharing accumulated data unintentionally. | Changed the default to `None` and initialised a dictionary inside the function when needed. |
| Parameters shadowing the global connection — Pylint W0621 | Maintainability | 8, 18, 26 | Function parameters reused the global variable name `conn`. | Renamed the parameters to `connection` and updated their references. |
| Missing module docstring — Pylint C0114 | Documentation | 1 | The module had no description of its purpose. | Added a module docstring describing the wildlife sightings program. |
| Missing function docstrings — Pylint C0116 | Documentation | 8, 14, 18, 26, 32 | Five functions lacked descriptions. | Added concise docstrings describing each function. |
| Function names not in snake_case — Pylint C0103 | Naming / Style | 8, 14, 18 | Three function names did not follow Python naming conventions. | Renamed them to `log_sighting`, `observer_id`, and `zone_summary`, and updated their calls. |
| Unnecessary `else` after `return` — Pylint R1705 | Code Quality | 20–23 | The `if` branch returned immediately, making the following `else` unnecessary. | Removed the `else` and returned the result directly after the `if` block. |
| String formatting warning — Pylint C0209 | Code Quality | 9 | Pylint flagged `.format()` in the SQL statement. | Resolved this together with B608 using a parameterised query rather than an f-string. |
| Excessive line lengths — Pylint C0301 and Flake8 E501 | Formatting | 5, 9, 19, 27 | Four lines exceeded Flake8's 79-character limit; two also exceeded Pylint's 100-character limit. | Wrapped SQL statements and method calls across multiple lines. |
| Ambiguous variable name — Flake8 E741 | Readability | 28–29 | The variable `l` could be confused with the digit `1` or uppercase `I`. | Renamed it to `rarest_row` and updated its use. |
| Missing assignment spacing — Flake8 E225 | Formatting | 28 | The assignment lacked spaces around `=`. | Added spaces around the assignment operator. |
| Missing final newline — Pylint C0304 and Flake8 W292 | Formatting — Remaining | 63 in the updated file | The latest reports show that the source file does not end with a newline. | Add a newline after the final `main()` call, save the file, and rerun the tools to verify removal of both warnings. |

## Verification Summary

The latest reports confirm that:

- All three original Bandit findings are resolved.
- The Pylint score increased from 3.46/10 to 9.66/10.
- All six original Flake8 findings are resolved.
- One formatting issue remains in the updated file: a missing final newline.

The lab's static-analysis requirements will be fully met once the final newline is added and a fresh Flake8 report confirms no remaining findings.

Program behaviour and the three required commits must be verified separately; the static-analysis reports alone do not establish these.

## Report Locations

### Before Changes

- `reports/before changes/pylint_report.txt`
- `reports/before changes/bandit_report.txt`
- `reports/before changes/flake8_report.txt`

### After Changes

- `reports/after changes/pylint_report.txt`
- `reports/after changes/bandit_report.txt`
- `reports/after changes/flake8_report.txt`

## Commit Organisation

The required changes are organised into three groups:

1. Bandit security fixes.
2. Pylint code-quality fixes.
3. Flake8 formatting fixes and lab evidence.