# Text Processing: grep, sed, and awk

This example demonstrates advanced text processing using the three most powerful command line tools: grep, sed, and awk.

## Setup

Open VSCode's integrated terminal (View > Terminal or Ctrl+`) and navigate to this directory:

```bash
cd week-2/examples/text-processing
```

## Overview

- **grep**: Search for patterns in text
- **sed**: Stream editor for text transformation
- **awk**: Pattern scanning and processing language

These tools are the workhorses of command line text processing. Master them and you can process data faster than most GUI tools.

## Part 1: Advanced grep

### Download Sample Data

```bash
# Download Huckleberry Finn for examples
curl -o huck_finn.txt https://www.gutenberg.org/files/76/76-0.txt
```

### Basic Pattern Matching

```bash
# Find all mentions of "river"
grep "river" huck_finn.txt

# Case-insensitive search
grep -i "river" huck_finn.txt

# Count matches
grep -ic "river" huck_finn.txt

# Show line numbers
grep -in "river" huck_finn.txt | head -10

# Show 2 lines of context before and after each match
grep -i -C 2 "mississippi" huck_finn.txt | head -20
```

### Regular Expressions

```bash
# Lines starting with "CHAPTER"
grep "^CHAPTER" huck_finn.txt

# Lines ending with a period
grep "\.$" huck_finn.txt | head -10

# Lines containing numbers
grep "[0-9]" huck_finn.txt | head -10

# Lines with exactly 3-digit numbers
grep "\b[0-9]\{3\}\b" huck_finn.txt | head -10

# Lines with words starting with capital letters
grep "\b[A-Z][a-z]*\b" huck_finn.txt | head -10

# Find email-like patterns (if any)
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" huck_finn.txt
```

### Advanced grep Options

```bash
# Only show the matching part, not the whole line
grep -o "river" huck_finn.txt | head -20

# Invert match - lines NOT containing "the"
grep -v "the" huck_finn.txt | head -10

# Multiple patterns with -e
grep -e "Tom" -e "Huck" huck_finn.txt | head -10

# Or use extended regex with -E
grep -E "Tom|Huck" huck_finn.txt | head -10

# Quiet mode - just return exit code (useful in scripts)
if grep -q "Mississippi" huck_finn.txt; then
    echo "Found Mississippi!"
fi

# List only filenames containing pattern
grep -l "river" *.txt
```

## Part 2: sed - Stream Editor

### Basic Substitution

```bash
# Replace first occurrence of "river" with "RIVER" on each line
sed 's/river/RIVER/' huck_finn.txt | head -20

# Replace ALL occurrences (global flag)
sed 's/river/RIVER/g' huck_finn.txt | head -20

# Case-insensitive replacement
sed 's/river/RIVER/gi' huck_finn.txt | head -20

# Replace and save to new file
sed 's/river/RIVER/gi' huck_finn.txt > huck_finn_modified.txt
```

### Deleting Lines

```bash
# Delete lines containing "CHAPTER"
sed '/CHAPTER/d' huck_finn.txt | head -20

# Delete first line
sed '1d' huck_finn.txt | head -10

# Delete lines 1-10
sed '1,10d' huck_finn.txt | head -10

# Delete last line
sed '$d' huck_finn.txt | tail -10

# Delete empty lines
sed '/^$/d' huck_finn.txt | head -20

# Delete lines starting with whitespace
sed '/^[[:space:]]/d' huck_finn.txt | head -20
```

### Extracting Lines

```bash
# Print only lines 100-110
sed -n '100,110p' huck_finn.txt

# Print lines containing "Mississippi"
sed -n '/Mississippi/p' huck_finn.txt

# Print from first CHAPTER to second CHAPTER
sed -n '/^CHAPTER I\./,/^CHAPTER II\./p' huck_finn.txt | head -50
```

### Multiple Operations

```bash
# Chain multiple sed commands
sed -e 's/river/RIVER/g' -e 's/Mississippi/MISSISSIPPI/g' huck_finn.txt | head -20

# Or use semicolons
sed 's/river/RIVER/g; s/Mississippi/MISSISSIPPI/g' huck_finn.txt | head -20
```

### Practical sed Examples

```bash
# Remove all punctuation
sed 's/[[:punct:]]//g' huck_finn.txt | head -20

# Convert to lowercase
sed 's/.*/\L&/' huck_finn.txt | head -20

# Add line numbers
sed = huck_finn.txt | head -20

# Remove leading whitespace
sed 's/^[[:space:]]*//' huck_finn.txt | head -20

# Remove trailing whitespace
sed 's/[[:space:]]*$//' huck_finn.txt | head -20
```

## Part 3: awk - Pattern Processing

### Basic awk Usage

```bash
# Print entire file (like cat)
awk '{print}' huck_finn.txt | head -10

# Print first word of each line
awk '{print $1}' huck_finn.txt | head -20

# Print first and third words
awk '{print $1, $3}' huck_finn.txt | head -20

# Print last word of each line
awk '{print $NF}' huck_finn.txt | head -20

# Print line number and first word
awk '{print NR, $1}' huck_finn.txt | head -20
```

### Working with CSV Data

Create a sample CSV file:

```bash
cat > books.csv << 'EOF'
title,author,year,pages
Huckleberry Finn,Mark Twain,1884,366
Pride and Prejudice,Jane Austen,1813,432
Moby Dick,Herman Melville,1851,585
Great Gatsby,F. Scott Fitzgerald,1925,180
1984,George Orwell,1949,328
EOF
```

Now process it with awk:

```bash
# Print all columns
awk -F',' '{print $1, $2, $3, $4}' books.csv

# Print just titles and authors
awk -F',' '{print $1, "by", $2}' books.csv

# Skip header row
awk -F',' 'NR>1 {print $1, "by", $2}' books.csv

# Books published after 1900
awk -F',' 'NR>1 && $3 > 1900 {print $1, $3}' books.csv

# Books with more than 300 pages
awk -F',' 'NR>1 && $4 > 300 {print $1, $4, "pages"}' books.csv
```

### awk Calculations

```bash
# Sum of all pages
awk -F',' 'NR>1 {sum += $4} END {print "Total pages:", sum}' books.csv

# Average pages
awk -F',' 'NR>1 {sum += $4; count++} END {print "Average pages:", sum/count}' books.csv

# Count books per century
awk -F',' 'NR>1 {century = int($3/100)+1; count[century]++} END {for (c in count) print c "00s:", count[c]}' books.csv

# Find longest book
awk -F',' 'NR>1 {if ($4 > max) {max = $4; title = $1}} END {print title, max, "pages"}' books.csv
```

### Advanced awk Patterns

```bash
# Print lines longer than 80 characters
awk 'length > 80' huck_finn.txt | head -10

# Print lines with more than 10 words
awk 'NF > 10' huck_finn.txt | head -10

# Print lines containing "river" (like grep)
awk '/river/' huck_finn.txt | head -10

# Case-insensitive pattern matching
awk 'tolower($0) ~ /river/' huck_finn.txt | head -10

# Print every 10th line
awk 'NR % 10 == 0' huck_finn.txt | head -20
```

### awk with Multiple Files

```bash
# Download another book
curl -o pride_prejudice.txt https://www.gutenberg.org/files/1342/1342-0.txt

# Count lines in each file
awk 'END {print FILENAME, NR}' huck_finn.txt pride_prejudice.txt

# Find which file has more occurrences of "love"
awk '/love/ {count[FILENAME]++} END {for (f in count) print f, count[f]}' *.txt
```

## Part 4: Combining grep, sed, and awk

### Example 1: Extract and Analyze Chapter Titles

```bash
# Extract chapter titles, clean them up, and number them
grep "^CHAPTER" huck_finn.txt | \
  sed 's/^CHAPTER //' | \
  awk '{print NR, $0}'
```

### Example 2: Word Frequency Analysis

```bash
# Get top 20 most common words
cat huck_finn.txt | \
  tr '[:upper:]' '[:lower:]' | \
  tr -s '[:space:]' '\n' | \
  grep -v '^$' | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -20
```

### Example 3: Extract Dialogue

```bash
# Find lines with dialogue, clean them up
grep '"' huck_finn.txt | \
  sed 's/.*"\(.*\)".*/\1/' | \
  head -20
```

### Example 4: Analyze Line Lengths

```bash
# Get statistics on line lengths
awk '{print length}' huck_finn.txt | \
  sort -n | \
  awk '{
    sum += $1
    count++
    if (NR == 1) min = $1
    max = $1
  }
  END {
    print "Min:", min
    print "Max:", max
    print "Average:", sum/count
  }'
```

### Example 5: Create a Simple Report

```bash
# Generate a book analysis report
{
  echo "Book Analysis Report"
  echo "===================="
  echo ""
  echo "File: huck_finn.txt"
  echo "Lines: $(wc -l < huck_finn.txt)"
  echo "Words: $(wc -w < huck_finn.txt)"
  echo "Characters: $(wc -c < huck_finn.txt)"
  echo ""
  echo "Chapters: $(grep -c "^CHAPTER" huck_finn.txt)"
  echo ""
  echo "Mentions of key terms:"
  echo "  River: $(grep -ic "river" huck_finn.txt)"
  echo "  Mississippi: $(grep -ic "mississippi" huck_finn.txt)"
  echo "  Tom: $(grep -iow "tom" huck_finn.txt | wc -l)"
  echo "  Huck: $(grep -iow "huck" huck_finn.txt | wc -l)"
  echo ""
  echo "Top 10 most common words:"
  cat huck_finn.txt | \
    tr '[:upper:]' '[:lower:]' | \
    tr -s '[:space:]' '\n' | \
    grep -v '^$' | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -10
} > book_report.txt

cat book_report.txt
```

## Practice Exercises

1. **Extract all character names**: Find all capitalized words that might be character names
   ```bash
   grep -o "\b[A-Z][a-z]*\b" huck_finn.txt | sort | uniq -c | sort -rn | head -20
   ```

2. **Find the longest word**: Extract all words and find the longest one
   ```bash
   tr -s '[:space:]' '\n' < huck_finn.txt | awk '{if (length > max) {max = length; word = $0}} END {print word, max}'
   ```

3. **Count sentences**: Approximate sentence count by counting periods
   ```bash
   grep -o "\." huck_finn.txt | wc -l
   ```

4. **Extract chapter summaries**: Get the first 3 lines after each chapter heading
   ```bash
   grep -A 3 "^CHAPTER" huck_finn.txt | head -40
   ```

5. **Compare two books**: Download another book and compare word frequencies
   ```bash
   # Your code here!
   ```

## Key Takeaways

- **grep**: Best for finding patterns and filtering lines
- **sed**: Best for text transformation and substitution
- **awk**: Best for columnar data and calculations

**When to use which:**
- Need to find something? → grep
- Need to replace something? → sed
- Need to calculate something? → awk
- Need to do all three? → Pipe them together!

## Common Patterns

```bash
# Remove duplicates
sort file.txt | uniq

# Count unique values
sort file.txt | uniq -c

# Get unique values with counts, sorted by frequency
sort file.txt | uniq -c | sort -rn

# Extract column from CSV
awk -F',' '{print $2}' file.csv

# Replace text in place (be careful!)
sed -i 's/old/new/g' file.txt  # Linux
sed -i '' 's/old/new/g' file.txt  # macOS
```

## Resources

- [grep manual](https://www.gnu.org/software/grep/manual/grep.html)
- [sed manual](https://www.gnu.org/software/sed/manual/sed.html)
- [awk manual](https://www.gnu.org/software/gawk/manual/gawk.html)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/)
- [Regex101](https://regex101.com/) - Test your regular expressions

## Next Steps

- Check out the `data-pipelines` example to see these tools in action
- Try the `bash-scripts` example to automate text processing tasks
- Practice with different text files from Project Gutenberg