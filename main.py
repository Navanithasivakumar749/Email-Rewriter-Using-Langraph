from langgraph_graph import build_graph

def run_email_polisher(raw_email: str):
    graph = build_graph()
    state = {"raw_email": raw_email}
    final_state = graph.invoke(state)
    print("\nPolished Email:\n")
    print(final_state["polished_email"])

if __name__ == "__main__":
    print("Enter your raw email text (press Enter twice to submit):\n")
    
    # Read multiline input
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    email_text = "\n".join(lines)

    if not email_text.strip():
        print("⚠️ No input provided. Exiting.")
    else:
        run_email_polisher(email_text)
