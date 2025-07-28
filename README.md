# 🏁 Mancala Board Game in Python

A command-line implementation of the classic **Mancala** (Μάνκαλα) board game, written in Python. The game supports two players (Player X and Player Y) taking turns with full rules including stone distribution, capturing, and turn management.

## 🎯 Features

- Complete CLI-based gameplay
- Capturing logic (mirror pits)
- Replay turn when last stone lands in your own empty pit
- Auto-detection of game end and winner announcement
- Accurate board rendering using ASCII layout
- Valid input handling and automatic move validation

## 📌 Game Rules Implemented

- Each player controls 6 pits and 1 store.
- Players take turns to move stones counter-clockwise, skipping opponent's store.
- Capturing occurs if the last stone lands in an empty pit on your side.
- Game ends when one player's pits are empty — remaining stones go to the opponent’s store.

## 🧠 How It Works

- The board is represented as a Python dictionary with each pit as a key.
- Player pits:
  - Player X: `A-F`, store: `X`
  - Player Y: `1-6`, store: `Y`
- Movement path is defined with a `path_pit` mapping.
- Mirror pit logic is handled with the `mirror_pit` dictionary.

## 🖥️ Game Output

The game is rendered in the console in the following structure:

+--<<--+--<<--+--<<--+-Player Y-<<-+--<<--+--<<--+--<<--+
|Y |6 |5 |4 |3 |2 |1 |X |
Y | XX | XX | XX | XX | XX | XX | X
B | | | | | | | B
A XX +------+------+------+------+------+------+ XX A
N |A |B |C |D |E |F | N
K | XX | XX | XX | XX | XX | XX | K
+-->>--+-->>--+-->>--+-Player X->>-+->>--+-->>--+-->>--+


(Where `XX` is the current count of balls)

## ▶️ How to Play

Run the game in your terminal:

```bash
python mancala.pyp
