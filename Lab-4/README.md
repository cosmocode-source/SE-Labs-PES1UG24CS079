# Lab 4 — Hangman Challenge

Enhancing a Python terminal game through bug fixing, session tracking, difficulty-based scoring, and input validation.

## Overview

The supplied Hangman game allows players to guess words from different categories across multiple rounds. This lab improves the existing implementation while retaining its modular structure and keeping all gameplay state in memory.

The work covers four areas:

- Prevent repeated guesses from affecting the round more than once.
- Track rounds, wins, and winning streaks throughout a session.
- Introduce difficulty levels with consistent scoring and hint penalties.
- Validate player input and provide clear, non-duplicated feedback.

## Folder Structure

```text
Lab-4/
├── README.md                          # Lab overview and submission details
├── BeforeChangesVideo.mp4             # Original bug demonstration
├── AfterChangesVideo.mp4              # Updated gameplay demonstration
└── Code Files (16_Hangman)/
    ├── README.md                      # Assignment and technical documentation
    ├── main.py                        # Application entry point
    ├── game.py                        # Gameplay, commands, and scoring
    ├── words.py                       # Word categories and hints
    ├── stats.py                       # Session statistics
    ├── requirements.txt               # Dependency information
    ├── .gitignore                     # Excludes generated Python caches
    └── tests/
        └── test_game.py               # Automated regression tests
```

This README documents the lab as a whole. The README inside the code folder provides the original assignment, detailed implementation notes, and technical instructions.

## Changes Implemented

| Task | Change | Expected Behaviour |
| --- | --- | --- |
| **1. Guess-state correctness** | Check both correct and incorrect previous guesses. | A repeated letter does not remove another life or count as a new guess. |
| **2. Session statistics** | Integrate `SessionStats` to record completed rounds, wins, and best streak. | Statistics persist between rounds; a loss resets the current streak but not the best streak. |
| **3. Difficulty and scoring** | Add difficulty selection and a once-per-round hint deduction. | Difficulty controls lives and rewards; hint scoring remains consistent even when the score starts at zero. |
| **4. Input and feedback** | Validate guesses, commands, category choices, difficulty choices, and replay answers. | Invalid input leaves gameplay state unchanged and each action receives clear feedback. |

### Original Bug and Fix

The original game removed a life whenever a wrong letter was entered, even if that letter had already been attempted.

| Action | Original Game | Updated Game — Medium Difficulty |
| --- | --- | --- |
| Start a round | 6 lives | 6 lives |
| Guess `z` | 5 lives; `Wrong.` | 5 lives; `Wrong.` |
| Guess `z` again | 4 lives; `Wrong.` | 5 lives; `Already guessed.` |

None of the supplied words contain `z`, making it a reliable demonstration of the defect.

### Difficulty and Scoring

| Difficulty | Starting Lives | Base Win Points | Hint Deduction |
| --- | ---: | ---: | ---: |
| Easy | 8 | 4 | 1 |
| Medium | 6 | 6 | 2 |
| Hard | 4 | 10 | 3 |

**Win reward = base win points + updated winning streak − hint deduction.**

The reward cannot fall below zero. A hint reduces the current round's eventual win reward only once. A loss earns no points, preserves earlier points, and resets the current winning streak. Quitting an unfinished round does not record it as a completed round.

## Running the Game

**Requirements:** Python 3.9 or later. No third-party packages are required.

From the `Lab-4` directory:

```bash
cd "Code Files (16_Hangman)"
python main.py
```

Choose a category and difficulty, then enter one letter at a time.

| Command | Action |
| --- | --- |
| `/hint` | Reveal one hint for the current round. |
| `/stats` | Display session statistics. |
| `/quit` | Exit during gameplay. |
| `q` | Exit from category, difficulty, or replay selection. |

All gameplay state is held in memory and ends when the program exits.

## Testing

From the code folder, run:

```bash
python -m unittest discover -s tests -v
```

Automated tests and manual gameplay checks should cover:

- Repeated correct and incorrect guesses.
- Invalid letters, empty input, and unknown commands.
- First and repeated hint requests.
- Category and difficulty changes between rounds.
- Multiple rounds, wins, losses, and streak resets.
- Session statistics and protection against duplicate round recording.
- Replay prompts, quitting, EOF, and Ctrl+C.

## Gameplay Videos

### Before Changes — 10 Seconds

Demonstrate the original repeated-guess bug:

1. Start with **6 lives** visible.
2. Enter `z` and show the decrease to **5 lives**.
3. Enter `z` again and show the incorrect decrease to **4 lives**.

### After Changes — 10 Seconds

Demonstrate the fix and new features:

1. Show the selected difficulty and available lives.
2. Enter `z` twice and show that the second attempt does **not** remove a life.
3. Use `/hint` to show the hint and scoring feedback.
4. Use `/stats` to show the session statistics.

Prepare the terminal before recording so the demonstration fits the required duration. Complete a round beforehand if you want the statistics to show a nonzero result.

## AI Assistance

AI assistance was used to inspect the code, explain proposed changes, and support implementation and testing. The student remains responsible for understanding the final code and verifying its behaviour.

**Complete chat-history link:** `ADD_ACCESSIBLE_SHARED_CHAT_LINK_HERE`

## Submission Checklist

- [ ] 10-second before-changes gameplay video.
- [ ] 10-second after-changes gameplay video.
- [ ] Accessible link to the complete AI chat history.

These are the three submission items listed in the assignment. A PDF is not required unless separately requested by the instructor.
