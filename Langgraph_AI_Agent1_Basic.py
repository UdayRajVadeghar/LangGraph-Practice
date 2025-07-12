from typing import TypedDict, List
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: List[HumanMessage]


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(response.content)
    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

user_input = input("Enter your message: ")
while user_input.lower() != "exit": 
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter your message: ")

print("Exiting...")