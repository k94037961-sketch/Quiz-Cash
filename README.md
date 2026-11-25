# Quiz-Cash


A command-line multiple-choice quiz and cash game written in Python where players answer four general knowledge questions to win a combined cash prize of **Rs. 66,000** only if they get every question right.

## How the Game Works
- Greets the player by name and asks all 4 multiple-choice questions (`A`, `B`, `C`, or `D`).
- Accepts lowercase or uppercase letters and ignores extra spaces (for example, `c` or ` C ` both match `C`).
- Continues to the next question even if a question is answered wrong, while marking `all_answers_correct = False`.
- Awards the sum of all rewards (`Rs. 1,000` + `Rs. 5,000` + `Rs. 10,000` + `Rs. 50,000` = `Rs. 66,000`) only when all answers are correct; otherwise ends with `Rs. 0`.

## Requirements
- Python 3.x

## How to Run
1. Save your script as `Quiz and cash.py`.
2. Open a terminal or command prompt in the folder containing the script.
3. Run:

```bash
python Quiz and cash.py
