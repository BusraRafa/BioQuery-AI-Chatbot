#--------------------used gpt5 instead of o3-deep-reaesrch model---------------------
from typing import List, Dict
from anthropic import Anthropic
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv
import os
from anthropic._exceptions import AuthenticationError as ClaudeAuthError
from openai import AuthenticationError as OpenAIAuthError
import json
from xai_sdk import Client
from xai_sdk.chat import user, system
from datetime import timedelta
from mistralai import Mistral
import threading

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
openai_api_key = os.getenv("OPENAI_API_KEY")
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
xai_api_key = os.getenv("XAI_API_KEY")
mistral_api_key = os.getenv("MISTRAL_API_KEY")

genai_model = genai.GenerativeModel('gemini-2.0-flash')
claude_model = "claude-opus-4-20250514"
chatgpt_model = "o3-deep-research-2025-06-26"
#gptmodel
gpt5_model = "gpt-5-mini-2025-08-07"
deepseek_model = "deepseek-chat"
xai_model = "grok-4"
mistral_model = "mistral-large-latest"
deepseek_url = os.environ.get("DEEPSEEK_URL")

openai_client = OpenAI(api_key=openai_api_key)
deepseek_client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)


def generate_response(input_text: str, chat_history: List[Dict] = None) -> Dict:

    system_prompt = """
You are a smart, friendly AI research assistant with deep expertise in biomedical and healthcare topics.

**Conversation Context**:
- You are participating in an **ongoing chat**. The user’s previous messages (chat history) are available and should be considered to maintain **natural conversation flow**.
- Use the chat history to **understand the user's journey**, avoid repetition, and **respond contextually** as if you're in a continuous, flowing conversation.
- Learn from what the user has previously shared and **build on it** in your answers.

**Response Style**:
- Use a warm, clear, and professional tone.
- Be empathetic, insightful, and easy to understand.
- Structure responses with **headings**, **bold text**, bullet points, and markdown where helpful.
- When applicable, **cite sources, links, or references**. If unavailable, explicitly mention: *"Produced from my trained knowledge base."*
- If the user's input is short and general (e.g., "ok", "thanks", "got it"), respond **casually and naturally** without sounding formal or research-heavy. Just say something friendly like:
  - "You're very welcome!"
  - "Glad it helped!"
  - "No problem—here if you need me."

**Goals**:
- Be the most **helpful, structured, and pleasant** assistant among others.
- When answering real questions, break down complex topics and explain them clearly.
- Provide concise **summaries** at the end of in-depth replies.
- Include links or citations if relevant. If not available, say: *"Produced from my trained knowledge base."*

**Persona**:
You are confident, intelligent, kind, and helpful—like a trusted guide who's part of the user’s long-term research workflow.

**When including external sources or citations:**
- Format links using markdown: `[Title](https://example.com)`
- Include them inline or at the end of the relevant section

"""

    if chat_history is None:
        chat_history = []

    responses = {}
    threads = []
    
    def claude():
        try:
            claude_messages = []
            for chat in chat_history:
                if chat.get("user", "").strip():
                    claude_messages.append({"role": "user", "content": chat["user"]})
                if chat.get("claude", "").strip():
                    claude_messages.append({"role": "assistant", "content": chat["claude"]})
            claude_messages.append({"role": "user", "content": input_text})
            response_obj = anthropic_client.messages.create(
                model=claude_model,
                system=system_prompt,
                max_tokens=4096,
                messages=claude_messages
            )
            result = response_obj.content[0].text if response_obj and response_obj.content else "No response generated."
        
        except ClaudeAuthError:
            result = "Invalid Claude API key."
        
        except Exception as e:
            result = f"Claude error: {str(e)}"
        responses["claude"] = result
        

    # def chatgpt():
    #     try:
    #         inputs = [{"role": "system", "content": system_prompt}]
    #         for chat in chat_history:
    #             if chat.get("user", "").strip():
    #                 inputs.append({"role": "user", "content": [{"type": "input_text", "text": chat["user"]}]})
    #             if chat.get("chatgpt", "").strip():
    #                 inputs.append({"role": "assistant", "content": [{"type": "output_text", "text": chat["chatgpt"]}]})
    #         inputs.append({"role": "user", "content": [{"type": "input_text", "text": input_text}]})
            
    #         #openai_client = OpenAI(api_key=openai_api_key)
    #         #client = OpenAI(api_key=openai_api_key)
    #         response_obj = openai_client.responses.create(
    #             model=chatgpt_model,
    #             input=inputs,
    #             reasoning={"effort": "medium",
    #                        "summary": "auto"},
    #             tools=[{"type": "web_search_preview"}],
    #             max_output_tokens=20000,
    #             max_tool_calls=7
    #         )
    #         result = "No response generated."
    #         if response_obj:
    #             output = getattr(response_obj, "output", None)
    #             if output and isinstance(output, list):
    #                 for item in output:
    #                     if hasattr(item, "content") and isinstance(item.content, list):
    #                         for content_item in item.content:
    #                             if hasattr(content_item, "text"):
    #                                 result = content_item.text.strip()
    #                                 break
    #                         if result != "No response generated.":
    #                             break
        
    #     except OpenAIAuthError:
    #         result = "Invalid OpenAI API key."
        
    #     except Exception as e:
    #         result = f"ChatGPT error: {str(e)}"
    #     responses["chatgpt"] = result

    def gpt5():
        try:
            context = system_prompt + "\n"
            for chat in chat_history:
                if chat.get("user", "").strip():
                    context += f"User: {chat['user']}\n"
                if chat.get("gpt5", "").strip():
                    context += f"Assistant: {chat['gpt5']}\n"
            context += f"User: {input_text}\nAssistant:"
            
            openai_client = OpenAI(api_key=openai_api_key)
            result_obj = openai_client.responses.create(
                model=gpt5_model,
                input=context,
                reasoning={"effort": "high"}
            )
            result = result_obj.output_text.strip() if result_obj else "No response generated."
        
        except Exception as e:
            result = f"GPT-5 error: {str(e)}"
        responses["gpt5"] = result
    

    def gemini():
        try:
            context = system_prompt
            # context = ""
            for chat in chat_history:
                if chat.get("user", "").strip():
                    context += f"User: {chat['user']}\n"
                if chat.get("gemini", "").strip():
                    context += f"Assistant: {chat['gemini']}\n"
            context += f"User: {input_text}\nAssistant:"
            response_obj = genai_model.generate_content(context)
            result = response_obj.text.strip() if response_obj else "No response generated."
        
        except Exception as e:
            result = f"Gemini error: {str(e)}"
        responses["gemini"] = result


    def deepseek():
        try:
            messages = []

            messages.append({"role": "system", "content": system_prompt.strip()})

            for chat in chat_history:
                if chat.get("user", "").strip():
                    messages.append({"role": "user", "content": chat["user"]})
                if chat.get("deepseek", "").strip():
                    messages.append({"role": "assistant", "content": chat["deepseek"]})
            messages.append({"role": "user", "content": input_text})
            
            #deepseek_client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)
            #client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)
            
            response_obj = deepseek_client.chat.completions.create(
                model=deepseek_model,
                messages=messages,
                stream=False
            )
            result = response_obj.choices[0].message.content if response_obj.choices else "No response generated."
        
        except OpenAIAuthError:
            result = "Invalid DeepSeek API key."
        
        except Exception as e:
            result = f"DeepSeek error: {str(e)}"
        responses["deepseek"] = result


    def xai():
        try:
            client = Client(api_key=xai_api_key)
            chat = client.chat.create(model=xai_model, messages=[system(system_prompt.strip())])
            chat.append(user(input_text))
            response = chat.defer(timeout=timedelta(minutes=10), interval=timedelta(seconds=10))
            result = response.content if response else "No response generated."
        
        except Exception as e:
            result = f"XAI error: {str(e)}"
        responses["xai"] = result


    def mistral():
        try:
            mistral_client = Mistral(api_key=mistral_api_key)
            result = ""
            stream_response = mistral_client.chat.stream(
                model=mistral_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": input_text}
                    ]
            )
            for chunk in stream_response:
                result += chunk.data.choices[0].delta.content
            if not result:
                result = "No response generated."
        
        except Exception as e:
            result = f"Mistral error: {str(e)}"
        responses["mistral"] = result


    
    thread_funcs = [ claude,gpt5,gemini,deepseek,xai,mistral] #,chatgpt
    for func in thread_funcs:
        thread = threading.Thread(target=func,daemon=True) #, daemon=True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return responses


if __name__ == "__main__":
    input_text = "What is the expression profile of PD-L1 across different cancer types in short?"
    #"What are novel druggable targets identified in non-small cell lung cancer (NSCLC)?"
    
    
    chat_history = [
        {
            "user": "Hello how are you?",    
            "claude": "I'm doing great, thanks for asking!",
            "chatgpt": "I'm doing well, thank you for asking!",
            "gemini": "I'm fine, thank you!",
            "deepseek": "I'm doing well, thanks for asking!",
            "xai": "I'm doing great, thanks for asking!",
            "mistral": "I'm doing well, thank you for asking!"
        },
    ]
    result = generate_response(input_text, chat_history)
    json_output = json.dumps(result, indent=2, ensure_ascii=False)
    print(json_output)
