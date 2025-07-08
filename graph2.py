from typing import TypedDict, List
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    values : List[int]
    name : str
    results: str



def process_values(state: AgentState)->AgentState:
    """This functions will process multiple values and return the results"""

    state["results"] = "The sum of the values is " + str(sum(state["values"])) + " and the name is " + state["name"]
    return state


graph = StateGraph(AgentState)

graph.add_node("node1" , process_values);
graph.set_entry_point("node1")
graph.set_finish_point("node1")
app = graph.compile()

result = app.invoke({"values" : [1,2,3] , "name" : "Uday" , "results" : ""})
print(result["results"])    


