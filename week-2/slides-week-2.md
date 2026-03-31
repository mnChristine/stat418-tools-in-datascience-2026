# STAT 418: Tools in Data Science
## Week 2: Data Science in the Command Line

**Instructor:** Nate Langholz  
**Date:** April 7, 2026

---

## Today's Agenda

1. **Unix Philosophy & History** - Why the command line matters
2. **File System Navigation** - Moving around efficiently
3. **Text Processing Tools** - grep, sed, awk
4. **Building Data Pipelines** - Chaining commands with pipes
5. **Bash Scripting Fundamentals** - Automating workflows
6. **Git Workflows** - Collaboration patterns
7. **Assignment 1 Overview** - Your first major project

**Where to Run Commands:**
- Use **VSCode's integrated terminal** (View > Terminal or Ctrl+`)
- Or your system terminal (Terminal on Mac, Git Bash on Windows)
- All examples are in the course repository under `week-2/examples/`

**Speaker Notes:**
Today we dive into the command line - the foundation of modern data science workflows. By the end of class, you'll understand why command line tools are so powerful and how to use them for data processing. All commands today should be run in VSCode's integrated terminal - it's already set up from Week 1 and works the same on Mac and Windows.

---

## Why the Command Line?

**The Reality of Data Science Work**

Most production data science happens on Linux servers without graphical interfaces. Cloud computing, data pipelines, and automated workflows all rely on command line tools.

**Key Advantages:**
- **Speed**: Process gigabytes of data in seconds
- **Composability**: Chain tools together like building blocks
- **Automation**: Scripts run without human intervention
- **Remote Access**: Work on servers anywhere in the world
- **Reproducibility**: Scripts document exactly what you did

**The Bottom Line:**
If you want to work in data science professionally, command line proficiency is not optional. Every production system, every cloud deployment, every data pipeline - they all require these skills.

**Speaker Notes:**
The command line might seem old-fashioned, but it's actually one of the most efficient ways to work with data. When you deploy a model to production, it runs on a Linux server. When you process large datasets, you use command line tools. This is the foundation of reproducible, automated data science.

---

## The Unix Philosophy

**Core Principles from the 1970s (Still Relevant Today)**

1. **Do one thing well**: Each tool has a single, focused purpose
2. **Work together**: Tools can be combined in unexpected ways
3. **Text streams**: Universal interface for data exchange
4. **Composability**: Build complex workflows from simple parts

**Example Pipeline:**
```bash
cat data.csv | grep "2026" | cut -d',' -f2 | sort | uniq -c
```

Each tool does one thing: read file, filter rows, extract column, sort, count unique values. Together they form a powerful data processing pipeline.

**Why This Matters:**
This is exactly like modern software engineering principles - microservices, single responsibility, composability. Unix developers figured this out 50 years ago, and it's more relevant than ever.

**Speaker Notes:**
The Unix philosophy is simple: build small tools that do one thing really well, then combine them. Text is the universal interface - if every tool can read and write text, any tool can work with any other tool. This composability is why Unix-based systems dominate data science and software development.

---

## File System Structure

**Unix File System Hierarchy**

```
/                    # Root directory
├── home/           # User home directories
│   └── username/   # Your home directory (~)
├── usr/            # User programs and data
│   ├── bin/        # User binaries
│   └── local/      # Locally installed software
├── etc/            # System configuration files
├── var/            # Variable data (logs, databases)
└── tmp/            # Temporary files
```

**Key Concepts:**
- Everything is a file (even devices and processes)
- Paths: absolute (`/home/user/file.txt`) vs relative (`../file.txt`)
- Home directory: `~` or `$HOME`
- Current directory: `.`
- Parent directory: `..`

**Speaker Notes:**
Unlike Windows with drive letters, Unix systems have a single root directory `/` and everything branches from there. Understanding paths (absolute vs relative) is essential for writing scripts that work correctly. The tilde `~` is a shortcut for your home directory.

---

## Essential Navigation Commands

**Moving Around the File System**

```bash
pwd                 # Print working directory
cd /path/to/dir    # Change directory
cd ~               # Go to home directory
cd ..              # Go up one level
cd -               # Go to previous directory

ls                 # List files
ls -la             # List all files with details
ls -lh             # Human-readable file sizes
```

**Finding Files:**
```bash
find . -name "*.csv"              # Find CSV files
find . -type f -mtime -7          # Files modified in last 7 days
find . -size +100M                # Files larger than 100MB
```

**Pro Tip:** Use tab completion! Start typing and press Tab to complete filenames and directory names. This saves time and prevents typos.

**Speaker Notes:**
These are the commands you'll use constantly. `pwd` tells you where you are, `cd` moves you around, `ls` shows what's there. The `find` command is incredibly powerful for searching large directory structures. Master tab completion - it will save you hours of typing.

---

## File Operations

**Creating and Manipulating Files**

```bash
touch file.txt              # Create empty file
mkdir data                  # Create directory
mkdir -p data/raw/2026     # Create nested directories

cp source.txt dest.txt      # Copy file
cp -r dir1/ dir2/          # Copy directory recursively
mv old.txt new.txt         # Move/rename file
rm file.txt                # Remove file
rm -r directory/           # Remove directory recursively
```

**Viewing Files:**
```bash
cat file.txt               # Display entire file
less file.txt              # Page through file (q to quit)
head -n 20 file.txt        # First 20 lines
tail -n 20 file.txt        # Last 20 lines
tail -f logfile.txt        # Follow file as it grows
```

**⚠️ Warning:** `rm` has no undo! When you delete something, it's gone. Be especially careful with `rm -r`.

**Speaker Notes:**
These are your basic file manipulation commands. `mkdir -p` creates parent directories as needed - very handy in scripts. For viewing files, use `less` for anything large - it doesn't load the entire file into memory. `tail -f` is essential for watching log files in real-time.

---

## Pipes and Redirection

**Connecting Commands Together**

**Redirection:**
```bash
command > file.txt          # Redirect output to file (overwrite)
command >> file.txt         # Append output to file
command < input.txt         # Read input from file
command 2> errors.txt       # Redirect errors to file
command &> all.txt          # Redirect both output and errors
```

**Pipes:**
```bash
command1 | command2         # Pipe output of command1 to command2
command1 | command2 | command3  # Chain multiple commands
```

**Examples:**
```bash
# Count lines in all CSV files
find . -name "*.csv" | wc -l

# Get unique values from a column
cat data.csv | cut -d',' -f2 | sort | uniq
```

**Speaker Notes:**
This is where the Unix philosophy really shines. The pipe symbol `|` connects the output of one command to the input of another. You can chain as many commands as you want, building sophisticated data processing pipelines from simple tools. Redirection lets you save results to files.

---

## Text Processing: grep

**Search for Patterns in Text**

```bash
# Basic usage
grep "pattern" file.txt              # Find lines containing pattern
grep -i "pattern" file.txt           # Case-insensitive search
grep -v "pattern" file.txt           # Invert match (lines NOT containing)
grep -c "pattern" file.txt           # Count matching lines
grep -n "pattern" file.txt           # Show line numbers

# Regular expressions
grep "^Error" logfile.txt            # Lines starting with "Error"
grep "Error$" logfile.txt            # Lines ending with "Error"
grep "[0-9]\{3\}-[0-9]\{4\}" file.txt  # Phone numbers (###-####)

# Recursive search
grep -r "TODO" .                     # Search all files in directory
grep -r "import pandas" --include="*.py"  # Search only Python files
```

**Speaker Notes:**
`grep` is one of the most useful command line tools. It searches for patterns in text files. Basic usage is simple, but it becomes incredibly powerful with regular expressions. The `-r` flag searches recursively through directories - essential for searching codebases.

---

## Real Example: Analyzing Huckleberry Finn

**Download and Analyze a Book from Project Gutenberg**

```bash
# Download The Adventures of Huckleberry Finn
curl -o huck_finn.txt https://www.gutenberg.org/files/76/76-0.txt

# How many lines?
wc -l huck_finn.txt
# Output: 12361 huck_finn.txt

# How many times is "river" mentioned?
grep -i "river" huck_finn.txt | wc -l
# Output: 87

# Show lines with "river" and line numbers
grep -in "river" huck_finn.txt | head -5
# Output:
# 123:down the river, and we would take the canoe and go out to where the
# 145:the river, and we would take the canoe and go out to where the
# 289:along down the river, and we would take the canoe and go out to where
```

**Speaker Notes:**
Let's work with real data! Project Gutenberg has thousands of free books in plain text. We download Huckleberry Finn with `curl`, then analyze it with command line tools. With one command, we count how many times "river" is mentioned. This same approach works for any text data - logs, CSV files, source code.

---

## Text Processing: sed

**Stream Editor for Text Transformation**

```bash
# Substitute text
sed 's/old/new/' file.txt              # Replace first occurrence per line
sed 's/old/new/g' file.txt             # Replace all occurrences (global)
sed 's/old/new/gi' file.txt            # Case-insensitive global replace

# Delete lines
sed '/pattern/d' file.txt              # Delete lines matching pattern
sed '1d' file.txt                      # Delete first line
sed '1,10d' file.txt                   # Delete lines 1-10

# Extract lines
sed -n '5,10p' file.txt                # Print lines 5-10
sed -n '/pattern/p' file.txt           # Print lines matching pattern
```

**Example with Huckleberry Finn:**
```bash
# Replace "river" with "RIVER"
sed 's/river/RIVER/gi' huck_finn.txt | grep "RIVER" | head -3

# Remove chapter headers
sed '/^CHAPTER/d' huck_finn.txt > huck_finn_no_chapters.txt

# Extract just the first chapter
sed -n '/^CHAPTER I\./,/^CHAPTER II\./p' huck_finn.txt
```

**Speaker Notes:**
`sed` is a stream editor that transforms text as it flows through. The most common use is substitution - replacing patterns. You can also delete lines or extract portions of files. The syntax `s/old/new/g` means "substitute old with new globally". This is incredibly powerful for text transformation.

---

## Text Processing: awk

**Pattern Scanning and Processing Language**

```bash
# Print specific columns
awk '{print $1}' file.txt              # Print first column
awk '{print $1, $3}' file.txt          # Print columns 1 and 3
awk -F',' '{print $2}' data.csv        # Use comma as delimiter

# Filtering
awk '$3 > 100' data.txt                # Print lines where column 3 > 100
awk '$1 == "Error"' logfile.txt        # Print lines where column 1 is "Error"

# Calculations
awk '{sum += $1} END {print sum}' numbers.txt     # Sum first column
awk '{sum += $1; count++} END {print sum/count}' numbers.txt  # Average
```

**Example with CSV data:**
```bash
# Sample CSV: name,age,city
# Extract just names
awk -F',' '{print $1}' people.csv

# People over 25
awk -F',' '$2 > 25 {print $1, $3}' people.csv

# Average age (skip header)
awk -F',' 'NR>1 {sum += $2; count++} END {print sum/count}' people.csv
```

**Speaker Notes:**
`awk` is a full programming language for text processing. It's particularly good with columnar data like CSV files. By default, it splits lines into columns based on whitespace. Use `-F','` for CSV files. The `END` block runs after all lines are processed - perfect for totals or averages.

---

## Building Data Pipelines

**Combining Tools for Complex Analysis**

```bash
# Download, extract, and analyze in one pipeline
curl -s "https://www.gutenberg.org/files/76/76-0.txt" | \
  grep -i "mississippi" | \
  wc -l

# Process CSV data
cat sales.csv | \
  grep "2026" | \
  cut -d',' -f3 | \
  sort -n | \
  tail -10

# Word frequency analysis
cat huck_finn.txt | \
  tr '[:upper:]' '[:lower:]' | \
  tr -s '[:space:]' '\n' | \
  grep -v '^$' | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -20
```

**Speaker Notes:**
This is where everything comes together. By chaining simple tools with pipes, we build sophisticated data processing pipelines. The word frequency example: convert to lowercase, split into words (one per line), remove empty lines, sort, count unique words, sort by frequency, show top 20. This is a complete text analysis in one command!

---

## Bash Scripting Basics

**Your First Script**

```bash
#!/bin/bash
# analyze_text.sh - Analyze a text file

# Check if file argument provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

FILE=$1

# Check if file exists
if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found"
    exit 1
fi

# Analysis
echo "File: $FILE"
echo "Lines: $(wc -l < "$FILE")"
echo "Words: $(wc -w < "$FILE")"
echo "Characters: $(wc -c < "$FILE")"
echo ""
echo "Top 10 most common words:"
cat "$FILE" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | \
  grep -v '^$' | sort | uniq -c | sort -rn | head -10
```

**To run:** `chmod +x analyze_text.sh && ./analyze_text.sh huck_finn.txt`

**Speaker Notes:**
A bash script is just a file containing commands you want to run together. The shebang `#!/bin/bash` tells the system to use bash. `$1`, `$2` are command line arguments. Always check inputs and quote variables. This script does basic text analysis - a template you can adapt for your own tasks.

---

## Bash Script: Variables and Loops

**Variables:**
```bash
#!/bin/bash

# Variable assignment (no spaces around =)
NAME="Alice"
AGE=25
OUTPUT_DIR="results"

# Using variables
echo "Name: $NAME"
echo "Age: $AGE"

# Command substitution
CURRENT_DATE=$(date +%Y-%m-%d)
FILE_COUNT=$(ls *.txt | wc -l)

echo "Date: $CURRENT_DATE"
echo "Text files: $FILE_COUNT"
```

**Loops:**
```bash
#!/bin/bash

# Loop over files
for file in *.csv; do
    echo "Processing $file..."
    lines=$(wc -l < "$file")
    echo "  Lines: $lines"
done

# Loop over numbers
for i in {1..5}; do
    echo "Iteration $i"
done

# While loop
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done
```

**Speaker Notes:**
Variables in bash have quirks: no spaces around `=`, use `$` to access values, always quote to handle spaces. Command substitution `$(command)` captures output. Loops let you process multiple files or repeat operations. The `for file in *.csv` pattern is very common for batch processing.

---

## Bash Script: Functions

**Organizing Code with Functions**

```bash
#!/bin/bash

# Function definition
analyze_file() {
    local file=$1
    
    if [ ! -f "$file" ]; then
        echo "Error: File not found"
        return 1
    fi
    
    echo "Analyzing $file..."
    echo "Lines: $(wc -l < "$file")"
    echo "Words: $(wc -w < "$file")"
    
    return 0
}

# Function with multiple parameters
process_csv() {
    local input=$1
    local output=$2
    local column=$3
    
    echo "Extracting column $column from $input to $output"
    cut -d',' -f"$column" "$input" > "$output"
}

# Using functions
analyze_file "data.txt"
process_csv "sales.csv" "prices.txt" 3

# Check return value
if analyze_file "missing.txt"; then
    echo "Analysis successful"
else
    echo "Analysis failed"
fi
```

**Speaker Notes:**
Functions organize your code and avoid repetition. Inside a function, `$1`, `$2` are the function's arguments. Use `local` for variables that only exist inside the function. Functions can return exit codes (0 = success, non-zero = error). This is the Unix philosophy applied to scripting - small, focused functions that do one thing well.

---

## Error Handling and Debugging

**Writing Robust Scripts**

```bash
#!/bin/bash

# Exit on error
set -e

# Exit on undefined variable
set -u

# Exit on pipe failure
set -o pipefail

# All together (best practice)
set -euo pipefail

# Custom error handling
download_file() {
    local url=$1
    local output=$2
    
    if ! curl -f -o "$output" "$url"; then
        echo "Error: Failed to download $url" >&2
        return 1
    fi
    
    echo "Downloaded $url to $output"
    return 0
}

# Trap errors
trap 'echo "Error on line $LINENO"' ERR
```

**Debugging:**
```bash
# Run with debug output
bash -x script.sh

# Debug specific sections
set -x  # Enable debug output
# ... commands to debug ...
set +x  # Disable debug output
```

**Speaker Notes:**
Error handling is crucial for robust scripts. `set -euo pipefail` is a best practice - it makes scripts exit on errors, undefined variables, and pipe failures. For debugging, `bash -x` shows each command before it runs. Always test scripts with invalid inputs and edge cases!

---

## Real-World Example: Data Pipeline Script

**Complete Pipeline for Downloading and Analyzing Text**

```bash
#!/bin/bash
set -euo pipefail

# Configuration
TOPIC="climate change"
OUTPUT_DIR="articles"
DATE=$(date +%Y-%m-%d)

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Download articles (using Project Gutenberg as demo)
echo "Downloading articles..."
curl -s "https://www.gutenberg.org/files/76/76-0.txt" > "$OUTPUT_DIR/article1.txt"
curl -s "https://www.gutenberg.org/files/1342/1342-0.txt" > "$OUTPUT_DIR/article2.txt"

# Analyze each article
for article in "$OUTPUT_DIR"/*.txt; do
    echo "Analyzing $(basename "$article")..."
    
    # Count mentions of topic
    mentions=$(grep -ic "$TOPIC" "$article" || true)
    echo "  Mentions of '$TOPIC': $mentions"
    
    # Word count
    words=$(wc -w < "$article")
    echo "  Total words: $words"
    
    # Extract sentences mentioning topic
    grep -i "$TOPIC" "$article" > "$OUTPUT_DIR/$(basename "$article" .txt)_mentions.txt" || true
done

# Generate summary report
echo "Generating summary report..."
{
    echo "Analysis Report - $DATE"
    echo "Topic: $TOPIC"
    echo "========================"
    echo ""
    
    for article in "$OUTPUT_DIR"/*.txt; do
        [ -f "$article" ] || continue
        echo "File: $(basename "$article")"
        echo "Lines: $(wc -l < "$article")"
        echo "Words: $(wc -w < "$article")"
        echo ""
    done
} > "$OUTPUT_DIR/summary_$DATE.txt"

echo "Analysis complete! Results in $OUTPUT_DIR/"
```

**Speaker Notes:**
This is a complete data pipeline demonstrating everything we've learned. The pattern - configure, collect, process, report - is common in data science workflows. Variables at the top for easy modification, error handling with `set -euo pipefail`, loops for batch processing, and a summary report. You can adapt this template for your own projects.

---

## Git Workflows for Collaboration

**Basic Workflow**

```bash
# Clone repository
git clone https://github.com/username/repo.git
cd repo

# Create feature branch
git checkout -b feature/my-analysis

# Make changes, then stage and commit
git add analysis.sh
git commit -m "Add data analysis script"

# Push to GitHub
git push origin feature/my-analysis

# Create pull request on GitHub
```

**Keeping Your Fork Updated:**
```bash
# Add upstream remote (original repo)
git remote add upstream https://github.com/original/repo.git

# Fetch upstream changes
git fetch upstream

# Merge upstream changes into your main branch
git checkout main
git merge upstream/main

# Push updated main to your fork
git push origin main
```

**Speaker Notes:**
Git workflows are essential for collaboration. Always work on a feature branch, never directly on main. Commit messages should be descriptive. When working with a forked repository (like the course repo), keep your fork updated by adding the original as an "upstream" remote. This workflow is how professional software development works.

---

## Assignment 1 Overview

**Due:** Two weeks from today (before Week 4 class)

**Objective:** Build a command line data processing pipeline

**Requirements:**
1. Download data from multiple sources (APIs, web scraping, or public datasets)
2. Process and clean the data using bash scripts
3. Perform analysis and generate insights
4. Create visualizations or summary reports
5. Document your work thoroughly
6. Submit via pull request with proper Git workflow

**Complexity Note:**
This assignment is more substantial than traditional homework because you have AI assistants to help with implementation. However:
- **You're responsible** for the architecture and logic
- **You must understand** what your code does
- **You must verify** correctness and handle edge cases
- AI can help you write code faster, but **you own the results**

**Speaker Notes:**
Assignment 1 is your chance to apply everything we've learned. The assignment is intentionally challenging because you have AI assistants. Use AI to help with bash syntax, but YOU design the pipeline, YOU decide what analysis to perform, YOU verify correctness. Think of AI as a knowledgeable assistant who can write code quickly but doesn't understand your specific problem.

---

## Key Takeaways

**What You Learned Today:**
1. The Unix philosophy: small, composable tools
2. Essential command line tools: grep, sed, awk, cut, sort, uniq
3. Building data pipelines with pipes
4. Writing bash scripts for automation
5. Error handling and debugging
6. Git workflows for collaboration

**Why It Matters:**
- Command line skills are essential for professional data science
- These tools are faster and more powerful than GUIs for many tasks
- Bash scripts enable reproducible, automated workflows
- These skills transfer to any Unix-based system (Linux, macOS, cloud servers)

**Next Steps:**
- Practice with the examples in the course repository
- Start thinking about Assignment 1
- Experiment with command line tools on your own data
- Use AI assistants to help, but make sure you understand the commands

**Speaker Notes:**
These skills might feel overwhelming at first, but they become second nature with practice. Don't try to memorize every command - learn to look things up efficiently and use AI assistants. The command line has a steep learning curve but enormous payoff. Once you're comfortable, you'll be significantly more productive.

---

## Resources and Next Steps

**Practice Resources:**
- [Command Line Challenge](https://cmdchallenge.com/) - Interactive exercises
- [Explain Shell](https://explainshell.com/) - Understand any command
- [Bash Scripting Tutorial](https://www.shellscript.sh/) - Comprehensive guide
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - Best practices

**Course Materials:**
- Week 2 examples in course repository
- Assignment 1 details and starter code
- Office hours for questions and help

**For Next Week:**
- More command line tools and Python project management with uv
- Introduction to containerization
- Continue working on Assignment 1

**Questions?**

**Speaker Notes:**
Command Line Challenge is great for practice - it gives you problems to solve and checks your solutions. Explain Shell breaks down complex commands. The course repository has all today's examples - clone it and experiment. Assignment 1 details are in the repository. Next week we'll go deeper into Git workflows and start data acquisition techniques. See you then!