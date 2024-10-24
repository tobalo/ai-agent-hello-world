 // Start Generation Here
## Hello World AI Agent

This guide will help you set up a simple Hello World AI agent using Python.

We will be using the `phidata`[phidata.com] library to build the agent with ollama[ollama.ai] as the LLM provider.

### Setup

We've provided setup scripts for both Windows and macOS/Linux to make the installation process easier.

First install and run ollama locally at the following link: [ollama.com/download](https://ollama.com/download)

Now setup the python environment using the following scripts:
#### Windows

1. Open PowerShell and navigate to the project directory.
2. Run the setup script:
```powershell
.\setup.ps1
```

#### macOS/Linux

1. Open Terminal and navigate to the project directory.
2. Make the setup script executable:
```bash
chmod +x setup.sh
```
3. Run the setup script:
```bash
./setup.sh
```

### Manual Setup (if you prefer)

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
ollama run llama2
```

5. **Run the agent:**
```bash
source ./aienv/bin/activate
python3 agent.py
```

### Next Steps

After running the setup script or following the manual setup, your Hello World AI agent should be up and running. You can now start interacting with it or customize it further based on your needs.
