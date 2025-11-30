# BioQuery‑AI‑Chatbot 🤖

BioQuery‑AI‑Chatbot is a Python‑based AI chatbot framework that leverages *multiple models* together to answer user queries intelligently. Rather than parsing PDFs, the system integrates several LLMs and models to produce responses — making it a flexible “multi‑model chatbot engine”.

## 🚀 Why BioQuery‑AI‑Chatbot

- Combines strengths of different models to improve answer quality, robustness, and versatility.  
- Provides a unified interface: you send a query, and the system runs multiple back‑end models and aggregates or selects the best response.  
- Modular and extensible: you can plug in additional models or adjust the existing ones for your use case.  
- Easy to set up and run locally (with support for environment variables for sensitive keys like API tokens).

## Features

- **Multi‑Model Integration**: Supports several LLMs (as configured in the code) — not just one fixed backend.  
- **Unified Chat Interface**: Seamlessly interacts with models and returns responses.  
- **Configurable via `.env`**: Keeps sensitive credentials (e.g. API keys) out of the code.  
- **Simple Setup & Lightweight**: Pure Python dependencies, minimal overhead, ideal for experimentation.  
- **Test Suite Included**: Basic tests (`test.py`, `test_main_function.py`) to verify core functionality.  

## 📦 Repository Structure
BioQuery‑AI‑Chatbot/
├── .gitignore
├── README.md
├── requirements.txt
├── test.py
├── test_main_function.py
└── (other source files and modules)


- **`requirements.txt`** — Python dependencies required to run the chatbot.  
- **Test files** — ensure that main functions run correctly and provide a base for future unit tests.  
- **Source files** — where models are integrated, and chatbot logic implemented.  

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or newer  
- (Recommended) A virtual environment tool (`venv`, `virtualenv`, etc.)  
- API key(s) or credentials for the model back‑ends (if applicable)  

### Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/BusraRafa/BioQuery‑AI‑Chatbot.git
cd BioQuery‑AI‑Chatbot

# 2. (Optional but recommended) Create a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your credentials 
#    Create a .env file in the root directory:
echo OPENAI_API_KEY=your_openai_key_here > .env
#    (and any other required environment vars for other models)
```
```bash
python app.py   # or whichever script is the main entry point

```




