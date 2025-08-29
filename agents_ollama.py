from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import os

# 100% FREE Option: Ollama (runs locally, no API keys needed)
# Install: https://ollama.ai/download
# Then run: ollama pull qwen2:0.5b (or any other model)

def get_llm():
    """Get LLM based on environment configuration"""
    if os.getenv("USE_OLLAMA", "false").lower() == "true":
        # Completely free local option
        model = os.getenv("OLLAMA_MODEL", "qwen2:0.5b")
        return OllamaLLM(model=model)
    else:
        # OpenAI free tier (requires API key but has $5 free credits)
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY"),
            max_tokens=1000,
            temperature=0.3
        )

# Load the appropriate LLM
llm = get_llm()

email_prompt = PromptTemplate.from_template("""
You are an email polishing assistant. Your job is to take a raw email with expanded abbreviations and turn it into a clean, professional format.

Input email:
{expanded_email}

Format:
Subject: ...
Body:
Hi Team,

...

Best regards,
""")
