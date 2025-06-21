# 🤖 Multi-Agent Tutor Bot

The **Multi-Agent Tutor Bot** is an intelligent, multi-agent web-based chatbot that can answer academic and general queries using modular AI agents. Built with Google's Generative AI API (Gemini), it offers a clean UI and smart delegation to specialized sub-agents.

---

## 📂 Project Structure

```text
multi-agent-tutor-bot/
├── .env                      # API key and environment configs
├── .gitignore                # Files/folders to ignore by git
├── main.py                   # FastAPI app with / and /ask routes
├── Readme.md                 # Project documentation
├── requirements.txt          # Python dependencies
│
├── templates/
│   └── index.html            # Tailwind-powered user interface
│
├── tutor_agent/
│   ├── __init__.py
│   ├── agent.py              # Main tutor agent
│   ├── sub_agents/
│   │   ├── math_agent/
│   │   │   ├── __init__.py
│   │   │   ├── agent.py      # Handles math queries
│   │   │   └── tools.py      # Helper functions for math
│   │   └── physics_agent/
│   │       ├── __init__.py
│   │       ├── agent.py      # Handles physics queries
│   │       └── tools.py      # Helper functions for physics
│   └── __pycache__/          # Python cache files (auto-generated)
│
├── __pycache__/              # Root-level cache (auto-generated)

```


---

## 🚀 Features

✅ Multi-agent system  
✅ Math and general agents  
✅ Modular design for adding new agents  
✅ Google Gemini API integration  

---

## 🧠 How It Works

1. The user submits a question through the web interface.
2. `main.py` receives it and sends it to the `tutor_agent`.
3. The `tutor_agent` uses intelligent routing logic to delegate the task to:
   - `math_agent` for arithmetic and math questions
   - `physics_agent` for physics-related questions
4. The selected sub-agent generates a response via the Google Gemini model.
5. The answer is returned and displayed to the user.

---

## 💡 Example Questions to Try

- `2 + 2`
- `Who is the president of India?`
- `Explain polymorphism in OOP.`
- `What is the capital of France?`

---

## ⚙️ Local Setup

### 1. Clone the Repo

```bash
git clone https://github.com/KaranOps/multi-agent-tutor-bot.git
cd multi-agent-tutor-bot
```
### 2. Set Up Virtual Environment
```bash
python -m venv venv

# Activate (each new terminal)
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
# Windows PowerShell:
.venv\Scripts\Activate.ps1
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Create .env File
```bash
GOOGLE_API_KEY=your_google_api_key_here
```
### 4. Run the App
```bash
adk web
```

## 🙋 About Me

Hi! I’m **Karan** 👋 — a full-stack developer passionate about **AI**, **creativity tools**, and building solutions that solve real-world problems.

Let’s connect on [LinkedIn](https://www.linkedin.com/in/karanops93) or check out more of my work on [GitHub](https://github.com/KaranOps).

---

Made with ❤️

