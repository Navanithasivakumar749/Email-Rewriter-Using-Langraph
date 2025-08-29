from typing import TypedDict
from langgraph.graph import StateGraph, END
from tool_abbr_expand import expand_abbreviations
from agents import llm, email_prompt

# 👇 STEP 1: Define the expected structure of the state
class EmailState(TypedDict):
    raw_email: str
    expanded_email: str
    polished_email: str

# 👇 STEP 2: Node to expand abbreviations
def abbreviation_node(state: EmailState) -> EmailState:
    state['expanded_email'] = expand_abbreviations(state['raw_email'])
    return state

# 👇 STEP 3: Node to polish the email using the LLM
def polishing_node(state: EmailState) -> EmailState:
    prompt = email_prompt.format(expanded_email=state['expanded_email'])
    response = llm.invoke(prompt)
    # Claude returns an AIMessage object, extract the content
    if hasattr(response, 'content'):
        state['polished_email'] = response.content
    else:
        state['polished_email'] = str(response)
    return state

# 👇 STEP 4: Build the LangGraph
def build_graph():
    graph = StateGraph(EmailState)  # ✅ This is the line that fixes your error
    graph.add_node("expand_abbr", abbreviation_node)
    graph.add_node("polish_email", polishing_node)

    graph.set_entry_point("expand_abbr")
    graph.add_edge("expand_abbr", "polish_email")
    graph.add_edge("polish_email", END)

    return graph.compile()
