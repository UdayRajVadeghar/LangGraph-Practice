
from typing import TypedDict
from langgraph.graph import StateGraph , END , START

class AgentState(TypedDict):
    name:str
    count:int
    Output: str


def initial_node(state:AgentState)->AgentState:
    state["name"] = "Uday"
    state["count"] = 0
    state["Output"] = ""
    
    return state


def countNode(state:AgentState) -> AgentState:
    state["count"] += 1
    state["Output"] = state["Output"] + "You are Goated"
    return state

def should_continue(state:AgentState):
    if state["count"] < 5:
        return "Repeat"
    else:
        return "Exit"

graph = StateGraph(AgentState)
graph.add_node("firstNode" , initial_node)
graph.add_node("repeatNode" , countNode)

graph.add_edge("firstNode", "repeatNode")

graph.add_conditional_edges(
    "repeatNode",
    should_continue,
    {
        "Exit":END,
        "Repeat":"repeatNode"
    }
)

graph.set_entry_point("firstNode")

app = graph.compile()

result = app.invoke({"name": "uday", "count": 1, "Output": ""})

print(result["Output"])