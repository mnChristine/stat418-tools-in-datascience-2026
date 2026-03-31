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

# Made with Bob
