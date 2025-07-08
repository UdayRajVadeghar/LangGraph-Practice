from typing import List,TypedDict
from langgraph.graph import StateGraph



class AgentState(TypedDict):
    name: str
    age: str
    final: str


def first_node(state: AgentState)->AgentState:
    state["final"] = f'This is {state["name"]}'
    return state; 

def second_node(state: AgentState)->AgentState:
    state["final"] = f'{state["final"]} and i am {state["age"]} years old'
    return state


graph = StateGraph(AgentState)
graph.add_node("firstNode" , first_node)
graph.set_entry_point("firstNode")
graph.add_node("secondNode",second_node)
graph.add_edge("firstNode", "secondNode")
graph.set_finish_point("secondNode")
app = graph.compile()

result = app.invoke({"name" : "uday" , "age" : "21" , "final" : ""})

print(result["final"])


