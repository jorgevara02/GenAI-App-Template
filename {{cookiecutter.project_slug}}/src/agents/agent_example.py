from langchain.agents import create_agent

from src.agents import get_llm

agent = create_agent(
    model=get_llm(),
    tools=[],
    system_prompt="You are a helpful assistant.",
)


if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "How are you doing?"}]}
    )
    print(result["messages"][-1].content)
