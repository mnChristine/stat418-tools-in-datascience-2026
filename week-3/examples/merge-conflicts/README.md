# Merge Conflicts: Understanding and Resolving

This example teaches you how to handle merge conflicts confidently.

## Setup

Open VSCode's integrated terminal and navigate to this directory:

```bash
cd week-3/examples/merge-conflicts
```

## Overview

Merge conflicts happen when:
- Two people edit the same lines of code
- One person deletes a file another person modified
- Changes can't be automatically merged

**Don't panic!** Conflicts are normal and easy to resolve once you understand them.

## Understanding Conflict Markers

When Git can't automatically merge changes, it adds conflict markers to show both versions:

```python
<<<<<<< HEAD
# Your current branch's version
def calculate_total(items):
    return sum(items)
=======
# The incoming branch's version
def calculate_total(items):
    return sum(item * 1.1 for item in items)
>>>>>>> feature/add-markup
```

**Markers explained:**
- `<<<<<<< HEAD` - Start of your current branch's version
- `=======` - Separator between versions
- `>>>>>>> branch-name` - End of incoming branch's version

## Example 1: Simple Conflict

### Create the Conflict

**1. Create a test repository:**
```bash
mkdir conflict-practice
cd conflict-practice
git init
```

**2. Create initial file:**
```bash
cat > calculator.py << 'EOF'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
EOF

git add calculator.py
git commit -m "Initial calculator functions"
```

**3. Create a branch and modify:**
```bash
# Create feature branch
git checkout -b feature/add-divide

# Modify the file
cat > calculator.py << 'EOF'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
EOF

git add calculator.py
git commit -m "Add divide function with error handling"
```

**4. Go back to main and make different changes:**
```bash
# Switch to main
git checkout main

# Make different changes to same file
cat > calculator.py << 'EOF'
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b
EOF

git add calculator.py
git commit -m "Add docstrings to functions"
```

**5. Try to merge - this creates a conflict:**
```bash
git merge feature/add-divide
# Auto-merging calculator.py
# CONFLICT (content): Merge conflict in calculator.py
# Automatic merge failed; fix conflicts and then commit the result.
```

### Resolve the Conflict

**1. Check status:**
```bash
git status
# On branch main
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#         both modified:   calculator.py
```

**2. Open the file and see the conflict:**
```python
def add(a, b):
<<<<<<< HEAD
    """Add two numbers."""
=======
>>>>>>> feature/add-divide
    return a + b

def subtract(a, b):
<<<<<<< HEAD
    """Subtract b from a."""
=======
>>>>>>> feature/add-divide
    return a - b

def multiply(a, b):
<<<<<<< HEAD
    """Multiply two numbers."""
=======
>>>>>>> feature/add-divide
    return a * b
<<<<<<< HEAD
=======

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
>>>>>>> feature/add-divide
```

**3. Resolve by keeping both changes:**
```python
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**4. Mark as resolved and commit:**
```bash
# Stage the resolved file
git add calculator.py

# Check status
git status
# On branch main
# All conflicts fixed but you are still merging.
#   (use "git commit" to conclude merge)

# Commit the merge
git commit -m "Merge feature/add-divide: combine docstrings and divide function"
```

## Example 2: Conflicting Logic

### The Scenario

Two developers implement the same feature differently.

**Developer A's version:**
```python
def calculate_discount(price, customer_type):
    if customer_type == "premium":
        return price * 0.8  # 20% discount
    return price
```

**Developer B's version:**
```python
def calculate_discount(price, customer_type):
    discounts = {
        "premium": 0.2,
        "regular": 0.05,
        "new": 0.1
    }
    discount = discounts.get(customer_type, 0)
    return price * (1 - discount)
```

### Resolution Strategy

**Option 1: Choose one version**
```python
# Keep Developer B's more flexible approach
def calculate_discount(price, customer_type):
    discounts = {
        "premium": 0.2,
        "regular": 0.05,
        "new": 0.1
    }
    discount = discounts.get(customer_type, 0)
    return price * (1 - discount)
```

**Option 2: Combine best of both**
```python
# Use B's structure with A's explicit premium handling
def calculate_discount(price, customer_type):
    """Calculate discount based on customer type."""
    discounts = {
        "premium": 0.2,   # 20% for premium (from A)
        "regular": 0.05,  # 5% for regular
        "new": 0.1        # 10% for new customers
    }
    discount = discounts.get(customer_type, 0)
    return price * (1 - discount)
```

## Example 3: Data File Conflicts

### The Scenario

Two people modify a CSV file.

**Person A adds:**
```csv
name,age,city
Alice,25,NYC
Bob,30,LA
Charlie,35,Chicago
```

**Person B adds:**
```csv
name,age,city
Alice,25,NYC
Bob,30,LA
David,28,Boston
```

### Conflict:
```csv
name,age,city
Alice,25,NYC
Bob,30,LA
<<<<<<< HEAD
Charlie,35,Chicago
=======
David,28,Boston
>>>>>>> feature/add-david
```

### Resolution:
```csv
name,age,city
Alice,25,NYC
Bob,30,LA
Charlie,35,Chicago
David,28,Boston
```

## Example 4: Configuration Conflicts

### The Scenario

Two developers modify configuration settings.

**Developer A:**
```python
config = {
    "database": "postgresql",
    "host": "localhost",
    "port": 5432,
    "debug": True
}
```

**Developer B:**
```python
config = {
    "database": "postgresql",
    "host": "db.example.com",
    "port": 5432,
    "timeout": 30
}
```

### Conflict:
```python
config = {
    "database": "postgresql",
<<<<<<< HEAD
    "host": "localhost",
    "port": 5432,
    "debug": True
=======
    "host": "db.example.com",
    "port": 5432,
    "timeout": 30
>>>>>>> feature/add-timeout
}
```

### Resolution:
```python
# Keep both settings, use environment-appropriate host
config = {
    "database": "postgresql",
    "host": "localhost",  # Will be overridden in production
    "port": 5432,
    "debug": True,
    "timeout": 30
}
```

## Conflict Resolution Strategies

### Strategy 1: Accept Theirs

```bash
# Accept all changes from the incoming branch
git checkout --theirs <file>
git add <file>
```

### Strategy 2: Accept Ours

```bash
# Keep all changes from current branch
git checkout --ours <file>
git add <file>
```

### Strategy 3: Manual Resolution

```bash
# Edit the file manually
nano <file>

# Remove conflict markers
# Combine changes as needed
# Save file

# Stage resolved file
git add <file>
```

### Strategy 4: Use a Merge Tool

```bash
# Configure merge tool (one time)
git config --global merge.tool vimdiff

# Use merge tool
git mergetool
```

## Common Conflict Patterns

### Pattern 1: Whitespace Conflicts

**Conflict:**
```python
<<<<<<< HEAD
def hello():
    print("Hello")
=======
def hello():
	print("Hello")  # Tab instead of spaces
>>>>>>> feature/formatting
```

**Resolution:**
```python
# Choose consistent style (spaces)
def hello():
    print("Hello")
```

### Pattern 2: Import Conflicts

**Conflict:**
```python
<<<<<<< HEAD
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
=======
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
>>>>>>> feature/add-scaling
```

**Resolution:**
```python
# Keep both imports, sort alphabetically
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

### Pattern 3: Function Signature Conflicts

**Conflict:**
```python
<<<<<<< HEAD
def process_data(filename, encoding='utf-8'):
=======
def process_data(filename, delimiter=','):
>>>>>>> feature/add-delimiter
```

**Resolution:**
```python
# Combine both parameters
def process_data(filename, encoding='utf-8', delimiter=','):
```

## Preventing Conflicts

### Best Practices

**1. Pull frequently:**
```bash
# Start each day by pulling
git checkout main
git pull origin main
```

**2. Keep branches short-lived:**
```bash
# Merge feature branches quickly
# Don't let them diverge too much
```

**3. Communicate with team:**
```bash
# Let team know what files you're working on
# Coordinate on major changes
```

**4. Make small, focused commits:**
```bash
# Easier to resolve conflicts in small commits
git add specific_file.py
git commit -m "Specific change"
```

**5. Rebase regularly:**
```bash
# Keep feature branch updated with main
git checkout feature/my-work
git rebase main
```

## Testing After Resolution

**Always test after resolving conflicts:**

```bash
# Run tests
python -m pytest

# Run linter
flake8 .

# Try running the application
python app.py

# If everything works
git add .
git commit -m "Resolve merge conflicts"
```

## Aborting a Merge

**If you want to start over:**

```bash
# Abort the merge
git merge --abort

# You're back to pre-merge state
git status
```

## Practice Exercises

### Exercise 1: Create and Resolve a Simple Conflict

```bash
# 1. Create a repository
mkdir practice
cd practice
git init

# 2. Create a file
echo "Line 1" > file.txt
git add file.txt
git commit -m "Initial commit"

# 3. Create a branch and modify
git checkout -b branch-a
echo "Line 2 from branch A" >> file.txt
git add file.txt
git commit -m "Add line from branch A"

# 4. Go back and make different change
git checkout main
echo "Line 2 from main" >> file.txt
git add file.txt
git commit -m "Add line from main"

# 5. Merge and resolve conflict
git merge branch-a
# Resolve the conflict
# Commit the resolution
```

### Exercise 2: Resolve a Code Conflict

Create a conflict in a Python function and resolve it by combining both improvements.

### Exercise 3: Resolve a Data Conflict

Create a conflict in a CSV file and resolve it by keeping all unique rows.

## Troubleshooting

### "I resolved the conflict but Git still shows it"

```bash
# Make sure you staged the file
git add <resolved-file>

# Check status
git status
```

### "I made a mistake in my resolution"

```bash
# Before committing
git checkout <file>  # Restore conflict markers
# Resolve again

# After committing
git reset --soft HEAD~1  # Undo commit, keep changes
# Resolve again
```

### "Too many conflicts, want to start over"

```bash
# Abort the merge
git merge --abort

# Try a different approach
git rebase main  # Or merge again later
```

## Resources

- [Git Merge Conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
- [Resolving Conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)
- [Git Merge Strategies](https://git-scm.com/docs/merge-strategies)