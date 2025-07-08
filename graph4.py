from functools import lru_cache
from typing import Literal, TypedDict
from langgraph.graph import StateGraph, START,END


class AgentState(TypedDict):
    number1: int
    number2: int
    operation: str
    finalNumber: int


def adder(state: AgentState)->AgentState:
    state["finalNumber"] = state["number1"]+state["number2"]
    return state

def multiplier(state: AgentState)->AgentState:
    state["finalNumber"] = state["number1"]*state["number2"]
    return state

def router(state: AgentState):
    
    if state["operation"] == "+":
        return "addition_operation"
    else:
        return "multiply_operation"


graph = StateGraph(AgentState)

graph.add_node("addition_node" , adder)
graph.add_node("multiplication_node" , multiplier)
graph.add_node("router" , lambda state:state)
graph.add_edge(START , "router")

graph.add_conditional_edges(
    #src 
    "router",
    router,
    {
        #edge and node
        "addition_operation":"addition_node",
        "multiply_operation":"multiplication_node"

    }

)

graph.add_edge("addition_node" , END)
graph.add_edge("multiplication_node" , END)

app = graph.compile()

result = app.invoke({"number1" : 10 , "number2" : 10 , "operation":"*" , "finalNumber": 0})

print(result["finalNumber"])








    


