
# 🎮 Hangman Game in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Made With Love](https://img.shields.io/badge/Made%20With-❤️-red)

> 🎯 A fun CLI-based Hangman game to practice Python fundamentals

---

## ✨ Features

| Feature           | Description                              |
| ----------------- | ---------------------------------------- |
| 🎲 Random Word    | Selects a random word each time you play |
| ⌨️ User Input     | Interactive letter guessing              |
| ❤️ Lives System   | Limited attempts to guess the word       |
| 🎨 ASCII Art      | Visual hangman representation            |
| 🔁 Game Loop      | Runs until win or loss                   |
| 🧠 Smart Tracking | Keeps track of guessed letters           |

---

## 🧠 Concepts Used

* 🔁 Loops (`while`, `for`)
* 🔀 Conditional Statements (`if-elif-else`)
* 📚 Lists & Strings
* 🎯 Game Logic Design
* 📥 User Input Handling
* 🧩 State Management (lives, guesses)

---

## 🕹️ Gameplay Logic

```mermaid
graph TD
A[Start Game] --> B[Random Word Selected]
B --> C[Display Blanks]
C --> D[User Guesses Letter]
D --> E{Correct?}
E -->|Yes| F[Reveal Letter]
E -->|No| G[Reduce Life]
F --> H{Word Complete?}
G --> I{Lives Left?}
H -->|Yes| J[Win 🎉]
H -->|No| D
I -->|Yes| D
I -->|No| K[Lose 💀]
```

---

## 🎮 Rules

* You can guess **one letter at a time**
* Each wrong guess reduces your ❤️ lives
* You win if you guess the word before lives reach 0
* You lose if all lives are exhausted

---

## 📷 Sample Output

```
_ _ _ _ _
Guess the letter: a
Lives left: 5
_ a _ _ _
```

---

## ⚠️ Known Limitations

* No input validation for invalid characters
* No replay option after game ends
* Limited word list

---

## 🚀 Future Improvements

* ✅ Input validation (only single letter allowed)
* 🎚️ Difficulty levels (Easy / Medium / Hard)
* 🏆 Score tracking system
* 🖥️ GUI version (Tkinter / PyGame)
* 👥 Multiplayer mode
* 🗂️ Word categories (Animals, Fruits, etc.)

---

## 🛠️ Requirements

* Python 3.x
* Works on any OS (Windows / Linux / Mac)

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 🙌 Acknowledgements

* Inspired by the classic Hangman game
* Built as part of learning Python fundamentals

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 💡 Author

**Prem Kumar**
Made with ❤️ and logic 😄
