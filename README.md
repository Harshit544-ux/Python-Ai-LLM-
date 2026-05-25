# 🐍 Python AI & LLM Learning Repository

> A comprehensive collection of Python programming fundamentals and advanced AI/LLM concepts for learners at all levels.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📚 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Python Fundamentals](#python-fundamentals)
- [AI & LLM Section](#ai--llm-section)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Contributing](#contributing)

---

## 🎯 Overview

This repository is designed as a comprehensive learning resource that covers:
- **Python Basics**: Essential programming concepts for beginners
- **Advanced Topics**: Exception handling, threading, and OOP principles
- **AI & LLM Integration**: Practical examples with Gemini and GPT models, including advanced prompting techniques

Whether you're a beginner learning Python or an intermediate developer exploring LLM integration, this repository has something for you.

---

## 📁 Project Structure

```
Python-Ai-LLM/
├── 1_print.py                 # Print function and output formatting
├── 2_dataType.py              # Data types and type conversion
├── 3_operator.py              # All Python operators
├── 4_ifElse.py                # Conditional statements
├── 5_function.py              # Function definition and usage
├── 6_opps.py                  # Object-Oriented Programming
├── 7_exception_handling.py    # Error handling and exceptions
├── 8_thread.py                # Threading and concurrency
├── LLM/                        # AI & LLM Integration
│   ├── gemini.py              # Google Gemini integration
│   ├── gpt.py                 # OpenAI GPT integration
│   ├── tokenization.py        # Text tokenization utilities
│   └── prompting/             # Advanced prompting techniques
│       ├── chain_of_thought.py    # Chain-of-Thought prompting
│       ├── few_shot.py            # Few-Shot prompting examples
│       └── zero.py                # Zero-Shot prompting
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

---

## 🎓 Python Fundamentals

### Core Concepts

| File | Topic | Description |
|------|-------|-------------|
| `1_print.py` | Print Function | Output formatting with separators and end parameters |
| `2_dataType.py` | Data Types | Integers, floats, strings, lists, tuples, dictionaries, sets, and type checking |
| `3_operator.py` | Operators | Arithmetic, relational, logical, bitwise, assignment, and membership operators |
| `4_ifElse.py` | Conditionals | If/elif/else statements with practical examples like login systems and menu programs |
| `5_function.py` | Functions | Function definition, parameters, return values, and scope |
| `6_opps.py` | OOP | Classes, objects, constructors, encapsulation, and real-world ATM simulation |
| `7_exception_handling.py` | Exception Handling | Try/except blocks, error management, and graceful error handling |
| `8_thread.py` | Threading | Concurrent execution, thread management, and synchronization |

---

## 🤖 AI & LLM Section

### Overview

The `LLM/` directory contains practical implementations for integrating Large Language Models into Python applications.

### Core Modules

#### 🔷 `gemini.py`
Integration with Google's Gemini API for advanced AI capabilities.

#### 🟢 `gpt.py`
Integration with OpenAI's GPT models for natural language processing tasks.

#### 🧮 `tokenization.py`
Utilities for text tokenization and token counting across different models.

### Advanced Prompting Techniques (`LLM/prompting/`)

#### ⛓️ `chain_of_thought.py`
Implements Chain-of-Thought (CoT) prompting for complex reasoning tasks.
- Break down problems into logical steps
- Improve accuracy on multi-step problems
- Better for mathematical and logical reasoning

#### 🎯 `few_shot.py`
Demonstrates Few-Shot prompting with practical examples.
- Learn from limited examples
- Task-specific pattern recognition
- Reduces hallucinations through examples

#### 🚀 `zero.py`
Zero-Shot prompting examples for immediate task execution.
- Direct instruction without examples
- Fast results for well-defined tasks
- Baseline approach for various tasks

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Python-Ai-LLM-.git
   cd Python-Ai-LLM-
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 How to Use

### Running Python Fundamentals

Each file can be executed independently:

```bash
# Basic concepts
python3 1_print.py
python3 2_dataType.py
python3 3_operator.py

# Intermediate concepts
python3 4_ifElse.py
python3 5_function.py
python3 6_opps.py

# Advanced concepts
python3 7_exception_handling.py
python3 8_thread.py
```

### Running LLM Examples

```bash
# Gemini integration
python3 LLM/gemini.py

# GPT integration
python3 LLM/gpt.py

# Prompting techniques
python3 LLM/prompting/chain_of_thought.py
python3 LLM/prompting/few_shot.py
python3 LLM/prompting/zero.py
```

### Configuration

Before running LLM examples, ensure your API keys are set:

```bash
export GOOGLE_API_KEY="your-gemini-key"
export OPENAI_API_KEY="your-openai-key"
```

---

## 🛠️ Requirements

Check `requirements.txt` for all dependencies:

```bash
pip install -r requirements.txt
```

---

## 📝 Learning Path

**Beginner** → Start with files 1-4 (Print, Data Types, Operators, Conditionals)

**Intermediate** → Progress to files 5-7 (Functions, OOP, Exception Handling)

**Advanced** → Explore file 8 (Threading) and LLM integration examples

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new examples
- Improve documentation
- Fix bugs
- Suggest enhancements

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 💡 Tips for Success

- 📖 Read the code comments carefully
- 🧪 Modify and experiment with the code
- 🐛 Use a debugger to step through complex sections
- 📚 Combine concepts to build mini-projects
- 🔄 Practice regularly

---

## 📞 Support

If you have questions or need help:
- Open an issue on GitHub
- Check existing documentation
- Review code comments
- Experiment with variations

---

**Happy Learning! 🎉**