# Space Rescue Tutorials

Tutorials for building a 2D space game in Python with [Pygame](https://www.pygame.org/) and the [GameFrame](https://gitlab.com/tuxta/gameframe) framework, then improving it with game design mechanics. Written for Year 9/10 Digital Technologies students using VS Code (Thonny also works).

Live site: <https://damom73.github.io/space-rescue-tutorials/>

Students build the game in their own copy of the [Space Rescue Resources](https://github.com/DamoM73/space-rescue-resources) repo, which holds GameFrame and all the images and sounds.

## Preview the site

```
pip install -r requirements.txt
zensical serve
```

Then open <http://localhost:8000>. To build the site: `zensical build --clean` (expect `No issues found`).

## Scripts

- `python scripts/make_zip.py` builds `docs/downloads/space_rescue_checkpoints.zip`: the game's code at the end of every lesson and game design page, plus the demo games.
- `python scripts/check_explanations.py` checks every Code explanation box against the code it explains (expect `0 issue(s) found`).
- `python scripts/test_checkpoints.py --starter ../space-rescue-resources` plays every checkpoint headless with scripted key presses and reports any crash (needs `pygame` and a clone of the resources repo).

## Layout

```
zensical.toml                 site config and navigation
docs/
  index.md                    home page
  start/                      introduction, setup, GameFrame overview
  lessons/                    the 14 lessons that build the core game
  design/                     game design and the mechanic pages
  own_game/                   planning, flowcharts, other game types, databases
  reference/                  GameFrame API, topic index, common errors, finished game, Thonny, licence
  examples/<section>/<page>/stepNN/<path>.py
                              every version of every file shown on a page
  assets/                     images
  stylesheets/extra.css       colours, callouts and code block styles
  downloads/                  the checkpoint zip
scripts/                      make_zip.py, check_explanations.py, test_checkpoints.py
design/                       draw.io sources for the diagrams
```

A `stepNN` folder holds only the files that changed in that step, at their path in the game (for example `step03/Objects/Ship.py`). Pages include them with `--8<-- "examples/..."` and mark new or changed lines with `hl_lines`.

## Licence

Content is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Code is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html). GameFrame is by Steven Tucker, under the GNU GPL.
