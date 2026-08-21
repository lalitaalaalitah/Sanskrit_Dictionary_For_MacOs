#!/bin/bash


# """
# Sanskrit Dictionary Installer for macOS
# =======================================
# Author: lalitaalaalitah
# Website: https://www.lalitaalaalitah.com
# GitHub Profile: https://github.com/lalitaalaalitah
# Version: 1.0.0

# An automated tool to download, extract, and install Sanskrit .dictionary files
# into the macOS native Dictionary application.
# """

# Configuration
# --- Color Definitions ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# --- Configuration ---
REPO="lalitaalaalitah/Sanskrit_Dictionary_For_MacOs"
WEBSITE="https://www.lalitaalaalitah.com"
INSTALL_DIR="$HOME/Library/Dictionaries"
TEMP_DIR="/tmp/sanskrit_dict_temp"

# --- Visual Banner ---
clear
echo -e "${PURPLE}================================================================${NC}"
echo -e "${BOLD}       🪔  SANSKRIT DICTIONARY INSTALLER FOR MACOS  🪔${NC}"
echo -e "${PURPLE}================================================================${NC}"
echo -e "${BOLD}Author:${NC}   lalitaalaalitah"
echo -e "${BOLD}Version:${NC}  1.0.0"
echo -e "${BOLD}Website:${NC}  ${BLUE}$WEBSITE${NC}"
echo -e "${BOLD}GitHub:${NC}   https://github.com/$REPO"
echo -e "${PURPLE}----------------------------------------------------------------${NC}"
echo -e "${BOLD}Target:${NC}   $INSTALL_DIR"
echo -e "${BOLD}Data:${NC}     ~14.0 GB (Total Collection)"
echo -e "${PURPLE}================================================================${NC}"
echo ""


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
