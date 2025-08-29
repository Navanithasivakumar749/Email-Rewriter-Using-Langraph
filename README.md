# Langraph Email Rewriter

A powerful email polishing tool that transforms casual, informal emails into professional, well-structured communications using AI. Supports both local models via Ollama and cloud-based Claude API for high-quality results.

## 🎯 Overview

This project provides a flexible email polishing system with the following key features:
- Two-stage processing pipeline: abbreviation expansion followed by style refinement
- Support for both local (Ollama) and cloud (Claude API) language models
- Simple command-line interface for easy integration into any workflow
- Environment-based configuration for flexible deployment

## ✨ Features

- **🤖 Multiple LLM Backends**: Choose between local Ollama models or Claude API
- **🔧 Professional Polish**: Transforms casual emails into business-appropriate communication
- **📝 Smart Abbreviation Expansion**: Automatically expands informal abbreviations (e.g., "ASAP" → "as soon as possible")
- **⚙️ Configurable**: Easily switch between models via environment variables
- **🔌 Extensible**: Modular design makes it easy to add new features or integrations
- **📊 Two-Stage Processing**: Separates abbreviation expansion from style refinement for better results

## 🏗️ Architecture

### Core Components

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Raw Email     │───▶│   Abbreviation   │───▶│   Email         │
│   Input         │    │   Expansion      │    │   Polishing    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │   LangGraph      │    │   LLM Backend   │
                       │   Workflow       │    │   (Ollama/Claude)
                       └──────────────────┘    └─────────────────┘
```

### File Structure

```
Langraph_email/
├── main.py                    # Command-line interface
├── langgraph_graph.py         # LangGraph workflow orchestration
├── agents.py                  # LLM configuration and prompts
├── agents_ollama.py           # Ollama-specific LLM configuration
├── agents_claude_only.py       # Claude API configuration
├── agents_flexible.py         # Flexible LLM selection
├── abbreviations.py           # Abbreviation expansion logic
├── tool_abbr_expand.py        # Abbreviation expansion tool
├── mcp_server.py              # Optional MCP server
├── requirements.txt           # Python dependencies
├── start_email_rewriter.bat   # Windows startup script
├── .env.example              # Example environment config
└── README.md                 # This documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- (Optional) Ollama installed with a supported model (e.g., qwen3:0.6b)
- (Optional) Anthropic API key for Claude models

### Installation

1. Clone the repository and install dependencies:

```bash
git clone <repository-url>
cd Langraph_email
pip install -r requirements.txt
```

2. Configure your environment by creating a `.env` file:

```env
# For local models (Ollama)
USE_OLLAMA=true
OLLAMA_MODEL=qwen3:0.6b

# OR for Claude API
# USE_OLLAMA=false
# ANTHROPIC_API_KEY=your_api_key_here
# CLAUDE_MODEL=claude-3-haiku-20240307
```

## 🖥️ Usage

### Command Line Interface

Simply run:

```bash
python main.py
```

Then paste your email text and press Enter twice to process it.

### MCP Server (Optional)

To use with Claude Desktop, configure your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "email-rewriter": {
      "command": "python",
      "args": ["path/to/mcp_server.py"],
      "env": {
        "PYTHONPATH": "path/to/Langraph_email"
      }
    }
  }
}
```

Then start the server:

```bash
python mcp_server.py
```

## 🔧 Configuration

### Environment Variables

- `USE_OLLAMA`: Set to "true" to use local Ollama models (default: false)
- `OLLAMA_MODEL`: Model name for Ollama (default: "qwen3:0.6b")
- `ANTHROPIC_API_KEY`: Required when using Claude API
- `CLAUDE_MODEL`: Claude model name (default: "claude-3-haiku-20240307")

**Option B: Direct Python**
```bash
python mcp_server.py
```

## 📖 Usage

### In Claude Desktop

1. Open Claude Desktop
2. Start a new conversation
3. Use the email rewriting tool by providing your raw email content
4. The system will automatically:
   - Expand abbreviations
   - Polish the tone and structure
   - Return a professional email

### Example

**Input:**
```
Hi,
Can u send me the report ASAP? I kinda need it for the meeting tomorrow.
Thanks!
```

**Output:**
```
Subject: Request for Report

Dear Sir/Madam,

I hope this message finds you well. Could you please send me the report as soon as possible? I would somewhat appreciate having it available for tomorrow's meeting.

Thank you for your time and assistance.

Best regards,
```

### Standalone Testing

```bash
python main.py
### State Management

```python
class EmailState(TypedDict):
    raw_email: str        # Original input
    expanded_email: str   # After abbreviation expansion
    polished_email: str   # Final polished output
```

### Model Configuration

The system supports multiple AI models:

- **Primary**: Ollama qwen3:0.6b (free, local)
- **Fallback**: Claude API (requires API key)
- **Backup**: Simple text replacement logic

## 🛠️ Configuration Options

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `USE_OLLAMA` | `true` | Use local Ollama model |
| `OLLAMA_MODEL` | `qwen3:0.6b` | Ollama model name |
| `ANTHROPIC_API_KEY` | - | Claude API key (optional) |
| `CLAUDE_MODEL` | `claude-3-haiku-20240307` | Claude model version |

### Customizing Prompts

Edit `agents.py` to modify the email polishing prompt:

```python
email_prompt = PromptTemplate.from_template("""
Your custom prompt here...
""")
```

## 🔍 Troubleshooting

### Common Issues

**1. MCP Server Won't Start**
- Check Python path in Claude Desktop config
- Verify all dependencies are installed
- Ensure Ollama is running

**2. Model Not Found**
- Verify Ollama qwen3:0.6b is installed: `ollama list`
- Pull model if missing: `ollama pull qwen3:0.6b`

**3. Connection Issues**
- Restart Claude Desktop after config changes
- Check server logs for error messages
- Verify file paths are correct

### Debug Mode

Enable verbose logging by modifying `mcp_server.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📋 Dependencies

### Core Requirements

```txt
mcp>=0.9.0                 # Model Context Protocol framework
pydantic>=2.0.0           # Data validation
langgraph                 # Workflow orchestration
langchain                 # LLM framework
langchain-anthropic       # Claude API support
langchain-ollama          # Ollama integration
python-dotenv             # Environment management
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the logs for error messages
3. Verify your configuration matches the setup guide

## 🔄 Version History

- **v1.0**: Initial release with Ollama integration
- **v1.1**: Added FastMCP framework support
- **v1.2**: Improved error handling and fallback logic
- **Current**: Stable MCP server with Claude Desktop integration

---

**Note**: This project runs entirely on your local machine, ensuring privacy and eliminating ongoing costs. The Ollama qwen3:0.6b model provides excellent results for email polishing while being completely free to use.
