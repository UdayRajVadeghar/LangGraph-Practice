from typing import TypedDict
from langchain_core.runnables.utils import Output
from langgraph.graph import StateGraph,START,END


class AgentState(TypedDict):
    initialNum1 : int
    initialNum2 : int
    initialOperation: str
    output1 : int
    laterNum : int
    laterOperation : str
    output2 : int
    

def first_addition_node(state:AgentState)->AgentState:
    
    state["output1"] = state["initialNum1"] + state["initialNum2"]
    return state


def first_multiplication_node(state:AgentState)->AgentState:
    
    state["output1"] = state["initialNum1"] * state["initialNum2"]
    return state


def second_addition_node(state:AgentState)->AgentState:

    state["output2"] =  state["output1"] + state["laterNum"]
    return state

def second_multipication_node(state:AgentState)->AgentState:

    state["output2"] = state["output1"] * state["laterNum"]
    return state

def router1(state : AgentState):
    
    if state["initialOperation"] == "+":
        return "initial_addition_node"
    else:
        return "initial_multiplication_node"

def router2(state: AgentState):

    if state["laterOperation"] == "+":
        return "later_addition_node"
    else:
        return "later_multiplication_node"


graph = StateGraph(AgentState)

graph.add_node("firstAdder" , first_addition_node)
graph.add_node("firstMultiplicator" , first_multiplication_node)
graph.add_node("secondAdder" , second_addition_node)
graph.add_node("secondMultiplicator" , second_multipication_node)
graph.add_node("router1" , lambda state:state)
graph.add_node("router2" , lambda state:state)

graph.add_edge(START , "router1")
graph.add_conditional_edges(
    "router1",
    router1,
    {
        "initial_addition_node" : "firstAdder",
        "initial_multiplication_node" : "firstMultiplicator"

    }
    
)

graph.add_edge("firstAdder" , "router2")
graph.add_edge("firstMultiplicator" , "router2")

graph.add_conditional_edges(
    "router2",
    router2,
    {
        "later_addition_node" : "secondAdder",
        "later_multiplication_node" : "secondMultiplicator"
    }
)

graph.add_edge("secondAdder" , END)
graph.add_edge("secondMultiplicator" , END)

app = graph.compile()

result = app.invoke({"initialNum1":10 , "initialNum2" : 10 , "initialOperation": "+" , "laterNum" : 10 , "laterOperation": "+" , "output1":0 ,"output2": 0 })

print(result["output2"])




