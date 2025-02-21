🇰🇷 [README 한국어 버전](README.md)

🇯🇵 [README 日本語バージョン](README_jp.md)

# 🍎 Apple Game Macro

This is an automated macro for the Apple Game, optimized for MacBook Retina displays.
[Game Link](https://www.gamesaien.com/game/fruit_box_a/)

> This project was created purely for educational and learning purposes. Using macros in actual games may violate the game's terms of service, and the creator assumes no responsibility for any consequences.

## 🚀 Installation

1. Create and activate Python virtual environment

~~~zsh
python -m venv venv
source venv/bin/activate
~~~

2. Install required packages

~~~zsh
pip install -r requirements.txt
~~~

## 🎮 How to Run
1. With the game screen open, run the macro using the following command

~~~zsh
python apple_game_solver.py
~~~

## ✨ Key Features

- 🔢 Automatic recognition of numbers 1-9 (apples) on screen
- 🎯 Automatically finds and drags combinations that sum to 10
- 📏 Searches for valid combinations in horizontal/vertical lines and rectangular areas
- 🖥️ Automatic resolution adjustment for Retina displays
- 🔄 Automatic detection of consecutive number combinations
- ➕ Calculation of number sums within rectangular areas

## ⚠️ Notes

- 💻 Optimized for MacBook Retina displays
- 🔧 Coordinate adjustment needed for different environments
- ⌨️ Press Ctrl+C to stop the macro while running
- 🎯 Game window must be active before running
- ⏱️ Performs new scan every 3 seconds
