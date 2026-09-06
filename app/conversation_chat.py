import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_deepseek import ChatDeepSeek


load_dotenv()
api_key = os.getenv("Deep_Seek_API_KEY")

# Set up your API key
os.environ["DEEPSEEK_API_KEY"] = os.getenv("Deep_Seek_API_KEY")

# 1. Define the state schema
# add_messages ensures new messages are appended to the list rather than overwriting it
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 2. Initialize the graph builder
workflow = StateGraph(State)

# 3. Initialize the LLM
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# 4. Define the node function that calls the LLM
def call_model(state: State):
    response = llm.invoke(state["messages"])
    # Return the response wrapped in a message list
    return {"messages": [response]}

# 5. Add the node to the graph
workflow.add_node("agent", call_model)

# 6. Set entry and exit edges
workflow.add_edge(START, "agent")
workflow.add_edge("agent", END)

# 7. Compile the graph into an executable application
app = workflow.compile()

# 8. Run the agent
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
ai_msg.content
for step in app.stream(inputs, stream_mode="values"):
    step["messages"][-1].pretty_print()