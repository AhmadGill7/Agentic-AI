# AGI Day 1 - OpenAI Responses API CLI

A command-line interface (CLI) tool for interacting with OpenAI's Responses API. This project provides a conversational AI experience with built-in memory, allowing you to have continuous conversations across multiple CLI sessions.

## ✨ Features

- 💬 **Interactive CLI**: Chat with OpenAI models directly from the command line
- 🧠 **Conversation Memory**: Maintains context across multiple CLI runs using OpenAI's Responses API
- 🔍 **Web Search Integration**: Optional web search capabilities for real-time information
- 🎯 **Multiple Models**: Support for different OpenAI models (default: gpt-4o-mini)
- 🔒 **Secure**: API keys stored in environment variables (never hardcoded)

## 📋 Prerequisites

- **Python 3.12+** (required)
- **UV** package manager ([Install UV](https://github.com/astral-sh/uv))
- **OpenAI API Key** ([Get your API key](https://platform.openai.com/api-keys))

## 🚀 Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/AhmadGill7/Agentic-AI.git
cd Agentic-AI/"Day 1 - UV"/AGI-Day-1/
```

Or simply navigate to the project directory if you already have it.

### 2. Install Dependencies

This project uses [UV](https://github.com/astral-sh/uv) for fast Python package management. Install dependencies with:

```bash
uv sync
```

This will:
- Create a virtual environment (`.venv/`)
- Install all required dependencies
- Set up the project for development

### 3. Set Up Your API Key

Create a `.env` file in the `AGI-Day-1/` directory:

```bash
# On Windows (PowerShell)
echo "OPENAI_API_KEY=your-api-key-here" > .env

# On Windows (Git Bash)
echo "OPENAI_API_KEY=your-api-key-here" > .env

# On Linux/Mac
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

**Important:** Replace `your-api-key-here` with your actual OpenAI API key.

You can get your API key from: https://platform.openai.com/api-keys

## 📖 Usage

### Basic Usage

Run the CLI with a prompt:

```bash
uv run agi-day-1 "What's the weather in Paris?"
```

### Conversation Memory

The tool automatically remembers previous conversations. Just ask follow-up questions:

```bash
# First message
uv run agi-day-1 "What's the capital of France?"

# Follow-up (remembers previous conversation)
uv run agi-day-1 "What did I ask you before?"
```

### Command-Line Options

```bash
# Clear conversation history
uv run agi-day-1 --clear

# Disable web search
uv run agi-day-1 "Tell me a joke" --no-web-search

# Use a different model
uv run agi-day-1 "Explain quantum computing" --model "gpt-4o"

# Show help
uv run agi-day-1 --help
```

### Available Options

| Option | Description |
|--------|-------------|
| `prompt` | Your message/prompt to send to the AI (required) |
| `--clear` | Clear conversation history and start fresh |
| `--no-web-search` | Disable web search tool |
| `--model MODEL` | Specify the model to use (default: `gpt-4o-mini`) |
| `--help` | Show help message |

## 📁 Project Structure

```
Agentic-AI/
└── Day 1 - UV/
    ├── AGI-Day-1/
    │   ├── package/
    │   │   ├── __init__.py
    │   │   └── main.py          # Main application code
    │   ├── .venv/               # Virtual environment (auto-generated)
    │   ├── .conversation_id     # Conversation state (auto-generated)
    │   ├── .env                 # Your API key (create this)
    │   ├── pyproject.toml       # Project configuration & dependencies
    │   └── uv.lock              # Dependency lock file
    └── README.md                # This file
```

## 🔧 How It Works

1. **First Run**: When you run the CLI for the first time, it creates a new conversation
2. **Memory Storage**: After each response, the conversation ID is saved to `.conversation_id`
3. **Next Run**: The tool loads the previous conversation ID and continues the conversation
4. **Clear History**: Use `--clear` to start a fresh conversation

## 🐛 Troubleshooting

### Error: `OPENAI_API_KEY environment variable is not set!`

**Solution**: Make sure you've created a `.env` file in the `AGI-Day-1/` directory with your API key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### Error: `Python 3.12+ required`

**Solution**: Install Python 3.12 or higher. Check your version:
```bash
python --version
```

### Error: `uv: command not found`

**Solution**: Install UV package manager:
```bash
# On Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# On Linux/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Conversation not remembering previous messages

**Solution**: 
- Check if `.conversation_id` file exists in the `AGI-Day-1/` directory
- Make sure you're running commands from the `AGI-Day-1/` directory
- Try clearing and starting fresh: `uv run agi-day-1 --clear`

## 🔐 Security Notes

- **Never commit your `.env` file** - It's already in `.gitignore`
- **Never share your API key** - Keep it private
- The `.conversation_id` file is also ignored by git for privacy

## 📚 Dependencies

- `openai>=2.14.0` - OpenAI Python SDK
- `python-dotenv>=1.0.0` - Environment variable management
- `requests>=2.32.5` - HTTP library (for potential future features)

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests!

## 📝 License

[Add your license here]

## 🙏 Acknowledgments

- Built with [UV](https://github.com/astral-sh/uv) for fast Python package management
- Uses [OpenAI API](https://platform.openai.com/) for AI capabilities

---

**Happy Chatting! 🚀**

