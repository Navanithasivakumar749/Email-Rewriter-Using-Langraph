from langchain_core.prompts import PromptTemplate
import os

def get_llm():
    """
    Get LLM based on environment configuration.
    Supports both Claude API and free Ollama options.
    """
    use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"
    
    if use_ollama:
        # FREE Option: Use your local Ollama model
        from langchain_ollama import OllamaLLM
        model = os.getenv("OLLAMA_MODEL", "qwen3:0.6b")
        print(f"Using FREE Ollama model: {model}")
        return OllamaLLM(model=model)
    else:
        # PAID Option: Use Claude API for high-quality results
        from langchain_anthropic import ChatAnthropic
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("WARNING: ANTHROPIC_API_KEY not found! Falling back to Ollama...")
            from langchain_ollama import OllamaLLM
            return OllamaLLM(model="qwen3:0.6b")
        
        model = os.getenv("CLAUDE_MODEL", "claude-3-haiku-20240307")
        print(f"Using Claude API model: {model}")
        return ChatAnthropic(
            model=model,
            api_key=api_key,
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
