from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv





load_dotenv(override=True)

ollama_url="http://localhost:11434/v1"
ollama = OpenAI(api_key="ollama", base_url=ollama_url)

MODEL="llama3.2"

system_message=""" You are master of teaching, encouraging Python tutor for beginners.
Your teaching style:
- Explain concepts simply, with short examples
- When the user asks a question, give a hint first before the full answer (unless they say "just tell me" or "show me the answer")
- Use code blocks with ```python for all code examples
- After explaining, suggest a small practice exercise they can try
- If they paste code with errors, help them debug step by step — don't just fix it silently
- Keep responses focused; avoid overwhelming walls of text
You are running locally via Ollama. The student is learning Python from scratch."""




def chat(message, history):
    history = [{"role": h["role"], "content": h["content"]} for h in history]

    relevant_system_message = system_message

    if "beginner" in message.lower() or "start" in message.lower():
        relevant_system_message += "\nAssume zero prior programming experience."
    if "error" in message.lower() or "traceback" in message.lower():
         relevant_system_message += "\nThe user is debugging. Walk through the error line by line."
    elif "exercise" in message.lower():
        relevant_system_message +="\nGive them a coding challenge appropriate to what you've discussed so far."

    messages = (
        [{"role":"system", "content" : relevant_system_message}]
        + history
        + [{"role":"user","content":message}]

    )

    stream = ollama.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
    )

    response = ""
    for chunk in stream : 
        response += chunk.choices[0].delta.content or ""
        yield response

if __name__ == "__main__":
    gr.ChatInterface(
        fn=chat,
        type="messages",
        title="🐍 Python Tutor (Ollama)",
        description="Ask anything about Python — concepts, syntax, debugging, exercises.",
        examples=[
        "What is a variable in Python?",
        "Explain lists vs tuples with examples",
        "Why am I getting IndexError?",
        "Give me a beginner exercise on loops",
        ],
        
    ).launch()