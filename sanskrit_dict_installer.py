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
into the macOS native Dictionary application.
"""

import argparse
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

GITHUB_ZIP_URL = "https://github.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs/archive/refs/heads/master.zip"

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

def download_with_progress(url, dest_path):
    """Download file from url with a progress display."""
    print_color(f"{COLOR_BLUE}Downloading dictionaries archive from GitHub...{CLR_RESET}")
    print_color(f"{COLOR_BLUE}Source URL: {url}{CLR_RESET}")
    
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            total_size = int(response.headers.get('content-length', 0))
            chunk_size = 1024 * 1024  # 1MB chunks
            downloaded = 0
            
            with open(dest_path, 'wb') as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        mb_downloaded = downloaded / (1024 * 1024)
                        mb_total = total_size / (1024 * 1024)
                        print_color(f"\r{COLOR_TEAL}Progress: {percent:.2f}% ({mb_downloaded:.1f}/{mb_total:.1f} MB){CLR_RESET}", end="")
                    else:
                        mb_downloaded = downloaded / (1024 * 1024)
                        print_color(f"\r{COLOR_TEAL}Downloaded: {mb_downloaded:.1f} MB{CLR_RESET}", end="")
            print_color("")  # New line after completion
    except Exception as e:
        print_error(f"Failed to download archive: {e}")
        sys.exit(1)

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

def extract_and_install_from_zip(zip_path, target_dir, force=False):
    """Selectively extracts and installs dictionaries from repository ZIP."""
    print_color(f"{COLOR_BLUE}Processing downloaded zip archive...{CLR_RESET}")
    
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                members = zip_ref.namelist()
                
                # Check for standard folder prefixes
                prefixes = [
                    "Sanskrit_Dictionary_For_MacOs-master/01_Sanskrit_Dictionary_For_MacOs/dictionaries/",
                    "Sanskrit_Dictionary_For_MacOs-master/dictionaries/",
                    "dictionaries/"
                ]
                
                dict_prefix = None
                dict_members = []
                
                for pref in prefixes:
                    matched = [m for m in members if m.startswith(pref)]
                    if matched:
                        dict_prefix = pref
                        dict_members = matched
                        break
                        
                if not dict_prefix:
                    # Generic traversal search if the directory structure changes
                    for m in members:
                        if "/dictionaries/" in m:
                            parts = m.split("/dictionaries/")
                            dict_prefix = parts[0] + "/dictionaries/"
                            dict_members = [x for x in members if x.startswith(dict_prefix)]
                            break
                            
                if not dict_prefix:
                    print_error("Could not locate 'dictionaries/' directory structure inside the downloaded ZIP.")
                    sys.exit(1)
                    
                print_color(f"{COLOR_BLUE}Extracting dictionary files (selective extraction)...{CLR_RESET}")
                zip_ref.extractall(path=temp_dir, members=dict_members)
                
                # Locate the extracted folder
                extracted_dicts_path = os.path.join(temp_dir, dict_prefix)
                if not os.path.isdir(extracted_dicts_path):
                    for root, dirs, _ in os.walk(temp_dir):
                        if os.path.basename(root) == "dictionaries":
                            extracted_dicts_path = root
                            break
                            
                if os.path.isdir(extracted_dicts_path):
                    return install_from_directory(extracted_dicts_path, target_dir, force)
                else:
                    print_error("Could not find extracted dictionaries directory.")
                    return False
    except Exception as e:
        print_error(f"An error occurred while unzipping: {e}")
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
    parser.add_argument("-d", "--download-only", action="store_true", help="Only download/extract, do not install to Library/Dictionaries")
    args = parser.parse_args()

    if args.version:
        print_color(f"Sanskrit Dictionary Installer v{__version__}")
        sys.exit(0)

    # Reset screen style with base background and display banner
    sys.stdout.write(f"{BG_BASE}{FG_TEXT}")
    sys.stdout.flush()
    print_color(BANNER)

    target_dir = os.path.expanduser("~/Library/Dictionaries")
    
    # 4-Tier Asset Resolution Chain
    # Tier 1 & 2: Local folder / cloned repo
    script_dir = os.path.dirname(os.path.realpath(__file__))
    local_dicts = os.path.join(script_dir, "dictionaries")
    
    # Tier 3: Nix Store relative resolution
    nix_dicts = os.path.abspath(os.path.join(script_dir, "..", "share", "Dictionaries"))
    
    source_dir = None
    
    if os.path.isdir(local_dicts) and any(d.endswith(".dictionary") for d in os.listdir(local_dicts)):
        print_color(f"{COLOR_GREEN}Found local dictionaries in repository clone: {local_dicts}{CLR_RESET}")
        source_dir = local_dicts
    elif os.path.isdir(nix_dicts) and any(d.endswith(".dictionary") for d in os.listdir(nix_dicts)):
        print_color(f"{COLOR_GREEN}Found dictionaries in Nix Store location: {nix_dicts}{CLR_RESET}")
        source_dir = nix_dicts
        
    if source_dir:
        # Install from local source
        success = install_from_directory(source_dir, target_dir, args.force)
        if success:
            print_post_install_instructions()
    else:
        # Tier 4: Fallback to Download
        print_color(f"{COLOR_YELLOW}No local dictionaries found. Falling back to downloading from GitHub.{CLR_RESET}")
        
        with tempfile.TemporaryDirectory() as temp_download_dir:
            zip_path = os.path.join(temp_download_dir, "master.zip")
            download_with_progress(GITHUB_ZIP_URL, zip_path)
            
            if args.download_only:
                print_color(f"{COLOR_GREEN}Download completed. File saved at: {zip_path}{CLR_RESET}")
            else:
                success = extract_and_install_from_zip(zip_path, target_dir, args.force)
                if success:
                    print_post_install_instructions()

    # Final cleanup to leave terminal clean
    sys.stdout.write(CLR_RESET + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
