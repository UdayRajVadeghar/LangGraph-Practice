from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display


class AgentState(TypedDict): # our state schema
    message : str
    mood : str


def greeting_node(state : AgentState):

    """Simple node that adds a greeting message to the state """
    state["message"] = "Hey " + state["message"] + ", How is it going?"
    state["mood"] = "I am " + state["mood"] + " today"
    return state


graph = StateGraph(AgentState)

graph.add_node("greeter" , greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")
app = graph.compile()

# display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"message" : "Uday" , "mood" : "happy"})
print(result["message"])
print(result["mood"])







