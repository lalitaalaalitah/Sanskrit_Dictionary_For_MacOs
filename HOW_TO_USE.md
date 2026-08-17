# How to Use the Sanskrit Dictionary Installer

This repository provides Sanskrit dictionary files for the native macOS Dictionary application. You can install them manually, use the automated Python installer script, or automate installation using Nix and Home Manager.

---

## Method 1: Cloned Repository Installation (Recommended)

If you have cloned the repository, you can run the installer script directly. It will detect the local dictionaries and copy them to your native macOS Dictionary directory without performing any downloads.

### Prerequisites

Make sure you have `uv` installed. If you do not have `uv`, you can run the script using standard Python 3.

### Running the Installer

Navigate to the repository directory and run:

```bash
uv run sanskrit_dict_installer.py
# Or using standard python
python3 sanskrit_dict_installer.py
```

### Options

* **Force Overwrite:** If you want to overwrite any previously installed dictionaries, use the `--force` (or `-f`) flag:
  ```bash
  uv run sanskrit_dict_installer.py --force
  ```

---

## Method 2: Standalone Script Installation (Zero Clone)

If you don't want to clone the entire 1.2 GB repository, you can download only the `sanskrit_dict_installer.py` script and run it. The script will automatically download the dictionaries from GitHub, extract them selectively to a temporary folder, and install them.

```bash
# Download the script
curl -o sanskrit_dict_installer.py https://raw.githubusercontent.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs/master/sanskrit_dict_installer.py

# Run the installer
uv run sanskrit_dict_installer.py
```

---

## Method 3: Nix & Home Manager Automation

If you manage your macOS system using Nix and Home Manager, you can declare the installation in your system flake. This will automatically link the dictionaries into `~/Library/Dictionaries` during system rebuilds.

### 1. Add Flake Input

Add the repository input to your system `flake.nix` (e.g., `~/nix/flake.nix`):

```nix
inputs = {
  sanskrit-dictionary = {
    url = "github:lalitaalaalitah/Sanskrit_Dictionary_For_MacOs";
    inputs.nixpkgs.follows = "nixpkgs";
  };
};
```

And receive `sanskrit-dictionary` in the arguments list of your `outputs` function.

### 2. Enable in Home Manager Configuration

Import the module in your custom apps config (e.g., `~/nix/custom_apps/darwin/sanskrit-dictionary.nix`):

```nix
{ config, lib, pkgs, sanskrit-dictionary, ... }:
{
  imports = [
    sanskrit-dictionary.homeManagerModules.default
  ];

  programs.sanskrit-dictionary.enable = true;
}
```

This configuration adds the package to your path and link all dictionaries recursively into `~/Library/Dictionaries`.

---

## Post-Installation Activation Steps

Once installed, macOS Dictionary.app needs to be configured to look up words in the new dictionaries:

1. Open the **Dictionary** application on your Mac.
2. In the menu bar, go to **Dictionary** -> **Preferences** (or press `Command` + `,`).
3. Scroll down the list of active dictionaries and check the boxes next to the newly installed Sanskrit dictionaries to enable them.
4. You can drag the dictionaries up or down to set their search priority.
