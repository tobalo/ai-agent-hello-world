from phi.agent import Agent
from phi.model.ollama import Ollama

llm = Ollama(id="llama3")

hello_world_agent = Agent(
    model=llm,
    description="Hello World Agent, give me a brief introduction to GenAI and Traditional AI for beginners and enthusiasts",
)

hello_world_agent.print_response("Educate the user about the world of GenAI and Traditional AI", stream=True)
