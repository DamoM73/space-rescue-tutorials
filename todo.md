# Space Rescue: Damien's tasks

Tasks from the Zensical rework that need a person, not Claude. Claude in VS Code works from `VSCODE_CLAUDE_TASKS.md`.

## Play-test

1. Play the game from each checkpoint in `docs/downloads/space_rescue_checkpoints.zip`, especially the Game Design pages (Difficulty, Goals and Rewards, Bonus Pickups, Subgoals, Ship Choice).
2. Decide whether these settings feel right, and change them on the pages if not:
    - difficulty settings: Easy 30–180 ticks at speed 7, Medium 15–150 at 10, Hard 8–90 at 14
    - rescue goal: 10 astronauts, +500 bonus
    - bonus pickup timer: 300–600 ticks
    - special power: 150 ticks on, 300 ticks cooldown
3. Check the Rescued and Streak counters fit at the bottom of the screen on Windows with Arial Black.
4. Check the menu positions (DifficultySelect, ShipSelect) and the HighScores screen layout.
5. Check the platformer demo's Jumper can reach both platforms.
6. Check the volume of the new sounds (`Bonus_score.mp3`, `Life_increase.ogg`, `Shields.ogg`, `Max_shot_increase.wav`, `Skill_used.mp3`).

## Decisions

1. Subgoal: shooting an astronaut takes one off the **rescued count**. Game Design originally said "subtracts one from the goal total". Change `docs/design/subgoals.md` if you meant something else.
2. Decide whether to add IPO table images to the new mechanic pages to match the lessons (they use markdown tables now).

## Diagrams (draw.io sources in `design/`)

1. `asteroid_direction.png` measures angles anticlockwise, but GameFrame measures them clockwise (90° is down). Fix the image, then remove the "Which way do the angles go?" tip from Lesson 8.
2. `lives_update_IPO.png` says `lives_list`, but the code uses `lives_icon`.

## space-rescue-resources repo

1. `Images/Sheild.png` is misspelt. The pages use `Shield_frames/Shield_0.png` instead, so renaming is optional.
2. `GameFrame/DataBaseController.py` still has the `get_lesson` example that the database page asks students to replace. Decide whether to leave it.
