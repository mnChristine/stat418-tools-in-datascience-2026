# Git Workflow Example

This example demonstrates a basic Git workflow for version control.

## What You'll Learn

- Initialize a Git repository
- Stage and commit changes
- View commit history
- Create a .gitignore file
- Connect to GitHub (optional)

## Steps

### 1. Create a New Project

```bash
mkdir my-git-project
cd my-git-project
```

### 2. Initialize Git Repository

```bash
git init
```

This creates a hidden `.git` folder that tracks your changes.

### 3. Check Repository Status

```bash
git status
```

You should see "No commits yet" and "nothing to commit".

### 4. Create Your First File

```bash
echo "# My First Git Project" > README.md
echo "This is a test project to learn Git." >> README.md
```

### 5. Check Status Again

```bash
git status
```

You should see `README.md` listed as an "untracked file".

### 6. Stage the File

```bash
git add README.md
```

Or stage all files:

```bash
git add .
```

### 7. Check Status

```bash
git status
```

Now `README.md` should be listed under "Changes to be committed".

### 8. Commit Your Changes

```bash
git commit -m "Initial commit: Add README"
```

The `-m` flag lets you add a commit message inline.

### 9. View Commit History

```bash
git log
```

Or for a compact view:

```bash
git log --oneline
```

### 10. Make More Changes

```bash
echo "" >> README.md
echo "## Features" >> README.md
echo "- Version control with Git" >> README.md
echo "- Collaborative development" >> README.md
```

### 11. View Changes

```bash
git diff
```

This shows what changed since your last commit.

### 12. Stage and Commit

```bash
git add README.md
git commit -m "Add features section to README"
```

### 13. Create a .gitignore File

```bash
cat > .gitignore << EOF
# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF
```

### 14. Commit .gitignore

```bash
git add .gitignore
git commit -m "Add .gitignore file"
```

### 15. View Your History

```bash
git log --oneline --graph
```

## Common Git Commands

```bash
# Check status
git status

# Stage files
git add <filename>      # Stage specific file
git add .               # Stage all changes

# Commit changes
git commit -m "message"

# View history
git log
git log --oneline

# View changes
git diff                # Unstaged changes
git diff --staged       # Staged changes

# Undo changes
git restore <filename>  # Discard unstaged changes
git restore --staged <filename>  # Unstage file
```

## Connecting to GitHub (Optional)

If you want to push this to GitHub:

### 1. Create Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name it (e.g., "my-git-project")
4. Don't initialize with README (we already have one)
5. Click "Create repository"

### 2. Add Remote

```bash
git remote add origin https://github.com/YOUR_USERNAME/my-git-project.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Push to GitHub

```bash
git branch -M main
git push -u origin main
```

## Try It Yourself

1. Create a new file called `notes.txt`
2. Add some content to it
3. Stage and commit the file
4. Make changes to the file
5. View the diff
6. Commit the changes
7. View your commit history

## Common Issues

**Problem**: `git: command not found`
- Make sure you completed Git installation in STUDENT_SETUP.md
- Restart your terminal

**Problem**: "Please tell me who you are" error
- Run:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@ucla.edu"
  ```

**Problem**: Can't push to GitHub
- Make sure you created the repository on GitHub first
- Check that the remote URL is correct: `git remote -v`
- You may need to set up authentication (SSH keys or Personal Access Token)

## Best Practices

1. **Commit often** - Make small, focused commits
2. **Write clear messages** - Describe what and why, not how
3. **Use .gitignore** - Don't commit generated files or secrets
4. **Pull before push** - Always get latest changes first
5. **Review before commit** - Use `git diff` to check your changes

## Good Commit Messages

Good examples:
- "Add user authentication feature"
- "Fix bug in data processing pipeline"
- "Update README with installation instructions"

Bad examples:
- "Update"
- "Fix stuff"
- "asdfasdf"

## Next Steps

- Learn about branches: `git branch`, `git checkout`
- Learn about merging: `git merge`
- Practice with pull requests on GitHub
- Explore Git GUI tools (GitKraken, GitHub Desktop)