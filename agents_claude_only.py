from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
import os

# Load Claude model for high-quality email rewriting
# Get your API key from: https://console.anthropic.com/
llm = ChatAnthropic(
    model="claude-3-haiku-20240307",  # Fast and cost-effective
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    max_tokens=1000,
    temperature=0.3
)


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

