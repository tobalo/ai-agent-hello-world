from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
web_search_agent = Agent(
    model=Ollama(id="llama3.2:1b"),
    description="Web Search Agent demonstrating how to use DuckDuckGo search tool",
    tools=[DuckDuckGoTools()],
)
web_search_agent.print_response("When does March Madness Start?", stream=True)
