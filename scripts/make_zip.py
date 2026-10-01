"""Build the student download: the game's code at the end of each lesson.

Each page's code lives in docs/examples/<section>/<page>/stepNN/<path>,
where a step folder only holds the files that changed in that step
(for example step03/Objects/Ship.py). For every page, the zip gets the
latest version of each file, carried forward from earlier pages, so every
folder is a checkpoint of the whole game at the end of that page:

    space_rescue/lessons/05_ship_in_room/Objects/Ship.py

Students copy a checkpoint's Objects, Rooms and GameFrame folders over
the same folders in their space-rescue-resources repo. The images, sounds
and the rest of GameFrame come from that repo, so they aren't in the zip.

The demo games in STANDALONE don't build on Space Rescue, so their
folders only hold the demo's own files.

Folders that don't start with "step" (for example the movement options in
lessons/04_advanced_movement) are alternatives and aren't carried forward.

Run from the repo root: python scripts/make_zip.py
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "docs" / "examples"
ZIP_PATH = ROOT / "docs" / "downloads" / "space_rescue_checkpoints.zip"

# Pages in the order they are built. Each starts from the end of the one before.
CHECKPOINTS = [
    "lessons/01_welcome",
    "lessons/02_gameplay",
    "lessons/03_spaceship",
    "lessons/04_advanced_movement",
    "lessons/05_ship_in_room",
    "lessons/06_zork",
    "lessons/07_asteroids",
    "lessons/08_moving_asteroids",
    "lessons/09_ship_asteroid_collision",
    "lessons/10_laser",
    "lessons/11_laser_asteroid_collision",
    "lessons/12_astronauts",
    "lessons/13_scoring",
    "lessons/14_lives",
    "design/audio",
    "design/unfair_punishment",
    "design/difficulty",
    "design/goals_rewards",
    "design/bonuses",
    "design/subgoals",
    "design/ship_choice",
    "own_game/databases",
]

# Small demo games that start from an empty project, not from Space Rescue.
STANDALONE = [
    "own_game/platformer",
    "own_game/top_down",
    "own_game/scrolling",
]


def apply_steps(page, files):
    """Return {relative path: source} after applying every step in a page."""
    files = dict(files)
    folder = EXAMPLES / page
    if folder.exists():
        steps = sorted(p for p in folder.iterdir() if p.is_dir() and p.name.startswith("step"))
        for step in steps:
            for source in sorted(step.rglob("*.py")):
                files[source.relative_to(step).as_posix()] = source
    return files


def checkpoints():
    """Yield (page, {relative path: source}) for every page, in order."""
    files = {}
    for page in CHECKPOINTS:
        files = apply_steps(page, files)
        yield page, files
    for page in STANDALONE:
        yield page, apply_steps(page, {})


def main():
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as archive:
        for page, files in checkpoints():
            for name, source in sorted(files.items()):
                archive.write(source, f"space_rescue/{page}/{name}")
                count += 1
    print(f"Wrote {count} file(s) to {ZIP_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
