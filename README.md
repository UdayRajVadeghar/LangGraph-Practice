# LangGraph Project

A Python project for working with LangGraph.

## Rule Number One: Virtual Environment ✅

This project follows the fundamental rule of Python development: **Always use a virtual environment!**

## Project Structure

```
langGraph/
├── venv/                 # Virtual environment (DO NOT commit)
├── src/                  # Source code package
│   └── __init__.py      # Package initialization
├── main.py              # Main entry point
├── requirements.txt     # Project dependencies
├── .gitignore          # Git ignore patterns
└── README.md           # This file
```

## Setup Instructions

1. **Create virtual environment** (Already done!):

   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**:

   ```bash
   # On Windows (Git Bash)
   source venv/Scripts/activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project**:
   ```bash
   python main.py
   ```

## Development

- Always activate the virtual environment before working
- Add new dependencies to `requirements.txt`
- Follow PEP 8 style guidelines
- Write tests for your code

## Dependencies

- LangChain: Framework for building applications with LLMs
- LangSmith: Platform for debugging and monitoring LLM applications
- LangGraph: Library for building stateful multi-actor applications

Happy coding! 🐍✨
