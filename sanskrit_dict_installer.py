#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

"""
Sanskrit Dictionary Installer for macOS
=======================================
Author: lalitaalaalitah
Website: https://www.lalitaalaalitah.com
GitHub Profile: https://github.com/lalitaalaalitah
Version: 1.0.0

An automated tool to download, extract, and install Sanskrit .dictionary files 
into the macOS native Dictionary application from GitHub Releases.
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
import urllib.request
import zipfile

__version__ = "1.0.0"

# Catppuccin Mocha 24-bit Truecolor ANSI Palette (Base background: #1e1e2e)
BG_BASE = "\033[48;2;30;30;46m"
FG_TEXT = "\033[38;2;205;214;244m"
# Smart reset preserves the base background and default text colors
CLR_RESET = "\033[0;48;2;30;30;46;38;2;205;214;244m"

# Style Foregrounds
COLOR_ROSEWATER = "\033[38;2;245;224;220m"
COLOR_PINK = "\033[38;2;245;194;231m"
COLOR_MAUVE = "\033[38;2;203;166;247m"
COLOR_RED = "\033[38;2;243;139;168m"
COLOR_YELLOW = "\033[38;2;249;226;175m"
COLOR_GREEN = "\033[38;2;166;227;161m"
COLOR_TEAL = "\033[38;2;148;226;213m"
COLOR_BLUE = "\033[38;2;137;180;250m"

BANNER = f"""{COLOR_MAUVE}╔══════════════════════════════════════════════════════════════════╗
║                   Sanskrit Dictionary Installer                  ║
║                                                                  ║
║  Author: lalitaalaalitah                                         ║
║  Website: https://www.lalitaalaalitah.com                         ║
║  GitHub: https://github.com/lalitaalaalitah                      ║
║  Version: {__version__:<55}║
╚══════════════════════════════════════════════════════════════════╝{CLR_RESET}"""

REPO = "lalitaalaalitah/Sanskrit_Dictionary_For_MacOs"
API_URL = f"https://api.github.com/repos/{REPO}/releases/latest"

def print_color(text, end="\n"):
    """Print wrapper to enforce Catppuccin base styling."""
    sys.stdout.write(f"{BG_BASE}{FG_TEXT}{text}{CLR_RESET}{end}")
    sys.stdout.flush()

def print_error(text):
    """Prints a styled error message."""
    print_color(f"{COLOR_RED}Error: {text}{CLR_RESET}")

def print_warning(text):
    """Prints a styled warning message."""
    print_color(f"{COLOR_YELLOW}Warning: {text}{CLR_RESET}")

def get_release_zip_urls():
    """Fetches dictionary zip asset download URLs from GitHub Releases API."""
    print_color(f"{COLOR_BLUE}Fetching latest release metadata from GitHub API...{CLR_RESET}")
    req = urllib.request.Request(
        API_URL,
        headers={'User-Agent': 'Sanskrit-Dict-Installer/1.0 (macOS)'}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            assets = data.get('assets', [])
            urls = [
                asset['browser_download_url']
                for asset in assets
                if asset.get('name', '').endswith('.zip') or asset.get('browser_download_url', '').endswith('.zip')
            ]
            if not urls:
                # Fallback to all browser_download_urls if zip filter returns empty
                urls = [asset['browser_download_url'] for asset in assets if 'browser_download_url' in asset]
            return urls
    except Exception as e:
        print_error(f"Failed to fetch release assets from GitHub API: {e}")
        return []

def download_file(url, dest_path):
    """Download a file from URL with basic progress output."""
    filename = os.path.basename(dest_path)
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    )
    try:
        with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as f:
            total_size = int(response.headers.get('content-length', 0))
            chunk_size = 1024 * 1024  # 1MB chunks
            downloaded = 0
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    mb_down = downloaded / (1024 * 1024)
                    mb_tot = total_size / (1024 * 1024)
                    print_color(f"\r{COLOR_TEAL}[Downloading {filename}] {percent:.1f}% ({mb_down:.1f}/{mb_tot:.1f} MB){CLR_RESET}", end="")
                else:
                    mb_down = downloaded / (1024 * 1024)
                    print_color(f"\r{COLOR_TEAL}[Downloading {filename}] {mb_down:.1f} MB{CLR_RESET}", end="")
            print_color("")
        return True
    except Exception as e:
        print_error(f"Failed to download {filename}: {e}")
        return False

def install_from_directory(src_dir, target_dir, force=False):
    """Copies all .dictionary directories from src_dir to target_dir."""
    if not os.path.isdir(src_dir):
        print_error(f"Source directory {src_dir} does not exist.")
        return False
        
    dict_folders = [d for d in os.listdir(src_dir) if d.endswith(".dictionary")]
    if not dict_folders:
        print_warning(f"No .dictionary directories found in {src_dir}")
        return False
        
    print_color(f"\n{COLOR_BLUE}Installing {len(dict_folders)} dictionaries to {target_dir}...{CLR_RESET}")
    os.makedirs(target_dir, exist_ok=True)
    
    installed_count = 0
    skipped_count = 0
    
    for df in sorted(dict_folders):
        src_path = os.path.join(src_dir, df)
        dest_path = os.path.join(target_dir, df)
        
        if os.path.exists(dest_path):
            if not force:
                skipped_count += 1
                continue
            else:
                print_color(f"{COLOR_PINK}Overwriting existing {df}...{CLR_RESET}")
                if os.path.isdir(dest_path) and not os.path.islink(dest_path):
                    shutil.rmtree(dest_path)
                else:
                    os.remove(dest_path)
        
        try:
            shutil.copytree(src_path, dest_path)
            installed_count += 1
            print_color(f"{COLOR_GREEN}✓ Installed {df}{CLR_RESET}")
        except Exception as e:
            print_error(f"Failed to install {df}: {e}")
            
    print_color(f"\n{COLOR_GREEN}Installation complete!{CLR_RESET}")
    print_color(f"{COLOR_BLUE}Installed: {installed_count}, Skipped: {skipped_count} (already exist).{CLR_RESET}")
    if skipped_count > 0:
        print_color(f"{COLOR_YELLOW}Use --force (or -f) to overwrite skipped dictionaries.{CLR_RESET}")
    return True

def extract_and_install_zip(zip_path, target_dir):
    """Extracts a zip file directly into target_dir."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(path=target_dir)
        return True
    except Exception as e:
        print_error(f"Failed to extract {os.path.basename(zip_path)}: {e}")
        return False

def print_post_install_instructions():
    """Prints instructions for Dictionary.app activation."""
    print_color(f"\n{COLOR_MAUVE}================================================================{CLR_RESET}")
    print_color(f"{COLOR_MAUVE}📝 Post-Installation Steps:{CLR_RESET}")
    print_color(f"{COLOR_MAUVE}================================================================{CLR_RESET}")
    print_color(f"{COLOR_ROSEWATER}1. Open the Dictionary application on your Mac.{CLR_RESET}")
    print_color(f"{COLOR_ROSEWATER}2. Go to the menu bar: Dictionary -> Preferences (or Command + ,).{CLR_RESET}")
    print_color(f"{COLOR_ROSEWATER}3. Scroll down and check the boxes for the newly installed Sanskrit dictionaries.{CLR_RESET}")
    print_color(f"{COLOR_ROSEWATER}4. Drag the dictionaries up or down to set search priority order.{CLR_RESET}")
    print_color(f"{COLOR_MAUVE}================================================================{CLR_RESET}\n")

def main():
    parser = argparse.ArgumentParser(description="Downloads and installs Sanskrit dictionaries for macOS Dictionary.app")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    parser.add_argument("-f", "--force", action="store_true", help="Force overwrite of already installed dictionaries")
    args = parser.parse_args()

    if args.version:
        print_color(f"Sanskrit Dictionary Installer v{__version__}")
        sys.exit(0)

    # Set terminal colors
    sys.stdout.write(f"{BG_BASE}{FG_TEXT}")
    sys.stdout.flush()
    print_color(BANNER)

    target_dir = os.path.expanduser("~/Library/Dictionaries")
    script_dir = os.path.dirname(os.path.realpath(__file__))
    local_dicts = os.path.join(script_dir, "dictionaries")

    # 4-Tier Asset Resolution Check
    if os.path.isdir(local_dicts) and any(d.endswith(".dictionary") for d in os.listdir(local_dicts)):
        print_color(f"{COLOR_GREEN}Found local dictionaries folder in repository: {local_dicts}{CLR_RESET}")
        success = install_from_directory(local_dicts, target_dir, args.force)
        if success:
            print_post_install_instructions()
    else:
        print_color(f"{COLOR_YELLOW}No local dictionaries folder found. Downloading release assets from GitHub...{CLR_RESET}")
        urls = get_release_zip_urls()
        if not urls:
            print_error("No release zip files found to download.")
            sys.exit(1)

        print_color(f"{COLOR_BLUE}Found {len(urls)} release files to download and install.{CLR_RESET}")
        os.makedirs(target_dir, exist_ok=True)

        with tempfile.TemporaryDirectory() as temp_dir:
            success_count = 0
            for i, url in enumerate(urls, 1):
                filename = os.path.basename(url)
                dest_zip = os.path.join(temp_dir, filename)
                print_color(f"[{i}/{len(urls)}] Processing {filename}...")
                if download_file(url, dest_zip):
                    if extract_and_install_zip(dest_zip, target_dir):
                        success_count += 1
                    if os.path.exists(dest_zip):
                        os.remove(dest_zip)

            print_color(f"\n{COLOR_GREEN}Successfully processed {success_count}/{len(urls)} dictionary releases into {target_dir}.{CLR_RESET}")
            print_post_install_instructions()

    sys.stdout.write(CLR_RESET + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
