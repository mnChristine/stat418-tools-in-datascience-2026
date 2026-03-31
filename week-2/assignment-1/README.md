# Assignment 1: Web Server Log Analysis with Bash

**Due:** Two weeks from Week 2 class (before Week 4 class at 6:00 PM)

**Submission:** Pull request to the course repository

## Overview

You will analyze NASA web server access logs from July and August 1995 using bash scripting and command line tools. This assignment requires you to build a comprehensive data processing pipeline that downloads, cleans, analyzes, and reports on real-world log data.

**Why this matters:** Log analysis is a fundamental data science task. Whether you're analyzing web traffic, debugging systems, or monitoring applications, you'll use these skills constantly in production environments.

## Learning Objectives

By completing this assignment, you will:
- Build multi-stage data processing pipelines with bash
- Use grep, sed, awk, and other command line tools effectively
- Handle edge cases and errors in real-world data
- Write modular, well-documented scripts
- Practice Git workflows with pull requests
- Learn to use AI assistants effectively while maintaining code quality

## Data Source

NASA web server logs from July and August 1995:
- **July**: https://atlas.cs.brown.edu/data/web-logs/NASA_Jul95.log
- **August**: https://atlas.cs.brown.edu/data/web-logs/NASA_Aug95.log

**Log Format:**
```
host logname time method request protocol status bytes
```

**Example:**
```
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
```

## Requirements

### Part 1: Data Acquisition and Validation

Create a script that:
1. Downloads both log files
2. Validates the downloads (check file size, line count)
3. Creates a backup of the original files
4. Handles download failures gracefully
5. Logs all operations with timestamps

**Deliverable:** `download_data.sh`

### Part 2: Data Analysis

Create a script that answers the following questions for **each log file**:

#### Basic Analysis
1. **Top 10 hosts** - List the top 10 hosts/IPs making requests (exclude 404 errors)
2. **IP vs Hostname** - What percentage of requests came from IP addresses vs hostnames?
3. **Top 10 requests** - List the top 10 most requested URLs (exclude 404 errors)
4. **Request types** - List the most frequent HTTP methods (GET, POST, etc.) with counts
5. **404 errors** - How many 404 errors were reported?
6. **Response codes** - What is the most frequent response code and what percentage of responses did it account for?

#### Time-Based Analysis
7. **Peak hours** - What hours of the day see the most activity? When is it quiet?
8. **Busiest day** - Which date saw the most activity overall?
9. **Quietest day** - Excluding outage dates, which date saw the least activity?

#### Advanced Analysis
10. **Hurricane outage** - There was a hurricane in August causing a data outage. Identify the exact dates and times when data was not collected. How long was the outage?
11. **Response size** - What is the largest response (in bytes) and what is the average response size?
12. **Error patterns** - Are there any patterns in when errors occur (time of day, specific hosts, etc.)?

**Deliverable:** `analyze_logs.sh`

### Part 3: Reporting

Create a script that:
1. Generates a comprehensive markdown report with all findings
2. Includes summary statistics for both months
3. Compares July vs August activity
4. Includes visualizations (ASCII charts or data for plotting)
5. Highlights interesting findings or anomalies

**Deliverable:** `generate_report.sh`

### Part 4: Pipeline Integration

Create a master script that:
1. Runs all scripts in the correct order
2. Handles errors at each stage
3. Provides progress updates
4. Generates a final report
5. Cleans up temporary files

**Deliverable:** `run_pipeline.sh`

## Starter Code

We provide a starter script to help you get started:

```bash
#!/bin/bash
# hw1-starter.sh - Download NASA log files

set -euo pipefail

echo "Downloading NASA web server logs..."

# Download July log
curl -s https://atlas.cs.brown.edu/data/web-logs/NASA_Jul95.log > NASA_Jul95.log
echo "Downloaded NASA_Jul95.log"

# Download August log
curl -s https://atlas.cs.brown.edu/data/web-logs/NASA_Aug95.log > NASA_Aug95.log
echo "Downloaded NASA_Aug95.log"

echo "Download complete!"
```

## Submission Instructions

1. **Fork the course repository** (if you haven't already)

2. **Create a feature branch:**
   ```bash
   git checkout -b hw1-yourname
   ```

3. **Create your assignment directory:**
   ```bash
   mkdir -p week-2/assignment-1/submissions/yourname
   cd week-2/assignment-1/submissions/yourname
   ```

4. **Add your files:**
   - `download_data.sh`
   - `analyze_logs.sh`
   - `generate_report.sh`
   - `run_pipeline.sh`
   - `README.md` (explaining how to run your scripts)
   - `REPORT.md` (your analysis findings)

5. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add homework 1 submission - yourname"
   git push origin hw1-yourname
   ```

6. **Create a pull request** on GitHub:
   - Base: `main`
   - Compare: `hw1-yourname`
   - Title: "Homework 1 - Your Name"
   - Description: Brief summary of your approach

## Tips for Success

### Using AI Assistants Effectively

**DO:**
- Use AI to help with bash syntax and command options
- Ask AI to explain commands you don't understand
- Use AI to debug error messages
- Ask AI for alternative approaches

**DON'T:**
- Copy AI-generated code without understanding it
- Let AI design your pipeline architecture
- Skip testing because "AI wrote it"
- Submit code you can't explain

**Remember:** You're responsible for correctness. AI can help you write code faster, but YOU must verify it works correctly.

### Development Strategy

1. **Start simple:** Get basic functionality working first
2. **Test incrementally:** Test each script before moving to the next
3. **Use small samples:** Test with `head -100 logfile.log` before processing full files
4. **Add error handling:** Use `set -euo pipefail` and validate inputs
5. **Document as you go:** Write comments while the logic is fresh

### Common Pitfalls

1. **Not handling missing data:** Some log entries may have missing fields
2. **Incorrect field parsing:** Log format can vary slightly
3. **Memory issues:** These are large files; use streaming commands
4. **Timezone confusion:** Logs include timezone information
5. **Percentage calculations:** Remember to handle division by zero

### Testing Your Scripts

```bash
# Test with small sample
head -1000 NASA_Jul95.log > test_sample.log
./analyze_logs.sh test_sample.log

# Check for errors
bash -x ./analyze_logs.sh test_sample.log

# Validate output
# Compare your results with classmates (numbers should match!)
```

## Resources

### Command Line Tools
- [grep manual](https://www.gnu.org/software/grep/manual/grep.html)
- [awk manual](https://www.gnu.org/software/gawk/manual/gawk.html)
- [sed manual](https://www.gnu.org/software/sed/manual/sed.html)

### Log Analysis
- [Apache Log Format](https://httpd.apache.org/docs/current/logs.html)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Bash Scripting
- [Bash Guide](https://mywiki.wooledge.org/BashGuide)
- [ShellCheck](https://www.shellcheck.net/) - Validate your scripts

### Course Materials
- Week 2 examples: `bash-basics`, `text-processing`, `data-pipelines`, `bash-scripts`
- Week 2 slides: Command line tools and pipelines