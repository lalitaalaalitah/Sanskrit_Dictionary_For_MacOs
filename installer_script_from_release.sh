#!/bin/bash

# Configuration
REPO="lalitaalaalitah/Sanskrit_Dictionary_For_MacOs"
INSTALL_DIR="$HOME/Library/Dictionaries"
TEMP_DIR="/tmp/dictionary_download"

echo "================================================"
echo "   Apple Dictionary Bulk Installer"
echo "================================================"

# 1. Create the destination directory if it doesn't exist
mkdir -p "$INSTALL_DIR"
mkdir -p "$TEMP_DIR"

echo "Fetching file list from GitHub..."

# 2. Get all download URLs from the latest release using the GitHub API
# This avoids needing the GitHub CLI (gh) on the user's machine
URLS=$(curl -s "https://api.github.com/repos/$REPO/releases/latest" | grep "browser_download_url" | cut -d '"' -f 4)

if [ -z "$URLS" ]; then
    echo "Error: No dictionaries found in the latest release."
    exit 1
fi

COUNT=$(echo "$URLS" | wc -l | xargs)
echo "Found $COUNT dictionaries. Starting download (approx 14GB total)..."
echo "Target: $INSTALL_DIR"

# 3. Download and install each file
i=1
for url in $URLS; do
    filename=$(basename "$url")

    echo "[$i/$COUNT] Downloading $filename..."

    # Download to temp folder
    curl -L "$url" -o "$TEMP_DIR/$filename"

    echo "Installing $filename..."
    # Unzip directly into the macOS Dictionaries folder
    # -q: quiet, -o: overwrite, -n: skip existing (use -o to ensure updates work)
    unzip -q -o "$TEMP_DIR/$filename" -d "$INSTALL_DIR"

    # Remove the zip to save space
    rm "$TEMP_DIR/$filename"

    ((i++))
done

echo "------------------------------------------------"
echo "SUCCESS: $COUNT dictionaries installed."
echo "------------------------------------------------"
echo "TO ACTIVATE:"
echo "1. Open the 'Dictionary' app on your Mac."
echo "2. Go to Settings (Cmd + ,)."
echo "3. Scroll to the bottom and check the boxes for the new dictionaries."
echo "------------------------------------------------"

# Clean up
rm -rf "$TEMP_DIR"
