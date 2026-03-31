# Bash Scripts: Automating Data Science Tasks

This example provides practical, reusable bash scripts for common data science tasks.

## Setup

Open VSCode's integrated terminal and navigate to this directory:

```bash
cd week-2/examples/bash-scripts
```

## Overview

These scripts demonstrate:
- Proper script structure and error handling
- Command line argument processing
- Functions and modularity
- Real-world data science automation

All scripts include:
- Shebang line (`#!/bin/bash`)
- Error handling (`set -euo pipefail`)
- Input validation
- Help messages
- Comments

## Script 1: Text Analysis Tool

Create `analyze_text.sh`:

```bash
#!/bin/bash
# analyze_text.sh - Comprehensive text file analysis
# Usage: ./analyze_text.sh <file.txt>

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to display usage
usage() {
    echo "Usage: $0 <text_file>"
    echo ""
    echo "Analyzes a text file and provides statistics."
    echo ""
    echo "Options:"
    echo "  -h, --help    Show this help message"
    exit 1
}

# Function to analyze file
analyze_file() {
    local file=$1
    
    echo -e "${BLUE}Analyzing: $file${NC}"
    echo "===================="
    echo ""
    
    # Basic statistics
    echo "Basic Statistics:"
    echo "  Lines: $(wc -l < "$file")"
    echo "  Words: $(wc -w < "$file")"
    echo "  Characters: $(wc -c < "$file")"
    echo "  Unique words: $(cat "$file" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | grep -v '^$' | sort | uniq | wc -l)"
    echo ""
    
    # Line length statistics
    echo "Line Length Statistics:"
    awk '{print length}' "$file" | sort -n | awk '
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
    echo ""
    
    # Top 10 most common words (4+ letters)
    echo "Top 10 Most Common Words:"
    cat "$file" | \
        tr '[:upper:]' '[:lower:]' | \
        tr -s '[:space:]' '\n' | \
        grep -E '^[a-z]{4,}$' | \
        sort | \
        uniq -c | \
        sort -rn | \
        head -10 | \
        awk '{printf "  %3d %s\n", $1, $2}'
    echo ""
    
    echo -e "${GREEN}Analysis complete!${NC}"
}

# Main script
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: No file specified${NC}"
    usage
fi

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    usage
fi

FILE=$1

if [ ! -f "$FILE" ]; then
    echo -e "${RED}Error: File '$FILE' not found${NC}"
    exit 1
fi

analyze_file "$FILE"
```

Make it executable and test:

```bash
chmod +x analyze_text.sh

# Download a test file
curl -o test.txt https://www.gutenberg.org/files/76/76-0.txt

# Run the analysis
./analyze_text.sh test.txt
```

## Script 2: CSV Data Processor

Create `process_csv.sh`:

```bash
#!/bin/bash
# process_csv.sh - Process and analyze CSV files
# Usage: ./process_csv.sh <file.csv>

set -euo pipefail

usage() {
    echo "Usage: $0 <csv_file> [options]"
    echo ""
    echo "Options:"
    echo "  --summary         Show summary statistics"
    echo "  --column N        Extract column N"
    echo "  --filter COL=VAL  Filter rows where column COL equals VAL"
    echo "  --sort COL        Sort by column COL"
    echo "  -h, --help        Show this help message"
    exit 1
}

# Function to show CSV summary
show_summary() {
    local file=$1
    
    echo "CSV Summary:"
    echo "============"
    echo "File: $file"
    echo "Rows: $(tail -n +2 "$file" | wc -l)"
    echo "Columns: $(head -1 "$file" | tr ',' '\n' | wc -l)"
    echo ""
    echo "Column Names:"
    head -1 "$file" | tr ',' '\n' | nl
    echo ""
}

# Function to extract column
extract_column() {
    local file=$1
    local col=$2
    
    echo "Column $col:"
    echo "==========="
    awk -F',' -v col="$col" '{print $col}' "$file"
}

# Function to filter rows
filter_rows() {
    local file=$1
    local filter=$2
    
    # Parse filter (format: COL=VAL)
    local col=$(echo "$filter" | cut -d'=' -f1)
    local val=$(echo "$filter" | cut -d'=' -f2)
    
    echo "Filtering where column $col = $val:"
    echo "===================================="
    head -1 "$file"
    awk -F',' -v col="$col" -v val="$val" 'NR>1 && $col == val' "$file"
}

# Main script
if [ $# -eq 0 ]; then
    usage
fi

FILE=$1
shift

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found"
    exit 1
fi

# Process options
if [ $# -eq 0 ]; then
    show_summary "$FILE"
else
    case "$1" in
        --summary)
            show_summary "$FILE"
            ;;
        --column)
            if [ $# -lt 2 ]; then
                echo "Error: --column requires a column number"
                exit 1
            fi
            extract_column "$FILE" "$2"
            ;;
        --filter)
            if [ $# -lt 2 ]; then
                echo "Error: --filter requires COL=VAL format"
                exit 1
            fi
            filter_rows "$FILE" "$2"
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Error: Unknown option $1"
            usage
            ;;
    esac
fi
```

Test it:

```bash
chmod +x process_csv.sh

# Create test CSV
cat > test.csv << 'EOF'
name,age,city,score
Alice,25,NYC,85
Bob,30,LA,92
Charlie,25,NYC,78
David,35,Chicago,88
Eve,28,LA,95
EOF

# Try different operations
./process_csv.sh test.csv --summary
./process_csv.sh test.csv --column 1
./process_csv.sh test.csv --filter 3=NYC
```

## Script 3: Batch File Processor

Create `batch_process.sh`:

```bash
#!/bin/bash
# batch_process.sh - Process multiple files in batch
# Usage: ./batch_process.sh <directory> <operation>

set -euo pipefail

usage() {
    echo "Usage: $0 <directory> <operation>"
    echo ""
    echo "Operations:"
    echo "  count       Count lines in each file"
    echo "  wordfreq    Generate word frequency for each file"
    echo "  summary     Generate summary statistics"
    echo ""
    echo "Example:"
    echo "  $0 ./books count"
    exit 1
}

# Function to count lines
count_lines() {
    local dir=$1
    
    echo "Line Counts:"
    echo "============"
    for file in "$dir"/*.txt; do
        [ -f "$file" ] || continue
        lines=$(wc -l < "$file")
        printf "%-30s %8d lines\n" "$(basename "$file")" "$lines"
    done | sort -k2 -rn
}

# Function to generate word frequency
word_frequency() {
    local dir=$1
    local output_dir="$dir/word_freq"
    
    mkdir -p "$output_dir"
    
    echo "Generating word frequencies..."
    for file in "$dir"/*.txt; do
        [ -f "$file" ] || continue
        basename=$(basename "$file" .txt)
        
        echo "  Processing $basename..."
        cat "$file" | \
            tr '[:upper:]' '[:lower:]' | \
            tr -s '[:space:]' '\n' | \
            grep -E '^[a-z]{3,}$' | \
            sort | \
            uniq -c | \
            sort -rn | \
            head -50 > "$output_dir/${basename}_freq.txt"
    done
    
    echo "Results saved to $output_dir/"
}

# Function to generate summary
generate_summary() {
    local dir=$1
    local output="$dir/summary_report.txt"
    
    {
        echo "Batch Processing Summary"
        echo "======================="
        echo "Generated: $(date)"
        echo "Directory: $dir"
        echo ""
        
        for file in "$dir"/*.txt; do
            [ -f "$file" ] || continue
            
            echo "File: $(basename "$file")"
            echo "  Lines: $(wc -l < "$file")"
            echo "  Words: $(wc -w < "$file")"
            echo "  Size: $(ls -lh "$file" | awk '{print $5}')"
            echo ""
        done
        
        echo "Total files: $(ls "$dir"/*.txt 2>/dev/null | wc -l)"
        echo "Total lines: $(cat "$dir"/*.txt 2>/dev/null | wc -l)"
        echo "Total words: $(cat "$dir"/*.txt 2>/dev/null | wc -w)"
    } > "$output"
    
    cat "$output"
    echo ""
    echo "Report saved to $output"
}

# Main script
if [ $# -lt 2 ]; then
    usage
fi

DIR=$1
OPERATION=$2

if [ ! -d "$DIR" ]; then
    echo "Error: Directory '$DIR' not found"
    exit 1
fi

case "$OPERATION" in
    count)
        count_lines "$DIR"
        ;;
    wordfreq)
        word_frequency "$DIR"
        ;;
    summary)
        generate_summary "$DIR"
        ;;
    *)
        echo "Error: Unknown operation '$OPERATION'"
        usage
        ;;
esac
```

Test it:

```bash
chmod +x batch_process.sh

# Create test directory with files
mkdir -p test_books
curl -o test_books/huck_finn.txt https://www.gutenberg.org/files/76/76-0.txt
curl -o test_books/pride_prejudice.txt https://www.gutenberg.org/files/1342/1342-0.txt

# Run batch operations
./batch_process.sh test_books count
./batch_process.sh test_books summary
./batch_process.sh test_books wordfreq
```

## Script 4: Data Pipeline Automation

Create `run_pipeline.sh`:

```bash
#!/bin/bash
# run_pipeline.sh - Automated data processing pipeline
# Usage: ./run_pipeline.sh <config_file>

set -euo pipefail

# Configuration
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="logs"
OUTPUT_DIR="output"

# Setup logging
setup_logging() {
    mkdir -p "$LOG_DIR"
    LOG_FILE="$LOG_DIR/pipeline_$TIMESTAMP.log"
    exec 1> >(tee -a "$LOG_FILE")
    exec 2>&1
}

# Log function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Error handler
error_exit() {
    log "ERROR: $1"
    exit 1
}

# Download data
download_data() {
    log "Step 1: Downloading data..."
    mkdir -p "$OUTPUT_DIR/raw"
    
    curl -o "$OUTPUT_DIR/raw/data.txt" \
        https://www.gutenberg.org/files/76/76-0.txt \
        || error_exit "Failed to download data"
    
    log "  Downloaded $(wc -l < "$OUTPUT_DIR/raw/data.txt") lines"
}

# Clean data
clean_data() {
    log "Step 2: Cleaning data..."
    mkdir -p "$OUTPUT_DIR/cleaned"
    
    # Remove empty lines and normalize whitespace
    cat "$OUTPUT_DIR/raw/data.txt" | \
        grep -v '^$' | \
        tr -s '[:space:]' ' ' \
        > "$OUTPUT_DIR/cleaned/data_clean.txt"
    
    log "  Cleaned data: $(wc -l < "$OUTPUT_DIR/cleaned/data_clean.txt") lines"
}

# Analyze data
analyze_data() {
    log "Step 3: Analyzing data..."
    mkdir -p "$OUTPUT_DIR/analysis"
    
    # Word frequency
    cat "$OUTPUT_DIR/cleaned/data_clean.txt" | \
        tr '[:upper:]' '[:lower:]' | \
        tr -s '[:space:]' '\n' | \
        grep -E '^[a-z]{3,}$' | \
        sort | \
        uniq -c | \
        sort -rn | \
        head -100 > "$OUTPUT_DIR/analysis/word_freq.txt"
    
    log "  Generated word frequency analysis"
}

# Generate report
generate_report() {
    log "Step 4: Generating report..."
    
    {
        echo "Data Pipeline Report"
        echo "==================="
        echo "Generated: $(date)"
        echo "Pipeline ID: $TIMESTAMP"
        echo ""
        echo "Data Summary:"
        echo "  Raw lines: $(wc -l < "$OUTPUT_DIR/raw/data.txt")"
        echo "  Cleaned lines: $(wc -l < "$OUTPUT_DIR/cleaned/data_clean.txt")"
        echo "  Unique words: $(wc -l < "$OUTPUT_DIR/analysis/word_freq.txt")"
        echo ""
        echo "Top 10 Words:"
        head -10 "$OUTPUT_DIR/analysis/word_freq.txt" | \
            awk '{printf "  %3d %s\n", $1, $2}'
    } > "$OUTPUT_DIR/report_$TIMESTAMP.txt"
    
    log "  Report saved to $OUTPUT_DIR/report_$TIMESTAMP.txt"
}

# Main pipeline
main() {
    setup_logging
    
    log "Starting data pipeline..."
    log "========================"
    
    download_data
    clean_data
    analyze_data
    generate_report
    
    log "========================"
    log "Pipeline completed successfully!"
    log "Results in: $OUTPUT_DIR/"
    log "Log file: $LOG_FILE"
}

# Run pipeline
main
```

Run it:

```bash
chmod +x run_pipeline.sh
./run_pipeline.sh
```

## Script 5: Project Setup Script

Create `setup_project.sh`:

```bash
#!/bin/bash
# setup_project.sh - Set up a new data science project
# Usage: ./setup_project.sh <project_name>

set -euo pipefail

usage() {
    echo "Usage: $0 <project_name>"
    echo ""
    echo "Creates a new data science project with standard structure."
    exit 1
}

create_project() {
    local name=$1
    
    echo "Creating project: $name"
    echo "======================="
    
    # Create directory structure
    mkdir -p "$name"/{data/{raw,processed,analysis},scripts,notebooks,docs,output}
    
    # Create README
    cat > "$name/README.md" << EOF
# $name

## Project Structure

\`\`\`
$name/
├── data/
│   ├── raw/          # Original, immutable data
│   ├── processed/    # Cleaned, transformed data
│   └── analysis/     # Analysis results
├── scripts/          # Data processing scripts
├── notebooks/        # Jupyter notebooks
├── docs/             # Documentation
└── output/           # Final outputs, reports
\`\`\`

## Getting Started

1. Place raw data in \`data/raw/\`
2. Run processing scripts from \`scripts/\`
3. Analyze data in \`notebooks/\`
4. Generate reports in \`output/\`

## Created

$(date)
EOF
    
    # Create .gitignore
    cat > "$name/.gitignore" << EOF
# Data files
data/raw/*
data/processed/*
*.csv
*.txt
*.json

# Python
__pycache__/
*.py[cod]
.ipynb_checkpoints/

# Environment
.env
venv/
.venv/

# Output
output/*
!output/.gitkeep

# OS
.DS_Store
Thumbs.db
EOF
    
    # Create placeholder files
    touch "$name/data/raw/.gitkeep"
    touch "$name/data/processed/.gitkeep"
    touch "$name/data/analysis/.gitkeep"
    touch "$name/output/.gitkeep"
    
    # Create sample script
    cat > "$name/scripts/process_data.sh" << 'EOF'
#!/bin/bash
# process_data.sh - Process raw data

set -euo pipefail

echo "Processing data..."
# Add your processing steps here
EOF
    
    chmod +x "$name/scripts/process_data.sh"
    
    # Initialize git
    cd "$name"
    git init
    git add .
    git commit -m "Initial project setup"
    cd ..
    
    echo ""
    echo "Project created successfully!"
    echo "Next steps:"
    echo "  cd $name"
    echo "  # Add your data to data/raw/"
    echo "  # Edit scripts/process_data.sh"
}

# Main
if [ $# -eq 0 ]; then
    usage
fi

PROJECT_NAME=$1

if [ -d "$PROJECT_NAME" ]; then
    echo "Error: Directory '$PROJECT_NAME' already exists"
    exit 1
fi

create_project "$PROJECT_NAME"
```

Test it:

```bash
chmod +x setup_project.sh
./setup_project.sh my_analysis
cd my_analysis
ls -la
```

## Best Practices

### 1. Always Include Error Handling

```bash
#!/bin/bash
set -euo pipefail  # Exit on error, undefined variable, pipe failure

# Check prerequisites
command -v curl >/dev/null 2>&1 || { echo "curl required but not installed"; exit 1; }
```

### 2. Validate Inputs

```bash
if [ $# -eq 0 ]; then
    echo "Error: No arguments provided"
    usage
fi

if [ ! -f "$FILE" ]; then
    echo "Error: File not found"
    exit 1
fi
```

### 3. Use Functions

```bash
# Good: Modular and reusable
process_file() {
    local file=$1
    # processing logic
}

# Call function
process_file "data.txt"
```

### 4. Add Logging

```bash
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log "Starting process..."
```

### 5. Make Scripts Portable

```bash
# Use relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$SCRIPT_DIR/../data"

# Check for required commands
for cmd in curl awk sed; do
    command -v $cmd >/dev/null 2>&1 || {
        echo "Error: $cmd is required but not installed"
        exit 1
    }
done
```

## Common Script Patterns

### Pattern 1: Process All Files in Directory

```bash
for file in /path/to/files/*.txt; do
    [ -f "$file" ] || continue  # Skip if no files match
    echo "Processing $file..."
    # process file
done
```

### Pattern 2: Parallel Processing

```bash
# Process files in background
for file in *.txt; do
    process_file "$file" &
done
wait  # Wait for all background jobs
```

### Pattern 3: Progress Indicator

```bash
total=$(ls *.txt | wc -l)
current=0

for file in *.txt; do
    ((current++))
    echo "Processing $current/$total: $file"
    # process file
done
```

## Resources

- [Bash Scripting Tutorial](https://www.shellscript.sh/)
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- [ShellCheck](https://www.shellcheck.net/) - Script analysis tool
- [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls)

## Next Steps

- Adapt these scripts for your own projects
- Combine scripts into larger workflows
- Add error handling and logging to your scripts
- Share scripts with your team via Git