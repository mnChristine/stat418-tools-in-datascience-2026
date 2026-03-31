# Bash Basics: Command Line Fundamentals

This example demonstrates essential command line operations using real text data from Project Gutenberg.

## Getting Started

### Where to Run These Commands

You can run these bash commands in any of these terminals:

**Option 1: VSCode Integrated Terminal (Recommended)**
1. Open VSCode
2. Open the course repository folder (`File > Open Folder`)
3. Open the integrated terminal: `View > Terminal` or press `` Ctrl+` `` (backtick)
4. Navigate to this directory: `cd week-2/examples/bash-basics`

**Option 2: System Terminal**
- **macOS**: Open Terminal app (Applications > Utilities > Terminal)
- **Windows**: Open Command Prompt or PowerShell (search for "cmd" or "powershell")
- Navigate to this directory using `cd`

**Why VSCode Terminal?**
- Already in the right directory when you open the project
- Easy to switch between code and terminal
- Same terminal you'll use for Git commands
- Works the same on Mac and Windows

### Verify Your Setup

Before starting, verify you have the necessary tools:

```bash
# Check bash is available (should show version)
bash --version

# Check curl is available (for downloading files)
curl --version

# Check you're in the right directory
pwd
# Should show: .../stat418-tools-in-datascience-2026/week-2/examples/bash-basics
```

**Note for Windows users**: If you installed Git for Windows, you have Git Bash which provides Unix-like commands. Use Git Bash or the VSCode terminal for these examples.

## Overview

You'll learn:
- File system navigation
- File operations (create, copy, move, delete)
- Viewing and searching files
- Basic text processing with grep
- Pipes and redirection

## Example 1: Downloading and Exploring Text Data

Let's download a classic book from Project Gutenberg and explore it using command line tools.

```bash
# Download The Adventures of Huckleberry Finn
curl -o huck_finn.txt https://www.gutenberg.org/files/76/76-0.txt

# Check the file was created
ls -lh huck_finn.txt

# How many lines?
wc -l huck_finn.txt

# How many words?
wc -w huck_finn.txt

# How many characters?
wc -c huck_finn.txt

# All stats at once
wc huck_finn.txt
```

**Expected output:**
```
  12361  111908  600841 huck_finn.txt
```
This means: 12,361 lines, 111,908 words, 600,841 characters.

## Example 2: Viewing Files

```bash
# Display entire file (don't do this for large files!)
cat huck_finn.txt

# View first 20 lines
head -n 20 huck_finn.txt

# View last 20 lines
tail -n 20 huck_finn.txt

# Page through the file (press 'q' to quit, '/' to search)
less huck_finn.txt

# View specific line range (lines 100-110)
sed -n '100,110p' huck_finn.txt
```

## Example 3: Searching with grep

```bash
# Find all lines mentioning "river"
grep "river" huck_finn.txt

# Case-insensitive search
grep -i "river" huck_finn.txt

# Count how many lines mention "river"
grep -ic "river" huck_finn.txt

# Show line numbers
grep -in "river" huck_finn.txt | head -10

# Find lines that DON'T contain "the"
grep -v "the" huck_finn.txt | head -20

# Search for lines starting with "CHAPTER"
grep "^CHAPTER" huck_finn.txt

# Search for lines ending with a question mark
grep "?$" huck_finn.txt | head -10
```

## Example 4: Pipes and Redirection

```bash
# Save search results to a file
grep -i "mississippi" huck_finn.txt > mississippi_mentions.txt

# Count mentions of "Mississippi"
grep -i "mississippi" huck_finn.txt | wc -l

# Find and count mentions of "Tom"
grep -io "tom" huck_finn.txt | wc -l

# Get unique chapter titles
grep "^CHAPTER" huck_finn.txt | sort | uniq

# Find the 10 longest lines
awk '{print length, $0}' huck_finn.txt | sort -rn | head -10

# Extract just the chapter numbers
grep "^CHAPTER" huck_finn.txt | cut -d' ' -f2 | head -10
```

## Example 5: Working with Multiple Files

```bash
# Download another book (Pride and Prejudice)
curl -o pride_prejudice.txt https://www.gutenberg.org/files/1342/1342-0.txt

# Compare file sizes
ls -lh *.txt

# Count lines in all text files
wc -l *.txt

# Search for a word in all text files
grep -i "love" *.txt | head -20

# Count occurrences in each file
grep -ic "love" *.txt

# Find files containing "Elizabeth"
grep -l "Elizabeth" *.txt
```

## Example 6: Creating a Simple Analysis Script

Create a file called `analyze_book.sh`:

```bash
#!/bin/bash
# analyze_book.sh - Simple book analysis

if [ $# -eq 0 ]; then
    echo "Usage: $0 <book_file.txt>"
    exit 1
fi

BOOK=$1

if [ ! -f "$BOOK" ]; then
    echo "Error: File '$BOOK' not found"
    exit 1
fi

echo "Analyzing: $BOOK"
echo "===================="
echo "Lines: $(wc -l < "$BOOK")"
echo "Words: $(wc -w < "$BOOK")"
echo "Characters: $(wc -c < "$BOOK")"
echo ""
echo "Chapters: $(grep -c "^CHAPTER" "$BOOK")"
echo ""
echo "Most common words (top 10):"
cat "$BOOK" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | \
  grep -v '^$' | sort | uniq -c | sort -rn | head -10
```

Make it executable and run it:

```bash
chmod +x analyze_book.sh
./analyze_book.sh huck_finn.txt
```

## Example 7: File Organization

```bash
# Create a directory structure
mkdir -p books/american books/british

# Move books to appropriate directories
mv huck_finn.txt books/american/
mv pride_prejudice.txt books/british/

# List the directory structure
ls -R books/

# Find all text files recursively
find books/ -name "*.txt"

# Count total lines in all books
find books/ -name "*.txt" -exec wc -l {} \; | awk '{sum += $1} END {print sum}'
```

## Example 8: Cleaning Up

```bash
# Remove analysis results
rm -f mississippi_mentions.txt

# Remove books directory (be careful with rm -r!)
rm -r books/

# Or move to trash instead of deleting
mkdir -p ~/.trash
mv books/ ~/.trash/
```

## Practice Exercises

Try these on your own:

1. **Download a different book** from Project Gutenberg and analyze it
   - Find the URL at https://www.gutenberg.org/
   - Use `curl -o filename.txt URL`

2. **Find character mentions**: Count how many times main characters are mentioned
   ```bash
   grep -io "huck" huck_finn.txt | wc -l
   grep -io "tom" huck_finn.txt | wc -l
   ```

3. **Extract dialogue**: Find all lines containing quotation marks
   ```bash
   grep '"' huck_finn.txt | head -20
   ```

4. **Compare books**: Download two books and compare their word counts, chapter counts, etc.

5. **Create a word cloud data file**: Extract the 50 most common words with their counts
   ```bash
   cat huck_finn.txt | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | \
     grep -v '^$' | sort | uniq -c | sort -rn | head -50 > word_frequencies.txt
   ```

## Key Takeaways

- **Navigation**: `cd`, `pwd`, `ls` are your basic navigation tools
- **File operations**: `cp`, `mv`, `rm`, `mkdir` for managing files
- **Viewing**: `cat`, `less`, `head`, `tail` for reading files
- **Searching**: `grep` is incredibly powerful for finding patterns
- **Pipes**: `|` chains commands together
- **Redirection**: `>` saves output to files, `>>` appends

## Common Pitfalls

1. **Be careful with `rm`**: There's no undo! Always double-check before deleting.
2. **Quote variables**: Use `"$VAR"` not `$VAR` to handle spaces in filenames.
3. **Check file existence**: Use `[ -f "$FILE" ]` before operating on files.
4. **Use tab completion**: Press Tab to complete filenames and avoid typos.

## Troubleshooting

**"command not found" errors:**
- Make sure you're using the correct terminal (Git Bash on Windows)
- Check that the command is installed: `which curl` or `which grep`

**"Permission denied" when running scripts:**
- Make the script executable: `chmod +x script.sh`
- Or run with bash: `bash script.sh`

**Can't find downloaded files:**
- Check your current directory: `pwd`
- List files: `ls -la`
- Make sure you're in the right directory: `cd week-2/examples/bash-basics`

## Next Steps

- Explore the `text-processing` example for more advanced grep, sed, and awk usage
- Check out the `data-pipelines` example for chaining multiple commands
- Try the `bash-scripts` example for more complex automation

## Resources

- [Explain Shell](https://explainshell.com/) - Paste any command to understand it
- [Project Gutenberg](https://www.gutenberg.org/) - Free books for practice
- [grep documentation](https://www.gnu.org/software/grep/manual/grep.html)
- [Bash Guide](https://mywiki.wooledge.org/BashGuide)