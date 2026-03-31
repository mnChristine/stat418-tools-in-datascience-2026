# Python + uv Setup Example

This example demonstrates how to set up a Python project using uv.

## What You'll Learn

- Create a virtual environment with uv
- Install packages
- Create a simple Python script
- Run your code

## Steps

### 1. Create Project Directory

```bash
mkdir my-first-project
cd my-first-project
```

### 2. Create Virtual Environment

```bash
uv venv
```

This creates a `.venv` directory with an isolated Python environment.

### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

You should see `(.venv)` at the start of your terminal prompt.

### 4. Install Packages

```bash
# Install pandas for data manipulation
uv pip install pandas

# Install multiple packages at once
uv pip install numpy matplotlib
```

### 5. Create a Python Script

Create a file called `analyze_data.py`:

```python
import pandas as pd
import numpy as np

# Create sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'score': [85, 92, 78, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Student Data:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

# Calculate average score
avg_score = df['score'].mean()
print(f"\nAverage Score: {avg_score:.2f}")
```

### 6. Run Your Script

```bash
python analyze_data.py
```

### 7. Create requirements.txt

Save your dependencies:

```bash
uv pip freeze > requirements.txt
```

This creates a file listing all installed packages.

### 8. Deactivate Environment

When you're done:

```bash
deactivate
```

## Try It Yourself

1. Follow the steps above
2. Modify `analyze_data.py` to add a new column
3. Calculate the maximum score
4. Create a new script that uses matplotlib to plot the data

## Common Issues

**Problem**: `uv: command not found`
- Make sure you completed the installation in STUDENT_SETUP.md
- Restart your terminal

**Problem**: Virtual environment won't activate
- Make sure you're in the correct directory
- Check that `.venv` folder exists

**Problem**: Package installation fails
- Make sure virtual environment is activated
- Check your internet connection

## Next Steps

- Try installing other packages (requests, beautifulsoup4, etc.)
- Create more complex Python scripts
- Learn about Python modules and imports