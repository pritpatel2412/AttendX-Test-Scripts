# AttendX-Test-Scripts

Automation test scripts for the **AttendX** student attendance application.
All scripts are now version-controlled with Git and shared through GitHub
(replacing email and pen-drive sharing).

## Scripts
| File | Description |
|------|-------------|
| `login_test.py` | Verifies valid login and invalid-password login using Selenium WebDriver |
| `attendance_test.py` | Verifies marking a student present and absent on the attendance sheet |

## How to run
1. Install Python 3 and Google Chrome
2. `pip install selenium`
3. `python login_test.py`
4. `python attendance_test.py`

## Team workflow
- Always `git pull` before starting work
- Commit small changes with meaningful messages
- `git push` after every completed script change