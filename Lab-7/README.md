# Lab 7 – Fuzz Testing for Input Validation Bugs

## Application
This lab uses the Gym Membership application from Lab 6. The application contains:
- `membership_cost()`
- `can_enter()`
- `bmi_category()`

## Files
- `processor.py` – Lab 6 application. Start with this original version, then fix the bugs found by fuzz testing.
- `test_processor.py` – Hypothesis tests for all three functions.
- `requirements.txt` – Required Python packages.
- `screenshots/` – Execution screenshots.
- `report/` – Final consolidated PDF.

## Setup
```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

## Run
Run the original application:
```bash
python processor.py
```

Run fuzz tests against the original application:
```bash
python -m pytest -q test_processor.py
```

Fix the bugs in `processor.py`, then run:
```bash
python processor.py
python -m pytest -q test_processor.py
```

The initial fuzz-test run is expected to expose failures. After fixing the application, the final test run should pass.

## Evidence to capture
1. Original application execution.
2. Failing Hypothesis tests against the original application.
3. Corrected application execution.
4. Successful final Hypothesis test execution.

Save screenshots in `screenshots/` using these names:
- `01_original_application.png`
- `02_failing_fuzz_tests.png`
- `03_corrected_application.png`
- `04_successful_fuzz_tests.png`

## Submission
Push the complete `Lab_7` folder to the assigned Git repository. Prepare one PDF in `report/` containing all four screenshots and the complete contents of `processor.py` and `test_processor.py`. Upload that single PDF using the Google Form shared by the instructor.

Do not upload `.venv/`, `__pycache__/`, or `.pytest_cache/` to Git.
