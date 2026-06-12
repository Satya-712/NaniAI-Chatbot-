# 🤖 NaniAI Chatbot

> A rule-based AI chatbot built with Python — designed for intelligent, pattern-driven conversations without the overhead of large language models.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Type](https://img.shields.io/badge/Type-Rule--Based%20AI-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📌 Overview

**NaniAI Chatbot** is a lightweight, rule-based conversational AI built entirely in Python. It uses pattern matching and predefined response logic to simulate intelligent conversation — no external APIs, no heavy dependencies, no cloud costs.

This project demonstrates core concepts in natural language processing, dialogue management, and software design — making it an ideal showcase for AI/ML internships and portfolio presentations.

---

## ✨ Features

- 🧠 Rule-based response engine with pattern matching
- 💬 Multi-turn conversation support
- ⚡ Instant responses — no API calls or internet required
- 🗂️ Easily extensible rule sets
- 🖥️ Clean command-line interface
- 🪶 Zero heavy dependencies — pure Python

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/naniai-chatbot.git

# 2. Navigate into the project folder
cd naniai-chatbot

# 3. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 4. Install dependencies
pip install -r requirements.txt
```

### Run the Chatbot

```bash
python chatbot.py
```

---

## 🖼️ Screenshots

### Starting a Conversation
```
========================================
        Welcome to NaniAI Chatbot
========================================
Type 'quit' or 'exit' to end the chat.

You: Hello
NaniAI: Hi there! How can I help you today?

You: What can you do?
NaniAI: I can answer questions, have conversations, and assist with basic queries. Try me!

You: Tell me a joke
NaniAI: Why don't scientists trust atoms? Because they make up everything! 😄
```

### Handling Unknown Inputs
```
You: asdfghjkl
NaniAI: I'm not sure I understand that. Could you rephrase?

You: bye
NaniAI: Goodbye! Have a wonderful day. 👋
```

---

## 📁 Project Structure

```
naniai-chatbot/
│
├── chatbot.py          # Main chatbot application (single file)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── LICENSE             # MIT License
└── .gitignore          # Git ignore rules
```

---

## 🛠️ How It Works

NaniAI uses a **rule-based architecture**:

1. **Input Processing** — User input is normalized (lowercased, stripped, tokenized)
2. **Pattern Matching** — Input is matched against a set of predefined rules using keywords or regex
3. **Response Selection** — The matched rule triggers a curated response
4. **Fallback Handling** — Unmatched inputs receive a graceful default response

This approach is transparent, predictable, and easy to extend — ideal for controlled environments and learning purposes.

---

## 🔧 Customization

To add new conversation rules, open `chatbot.py` and extend the rules dictionary or pattern list:

```python
# Example rule addition
"rules": [
    {"patterns": ["your name", "who are you"], "response": "I'm NaniAI, your friendly chatbot!"},
    {"patterns": ["weather"], "response": "I can't check live weather, but it's always sunny in code! ☀️"},
]
```

---

## 🧪 Use Cases

- Learning how rule-based AI systems work
- Building a foundation before moving to ML-based NLP
- Internship project demonstrating Python and AI fundamentals
- Portfolio piece for AI/CS roles

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the rule set, add features, or enhance documentation.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-rules`)
3. Commit your changes (`git commit -m 'Add new conversation rules'`)
4. Push to the branch (`git push origin feature/new-rules`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Nani**

- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)

---

## 🌟 Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub — it helps others discover it!

---

*Built with ❤️ and Python*
