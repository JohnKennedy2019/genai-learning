# GenAI 01 - Gemini CLI Chatbot

## Project Overview

This project is a command-line chatbot built using Google's Gemini API.

The application accepts user questions, sends them to Gemini, displays the response, maintains chat history, saves conversations to a file, and records application logs.

This project is part of a GenAI learning roadmap focused on building practical AI applications using Python and Gemini.

---

## Features

- Gemini API Integration
- Secure API Key Management
- Interactive Command-Line Chatbot
- Chat History Tracking
- Chat History File Export
- Application Logging
- Response Time Measurement
- Input Validation
- Modular Python Design

---

## Technology Stack

- Python 3.11+
- Google Gemini API
- google-genai SDK
- python-dotenv

---

## Project Structure

```text
genai-01-gemini-chatbot/

├── genai_env/
│
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── chatbot.py
│   ├── chat_history.py
│   ├── file_manager.py
│   └── logger.py
│
├── logs/
│   └── application.log
│
├── prompts/
│   └── system_prompt.txt
│
└── chat_history.txt
```

---

## Prerequisites

Ensure the following software is installed:

- Python 3.11 or later
- Git
- VS Code (Recommended)

Verify Python:

```bash
python --version
```

Example:

```bash
Python 3.11.9
```

---

## Create Virtual Environment

Navigate to the project folder:

```bash
cd genai-01-gemini-chatbot
```

Create a virtual environment:

```bash
python -m venv genai_env
```

---

## Activate Virtual Environment

### Windows

```bash
genai_env\Scripts\activate
```

### Linux / macOS

```bash
source genai_env/bin/activate
```

After activation you should see:

```bash
(genai_env)
```

at the beginning of the terminal.

---

## Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Gemini API Key Setup

Generate a Gemini API key from:

https://aistudio.google.com/

Create a file named:

```text
.env
```

Add the following:

```env
GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_API_KEY
```

Example:

```env
GEMINI_API_KEY=AIzaSyXXXXXX
```

---

## Environment Variables

The project uses environment variables for security.

### Local File

```text
.env
```

### GitHub Safe Template

```text
.env.example
```

Example:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## Run Application

Start the chatbot:

```bash
python main.py
```

---

## Available Commands

### Ask Questions

```text
You: What is Generative AI?
```

---

### View Chat History

```text
You: history
```

Shows all questions and responses from the current session.

---

### Exit Application

```text
You: exit
```

Stops the application.

---

## Example Execution

```text
============================================================
GENAI 01 - GEMINI CHATBOT
============================================================

Commands:
history -> Show Chat History
exit -> Exit Application

You: What is RAG?

Question Number: 1

Gemini:
RAG stands for Retrieval Augmented Generation.

Response Time: 1.24 sec
```

---

## Generated Files

### Chat History

```text
chat_history.txt
```

Stores all conversations.

Example:

```text
USER: What is RAG?

GEMINI: RAG stands for Retrieval Augmented Generation.
```

---

### Application Logs

```text
logs/application.log
```

Stores application events.

Example:

```text
INFO - Question: What is RAG?
INFO - Answer: RAG stands for Retrieval Augmented Generation.
```

---

## Security Best Practices

### Never Commit

```text
.env
```

Contains API secrets.

---

### Commit

```text
.env.example
```

Contains sample configuration without secrets.

---

## Learning Outcomes

After completing this project you should understand:

- What an LLM API is
- How to call Gemini using Python
- How environment variables work
- Why API keys should be protected
- How request/response flow works
- Basic logging
- Basic file handling
- Modular Python project structure

---

## Future Enhancements

Potential improvements:

- Conversation Memory
- Streaming Responses
- Function Calling
- Tool Calling
- FastAPI Integration
- Web UI
- RAG Integration
- Vector Database Integration

---

## Author

Created as part of a hands-on Generative AI learning journey focused on building production-oriented AI applications using Gemini, Python, FastAPI, LangChain, RAG, and Agentic AI.