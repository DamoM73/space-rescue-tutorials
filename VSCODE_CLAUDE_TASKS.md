# Tasks for Claude in VS Code

These tasks finished the Zensical rework of *Space Rescue*. They couldn't be done from Cowork, which could only create and overwrite files in this folder. It couldn't delete files, run git, access GitHub or write inside `.github/`.

The rework is live. All work now happens on `main` — the `zensical` branch is no longer used. Check with Damien before each task marked **Confirm first**. Report the output of the checks after each task.

## Context

- **Site generator:** Zensical 0.0.67 (pinned in `requirements.txt`). Config is `zensical.toml`. Pages are in `docs/`.
- **Preview:** `zensical serve`. **Build:** `zensical build --clean` (must report "No issues found").
- **Audience:** Year 9/10 students using VS Code (Thonny is an alternative, see `docs/reference/using_thonny.md`). Students clone `DamoM73/space-rescue-resources`, which holds GameFrame, the images and the sounds, and build the game in their copy.
- **Structure:** Home (`docs/index.md`); Start (`docs/start/`: introduction, setup, gameframe); Build the Game (`docs/lessons/01_welcome.md` to `14_lives.md`); Game Design (`docs/design/`: game_design, audio, unfair_punishment, then the new mechanic pages difficulty, goals_rewards, bonuses, subgoals, ship_choice); Your Own Game (`docs/own_game/`: planning, design_flowchart, coding_flowcharts, other_game_types, databases); Reference (`docs/reference/`: gameframe_api, index_of_topics, common_errors, finished_game, using_thonny, licence).
- **Examples:** the site builds one multi-file game. Every version of a file shown on a page is a snippet file at `docs/examples/<section>/<page>/stepNN/<path>.py`, where a step folder holds only the files that changed in that step, at their path in the game (for example `docs/examples/lessons/03_spaceship/step04/Objects/Ship.py`). Pages include them with `--8<-- "examples/..."` inside ```` ```python linenums="1" hl_lines="..." title="Objects/Ship.py" ````; `hl_lines` marks new or changed lines and `title` shows the file's path in the game. Fragments use a line range, for example `--8<-- "examples/lessons/05_ship_in_room/step01/Objects/Ship.py:32:39"` with `linenums="32"`; `hl_lines` still counts from 1 in those blocks. `docs/examples/lessons/04_advanced_movement/option_*` are alternative versions that aren't carried forward.
- **Checkpoint zip:** `python scripts/make_zip.py` builds `docs/downloads/space_rescue_checkpoints.zip` (260 files). Each `space_rescue/<section>/<page>/` folder holds the `Objects/`, `Rooms/` and `GameFrame/` files at the end of that page, carried forward in the order listed in `CHECKPOINTS` (lessons, then the design pages, then `own_game/databases`). `own_game/platformer`, `top_down` and `scrolling` are standalone demo games (`STANDALONE`). Images and sounds aren't in the zip; students copy the folders over their resources repo.
- **Checks:**
    - `python scripts/check_explanations.py` confirms every Code explanation line number matches its snippet. When a code block has `hl_lines`, only highlighted code lines need explaining; comment lines are never referenced. Expect `0 issue(s) found`.
    - `python scripts/test_checkpoints.py --starter ../space-rescue-resources` copies the resources repo, applies each checkpoint and plays it headless (SDL dummy drivers) with scripted keys. Expect `0 checkpoint(s) failed`. It also reports image or sound names whose capitals don't match the file (they work on Windows but crash on macOS and Linux).
- **Colour scheme:** charcoal slate `#37474F` (header, tabs, light-mode links and headings; 9.6:1 with white text), slate `#546E7A` (primary light, decorative only), light grey `#CFD8DC` (active and hovered tab, dark-mode headings and accent), light blue `#8AB4F8` (dark-mode links). Set in `docs/stylesheets/extra.css`. It's clearly different from the micro:bit (navy), Lego Spike (magenta), Turtle (teal) and Deepest Dungeon (burnt orange) banners.
- **Callouts:** five types, the same on all of Damien's tutorial sites:
    - `!!! learn "In this lesson we will learn"` (lessons and design pages) or `"On this page we will learn"` (other pages): amber, target icon, directly under the title. There are no videos on this site.
    - `!!! primm "PRIMM"`: green, flask icon, after each change students run
    - `??? note "Code explanation"`: purple, `</>` icon, collapsed, after each snippet
    - `!!! tip "Title"`: light blue, light bulb icon, every other aside
    - `!!! warning "Title"`: hot pink, triangle alert icon
- **Code blocks:** grey border on every code block; error messages use ```` ``` { .text .error linenums="1" } ```` (red border and text), followed by a line-by-line breakdown. `docs/own_game/design_flowchart.md` uses a Mermaid diagram (enabled in `zensical.toml` with `pymdownx.superfences.custom_fences`).
- **Writing style:** Australian English, written for Year 9/10, in Damien's inclusive "we" voice. Instructions follow the pattern "Open ***Objects/Ship.py***, add the highlighted code below and save it." Code explanations are `- **line n** → full sentence ending in a full stop.`, with `…` joining an `if` and its body across lines. Each page ends with a **Commit and push** section. There are no exercises; PRIMM **Modify** prompts and the "Where next?" ideas take their place.
- **Restart fix:** `Objects/Title.py` resets `Globals.SCORE`, `LIVES`, `rescued` and `streak` when space is pressed (Lesson 14 explains why). `Globals.end_game_level` is `0`. Background music only starts once, using `Globals.music_playing` (Audio page).
- **Rework plan:** the full audit and plan are in Damien's Claude project as `claude/space-rescue-tutorials_rework_plan.md`, with progress in `claude/space-rescue-tutorials_progress.md`.

## 1. Remove the old Sphinx site — Confirm first

The old site is still on `main` and will be tagged before merging (task 6), so nothing is lost. Show Damien this list before deleting anything:

- root pages: `index.md`, `01_introduction.md` to `20_unfair_punishment.md`, `95_planning.md`, `96_creating.md`, `97_using_thonny.md`, `98_index_of_topics.md`, `99_documentation.md`
- Sphinx files: `conf.py`, `Makefile`, `make.bat`, `_build/`, `_ext/`, `_static/`
- old content folder: `assets/` (the images in use were copied to `docs/assets/`; the draw.io sources were copied to `design/`)
- stray notes: `style.md` (the old Sphinx admonition guide)
- `%GIT%space-rescue-tutorials/` (a stray chat history folder)
- `assets/.$diagrams.drawio.bkp` and `assets/.$Designing in GameFrame.drawio.bkp` (draw.io backups, removed with `assets/`)

These images in `assets/img/` weren't used by the old site and weren't copied: `create_room.png`, `create_venv_trouble.png`, `handle_collisions.png`, `move_object_with_keys.png`, `new_terminal.png`, `spaceship_out_of_bounds.png`, `title.png`, `venv_confirm.png`. Ask Damien if any should be kept (they'll go with `assets/`).

Keep `README.md`, `todo.md` (Damien's own task list), `.gitignore`, `.gitattributes`, `requirements.txt`, `zensical.toml`, `VSCODE_CLAUDE_TASKS.md`, `docs/`, `scripts/`, `design/` and `.github/`. `.venv/` is local and already ignored.

Before deleting, search the repo to confirm nothing in `docs/`, `scripts/` or `zensical.toml` references these files. Then run `zensical build --clean`.

## 2. Replace the licence file — Confirm first

`LICENSE` is the MIT licence, but the site now uses CC BY-NC-SA 4.0 for content and GPLv3 for code (see `docs/reference/licence.md` and the README). Ask Damien whether to replace `LICENSE` with the GPLv3 text (as on his other tutorial sites), then do it.

## 3. Replace the deploy workflow

Delete `.github/workflows/write_to_gh_pages.yml` and create `.github/workflows/deploy.yml` with the workflow below. It builds with Zensical and deploys with GitHub Pages Actions. It only runs on `main`, so pushing to `zensical` won't change the live site.

```yaml
name: Deploy site

# Runs only when changes are pushed to main
on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v6
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: zensical build --clean
      - uses: actions/upload-pages-artifact@v5
        with:
          path: site
      - uses: actions/deploy-pages@v5
        id: deployment
```

The action versions come from Zensical's own template. Confirm each version exists on GitHub before committing.

## 4. Play-test the new pages

The new pages (Difficulty, Goals and Rewards, Bonus Pickups, Subgoals, Ship Choice, Other Game Types, Saving Data with a Database) were written in Cowork and tested headless: every checkpoint runs without errors, and each mechanic was unit-tested (goal reached ends the game with +500, repair kits cap lives at 5, shields block asteroid damage and turn off after their timer, the streak limits lasers to 1–5 and resets on damage, the Swerver doubles speed for 150 ticks then cools down for 300, the Attractor pulls astronauts towards the ship, high scores save to `GameFrame/scores.db` and come back highest first). Things that couldn't be checked without a screen and speakers:

1. Fonts: the HUD uses `'Arial Black'`. Check the Rescued and Streak counters fit at the bottom of the screen on Windows and don't overlap.
2. The menu positions on the DifficultySelect and ShipSelect screens, and the HighScores screen layout (positions were calculated, not seen).
3. The platformer demo's jump: the Jumper should be able to reach both platforms.
4. Sound levels for the new sounds (`Bonus_score.mp3`, `Life_increase.ogg`, `Shields.ogg`, `Max_shot_increase.wav`, `Skill_used.mp3`, which is 4 seconds long).

If `pygame` is installed, also run `python scripts/test_checkpoints.py --starter <path to space-rescue-resources>` and report the result.

## 5. Final checks

1. Run `python scripts/make_zip.py`. Expected: `Wrote 260 file(s)`.
2. Run `python scripts/check_explanations.py`. Expected: `0 issue(s) found`.
3. Run `zensical build --clean`. Expected: `No issues found`.
4. Check every external link in `docs/` returns a working page (python.org, git-scm.com, GitHub Desktop, VS Code Marketplace, Pygame docs, GitLab, Quantic Foundry, the Psychology of Games, Deepest Dungeon, Turtle, Creative Commons). Report broken ones to Damien rather than guessing replacements.
5. Spell-check the pages for Australian English. Leave any American spellings inside code and library names as they are.
6. Commit to `zensical` and push.

## 6. Go live — Confirm first

1. Tag the current `main` as `v1-sphinx` and push the tag, so the old site can be restored.
2. Merge `zensical` into `main` and push.
3. Change the Pages source to GitHub Actions: **Settings** → **Pages** → **Source**, or `gh api -X PUT repos/DamoM73/space-rescue-tutorials/pages -f build_type=workflow`.
4. Watch the **Deploy site** workflow run, then check that <https://damom73.github.io/space-rescue-tutorials/> shows the new site.
5. Once the new site is confirmed working, the old `gh-pages` branch can be deleted. **Confirm first.**
6. From now on, all work happens on `main`. Update the intro of this file to say so.

## Tasks for Damien (not for Claude)

These are also in `todo.md`, which Damien keeps up to date. Don't delete or edit it unless he asks.


- Play through the game from each checkpoint, especially the new mechanic pages, and decide whether the difficulty settings, the rescue goal (10), the bonus timers and the power timings feel right.
- Check the subgoal interpretation: shooting an astronaut takes one off the **rescued count** (Game Design said "subtracts one from the goal total"). Change it on the Subgoals page if you meant something else.
- Fix these diagrams in draw.io (sources in `design/`):
    - `asteroid_direction.png` measures angles anticlockwise; GameFrame measures them clockwise (90° is down). Lesson 8 has a tip explaining this; remove it once the image is fixed.
    - `lives_update_IPO.png` says `lives_list`, but the code uses `lives_icon`.
- Add IPO table images for the new mechanic pages if you'd like them to match the lessons (they currently use markdown tables).
- Check whether `space-rescue-resources` should be updated: `Images/Sheild.png` is misspelt (the pages use `Shield_frames/Shield_0.png` instead), and `GameFrame/DataBaseController.py` still has the `get_lesson` example that the database page asks students to replace.
