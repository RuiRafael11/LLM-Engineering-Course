🐍 Python Tutor Chatbot (Ollama + Gradio)

A local AI-powered Python tutor that runs entirely on your machine using Ollama and a Gradio chat interface.



✨ Features



Explains Python concepts in simple terms with code examples

Gives hints before full answers (Socratic teaching style)

Helps debug errors step by step

Suggests practice exercises after each explanation

Adapts context dynamically (beginner mode, debug mode, exercise mode)

Runs 100% locally — no API key or internet connection required





🛠️ Prerequisites



Python 3.10+

Ollama installed and running

The llama3.2 model pulled locally





⚙️ Setup

1\. Install Ollama

Download and install from https://ollama.com/download.

Then pull the model:

bashollama pull llama3.2

Make sure Ollama is running (it starts automatically on most systems, or run ollama serve).

2\. Clone the repository

bashgit clone https://github.com/RuiRafael11/YOUR-REPO-NAME.git

cd YOUR-REPO-NAME

3\. Create a virtual environment and install dependencies

bashpython -m venv venv



\# Windows

venv\\Scripts\\activate



\# macOS/Linux

source venv/bin/activate



pip install openai gradio python-dotenv

4\. Run the chatbot

bashpython chatbotOllama.py

Gradio will open a local URL (usually http://127.0.0.1:7860) in your browser.



🗂️ Project Structure

.

├── chatbotOllama.py   # Main application

├── .env               # Optional environment variables (not committed)

└── README.md



💬 Example Prompts

PromptWhat it triggersWhat is a variable in Python?Basic concept explanation with hintExplain lists vs tuples with examplesComparison with code blocksWhy am I getting IndexError?Step-by-step debug modeGive me a beginner exercise on loopsPractice challenge



⚙️ Configuration

You can change the model in chatbotOllama.py:

pythonMODEL = "llama3.2"  # Replace with any model you have pulled in Ollama

Other compatible models: llama3.1, mistral, deepseek-coder, phi3, etc.

To check which models you have available locally:

bashollama list



📝 Notes



The chatbot uses the OpenAI-compatible API that Ollama exposes on http://localhost:11434/v1

No data leaves your machine

The .env file is loaded but not strictly required for local Ollama usage

