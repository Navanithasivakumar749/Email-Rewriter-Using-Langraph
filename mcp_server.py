#!/usr/bin/env python3

"""MCP Email Rewriter Server using FastMCP"""

import sys
import os
from mcp.server.fastmcp import FastMCP

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Create an MCP server
mcp = FastMCP("Email Rewriter")

# Initialize graph as None, will be loaded when needed
graph = None

def get_graph():
    """Lazy load the graph to avoid startup issues"""
    global graph
    if graph is None:
        try:
            from langgraph_graph import build_graph
            graph = build_graph()
            print("Successfully loaded LangGraph")
        except Exception as e:
            print(f"Warning: Could not load LangGraph: {e}")
            # Create a simple fallback implementation
            class SimpleGraph:
                def invoke(self, state):
                    email = state.get('raw_email', '')
                    # Simple email polishing logic
                    polished = email.replace('Hi,', 'Dear Sir/Madam,')
                    polished = polished.replace('Thanks!', 'Best regards,')
                    polished = polished.replace('ASAP', 'as soon as possible')
                    polished = polished.replace('kinda', 'somewhat')
                    return {"polished_email": f"Subject: Professional Communication\n\n{polished}\n\nThank you for your time."}
            graph = SimpleGraph()
    return graph

@mcp.tool()
def rewrite_email(email: str) -> str:
    """
    Rewrite and polish an email using AI to improve clarity, tone, and professionalism.
    
    Args:
        email: The raw email content to be rewritten and polished
        
    Returns:
        The polished and improved email content
    """
    if not email.strip():
        return "Error: Missing email input. Please provide an email to rewrite."
    
    try:
        # Use the LangGraph to process the email
        current_graph = get_graph()
        state = {"raw_email": email.strip()}
        result = current_graph.invoke(state)
        
        polished_email = result.get("polished_email", "Failed to generate polished email")
        
        return f"Polished Email:\n\n{polished_email}"
        
    except Exception as e:
        return f"Error processing email: {str(e)}"

if __name__ == "__main__":
    print("Starting FastMCP Email Rewriter Server...")
    mcp.run()
