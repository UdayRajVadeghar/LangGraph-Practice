from itertools import product
from typing_extensions import Literal
from langgraph.graph import StateGraph
from typing import TypedDict, List


class AgentState(TypedDict):
    list: List[int]
    name: str
    operation: Literal["*" , "+"]
    result: str


def processNode(state: AgentState)->AgentState:
    """This function will process the list and return the results"""
    if(state["operation"] == "+"):
        state["result"] = "Hello my name is " + state["name"]+ " " + "the sum of the numbers is" + str(sum(state["list"]))
    else:
        state["result"] = "Hello my name is " + state["name"]+ " " + "the product of the numbers is" + str(product(state["list"]))  

    return state    
    


graph = StateGraph(AgentState)

graph.add_node("processNode" , processNode)
graph.set_entry_point("processNode")
graph.set_finish_point("processNode")
app = graph.compile()

result = (app.invoke({"list":[1,2,3,4] , "name": "uday" , "operation": "+" , "result":""}))

print(result["result"])
