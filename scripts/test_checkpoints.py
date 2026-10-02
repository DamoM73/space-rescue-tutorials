"""Play every checkpoint headless and report any crash.

For each page in scripts/make_zip.py, this copies the space-rescue-resources
starter repo into a temporary folder, copies the checkpoint's files over
it, then runs MainController.py with no window or sound. A script presses
keys (space, W, S and the other keys the game uses) for a set number of
frames. The game passes if it reaches the last frame without an exception.

It also reports image and sound file names whose case doesn't match the
file on disk, which works on Windows but crashes on macOS and Linux.

Run from the repo root:
    python scripts/test_checkpoints.py --starter ../space-rescue-resources
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_zip import checkpoints  # noqa: E402

HARNESS = r'''
import os, random, runpy, sys
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
random.seed(int(os.environ.get("SEED", "1")))
import pygame
sys.path.insert(0, os.getcwd())
FRAMES = int(os.environ.get("FRAMES", "3000"))
frame = [0]
case = set()
rooms = []

def exact(path):
    if not isinstance(path, str) or os.path.exists(path):
        return path
    folder, name = os.path.split(path)
    for other in os.listdir(folder or "."):
        if other.lower() == name.lower():
            case.add(path)
            return os.path.join(folder, other)
    return path

_load = pygame.image.load
pygame.image.load = lambda p, *a: _load(exact(p), *a)
_sound = pygame.mixer.Sound
pygame.mixer.Sound = lambda p, *a, **k: _sound(exact(p), *a, **k)
_music = pygame.mixer.music.load
pygame.mixer.music.load = lambda p, *a: _music(exact(p), *a)

# keys held on each frame
PLAN = {
    pygame.K_SPACE: lambda f: f % 40 in (5, 6) or (f % 7 == 0),
    pygame.K_w: lambda f: f > 50 and (f // 45) % 2 == 0,
    pygame.K_s: lambda f: f > 50 and (f // 45) % 2 == 1,
    pygame.K_e: lambda f: f % 97 == 10,
    pygame.K_m: lambda f: f % 89 == 10,
    pygame.K_h: lambda f: f % 83 == 10,
    pygame.K_a: lambda f: f % 61 == 10,
    pygame.K_RETURN: lambda f: f % 53 == 10,
    pygame.K_LCTRL: lambda f: f % 150 == 75,
    pygame.K_RCTRL: lambda f: f % 150 == 75,
    pygame.K_d: lambda f: (f // 60) % 3 == 0,
    pygame.K_LEFT: lambda f: (f // 40) % 4 == 0,
    pygame.K_RIGHT: lambda f: (f // 40) % 4 == 1,
    pygame.K_UP: lambda f: (f // 40) % 4 == 2,
    pygame.K_DOWN: lambda f: (f // 40) % 4 == 3,
}

class Keys(list):
    def __getitem__(self, key):
        rule = PLAN.get(key)
        return bool(rule and rule(frame[0]))

pygame.key.get_pressed = lambda: Keys([False] * 512)

class Clock:
    def tick(self, fps=0):
        frame[0] += 1
        if frame[0] >= FRAMES:
            from GameFrame import Globals
            print("ROOMS", " ".join(rooms))
            print("SCORE", Globals.SCORE, "LIVES", Globals.LIVES)
            if case:
                print("CASE", " ".join(sorted(case)))
            print("PASS")
            sys.stdout.flush()
            os._exit(0)
        return 33
    def get_fps(self):
        return 30

pygame.time.Clock = Clock
from GameFrame import Level
_run = Level.run
def run(self):
    rooms.append(type(self).__name__)
    return _run(self)
Level.run = run
runpy.run_path("MainController.py", run_name="__main__")
print("EXITED")
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--starter", default="../space-rescue-resources")
    parser.add_argument("--frames", default="3000")
    parser.add_argument("--page", help="only test pages containing this text")
    args = parser.parse_args()
    starter = Path(args.starter).resolve()
    if not (starter / "MainController.py").exists():
        sys.exit(f"Can't find the starter repo at {starter}")
    failures = 0
    for page, files in checkpoints():
        if args.page and args.page not in page:
            continue
        with tempfile.TemporaryDirectory() as tmp:
            game = Path(tmp) / "game"
            shutil.copytree(starter, game, ignore=shutil.ignore_patterns(".git", ".venv"))
            if any(name.startswith("Rooms/") for name in files) and "own_game/" in page and page != "own_game/databases":
                # demo games replace the starter's Rooms and Objects
                for folder in ("Rooms", "Objects"):
                    for old in (game / folder).glob("*.py"):
                        old.unlink()
            for name, source in files.items():
                (game / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(source, game / name)
            (game / "harness.py").write_text(HARNESS)
            env = dict(os.environ, FRAMES=args.frames)
            result = subprocess.run([sys.executable, "harness.py"], cwd=game, env=env,
                                    capture_output=True, text=True, timeout=600)
            out = result.stdout + result.stderr
            ok = "PASS" in result.stdout
            failures += not ok
            summary = [line for line in result.stdout.splitlines() if line.startswith(("ROOMS", "SCORE", "CASE"))]
            print(f"{'PASS' if ok else 'FAIL'}  {page}")
            for line in summary:
                print(f"      {line[:150]}")
            if not ok:
                print("\n".join("      " + line for line in out.strip().splitlines()[-12:]))
    print(f"{failures} checkpoint(s) failed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
