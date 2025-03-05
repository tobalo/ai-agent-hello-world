# Hello World AI Agent

Build your first AI agent using Python! This project demonstrates how to create a simple conversational AI agent using modern tools and frameworks.

## Overview
```mermaid
flowchart TB
    subgraph User["User Interaction Layer"]
        UI[User Input]
        OR[Output Response]
    end

    subgraph Agent["AI Agent Core"]
        LLM["Language Model
        (Understanding & Generation)"]
        CT[(Context Storage
        - Memory & History
        - Instructions
        - Knowledge)]
        TM{"Tool Manager
        - Tool Selection
        - Task Routing"}
    end

    subgraph Tools["Available Tools"]
        MT[("Storage Systems
        - Databases
        - Files")]
        CT1{{Computation Tools
        - Math & Analysis}}
        ET>External Tools
        - Web & APIs]
        OB(((Observability)))
    end

    UI --> LLM
    LLM <--> CT
    LLM <--> TM
    TM <--> MT
    TM <--> CT1
    TM <--> ET
    TM <--> OB
    LLM --> OR

    classDef primary fill:#e1f5fe,stroke:#01579b,color:black
    classDef secondary fill:#f3e5f5,stroke:#4a148c,color:black
    classDef tertiary fill:#e8f5e9,stroke:#1b5e20,color:black
    
    class UI,OR primary
    class LLM,CT,TM secondary
    class MT,CT1,ET,OB tertiary
```
This project uses:
- [Agno](https://Agno.com) - A powerful framework for building AI agents
- [ollama](https://ollama.com) - Local LLM provider for AI capabilities

## Prerequisites

Before you begin, ensure you have the following installed:
- [git](https://git-scm.com/)
- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://astral.sh/uv) - Modern Python package installer and environment manager
- [ollama](https://ollama.com/download) - Local LLM provider
- Your favorite text editor (Vim, VSCode, Notepad++, Windsurf, Cursor, etc)

Then run:   
```bash
git clone https://github.com/tobalo/ai-agent-hello-world.git
cd ai-agent-hello-world # navigate into the cloned repository
```

## Installation

### Quick Setup
1. Download and install Ollama from [ollama.com/download](https://ollama.com/download)
2. Install uv:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Project Setup

1. Create a virtual environment:
```bash
uv venv
```

2. Activate the virtual environment:
```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install agno ollama
```

4. Start Ollama:
```bash
ollama run llama3.2:1b
```

5. Launch the agent:
```bash
python3 agent.py
```

6. Launch the web search agent:
```bash
python3 websearch-agent.py
```

## Next Steps

Now that your AI agent is running, you can:
- Customize its behavior and responses
- Add new capabilities using [Agno's toolkits](https://docs.Agno.com/tools/toolkits)
- Experiment with different LLM models available through Ollama

## Resources

- [Agno Documentation](https://docs.Agno.com)
- [Ollama Blog](https://ollama.com/blog)
- [Project Issues](https://github.com/yourusername/ai-agent-hello-world/issues)

