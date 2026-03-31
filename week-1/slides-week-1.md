# STAT 418: Tools in Data Science
## Week 1: Introduction & Modern Development Environment

**Instructor:** Nate Langholz  
**Date:** March 31, 2026  
**Class Time:** Tuesdays 6:00-9:00 PM

---

## Welcome to STAT 418

**Building Real, Deployable Data Products**

This course focuses on the practical tools that data scientists use to build real, deployable data products. Over 10 weeks, we'll take a data science project from initial idea all the way through to a deployed application that others can use.

- **10 weeks**: Idea → Deployed Application
- **Hands-on learning** with industry tools
- **Tools change, fundamentals endure**

The landscape of data science tools changes rapidly. What was cutting edge five years ago might be obsolete today. But the fundamental concepts - version control, reproducible environments, testing, deployment - these endure.

**Speaker Notes:**
This isn't a theory course - it's about getting your hands dirty with the actual tools and workflows used in industry today. We'll learn current tools while understanding the principles that will serve you throughout your career, regardless of which specific technologies are popular at any given moment. The course builds progressively from foundational tools to production deployment systems.

---

## Course Structure

**Progressive Learning Over 10 Weeks**

- **Tuesdays 6:00-9:00 PM** - 3-hour sessions
- **4 problem sets** on alternating weeks
- **Individual final project** throughout the quarter
  - **Week 6**: Proposal presentation with acquired data
  - **Week 10**: Final presentation of completed project

**Course Arc:**
- **Weeks 1-3**: Foundation (Git, Python, Command Line, Containers)
- **Weeks 4-5**: Data Acquisition & AI Integration (Web Scraping, LLMs, RAG)
- **Weeks 6-8**: Deployment & Applications (Streamlit, APIs, MCP Servers)
- **Weeks 9-10**: Production Systems & Presentations (CI/CD, Final Projects)

**Speaker Notes:**
The course is structured around hands-on learning. Each problem set builds on previous concepts, and your final project will showcase all the skills you've learned. By the end, you'll have built and deployed a complete data product that demonstrates your capabilities to potential employers. The progressive structure ensures you have the foundational skills before moving to more complex topics.

---

## AI-Assisted Development in 2026

**AI Assistants as Productivity Tools**

AI coding assistants are everywhere in 2026. They can write code, explain code, debug code, and generate documentation. This fundamentally changes how we approach software development, but it doesn't make learning to code obsolete.

**Our Philosophy:**
- **AI enhances productivity**, doesn't replace understanding
- **Like calculators in math**: frees you for higher-level thinking
- **Learn when to trust**, when to question
- **Focus on architecture and problem-solving**, not syntax memorization

This course embraces AI assistants while building deep understanding of what we're doing and why.

**Speaker Notes:**
Some people worry AI makes learning to code obsolete. That's not true, but it does change what we need to learn and how we learn it. AI assistants free you from memorizing syntax so you can focus on architecture, logic, and problem-solving. We'll learn to use AI effectively while building the fundamentals that let you understand and improve what AI generates. You'll learn how to prompt effectively and how to evaluate generated code.

---

## Part 1: Version Control with Git

**The Problem We're Solving**

If you've ever worked on a document and ended up with files named:
```
final_version.doc
final_version_2.doc
final_version_ACTUALLY_FINAL.doc
```

You understand the problem version control solves. Now imagine that problem with code, where you have dozens of files that all depend on each other, and multiple people making changes simultaneously.

**What Version Control Provides:**
- **Track every change** made to your code over time
- **See who changed what, when, and why**
- **Experiment without fear** of breaking working code
- **Collaborate without conflicts**
- **Roll back to any previous state** if something goes wrong

**Speaker Notes:**
Version control systems are fundamental to professional software development. Without them, collaboration becomes impossible and experimentation becomes dangerous. Git has become the industry standard, and understanding it is essential for any data science career. Your GitHub profile essentially becomes your professional portfolio.

---

## Git: A Brief History

**Created by Linus Torvalds in 2005**

Git was created for Linux kernel development after the version control system they were using became unavailable. Torvalds needed something that could handle the massive Linux codebase with thousands of contributors working simultaneously.

**Design Goals:**
- **Speed**: Operations that took minutes now take seconds
- **Distributed architecture**: Every developer has complete history
- **Powerful branching**: Easy to experiment and collaborate
- **Handle large projects** with many contributors

**Why Git Won:**
- Genuinely fast performance
- Distributed workflow (work offline)
- Powerful branching and merging
- **GitHub made it accessible** (2008)

**Speaker Notes:**
Git won the version control wars for technical reasons, but GitHub's social platform made it dominant. GitHub turned Git from a command-line tool into a collaborative platform with web interfaces, pull requests, issue tracking, and social features. Today, having a GitHub profile with your projects is essentially a portfolio for developers and data scientists. In this course, all your work will be on GitHub.

---

## How Git Works

**Three States of Your Code**

Git thinks about your code in three states:

1. **Working Directory** - Your actual files that you're editing
2. **Staging Area (Index)** - Files you've marked as ready to save
3. **Repository (.git directory)** - The committed history of your project

**Basic Workflow:**
```bash
git status                    # Check what's changed
git add filename.py          # Stage specific changes
git add .                    # Stage all changes
git commit -m "Add feature"  # Commit with descriptive message
git push origin main         # Push to GitHub
```

**The Process:** Make changes → Stage changes → Commit changes → Push to remote

**Speaker Notes:**
The basic workflow is simple but powerful. You make changes to files in your working directory, stage the changes you want to save, then commit those staged changes to the repository with a message describing what you did. Once committed, those changes are permanently recorded in the project history. When working with GitHub, you push your commits to back up your work and share with collaborators.

---

## Git Best Practices

**Commit Messages Matter**

Your commit messages should explain what changed and why, not how:

- **Good**: "Add user authentication feature"
- **Good**: "Fix bug in data processing pipeline"
- **Bad**: "Update files"
- **Bad**: "Change line 47"

**Commit Strategy:**
- **Commit often** - don't wait until everything is perfect
- **Commit logical units** - each commit should represent one coherent change
- **Don't commit half-finished features**
- **Don't commit 500 lines of changes at once**

**Use .gitignore:**
- Generated files, temporary files, files with secrets
- Virtual environment directories (`venv/`, `.venv/`)
- Compiled Python files (`*.pyc`, `__pycache__/`)
- IDE configuration files
- Environment files (`.env`)

**Speaker Notes:**
Good commit messages are crucial for understanding project history. Future you (and your collaborators) will thank you for clear commit messages when trying to understand what changed and why. Each commit should tell a story about the evolution of your project. The .gitignore file prevents you from accidentally committing files that shouldn't be in version control, especially sensitive information like API keys.

---

## Part 2: The Python Package Management Problem

**Different Projects Need Different Versions**

Python has become the dominant language for data science, but it has a fundamental problem:

```
Project A needs:           Project B needs:
- pandas 1.5.0            - pandas 2.0.0
- numpy 1.23.0            - numpy 1.24.0

But system Python can only have ONE version of each package!
```

If you install pandas 2.0.0 for Project B, you break Project A.

**The Solution: Virtual Environments**

A virtual environment is an isolated Python installation for a specific project:
- Each project gets its own environment with its own packages
- Project A's environment has pandas 1.5.0
- Project B's environment has pandas 2.0.0
- They don't interfere with each other
- Full reproducibility when sharing projects

**Speaker Notes:**
This isolation is crucial for reproducibility. You can share your project with someone else, they can create a virtual environment and install the same package versions you used, and the code will work the same way. Without virtual environments, "it works on my machine" becomes a constant problem in data science projects.

---

## The Python Package Management Saga

**Historical Solutions (All Had Issues)**

Python's ecosystem has had many competing tools for managing packages and environments, and they've all had significant problems:

- **virtualenv (2007)**: Virtual environments, but clunky workflow
- **pip (2008)**: Package installer, but slow dependency resolution
- **conda (2012)**: Environments + packages, but heavy and slow
- **poetry (2018)**: Modern dependency management, but complex
- **pipenv (2017)**: Attempted to unify pip + virtualenv, but slow and confusing

**The Running Joke:**
"The hardest part of Python is managing Python itself"

For years, Python developers have struggled with environment and package management. Each tool tried to solve the problem but introduced new complexities.

**Speaker Notes:**
This has been a persistent pain point in the Python ecosystem. Developers would spend more time fighting with package management than actually writing code. Each tool had its advocates, but none provided a simple, fast, reliable solution that worked well for everyone. This fragmentation made Python harder to learn and use effectively.

---

## Enter uv: Modern Python Package Management

**Released 2024 by Astral (creators of Ruff)**

uv represents a new approach to Python package management, designed from the ground up to be fast, simple, and reliable:

**Key Advantages:**
- **Written in Rust**: 10-100x faster than pip
- **Unified tool**: Handles both packages AND environments
- **Simple, intuitive commands**: One way to do things
- **Compatible**: Works with pip and requirements.txt
- **Cross-platform**: Same experience on Mac, Windows, Linux
- **Free and open source**

**Why uv for this course:**
- Fast enough you won't wait for installations
- Simple enough you won't get confused
- Modern and actively developed
- Solves practical problems that have plagued Python for years

**Speaker Notes:**
uv solves a practical problem for this course: you won't waste time waiting for packages to install or fighting with environment management. You'll spend your time actually learning data science tools instead of fighting with the tools that manage the tools. The speed difference is genuinely dramatic - installations that took minutes now take seconds.

---

## uv Workflow

**Creating a Project**

```bash
# Create project directory
mkdir my-project
cd my-project

# Initialize uv project (creates pyproject.toml)
uv init

# Create virtual environment
uv venv

# Activate environment
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
```

**Installing Packages**

```bash
# Add packages to project
uv add pandas numpy matplotlib

# Or install with pip interface
uv pip install pandas numpy matplotlib

# Install from requirements file
uv pip install -r requirements.txt

# Save current packages
uv pip freeze > requirements.txt
```

**How It Works:**
When you create a virtual environment, uv creates a `.venv` directory containing a complete Python installation. When activated, your shell uses this isolated Python instead of your system Python.

**Speaker Notes:**
The .venv directory contains the Python interpreter, standard library, and space for packages you install. Once activated, any packages you install go into this environment's directory, not your system Python. When you're done working, you deactivate the environment and return to system Python. If you need to delete the environment, just delete the .venv directory and create a new one. This isolation is what makes projects reproducible.

---

## Part 3: VSCode - The Modern Code Editor

**Evolution of Code Editors**

The history of code editors shows a progression toward more integrated, user-friendly tools:

- **1970s-1980s**: vi, Emacs (terminal-based, steep learning curve)
- **1990s-2000s**: Eclipse, Visual Studio (heavy IDEs, slow, language-specific)
- **2010s**: Sublime Text, Atom (lightweight, fast, but limited features)
- **2015-present**: VSCode (the winner)

**Why VSCode Won:**
- **Free and open source** (Microsoft)
- **Fast and lightweight** (built on Electron)
- **Massive extension ecosystem** (JavaScript-based extensions)
- **Cross-platform** (Mac, Windows, Linux)
- **Strikes perfect balance** between lightweight and feature-rich

**Speaker Notes:**
VSCode quickly became the dominant code editor because it solved the trade-offs that plagued previous editors. It's lightweight enough to start quickly but feature-rich enough for complex projects. The extension ecosystem means it can be customized for any language or workflow. Being built on web technologies (Electron) makes it easy to extend and maintain across platforms.

---

## Why VSCode for Data Science

**Integrated Workflow - Everything in One Place**

VSCode offers a complete development environment without the complexity of traditional IDEs:

**Core Features:**
- **Code editor** with syntax highlighting and IntelliSense
- **Integrated terminal** - run commands without leaving the editor
- **Git interface** - visual diff, staging, commits, push/pull
- **Jupyter notebook support** - run notebooks directly in VSCode
- **Debugger** - step through code and inspect variables
- **Extension ecosystem** - customize for your specific needs

**No Context Switching:**
Write code, run commands, commit to Git, use AI assistants - all without leaving VSCode. This integrated workflow dramatically improves productivity.

**Python-Specific Benefits:**
- IntelliSense (intelligent code completion)
- Linting (automatic code quality checks)
- Formatting (automatic code style)
- Testing integration
- Virtual environment detection

**Speaker Notes:**
For data science work, the integrated workflow is crucial. You're constantly switching between writing code, running experiments, checking results, and iterating. Having everything in one interface eliminates the friction of switching between applications. The Python extension provides professional-grade development tools that help you write better code faster.

---

## Essential VSCode Extensions

**Three Must-Have Extensions for This Course**

**1. Python (Microsoft)**
- Complete Python language support
- IntelliSense, debugging, linting, formatting
- Virtual environment integration
- Jupyter notebook support
- Testing framework integration

**2. Cline (Claude Code) - AI Assistant**
- Open source AI coding assistant for VSCode
- Works with OpenRouter to access multiple LLM providers
- We'll configure it with Claude 3.5 Sonnet or free models
- Context-aware suggestions based on your codebase
- Code generation, explanation, debugging help
- Documentation writing assistance

**3. GitLens (Enhanced Git Integration)**
- Visual Git history and blame annotations
- See who changed each line of code and when
- Branch comparison and visualization
- Commit history exploration
- Essential for understanding project evolution

**Speaker Notes:**
These three extensions transform VSCode into a complete data science development environment. The Python extension provides the foundation for Python development. Cline brings AI assistance directly into your editor with access to multiple models through OpenRouter. GitLens makes Git visual and understandable, which is especially useful when working on team projects or trying to understand unfamiliar code. Together, they provide everything you need for modern data science development.

---

## Part 4: AI Coding Assistants

**The AI Revolution in Software Development (2021-2026)**

The rise of AI coding assistants represents a fundamental shift in how we write software:

**Timeline:**
- **2021**: GitHub Copilot launches (first mainstream AI assistant, paid)
- **2022-2023**: Explosion of alternatives from multiple companies
- **2024-2025**: Free tiers emerge, open source models become available
- **2026**: Standard practice in professional development

**Our Approach: Cline (Claude Code) + OpenRouter**

- **Cline**: Open source VSCode extension (formerly Claude Dev)
- **OpenRouter**: API gateway to multiple LLM providers
- **Free tier available**: Generous free credits for new users
- **Multiple models**: Claude, GPT, Gemini, Llama, and more
- **Free models**: Several models with `:free` suffix (no credit card needed)
- **Context-aware**: Understands your codebase
- **Customizable**: Can switch providers and models easily

**Speaker Notes:**
By 2026, AI coding assistants are ubiquitous - most professional developers use them daily. The question is no longer whether to use AI assistants, but how to use them effectively. For this course, Cline with OpenRouter provides a flexible, powerful solution. OpenRouter gives you access to multiple models including completely free options, so you can choose based on your needs and budget. The free tier is more than sufficient for coursework.

---

## What AI Assistants Excel At

**Tasks Where AI Provides Dramatic Speedup**

AI assistants are particularly good at certain types of coding tasks:

**Code Generation:**
- **Boilerplate code** - repetitive, standard code every project needs
- **Syntax help** - when you know what to do but can't remember exact syntax
- **Function scaffolding** - creating function signatures and basic structure

**Code Understanding:**
- **Explaining unfamiliar code** - especially useful with new libraries
- **Documentation generation** - docstrings, comments, README files
- **Code translation** - converting between languages or formats

**Development Tasks:**
- **Unit test generation** - creating test cases for your functions
- **Debugging simple errors** - explaining what went wrong
- **Code improvements** - suggesting more efficient or readable approaches
- **Refactoring** - restructuring code while maintaining functionality

**The Result:** Tasks that might take 30 minutes of documentation lookup and typing can be done in 30 seconds with AI assistance.

**Speaker Notes:**
These capabilities can dramatically speed up development, but the key is knowing when to use AI and when to think through problems yourself. AI is excellent at the mechanical aspects of coding but can't replace your domain knowledge, architectural thinking, or problem-solving skills. The goal is to use AI to handle routine tasks so you can focus on the interesting, creative aspects of data science.

---

## What AI Assistants Cannot Do

**Significant Limitations You Must Understand**

AI assistants have important limitations that mean you're still responsible for the critical aspects of development:

**Context Limitations:**
- **Don't understand your full system** - only see code you show them
- **Can't make architectural decisions** - don't understand long-term implications
- **Don't know your requirements** - can only work with what you tell them

**Technical Limitations:**
- **Struggle with domain-specific logic** - especially in specialized fields
- **Can't debug complex interactions** - between multiple systems
- **Don't understand security implications** - or performance at scale
- **May suggest outdated approaches** - training data has cutoff dates
- **Can hallucinate** - generate plausible but incorrect code

**Your Ongoing Responsibilities:**
- **Understanding the generated code** - don't just copy and paste
- **Testing thoroughly** - AI can't verify correctness
- **Making architectural decisions** - overall system design
- **Applying domain knowledge** - understanding what makes sense in your field
- **Security review** - ensuring code is safe and secure

**Speaker Notes:**
This is crucial to understand: AI assistants are tools that enhance your capabilities, not replacements for your judgment and expertise. They can help you implement solutions faster, but you still need to understand what you're building and why. The most dangerous mistake is blindly trusting AI-generated code without understanding it. Always review, test, and verify.

---

## Effective AI Prompting

**Getting Better Results Through Better Communication**

AI assistants work best when you communicate clearly and specifically:

**Be Specific About What You Want:**
- **Bad**: "write code"
- **Good**: "write a Python function that reads a CSV file using pandas, filters rows where the score column is above 80, and returns the filtered DataFrame"

**Provide Context When Asking for Help:**
- Explain what the code is supposed to do
- Show error messages if there are any
- Explain what you've already tried
- Describe the broader context of your project

**Iterate on Results:**
1. Start with a basic request
2. Review what the AI generates
3. Ask for improvements: "Now add error handling for missing files"
4. Refine further: "Add type hints and a docstring"
5. Continue until satisfied

**Ask for Explanations:**
- "Why did you choose this approach?"
- "What are the trade-offs of this solution?"
- "Are there alternative ways to do this?"

**Speaker Notes:**
Effective prompting is a skill that improves with practice. The more specific and contextual you are, the better results you'll get. Don't just ask for code - ask for understanding. The goal isn't just to get working code, it's to learn and understand what you're doing. AI can be an excellent teacher if you ask the right questions.

---

## The Modern Development Workflow

**How AI Changes the Development Process**

The workflow for building data science projects has evolved with AI assistants, but humans still drive the critical decisions:

**AI-Assisted Development Process:**

1. **Define the problem** (human) - understand requirements and constraints
2. **Research approaches** (human + AI) - explore solutions and best practices
3. **Design architecture** (human) - make high-level structural decisions
4. **Generate boilerplate** (AI) - create standard code structures
5. **Implement domain logic** (human + AI) - add business-specific functionality
6. **Review and refine** (human) - ensure quality and correctness
7. **Test thoroughly** (human + AI) - verify functionality and edge cases
8. **Document** (human + AI) - explain what was built and why
9. **Deploy and monitor** (human + AI) - put into production

**Key Insight:** Humans drive strategy and architecture, AI accelerates implementation.

**Speaker Notes:**
This workflow is faster than traditional development, but it requires different skills. You need to be good at prompting, able to quickly evaluate code quality, and have strong fundamentals so you can spot when AI makes mistakes. You also need to know when to use AI and when to write code yourself. The most important skill is maintaining the ability to think critically about what you're building.

---

## This Week's Setup Tasks

**Complete Before Next Week's Class**

You need to set up your complete development environment before we can start hands-on work:

**Required Installations:**
1. **Git** - Version control system
2. **Python 3.11+** - Programming language
3. **uv** - Package manager
4. **VSCode** - Code editor
5. **VSCode Extensions** - Python, Cline, GitLens
6. **OpenRouter API Key** - For AI assistant (free tier available)
7. **Configure Cline** - Connect to OpenRouter

**Detailed Instructions:**
- **STUDENT_SETUP.md** has step-by-step instructions
- Separate sections for Mac and Windows
- Troubleshooting guide for common issues
- Test procedures to verify everything works

**Don't Wait Until Last Minute:**
Setup issues are common and can take time to resolve. Start early so you have time to get help if needed.

**Speaker Notes:**
The setup guide is comprehensive and has been tested on both Mac and Windows systems. Follow it carefully and test that everything works. The most common issues are usually related to PATH configuration or permissions. If you run into problems, post in the Slack channel - your classmates might have solved the same issue. OpenRouter provides free credits and free models, so you don't need a credit card to get started.

---

## Week 1 Examples

**Three Hands-On Tutorials to Reinforce Concepts**

After completing setup, work through these examples in the `week-1/examples/` directory:

**1. python-setup/**
- Create virtual environment with uv
- Initialize a uv project with `uv init`
- Install packages (pandas, numpy, matplotlib)
- Run a data analysis script
- Create and use requirements.txt
- Practice the workflow you'll use throughout the course

**2. git-workflow/**
- Initialize a Git repository
- Make commits with good messages
- View project history with `git log`
- Create .gitignore file
- Use `git diff` to see changes
- Optional: Push to GitHub and practice branching

**3. ai-assistant-demo/**
- Use Cline for code generation
- Practice effective prompting techniques
- Ask for code explanations and documentation
- Debug with AI assistance
- Learn best practices for AI-assisted development
- Try different OpenRouter models (free and paid)

**Work through these step-by-step** - don't just read them, type the commands and experiment.

**Speaker Notes:**
These examples are designed to give you hands-on experience with the core tools. The python-setup example teaches the environment management workflow you'll use for every project. The git-workflow example covers the version control basics you'll need. The ai-assistant-demo shows you how to use Cline with OpenRouter effectively. Take time to experiment and break things - that's how you learn.

---

## Getting Help

**Multiple Resources Available**

If you run into issues with setup or the examples, don't struggle alone:

**Primary Resources:**
- **STUDENT_SETUP.md** - Comprehensive troubleshooting section
- **Course Slack** - #tech-help channel for quick questions
- **Office Hours** - Hands-on help with your laptop
- **Next Week's Class** - Dedicated troubleshooting time
- **Your Classmates** - Help each other, share solutions

**Common Issues:**
- Most setup problems have been encountered before
- Check Slack first - someone may have posted the solution
- Google error messages - often leads to Stack Overflow solutions
- Ask AI assistant (Cline) for help with error messages
- Check OpenRouter dashboard if having API issues

**Getting Help is Part of Learning:**
Don't view asking for help as failure. Professional developers constantly help each other and look up solutions. Learning to find help efficiently is a valuable skill.

**Speaker Notes:**
The troubleshooting section in STUDENT_SETUP.md covers the most common issues we've seen in previous years. The course Slack channel is usually the fastest way to get help - someone is usually online and willing to help. Office hours are great for complex issues that need hands-on debugging. Remember, everyone struggles with setup issues - it's normal and expected.

---

## Looking Ahead

**Course Progression Over 10 Weeks**

**Next Week (Week 2): Command Line & Unix Fundamentals**
- Bash scripting for data processing
- Text processing with grep, sed, awk
- Building data pipelines
- First homework assignment

**Week 3: Advanced Command Line & Containerization**
- More bash scripting techniques
- Introduction to Podman containerization
- Python project management best practices with uv

**Week 4: Data Acquisition**
- Web scraping with Beautiful Soup and Selenium
- API integration and authentication
- AI-assisted code generation for data collection

**Weeks 5-10: Advanced Topics**
- LLMs, RAG systems, vector databases (Week 5)
- Streamlit applications and deployment (Week 6)
- MCP servers and tool creation (Week 7)
- APIs and AI agents (Week 8)
- CI/CD pipelines with GitHub Actions (Week 9)
- Final presentations (Week 10)

**Speaker Notes:**
Each week builds on the previous ones. The command line skills you'll learn in weeks 2-3 will be essential for the containerization and deployment topics later. The AI assistant skills you're learning now will accelerate your work throughout the course. By week 10, you'll have a complete toolkit for building and deploying data science applications.

---

## Key Takeaways

**Fundamental Principles to Remember**

**Tools vs. Fundamentals:**
- Tools change rapidly, but fundamental concepts endure
- Learn the principles behind the tools, not just the tools themselves
- Understand why things work the way they do

**AI as Enhancement:**
- AI assistants are powerful tools that enhance productivity
- They don't replace understanding or critical thinking
- Use them to speed up implementation while maintaining deep knowledge
- Always review and understand generated code

**Learning by Doing:**
- Work through examples, don't just read them
- Break things and figure out how to fix them
- Experiment with variations and extensions

**Building in Public:**
- Share your work on GitHub - it's your portfolio
- Help classmates and ask for help when needed
- Document your projects well
- Your GitHub profile is your professional presence

**Stay Curious:**
- Follow interesting questions beyond just assignments
- Explore tangents that capture your interest
- The best data scientists are driven by curiosity

**Speaker Notes:**
These principles will serve you throughout your career, regardless of which specific tools are popular. The ability to learn new tools quickly, use AI effectively, and build robust systems will be valuable long after the specific technologies we're using have been replaced by something newer.

---

## This Week's Action Items

**Complete Before Next Tuesday**

**Setup Tasks:**
- [ ] Work through STUDENT_SETUP.md completely
- [ ] Install Git, Python 3.11+, uv, VSCode
- [ ] Install and configure VSCode extensions (Python, Cline, GitLens)
- [ ] Get OpenRouter API key and configure Cline
- [ ] Test that everything works

**Practice Tasks:**
- [ ] Complete all three examples in week-1/examples/
  - [ ] python-setup: Create virtual environment and run analysis
  - [ ] git-workflow: Practice Git commands and workflows
  - [ ] ai-assistant-demo: Use Cline with OpenRouter effectively
- [ ] Join the course Slack workspace
- [ ] Fork the course repository on GitHub
- [ ] Create your own test repository to practice Git

**Preparation:**
- [ ] Start thinking about final project ideas
- [ ] What data are you curious about?
- [ ] What would you like to build and deploy?

**Come to next class ready to code** with your environment fully set up and examples completed.

**Speaker Notes:**
Don't underestimate the time needed for setup - start early. The examples are designed to reinforce what we've covered today and give you confidence with the tools. Starting to think about your final project early will help you make better decisions throughout the course about what skills to focus on developing.

---

## Questions and Next Steps

**Rest of Today's Session**

Now we'll move to hands-on demonstrations:

- **Setup walkthrough** - we'll go through the installation process together
- **Git workflow demo** - see version control in action
- **Python and uv demonstration** - virtual environments and package management
- **AI assistant demo** - effective use of Cline with OpenRouter
- **Troubleshooting time** - help with any setup issues

**Bring Your Questions:**
- If something isn't clear, ask
- If you're stuck on setup, we'll troubleshoot together
- Goal: everyone leaves with a working development environment

**Next Week:**
- Come with setup complete and examples done
- We'll hit the ground running with command line fundamentals
- First homework will be assigned

**Welcome to STAT 418 - Let's build something great this quarter!**

**Speaker Notes:**
The hands-on portion is crucial for cementing the concepts we've discussed. Don't hesitate to ask questions during the demonstrations. The goal is for everyone to leave today with a clear understanding of what we're building toward and confidence that they can complete the setup successfully. Next week we'll assume everyone has a working development environment and can focus on learning new skills rather than fighting with tools.