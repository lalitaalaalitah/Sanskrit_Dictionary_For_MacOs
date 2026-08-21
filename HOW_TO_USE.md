# How to Use the Sanskrit Dictionary Installer for macOS

Author: `lalitaalaalitah`  
Website: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
GitHub Profile: [https://github.com/lalitaalaalitah](https://github.com/lalitaalaalitah)  
Version: `1.0.0`

This repository provides **260+ Sanskrit dictionary bundles** (~14GB) optimized for the native macOS Dictionary application. The dictionaries are hosted on GitHub Releases as compressed archives to allow fast, efficient installation.

---

## Method 1: Quick Shell Installer (Recommended)

To install all Sanskrit dictionaries directly into `~/Library/Dictionaries` without cloning the repository or installing additional software:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs/refs/heads/master/installer_script_from_release.sh)"
```

---

## Method 2: Automated Python Installer

You can also use `sanskrit_dict_installer.py` using `uv` or standard Python 3.

### Running with `uv` or `python3`:

```bash
# Using uv (Recommended)
uv run sanskrit_dict_installer.py

# Or using standard python
python3 sanskrit_dict_installer.py
```

### Options:

* **Version:** View installer version.
  ```bash
  uv run sanskrit_dict_installer.py --version
  ```
* **Force Overwrite:** Force overwrite of existing dictionaries in `~/Library/Dictionaries`:
  ```bash
  uv run sanskrit_dict_installer.py --force
  ```

---

## Method 3: Nix & Home Manager Integration

If you manage your macOS environment with Nix Flakes and Home Manager, you can include the package and run `sanskrit-dict-installer`.

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

### 2. Enable in Home Manager Configuration

Import the module in your custom apps configuration (e.g., `~/nix/custom_apps/darwin/sanskrit-dictionary.nix`):

```nix
{ config, lib, pkgs, sanskrit-dictionary, ... }:
{
  imports = [
    sanskrit-dictionary.homeManagerModules.default
  ];

  programs.sanskrit-dictionary.enable = true;
}
```

After building your system, run `sanskrit-dict-installer` from your terminal to download and install the dictionaries.

---

## Post-Installation Activation Steps

Once downloaded and extracted into `~/Library/Dictionaries`:

1. Open the **Dictionary** application on your Mac (`/System/Applications/Dictionary.app` or via Spotlight).
2. Open **Settings** / **Preferences** by pressing `Cmd + ,`.
3. Scroll down to the bottom of the dictionary list.
4. **Check the boxes** next to the newly installed Sanskrit dictionaries to enable them.
5. Drag dictionaries up or down to set search priority order.
