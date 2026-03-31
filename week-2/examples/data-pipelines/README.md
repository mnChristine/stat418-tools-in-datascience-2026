# Data Pipelines: Chaining Commands for Data Processing

This example demonstrates how to build sophisticated data processing pipelines by chaining simple command line tools together.

## Setup

Open VSCode's integrated terminal and navigate to this directory:

```bash
cd week-2/examples/data-pipelines
```

## The Power of Pipes

The Unix pipe (`|`) is one of the most powerful concepts in computing. It lets you connect the output of one command to the input of another, building complex workflows from simple tools.

**Philosophy**: Instead of one complex program, use many simple programs connected by pipes.

## Example 1: Text Analysis Pipeline

### Download Sample Data

```bash
# Download The Adventures of Huckleberry Finn
curl -o huck_finn.txt https://www.gutenberg.org/files/76/76-0.txt
```

### Word Frequency Analysis

```bash
# Complete pipeline: text → words → count → sort → top 20
cat huck_finn.txt | \
  tr '[:upper:]' '[:lower:]' | \
  tr -s '[:space:]' '\n' | \
  grep -v '^$' | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -20
```

**What each step does:**
1. `cat huck_finn.txt` - Read the file
2. `tr '[:upper:]' '[:lower:]'` - Convert to lowercase
3. `tr -s '[:space:]' '\n'` - Convert spaces to newlines (one word per line)
4. `grep -v '^$'` - Remove empty lines
5. `sort` - Sort alphabetically (required for uniq)
6. `uniq -c` - Count unique words
7. `sort -rn` - Sort numerically in reverse (highest first)
8. `head -20` - Show top 20

### Character Mention Analysis

```bash
# Count mentions of main characters
echo "Character Mentions:"
echo "==================="
for char in "Huck" "Tom" "Jim" "Aunt" "Widow"; do
  count=$(grep -iow "$char" huck_finn.txt | wc -l)
  echo "$char: $count"
done | sort -t':' -k2 -rn
```

### Extract and Analyze Dialogue

```bash
# Extract all dialogue, get word count
grep '"' huck_finn.txt | \
  sed 's/.*"\([^"]*\)".*/\1/' | \
  tr '[:upper:]' '[:lower:]' | \
  tr -s '[:space:]' '\n' | \
  grep -v '^$' | \
  sort | \
  uniq -c | \
  sort -rn | \
  head -20 > dialogue_words.txt

echo "Top 20 words in dialogue:"
cat dialogue_words.txt
```

## Example 2: CSV Data Processing

### Create Sample Sales Data

```bash
cat > sales.csv << 'EOF'
date,product,quantity,price,region
2026-01-15,Widget A,10,29.99,West
2026-01-16,Widget B,5,49.99,East
2026-01-17,Widget A,8,29.99,West
2026-01-18,Widget C,12,19.99,South
2026-01-19,Widget B,7,49.99,East
2026-01-20,Widget A,15,29.99,North
2026-01-21,Widget C,20,19.99,South
2026-01-22,Widget B,3,49.99,West
2026-01-23,Widget A,11,29.99,East
2026-01-24,Widget C,9,19.99,North
2026-01-25,Widget B,6,49.99,South
2026-01-26,Widget A,13,29.99,West
2026-01-27,Widget C,18,19.99,East
2026-01-28,Widget B,4,49.99,North
2026-01-29,Widget A,16,29.99,South
2026-01-30,Widget C,14,19.99,West
EOF
```

### Pipeline 1: Total Revenue by Product

```bash
# Calculate total revenue for each product
echo "Total Revenue by Product:"
echo "========================="
awk -F',' 'NR>1 {
  product = $2
  revenue = $3 * $4
  total[product] += revenue
}
END {
  for (p in total) {
    printf "%s: $%.2f\n", p, total[p]
  }
}' sales.csv | sort -t'$' -k2 -rn
```

### Pipeline 2: Sales by Region

```bash
# Total quantity sold by region
echo "Sales by Region:"
echo "================"
awk -F',' 'NR>1 {region[$5] += $3} END {for (r in region) print r, region[r]}' sales.csv | \
  sort -k2 -rn | \
  awk '{printf "%-10s %d units\n", $1, $2}'
```

### Pipeline 3: Best Selling Product

```bash
# Find best selling product by quantity
echo "Best Selling Product:"
awk -F',' 'NR>1 {product[$2] += $3} END {for (p in product) print product[p], p}' sales.csv | \
  sort -rn | \
  head -1 | \
  awk '{print $2, $3, "-", $1, "units sold"}'
```

### Pipeline 4: Daily Revenue Trend

```bash
# Calculate daily revenue
echo "Daily Revenue:"
echo "=============="
awk -F',' 'NR>1 {
  date = $1
  revenue = $3 * $4
  daily[date] += revenue
}
END {
  for (d in daily) {
    printf "%s: $%.2f\n", d, daily[d]
  }
}' sales.csv | sort
```

## Example 3: Log File Analysis

### Create Sample Log File

```bash
cat > server.log << 'EOF'
2026-03-01 10:23:45 INFO User login: alice@example.com
2026-03-01 10:24:12 INFO Page view: /home
2026-03-01 10:25:33 ERROR Database connection failed
2026-03-01 10:26:01 INFO User login: bob@example.com
2026-03-01 10:27:15 WARN Slow query: 2.3s
2026-03-01 10:28:42 INFO Page view: /products
2026-03-01 10:29:18 ERROR API timeout: /api/users
2026-03-01 10:30:05 INFO User logout: alice@example.com
2026-03-01 10:31:22 INFO Page view: /about
2026-03-01 10:32:47 ERROR Database connection failed
2026-03-01 10:33:11 WARN High memory usage: 85%
2026-03-01 10:34:29 INFO User login: charlie@example.com
2026-03-01 10:35:56 ERROR API timeout: /api/products
2026-03-01 10:36:13 INFO Page view: /contact
2026-03-01 10:37:40 WARN Slow query: 3.1s
EOF
```

### Pipeline 1: Error Summary

```bash
# Count errors by type
echo "Error Summary:"
echo "=============="
grep "ERROR" server.log | \
  awk '{print $4, $5, $6}' | \
  sort | \
  uniq -c | \
  sort -rn
```

### Pipeline 2: User Activity

```bash
# Extract unique users
echo "Active Users:"
echo "============="
grep "User login" server.log | \
  awk '{print $5}' | \
  sort | \
  uniq
```

### Pipeline 3: Hourly Activity

```bash
# Count events by hour
echo "Hourly Activity:"
echo "================"
awk '{print substr($2, 1, 2)}' server.log | \
  sort | \
  uniq -c | \
  awk '{printf "%s:00 - %d events\n", $2, $1}'
```

### Pipeline 4: Performance Issues

```bash
# Find all warnings and errors
echo "Performance Issues:"
echo "==================="
grep -E "WARN|ERROR" server.log | \
  awk '{$1=$2=""; print $0}' | \
  sed 's/^  //' | \
  sort | \
  uniq -c | \
  sort -rn
```

## Example 4: Multi-File Processing

### Download Multiple Books

```bash
# Download several books
curl -o huck_finn.txt https://www.gutenberg.org/files/76/76-0.txt
curl -o pride_prejudice.txt https://www.gutenberg.org/files/1342/1342-0.txt
curl -o moby_dick.txt https://www.gutenberg.org/files/2701/2701-0.txt
```

### Pipeline 1: Compare Book Lengths

```bash
# Compare word counts
echo "Book Lengths:"
echo "============="
for book in *.txt; do
  words=$(wc -w < "$book")
  echo "$book: $words words"
done | sort -t':' -k2 -rn
```

### Pipeline 2: Find Common Words

```bash
# Find words that appear in all books
echo "Finding common words..."

# Get word list from each book
for book in *.txt; do
  cat "$book" | \
    tr '[:upper:]' '[:lower:]' | \
    tr -s '[:space:]' '\n' | \
    grep -v '^$' | \
    sort | \
    uniq > "${book%.txt}_words.txt"
done

# Find intersection
comm -12 huck_finn_words.txt pride_prejudice_words.txt | \
  comm -12 - moby_dick_words.txt | \
  head -20

# Cleanup
rm *_words.txt
```

### Pipeline 3: Aggregate Statistics

```bash
# Generate statistics for all books
echo "Book Statistics:"
echo "================"
for book in *.txt; do
  echo ""
  echo "File: $book"
  echo "Lines: $(wc -l < "$book")"
  echo "Words: $(wc -w < "$book")"
  echo "Unique words: $(cat "$book" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | grep -v '^$' | sort | uniq | wc -l)"
  echo "Chapters: $(grep -c "^CHAPTER" "$book" 2>/dev/null || echo "N/A")"
done
```

## Example 5: Real-World Data Pipeline

### Complete Analysis Pipeline

Create a script that does comprehensive text analysis:

```bash
cat > analyze_all.sh << 'EOF'
#!/bin/bash
# analyze_all.sh - Comprehensive text analysis pipeline

set -euo pipefail

OUTPUT_DIR="analysis_results"
mkdir -p "$OUTPUT_DIR"

echo "Starting comprehensive analysis..."
echo ""

# Process each text file
for file in *.txt; do
  [ -f "$file" ] || continue
  
  echo "Analyzing $file..."
  
  # Basic stats
  {
    echo "Analysis of $file"
    echo "===================="
    echo "Generated: $(date)"
    echo ""
    echo "Basic Statistics:"
    echo "  Lines: $(wc -l < "$file")"
    echo "  Words: $(wc -w < "$file")"
    echo "  Characters: $(wc -c < "$file")"
    echo ""
    
    # Word frequency
    echo "Top 20 Most Common Words:"
    cat "$file" | \
      tr '[:upper:]' '[:lower:]' | \
      tr -s '[:space:]' '\n' | \
      grep -v '^$' | \
      grep -E '^[a-z]{4,}$' | \
      sort | \
      uniq -c | \
      sort -rn | \
      head -20 | \
      awk '{printf "  %3d %s\n", $1, $2}'
    echo ""
    
    # Line length statistics
    echo "Line Length Statistics:"
    awk '{print length}' "$file" | \
      sort -n | \
      awk '
        {
          sum += $1
          count++
          if (NR == 1) min = $1
          max = $1
        }
        END {
          printf "  Min: %d\n", min
          printf "  Max: %d\n", max
          printf "  Average: %.1f\n", sum/count
        }
      '
  } > "$OUTPUT_DIR/${file%.txt}_analysis.txt"
  
  echo "  Results saved to $OUTPUT_DIR/${file%.txt}_analysis.txt"
done

echo ""
echo "Analysis complete! Results in $OUTPUT_DIR/"
EOF

chmod +x analyze_all.sh
./analyze_all.sh
```

## Example 6: Data Transformation Pipeline

### Transform CSV to Different Formats

```bash
# CSV to TSV (tab-separated)
cat sales.csv | tr ',' '\t' > sales.tsv

# CSV to fixed-width
awk -F',' '{printf "%-12s %-12s %8s %8s %8s\n", $1, $2, $3, $4, $5}' sales.csv > sales.txt

# Extract specific columns
awk -F',' 'NR==1 {print $2, $5} NR>1 {print $2, $5}' sales.csv | column -t

# Pivot data: sum quantity by product and region
awk -F',' '
NR>1 {
  key = $2 "," $5
  quantity[key] += $3
}
END {
  print "Product,Region,Total Quantity"
  for (k in quantity) {
    print k "," quantity[k]
  }
}' sales.csv | sort
```

## Key Pipeline Patterns

### Pattern 1: Filter → Transform → Aggregate

```bash
# Example: Find errors, extract type, count
grep "ERROR" server.log | \
  awk '{print $4}' | \
  sort | \
  uniq -c | \
  sort -rn
```

### Pattern 2: Extract → Clean → Analyze

```bash
# Example: Get words, clean, count
cat file.txt | \
  tr '[:upper:]' '[:lower:]' | \
  tr -s '[:space:]' '\n' | \
  grep -E '^[a-z]+$' | \
  sort | \
  uniq -c | \
  sort -rn
```

### Pattern 3: Split → Process → Merge

```bash
# Example: Process multiple files and combine results
for file in *.txt; do
  wc -l "$file"
done | \
  sort -rn | \
  awk '{sum += $1; print} END {print "Total:", sum}'
```

## Performance Tips

1. **Use grep before awk/sed**: Filter early to reduce data
   ```bash
   # Good: Filter first
   grep "ERROR" huge_file.log | awk '{print $4}'
   
   # Bad: Process everything
   awk '/ERROR/ {print $4}' huge_file.log
   ```

2. **Avoid unnecessary sorting**: Only sort when needed
   ```bash
   # If you don't need sorted output
   awk '{count[$1]++} END {for (k in count) print k, count[k]}'
   ```

3. **Use built-in tools**: They're optimized
   ```bash
   # Good: Use wc
   wc -l file.txt
   
   # Bad: Count manually
   cat file.txt | awk 'END {print NR}'
   ```

4. **Process in parallel**: For multiple files
   ```bash
   # Process files in parallel (if you have GNU parallel)
   ls *.txt | parallel 'wc -l {}'
   ```

## Practice Exercises

1. **Create a sales report**: Calculate total revenue, average order value, and best-selling product

2. **Log analysis**: Find the busiest hour, most common error, and user with most activity

3. **Text comparison**: Compare vocabulary richness (unique words / total words) across multiple books

4. **Data cleaning**: Remove duplicates, fix formatting, and validate a CSV file

5. **Custom pipeline**: Design a pipeline for your own data analysis task

## Common Pipeline Mistakes

1. **Forgetting to sort before uniq**
   ```bash
   # Wrong: uniq without sort
   cat file.txt | uniq -c
   
   # Right: sort first
   cat file.txt | sort | uniq -c
   ```

2. **Not handling empty lines**
   ```bash
   # Add grep -v '^$' to remove empty lines
   cat file.txt | grep -v '^$' | sort
   ```

3. **Incorrect field separators**
   ```bash
   # Specify delimiter for awk
   awk -F',' '{print $2}' file.csv
   ```

4. **Not quoting variables in scripts**
   ```bash
   # Always quote variables
   grep "$pattern" "$file"
   ```

## Resources

- [Unix Pipeline Tutorial](https://www.tutorialspoint.com/unix/unix-pipes-filters.htm)
- [Advanced Bash Scripting Guide](https://tldp.org/LDP/abs/html/)
- [Data Science at the Command Line](https://datascienceatthecommandline.com/)

## Next Steps

- Check out the `bash-scripts` example for automating these pipelines
- Try building pipelines for your own data
- Experiment with different combinations of tools
- Time your pipelines to see which approaches are fastest