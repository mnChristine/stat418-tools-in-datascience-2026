# STAT 418: Tools in Data Science
## Week 3: Git Workflows & Containerization

**Instructor:** Nate Langholz  
**Date:** April 14, 2026

---

## Today's Agenda

1. **Advanced Git Workflows** - Branching, merging, rebasing
2. **Collaboration Patterns** - Pull requests and code reviews
3. **Merge Conflict Resolution** - Handling conflicts confidently
4. **Introduction to Containerization** - Reproducible environments
5. **Dockerfile Basics** - Building container images
6. **Practical Containerization** - Running data science in containers

**Where to Run Commands:**
- Use **VSCode's integrated terminal** (View > Terminal or Ctrl+`)
- All examples are in `week-3/examples/`

**Speaker Notes:**
Today we're building on your Git basics from Week 1 to cover professional collaboration workflows. We'll also introduce containerization - a fundamental technology for deploying data science applications. By the end of today, you'll understand how teams work together on code and how to package applications for consistent deployment.

---

## Why Advanced Git Matters

**The Reality of Professional Data Science**

In Week 1, you learned basic Git: init, add, commit, push. That's enough for solo projects. But professional data science is collaborative:

- **Multiple people** working on the same codebase
- **Parallel development** of different features
- **Code review** before merging changes
- **Version management** across environments
- **Rollback capability** when things break

**Without proper Git workflows:**
- Code conflicts and overwrites
- Lost work and confusion
- Difficulty tracking changes
- Hard to collaborate effectively

**Speaker Notes:**
Basic Git gets you started, but professional work requires understanding branching, merging, and collaboration patterns. These aren't just nice-to-have skills - they're essential for working on any team. Every tech company uses these workflows. Understanding them makes you a more valuable team member and helps you contribute to open source projects.

---

## Git Branching Fundamentals

**What is a Branch?**

A branch is an independent line of development. Think of it as a parallel universe where you can make changes without affecting the main codebase.

**Why Branch?**
- **Isolate features**: Work on new features without breaking main code
- **Experiment safely**: Try things without risk
- **Parallel development**: Multiple people work simultaneously
- **Organize work**: Each feature/fix gets its own branch

**Basic Branch Commands:**
```bash
# Create and switch to new branch
git checkout -b feature/my-feature

# List all branches
git branch

# Switch branches
git checkout main

# Delete branch
git branch -d feature/my-feature
```

**Speaker Notes:**
Branching is one of Git's most powerful features. The main branch (formerly called master) should always contain working, deployable code. When you want to add a feature or fix a bug, you create a new branch, make your changes there, and only merge back to main when everything works. This keeps the main branch stable while allowing experimentation.

---

## Branch Naming Conventions

**Common Patterns:**

```bash
# Feature branches
feature/user-authentication
feature/data-visualization
feature/api-integration

# Bug fix branches
fix/login-error
fix/data-parsing-bug
hotfix/critical-security-issue

# Experimental branches
experiment/new-algorithm
experiment/performance-optimization

# Personal branches
yourname/working-branch
```

**Best Practices:**
- Use descriptive names
- Include ticket/issue numbers if applicable
- Use lowercase with hyphens
- Keep names concise but clear

**Speaker Notes:**
Good branch names make it easy to understand what's being worked on. Many teams have conventions - some use prefixes like feature/ or fix/, others include ticket numbers. The key is consistency within your team. Descriptive names help when you're looking at a list of 20 branches trying to figure out which one has the code you need.

---

## Merging vs Rebasing

**Two Ways to Integrate Changes**

**Merging:**
```bash
git checkout main
git merge feature/my-feature
```
- Creates a merge commit
- Preserves complete history
- Shows when branches were merged
- Can create complex history graphs

**Rebasing:**
```bash
git checkout feature/my-feature
git rebase main
```
- Rewrites commit history
- Creates linear history
- Cleaner, easier to follow
- Can cause issues if branch is shared

**When to Use Which:**
- **Merge**: For shared branches, preserving history
- **Rebase**: For personal branches, cleaning up history

**Speaker Notes:**
Merging and rebasing both integrate changes, but they do it differently. Merging preserves the exact history of what happened - you can see when branches diverged and merged. Rebasing rewrites history to make it linear, as if you made your changes on top of the latest code. For beginners, stick with merging. As you get comfortable, you can use rebase to clean up your personal branches before merging to main.

---

## Merge Conflicts: Don't Panic!

**What is a Merge Conflict?**

A conflict occurs when Git can't automatically merge changes because two people modified the same lines of code.

**Conflict Markers:**
```python
<<<<<<< HEAD
def calculate_total(items):
    return sum(items)
=======
def calculate_total(items):
    return sum(item * 1.1 for item in items)
>>>>>>> feature/add-tax
```

**Resolution Steps:**
1. Open the conflicted file
2. Find the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Decide which version to keep (or combine them)
4. Remove the conflict markers
5. Test that the code works
6. Stage and commit the resolution

**Speaker Notes:**
Merge conflicts are normal and not scary once you understand them. They happen when two people edit the same part of a file. Git shows you both versions and asks you to decide which to keep. The markers show: HEAD is your current branch, the other side is what you're merging in. You manually edit the file to keep what you want, remove the markers, and commit. Always test after resolving conflicts!

---

## Resolving Conflicts: Example

**Before Resolution:**
```python
<<<<<<< HEAD
# Calculate total with 10% discount
total = sum(prices) * 0.9
=======
# Calculate total with tax
total = sum(prices) * 1.08
>>>>>>> feature/add-tax
```

**After Resolution:**
```python
# Calculate total with tax and discount
subtotal = sum(prices) * 0.9  # 10% discount
total = subtotal * 1.08        # 8% tax
```

**Commands:**
```bash
# After editing the file
git add conflicted_file.py
git commit -m "Resolve merge conflict: apply discount then tax"
```

**Speaker Notes:**
Here's a real example. Two people modified the same calculation - one added a discount, one added tax. The conflict shows both versions. You need to decide: keep one, keep both, or write something new. In this case, we combined them - apply discount first, then tax. After editing, stage the file and commit. The commit message should explain how you resolved the conflict.

---

## Pull Requests (PRs)

**What is a Pull Request?**

A pull request is a request to merge your branch into another branch (usually main). It's not a Git feature - it's a GitHub/GitLab feature that adds collaboration on top of Git.

**PR Workflow:**
1. Create a feature branch
2. Make your changes and commit
3. Push branch to GitHub
4. Open a pull request on GitHub
5. Team reviews your code
6. Address feedback
7. PR is approved and merged

**Why Use PRs?**
- **Code review**: Others check your work
- **Discussion**: Team discusses changes
- **Testing**: Automated tests run
- **Documentation**: Changes are documented
- **Quality control**: Catch bugs before merging

**Speaker Notes:**
Pull requests are how professional teams collaborate. Instead of directly merging to main, you open a PR and ask others to review your code. This catches bugs, shares knowledge, and maintains code quality. It might feel slow at first, but it prevents so many problems. Every major open source project uses PRs. Learning this workflow makes you ready for professional development.

---

## Code Review Best Practices

**As the Author:**
- Write clear PR descriptions
- Keep PRs small and focused
- Test your code before requesting review
- Respond to feedback professionally
- Don't take criticism personally

**As the Reviewer:**
- Be constructive and specific
- Explain why, not just what
- Praise good code
- Ask questions instead of demanding changes
- Review promptly

**Example Good Review Comment:**
```
This function works, but it loads the entire dataset into memory.
For large files, consider using pandas chunking:

for chunk in pd.read_csv('data.csv', chunksize=1000):
    process(chunk)

This would prevent memory issues with large datasets.
```

**Speaker Notes:**
Code review is a skill. As an author, make it easy to review your code - small PRs, clear descriptions, working tests. As a reviewer, be helpful not harsh. Explain why you're suggesting changes. Good reviews teach and improve code quality. Bad reviews create resentment and slow teams down. Remember: you're reviewing code, not the person.

---

## Forking vs Cloning

**Cloning:**
```bash
git clone https://github.com/username/repo.git
```
- Creates a local copy
- You need write access to push
- Used for repos you have permission to modify

**Forking:**
- Creates your own copy on GitHub
- You have full control of your fork
- Used for repos you don't have write access to
- Enables contributing to open source

**Fork Workflow:**
1. Fork repo on GitHub
2. Clone your fork locally
3. Make changes in a branch
4. Push to your fork
5. Open PR to original repo

**Speaker Notes:**
Cloning and forking serve different purposes. Clone when you're working on a repo you have access to - like your team's project. Fork when you want to contribute to someone else's project - like an open source library. Forking creates your own copy on GitHub that you control. You make changes there, then propose them back to the original via a pull request.

---

## Keeping Your Fork Updated

**The Problem:**

You fork a repo, but the original keeps getting updated. Your fork becomes outdated.

**The Solution:**

Add the original repo as an "upstream" remote:

```bash
# Add upstream remote (one time)
git remote add upstream https://github.com/original/repo.git

# Fetch updates from upstream
git fetch upstream

# Merge upstream changes into your main
git checkout main
git merge upstream/main

# Push updated main to your fork
git push origin main
```

**Check Your Remotes:**
```bash
git remote -v
# origin    https://github.com/yourname/repo.git (your fork)
# upstream  https://github.com/original/repo.git (original)
```

**Speaker Notes:**
This is crucial for contributing to open source or working with forks. The original repo (upstream) keeps changing. You need to pull those changes into your fork (origin) regularly. This prevents your fork from diverging too much, which makes merging harder. Do this before starting new work - always start from the latest upstream code.

---

## Introduction to Containerization

**The Problem We're Solving**

"It works on my machine!" - Every developer ever

**Common Issues:**
- Different Python versions
- Missing dependencies
- Different operating systems
- Configuration differences
- Environment-specific bugs

**The Solution: Containers**

A container packages your application with everything it needs:
- Code
- Dependencies
- System libraries
- Configuration
- Runtime environment

**Result:** Your application runs the same way everywhere - your laptop, your teammate's laptop, the production server.

**Speaker Notes:**
Containerization solves the "works on my machine" problem. You've probably experienced this - code works on your computer but breaks on someone else's. Maybe they have a different Python version, or missing libraries, or different OS. Containers package everything together so it runs identically everywhere. This is fundamental to modern software deployment.

---

## Containers vs Virtual Machines

**Virtual Machines:**
- Full operating system
- Heavy (GBs)
- Slow to start
- Resource intensive

**Containers:**
- Share host OS kernel
- Lightweight (MBs)
- Start instantly
- Efficient resource use

**Analogy:**
- **VM**: Buying a whole house for each guest
- **Container**: Giving each guest their own room in a shared house

**Why Containers Won:**
- Faster
- Lighter
- More portable
- Better for microservices
- Easier to manage

**Speaker Notes:**
Containers are lighter and faster than virtual machines. VMs include a full operating system - if you run 10 VMs, you're running 10 operating systems. Containers share the host OS, so they're much more efficient. They start in seconds instead of minutes, use less disk space, and use less memory. This efficiency is why containers became the standard for deploying applications.

---

## Docker vs Podman

**Docker:**
- Industry standard
- Requires daemon (background service)
- Needs root/admin access
- Widely used and documented

**Podman:**
- Drop-in Docker replacement
- No daemon required
- Runs without root access
- Compatible with Docker commands
- Better security model

**For This Course:**
We'll use Podman because:
- Works on under-resourced machines
- No daemon overhead
- Better security
- Most Docker commands work by replacing `docker` with `podman`

**Speaker Notes:**
Docker is the industry standard, but it requires a daemon - a background service that needs admin access. Podman is a newer alternative that doesn't need a daemon. For students with limited machines or restricted permissions, Podman is better. The good news: Podman is designed to be compatible with Docker. Most Docker commands work with Podman by just changing the command name.

---

## Dockerfile Basics

**What is a Dockerfile?**

A text file with instructions for building a container image. It's like a recipe for creating your environment.

**Basic Dockerfile:**
```dockerfile
# Start from a base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Command to run when container starts
CMD ["python", "app.py"]
```

**Speaker Notes:**
A Dockerfile is a recipe for building a container. Each line is an instruction. FROM specifies the base image - we're starting with Python 3.11. WORKDIR sets the working directory. COPY moves files into the container. RUN executes commands during build. CMD specifies what runs when the container starts. This Dockerfile creates a Python environment with your dependencies installed.

---

## Dockerfile Instructions

**Common Instructions:**

```dockerfile
# Base image
FROM python:3.11-slim

# Metadata
LABEL maintainer="you@example.com"

# Environment variables
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY src/ ./src/

# Run commands
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8000

# Default command
CMD ["python", "src/main.py"]
```

**Speaker Notes:**
These are the most common Dockerfile instructions. FROM sets the base image. ENV sets environment variables. WORKDIR changes directory. COPY moves files from your computer into the container. RUN executes commands during build (like installing packages). EXPOSE documents which ports the container uses. CMD sets the default command when the container runs.

---

## Building and Running Containers

**Build an Image:**
```bash
# Build from Dockerfile in current directory
podman build -t my-app:latest .

# -t: tag (name) for the image
# .: build context (current directory)
```

**Run a Container:**
```bash
# Run container
podman run my-app:latest

# Run with port mapping
podman run -p 8000:8000 my-app:latest

# Run interactively
podman run -it my-app:latest /bin/bash

# Run in background
podman run -d my-app:latest
```

**List and Manage:**
```bash
podman images          # List images
podman ps              # List running containers
podman ps -a           # List all containers
podman stop <id>       # Stop container
podman rm <id>         # Remove container
```

**Speaker Notes:**
Building creates an image from your Dockerfile. Running creates a container from that image. The -p flag maps ports - 8000:8000 means port 8000 in the container maps to port 8000 on your machine. The -it flags make it interactive with a terminal. The -d flag runs it in the background (detached). You can have multiple containers from the same image.

---

## Volume Mounting

**The Problem:**

Containers are isolated. They can't access files on your computer by default.

**The Solution: Volume Mounting**

Mount a directory from your computer into the container:

```bash
# Mount current directory to /data in container
podman run -v $(pwd):/data my-app:latest

# On Windows PowerShell
podman run -v ${PWD}:/data my-app:latest

# Multiple mounts
podman run -v $(pwd)/data:/app/data \
           -v $(pwd)/output:/app/output \
           my-app:latest
```

**Use Cases:**
- Access data files
- Save output
- Edit code without rebuilding
- Share files between host and container

**Speaker Notes:**
Volume mounting connects directories on your computer to directories in the container. This lets containers access your data files and save output back to your computer. Without mounting, files created in the container disappear when it stops. With mounting, you can work with your data, run analysis in a container, and save results back to your machine.

---

## Example: Python Data Science Container

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install data science packages
RUN pip install pandas numpy matplotlib seaborn jupyter

# Copy analysis scripts
COPY analysis.py .

# Default command
CMD ["python", "analysis.py"]
```

**Build and Run:**
```bash
# Build image
podman build -t data-analysis .

# Run with data mounted
podman run -v $(pwd)/data:/app/data \
           -v $(pwd)/output:/app/output \
           data-analysis

# Run Jupyter notebook
podman run -p 8888:8888 \
           -v $(pwd):/app/notebooks \
           data-analysis \
           jupyter notebook --ip=0.0.0.0 --allow-root
```

**Speaker Notes:**
Here's a practical example. We create a container with pandas, numpy, and other data science libraries. We mount our data directory so the container can read our data files. We mount an output directory so results are saved to our computer. For Jupyter, we map port 8888 and mount our notebooks directory. This gives us a consistent Python environment regardless of what's installed on our machine.

---

## Container Best Practices

**Keep Images Small:**
```dockerfile
# Use slim base images
FROM python:3.11-slim

# Clean up after installs
RUN pip install pandas && \
    rm -rf /root/.cache/pip

# Use .dockerignore
# (like .gitignore for containers)
```

**Layer Caching:**
```dockerfile
# Copy requirements first (changes less often)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code last (changes more often)
COPY . .
```

**Security:**
- Don't run as root
- Don't include secrets in images
- Use specific version tags
- Scan images for vulnerabilities

**Speaker Notes:**
Small images build faster, deploy faster, and use less disk space. Use slim base images and clean up after installations. Docker/Podman cache layers - if a layer hasn't changed, it reuses the cached version. Put things that change rarely (like dependencies) before things that change often (like code). This makes rebuilds faster. Never put passwords or API keys in Dockerfiles - use environment variables instead.

---

## Container Registries

**What is a Registry?**

A place to store and share container images. Like GitHub for containers.

**Popular Registries:**
- **Docker Hub**: Public registry, free for public images
- **GitHub Container Registry**: Integrated with GitHub
- **Google Container Registry**: Part of Google Cloud
- **Amazon ECR**: Part of AWS

**Using Registries:**
```bash
# Pull an image
podman pull python:3.11-slim

# Tag your image
podman tag my-app:latest username/my-app:latest

# Push to registry
podman push username/my-app:latest

# Pull from registry
podman pull username/my-app:latest
```

**Speaker Notes:**
Registries let you share container images. When you run `podman pull python:3.11-slim`, it downloads from Docker Hub. You can push your own images to registries so others can use them, or so you can deploy them to servers. Most registries are free for public images. Private images usually require a paid account, but GitHub offers free private container storage.

---

## Real-World Container Use Cases

**Development:**
- Consistent environment across team
- Easy onboarding for new developers
- Test with different Python versions

**Testing:**
- Run tests in clean environment
- Test on different OS configurations
- Automated CI/CD pipelines

**Deployment:**
- Deploy to any cloud provider
- Scale applications easily
- Roll back to previous versions
- Microservices architecture

**Data Science:**
- Reproducible analysis
- Share analysis environments
- Deploy models as APIs
- Run experiments in isolation

**Speaker Notes:**
Containers are used everywhere in modern software development. For development, they ensure everyone has the same environment. For testing, they provide clean, reproducible test environments. For deployment, they make it easy to run your application anywhere. In data science, they ensure your analysis is reproducible and make it easy to deploy models as web services.

---

## Practical Exercise: Build Your First Container

**Create a Simple Python App:**

```python
# app.py
import pandas as pd
import sys

def analyze_data(filename):
    df = pd.read_csv(filename)
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"\nSummary:\n{df.describe()}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_data(sys.argv[1])
    else:
        print("Usage: python app.py <data.csv>")
```

**Create Dockerfile:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install pandas
COPY app.py .
CMD ["python", "app.py"]
```

**Build and Run:**
```bash
podman build -t data-analyzer .
podman run -v $(pwd):/app data-analyzer data.csv
```

**Speaker Notes:**
Let's build a real container. This Python script analyzes a CSV file using pandas. The Dockerfile starts with Python 3.11, installs pandas, copies our script, and sets it as the default command. We build the image, then run it with our data directory mounted. The container has pandas installed even if your machine doesn't. This is the power of containers - consistent, reproducible environments.

---

## Debugging Containers

**Common Issues:**

**Container won't start:**
```bash
# Check logs
podman logs <container-id>

# Run interactively to debug
podman run -it my-app /bin/bash
```

**Can't access files:**
```bash
# Check volume mounts
podman inspect <container-id>

# Verify paths
podman run -it -v $(pwd):/app my-app ls /app
```

**Port not accessible:**
```bash
# Check port mapping
podman ps

# Verify application is listening
podman run -p 8000:8000 my-app
```

**Image build fails:**
```bash
# Build with verbose output
podman build --no-cache -t my-app .

# Check Dockerfile syntax
```

**Speaker Notes:**
When containers don't work, start with the logs - they usually tell you what's wrong. If the container won't start, run it interactively with /bin/bash to explore inside. If files aren't accessible, check your volume mounts. If ports don't work, verify the mapping and that your app is listening on 0.0.0.0, not localhost. Building with --no-cache forces a fresh build, which can help with caching issues.

---

## Git + Containers: Perfect Together

**Why They Work Well:**

**Git tracks:**
- Source code
- Dockerfiles
- Configuration
- Documentation

**Containers provide:**
- Consistent environment
- Reproducible builds
- Easy deployment
- Isolation

**Workflow:**
1. Write code and Dockerfile
2. Commit to Git
3. Build container image
4. Test in container
5. Push code to GitHub
6. Push image to registry
7. Deploy container

**Speaker Notes:**
Git and containers complement each other perfectly. Git tracks your code and Dockerfile. Containers ensure that code runs the same way everywhere. Together, they provide complete reproducibility - anyone can clone your repo, build your container, and run your code exactly as you did. This is the foundation of modern DevOps and data science workflows.

---

## Assignment 1 Reminder

**Due:** Next week (before Week 4 class at 6:00 PM)

**What's Due:**
- NASA web server log analysis
- 4 bash scripts (download, analyze, report, pipeline)
- Comprehensive analysis report
- Pull request submission

**Tips:**
- Start early if you haven't already
- Test with small data samples first
- Use AI assistants for bash syntax help
- Verify your results are correct
- Document your approach

**Getting Help:**
- Office hours
- Slack #homework-help channel
- Course examples in week-2/

**Speaker Notes:**
Assignment 1 is due next week. If you haven't started, start now. The assignment is substantial because you have AI assistants to help. Use them for syntax and debugging, but make sure you understand the logic. Test your scripts thoroughly - bash can be unforgiving. Come to office hours if you're stuck. The skills you're learning - bash scripting, data processing, Git workflows - are fundamental to data science.

---

## Key Takeaways

**Git Workflows:**
- Branches isolate work and enable parallel development
- Pull requests enable code review and collaboration
- Merge conflicts are normal and manageable
- Forking enables contributing to any project

**Containerization:**
- Containers solve the "works on my machine" problem
- Dockerfiles are recipes for building environments
- Volume mounting connects containers to your files
- Containers are fundamental to modern deployment

**Together:**
- Git tracks code, containers run it consistently
- Both are essential professional skills
- Practice makes perfect

**Speaker Notes:**
Today we covered two fundamental technologies: advanced Git workflows and containerization. Git workflows enable team collaboration. Containers enable consistent deployment. Together, they form the foundation of modern software development. These skills take practice - the more you use them, the more natural they become. Don't worry if it feels complex now. By the end of the course, these will be second nature.

---

## Resources and Next Steps

**Git:**
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

**Containerization:**
- [Podman Documentation](https://docs.podman.io/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Container Best Practices](https://docs.docker.com/develop/dev-best-practices/)

**Course Materials:**
- Week 3 examples in course repository
- Git collaboration exercises
- Container building tutorials

**For Next Week:**
- Data acquisition through APIs and web scraping
- Beautiful Soup, requests, and AI-assisted code generation
- Assignment 1 due before class!

**Practice:**
- Contribute to open source projects
- Containerize your own projects
- Practice resolving merge conflicts