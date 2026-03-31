# Student Setup Guide - STAT 418 Tools in Data Science

This guide will help you set up your development environment for STAT 418. Follow the instructions for your operating system.

## What You'll Install

1. **Git** - Version control system
2. **Python 3.11+** - Programming language
3. **uv** - Fast Python package manager
4. **VSCode** - Code editor
5. **Claude Code (Cline)** - AI coding assistant with OpenRouter

**Time Required**: 30-45 minutes

---

## Prerequisites

- **macOS**: macOS 10.15 (Catalina) or later
- **Windows**: Windows 10 or later
- Admin/sudo access on your machine
- Stable internet connection
- At least 5GB of free disk space

---

## 1. Git Installation

### macOS

Install Xcode Command Line Tools (includes Git):

```bash
xcode-select --install
```

A dialog will appear - click "Install" and follow the prompts.

### Windows

1. Download Git from [git-scm.com/download/win](https://git-scm.com/download/win)
2. Run the installer with default settings
3. When asked, select "Git from the command line and also from 3rd-party software"

### Verify Installation

Open a new terminal/command prompt and run:

```bash
git --version
# Should show: git version 2.x.x or higher
```

### Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@ucla.edu"
```

---

## 2. Python 3.11+ Installation

### macOS

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download **Python 3.11** or later for macOS
3. Open the downloaded `.pkg` file
4. Follow the installation wizard (use default settings)

### Windows

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download **Python 3.11** or later for Windows
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" at the bottom
5. Click "Install Now"

### Verify Installation

Open a new terminal/command prompt:

```bash
# macOS
python3 --version

# Windows
python --version

# Should show: Python 3.11.x or higher
```

---

## 3. uv Installation

uv is a fast Python package manager that replaces pip.

### macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, **close and reopen your terminal**.

### Windows

Open PowerShell and run:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, **close and reopen PowerShell**.

### Verify Installation

```bash
uv --version
# Should show: uv x.x.x
```

### Quick uv Tutorial

```bash
# Create a new project directory
mkdir my-project
cd my-project

# Initialize a uv project (creates pyproject.toml)
uv init

# Create a virtual environment
uv venv

# Activate the virtual environment
# macOS/Linux:
source .venv/bin/activate

# Windows PowerShell:
.venv\Scripts\activate

# Your prompt should now show (.venv) at the beginning

# Install packages
uv pip install pandas numpy

# Or add dependencies to your project
uv add pandas numpy

# Deactivate when done
deactivate
```

---

## 4. VSCode Installation

### macOS

1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Click "Download for Mac"
3. Open the downloaded `.zip` file
4. Drag "Visual Studio Code" to your Applications folder
5. Open VSCode from Applications

### Windows

1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Click "Download for Windows"
3. Run the installer
4. **Check "Add to PATH"** during installation
5. Use all other default settings

### Install Required Extensions

Open VSCode and install these extensions:

**1. Python Extension**
- Press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows)
- Search for "Python"
- Click Install on "Python" by Microsoft

**2. Cline (Claude Code) Extension**
- Search for "Cline"
- Click Install on "Cline" (formerly Claude Dev)
- This is our AI coding assistant that works with OpenRouter

**3. GitLens Extension**
- Search for "GitLens"
- Click Install on "GitLens" by GitKraken

### Configure Python in VSCode

1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
2. Type "Python: Select Interpreter"
3. Choose your Python 3.11+ installation from the list

---

## 5. OpenRouter + Claude Code Setup

Claude Code (Cline) is an AI coding assistant that runs in VSCode. We'll use it with OpenRouter's free API to access Claude and other models.

### Step 1: Get a Free OpenRouter API Key

1. Visit [openrouter.ai](https://openrouter.ai/)
2. Click "Sign In" in the top right
3. Sign in with your Google account (use your UCLA account or personal)
4. Once signed in, click on your profile icon → "Keys"
5. Click "Create Key"
6. Give it a name like "STAT418-Course"
7. Copy the API key and save it somewhere safe (you won't be able to see it again)

**Important**: OpenRouter provides free credits for new users and has free models available. The free tier is sufficient for this course.

### Step 2: Configure Claude Code (Cline)

1. In VSCode, click the Cline icon in the left sidebar (robot/chat icon)
2. Click the settings gear icon (⚙️) in the Cline panel
3. In the settings that appear:
   - **API Provider**: Select "OpenRouter"
   - **API Key**: Paste your OpenRouter API key
   - **Model**: Select "anthropic/claude-3.5-sonnet" (recommended) or a free model like "google/gemini-2.0-flash-exp:free"

### Step 3: Test Claude Code

1. Create a new file: `test.py`
2. Click the Cline icon in the left sidebar
3. Type: "Write a function that adds two numbers and returns the result"
4. Press Enter

If you get a response with Python code, you're all set! ✓

### Alternative Free Models on OpenRouter

If you want to use completely free models:
- `google/gemini-2.0-flash-exp:free` - Fast and capable
- `meta-llama/llama-3.2-3b-instruct:free` - Smaller but free
- `qwen/qwen-2.5-7b-instruct:free` - Good for coding

You can switch models anytime in the Cline settings.

---

## 6. Fork and Clone the Course Repository

### Step 1: Fork the Repository

1. Visit the course repository: [github.com/natelangholz/stat418-tools-in-datascience-2026](https://github.com/natelangholz/stat418-tools-in-datascience-2026)
2. Click the "Fork" button in the top right
3. This creates a copy of the repository under your GitHub account
4. You'll submit all assignments and your final project to different branches of your forked repo

### Step 2: Clone Your Fork

Open your terminal and run:

```bash
# Navigate to where you want to store course materials
cd ~/Documents  # or wherever you prefer

# Clone YOUR fork (replace YOUR-USERNAME with your GitHub username)
git clone https://github.com/YOUR-USERNAME/stat418-tools-in-datascience-2026.git

# Navigate into the repository
cd stat418-tools-in-datascience-2026

# Add the original repo as 'upstream' to get updates
git remote add upstream https://github.com/natelangholz/stat418-tools-in-datascience-2026.git
```

### Step 3: Set Up the Project Environment

```bash
# Create virtual environment
uv venv

# Activate it
# macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install course dependencies
uv pip install -e .

# Install optional dependencies for LLM work
uv pip install -e ".[llm]"

# Install web development dependencies
uv pip install -e ".[web]"
```

### Step 4: Create Your Assignment Branch

For each assignment, you'll create a new branch:

```bash
# Example for homework 1
git checkout -b hw1-yourname

# Do your work, then commit and push
git add .
git commit -m "Complete homework 1"
git push origin hw1-yourname

# Then create a Pull Request on GitHub to submit
```

---

## 7. Verification Test

Let's verify everything works together.

### Test the Course Environment

```bash
# Make sure you're in the course directory
cd stat418-tools-in-datascience-2026

# Activate virtual environment if not already active
source .venv/bin/activate  # macOS
# or
.venv\Scripts\activate  # Windows

# Create a test file
cat > test_setup.py << 'EOF'
import sys
import pandas as pd
import numpy as np
import requests

print("✓ Python version:", sys.version)
print("✓ Pandas version:", pd.__version__)
print("✓ NumPy version:", np.__version__)
print("✓ Requests version:", requests.__version__)
print("\n✓✓✓ Setup successful! ✓✓✓")
EOF

# Run the test
python test_setup.py
```

**Expected output**: Version information and "Setup successful!"

### Test in VSCode with Claude Code

```bash
# Open the course directory in VSCode
code .
```

In VSCode:
1. Open `test_setup.py`
2. Click the Cline icon
3. Ask: "Add docstrings to this code and explain what it does"
4. If Cline responds with documentation, everything is working! ✓

---

## 8. Setting Up Your .env File

For projects that use API keys, you'll need a `.env` file:

```bash
# In your project directory, copy the example
cp .env.example .env

# Edit .env with your API keys
# macOS:
nano .env
# Windows:
notepad .env
```

Add your OpenRouter API key:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

**IMPORTANT**: Never commit `.env` to git! It's already in `.gitignore`.

---

## Troubleshooting

### Git Issues

**Problem**: `git: command not found` (macOS)
- Run `xcode-select --install` again
- Restart your terminal
- If still not working, download Git from [git-scm.com](https://git-scm.com/download/mac)

**Problem**: `git: command not found` (Windows)
- Restart your terminal/PowerShell after installation
- Make sure you selected "Git from the command line" during installation

### Python Issues

**Problem**: `python: command not found` (macOS)
- Use `python3` instead of `python`
- macOS comes with Python 2.7, so always use `python3`

**Problem**: `python: command not found` (Windows)
- Reinstall Python
- Make sure "Add Python to PATH" is checked
- Restart your terminal after installation

**Problem**: Wrong Python version
- Make sure you downloaded Python 3.11 or later
- Check with `python3 --version` (Mac) or `python --version` (Windows)

### uv Issues

**Problem**: `uv: command not found`
- Close and reopen your terminal after installation
- The installer adds uv to your PATH, but you need a new terminal session

**Problem**: Virtual environment won't activate
- Make sure you're in the correct directory
- Check that `.venv` folder exists (run `ls -la` on Mac or `dir` on Windows)
- Try the full path: `.venv/bin/activate` (Mac) or `.venv\Scripts\activate` (Windows)

**Problem**: `uv pip install` fails
- Make sure virtual environment is activated (you should see `(.venv)` in prompt)
- Try `uv pip install --upgrade pip` first
- Check your internet connection

### VSCode Issues

**Problem**: `code` command not found (macOS)
- Open VSCode
- Press `Cmd+Shift+P`
- Type "Shell Command: Install 'code' command in PATH"
- Press Enter

**Problem**: Python extension can't find interpreter
- Press `Cmd+Shift+P` / `Ctrl+Shift+P`
- Type "Python: Select Interpreter"
- Click "Enter interpreter path..."
- Browse to your Python installation or select `.venv/bin/python`

### Claude Code (Cline) Issues

**Problem**: "API key invalid" error
- Double-check you copied the entire API key (no spaces)
- Make sure you selected "OpenRouter" as the API provider
- Try generating a new API key at [openrouter.ai](https://openrouter.ai/)

**Problem**: "Rate limit exceeded"
- Free tier has rate limits
- Wait a minute and try again
- Consider using a different free model
- Check your OpenRouter dashboard for usage

**Problem**: Cline not responding
- Check your internet connection
- Verify API key is correct in settings
- Restart VSCode
- Check Cline output panel for error messages (View → Output → Cline)

**Problem**: Model not available
- Some models require credits
- Switch to a free model (look for `:free` suffix)
- Check OpenRouter's model list for available free options

### Fork and Clone Issues

**Problem**: Can't fork repository
- Make sure you're logged into GitHub
- You need a GitHub account to fork

**Problem**: `git clone` fails
- Check your internet connection
- Make sure you're using YOUR fork URL, not the original
- If using SSH, make sure your SSH keys are set up

**Problem**: Can't push to repository
- Make sure you cloned YOUR fork, not the original
- Check that you're on a branch (not main)
- Verify your Git credentials are configured

---

## Getting Help

If you encounter issues not covered here:

1. **Course Slack** - Post in #tech-help channel
2. **Office Hours** - Bring your laptop for hands-on help
3. **Week 1 Class** - We'll dedicate time for troubleshooting
4. **GitHub Issues** - Report bugs in course materials

---

## Next Steps

Once your environment is set up:

1. ✅ Complete this setup guide
2. ✅ Fork the course repository on GitHub
3. ✅ Clone your fork to your local machine
4. ✅ Set up the project environment with uv
5. ✅ Test Claude Code with OpenRouter
6. 📚 Complete Week 1 exercises
7. 💬 Join the course Slack workspace

---

## Quick Reference Card

### Common Commands

```bash
# Git
git clone <url>                    # Clone a repository
git status                         # Check status
git checkout -b branch-name        # Create and switch to new branch
git add .                          # Stage all changes
git commit -m "message"            # Commit changes
git push origin branch-name        # Push branch to remote
git pull upstream main             # Get updates from original repo

# uv
uv init                            # Initialize new project
uv venv                            # Create virtual environment
source .venv/bin/activate          # Activate (Mac/Linux)
.venv\Scripts\activate             # Activate (Windows)
uv add <package>                   # Add package to project
uv pip install <package>           # Install package
uv pip install -e .                # Install project in editable mode
uv pip install -e ".[llm]"         # Install with optional dependencies
deactivate                         # Deactivate environment

# VSCode
code .                             # Open current directory
Cmd/Ctrl + Shift + P               # Command palette
Cmd/Ctrl + `                       # Toggle terminal
Cmd/Ctrl + B                       # Toggle sidebar
```

### File Locations

**macOS**:
- Python: `/Library/Frameworks/Python.framework/Versions/3.11/bin/python3`
- uv: `~/.cargo/bin/uv`
- VSCode config: `~/Library/Application Support/Code/User/settings.json`

**Windows**:
- Python: `C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe`
- uv: `%USERPROFILE%\.cargo\bin\uv.exe`
- VSCode config: `%APPDATA%\Code\User\settings.json`

### Important URLs

- Course Repository: [github.com/natelangholz/stat418-tools-in-datascience-2026](https://github.com/natelangholz/stat418-tools-in-datascience-2026)
- OpenRouter: [openrouter.ai](https://openrouter.ai/)
- OpenRouter Models: [openrouter.ai/models](https://openrouter.ai/models)
- Python Downloads: [python.org/downloads](https://www.python.org/downloads/)
- uv Documentation: [docs.astral.sh/uv](https://docs.astral.sh/uv/)

---

**Welcome to STAT 418! 🎉**

If you've completed this setup successfully, you're ready for Week 1!