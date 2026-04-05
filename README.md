# BioQuery‑AI‑Chatbot 🤖

BioQuery‑AI‑Chatbot is a custom AI-powered web platform designed for biomedical research. It allows researchers to input biomedical queries (e.g., **target discovery**, **protein expression**) and receive comprehensive responses from **multiple AI engines**. These engines include ChatGPT, Claude, Gemini, Mistral, XAI, and DeepSeek, which work in parallel to provide diverse insights and responses. The system displays side-by-side answers from all engines and provides citations where available.

## 🚀 Key Features

- **Multi‑Model Integration**: The chatbot uses six different AI models (ChatGPT, Claude, Gemini, Mistral, XAI, and DeepSeek) to generate diverse responses for biomedical queries.
- **Parallel Processing**: All models run simultaneously, and their answers are aggregated and displayed side by side.
- **Comprehensive Responses**: Each AI engine brings its unique strengths to the table, providing a rich and multi-faceted view of biomedical questions.
- **Citations and References**: When applicable, the system provides citations to sources for the answers or mentions that they were generated from the AI’s trained knowledge base.
- **Modular and Extensible**: You can easily integrate additional models or tweak the existing configurations as required for your research.
- **Test Suite Included**: Basic tests (`test.py`, `test_main_function.py`) to verify core functionality.  



## 🛠️ Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

1. **Python 3.8+**: Ensure you have Python 3.8 or a newer version installed.
2. **API Keys**: You need API keys for the various models integrated (e.g., OpenAI, Gemini, Claude, DeepSeek, XAI, and Mistral).
3. **(Optional) Virtual Environment**: Use `venv` or any other virtual environment tool to manage dependencies.

### Installation & Setup

```bash
# 1. Clone the repository
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

# 4. Set up your .env file for API keys
# Create a .env file in the root directory and add the following (replace with your actual keys):
GEMINI_API_KEY=your_gemini_api_key 
CLAUDE_API_KEY=your_claude_api_key 
OPENAI_API_KEY=your_openai_api_key 
DEEPSEEK_API_KEY=your_deepseek_api_key 
XAI_API_KEY=your_xai_api_key 
MISTRAL_API_KEY=your_mistral_api_key 
```




