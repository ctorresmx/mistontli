# Mistontli

*Last update: 2017-04-10*

Mistontli means `cat` in Nahuatl, the old Aztec language. This is a Tic-Tac-Toe sort of playground, basically I want to try
some AI algorithms for this game.

## Requirements

All you need is listed on the `requirements.txt` file, you can still that using Python's pip:

```bash
$ pip install -r requirements.txt
```

A virtual environment is advised.

*NOTE:* This is a Python 3 only software.

## How to run it

Python-fire gives easy execution, you just to need to run the main `mistontli.py` file, if you are in the root folder, you can use:

```bash
$ python mistontli.py start-game <game-mode>
```

## Game modes

Currently Mistontli has the following modes: 

- `vs` - This is a common game for two human players
- `classicAI` - This uses a sort of min-max algorithm.

More modes can be implemented subclassing from the Base classes of `Game` and `Player`.
