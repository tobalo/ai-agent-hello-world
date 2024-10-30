## Hello World AI Agent

This guide will help you set up a simple Hello World AI agent using Python.

We will be using the [phidata](https://phidata.com) library to build the agent with [ollama](https://ollama.com) as the LLM provider.

### Setup

We've provided setup scripts for both Windows and macOS/Linux to make the installation process easier.

First install and run ollama locally at the following link: [ollama.com/download](https://ollama.com/download)

### Manual Setup

If you'd rather set up the environment manually, follow these steps:

1. **Create a virtual environment:**
```bash
python3 -m venv ./aienv
```

2. **Activate the virtual environment:**
- On Windows:
```bash
.\aienv\Scripts\activate
```
- On macOS/Linux:
```bash
source ./aienv/bin/activate
```

3. **Install dependencies:**
```bash
pip3 install -r requirements.txt
```

4. **Run ollama locally:**
```bash
ollama run llama3
```

5. **Run the agent:**
```bash
source ./aienv/bin/activate
python3 agent.py
```

### Next Steps

After running the setup script or following the manual setup, your Hello World AI agent should be up and running. You can now start interacting with it or customize it further based on your needs.
