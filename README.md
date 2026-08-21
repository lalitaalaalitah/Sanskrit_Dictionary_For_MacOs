# 🕉️ Sanskrit Dictionaries for macOS

[![macOS Compatibility](https://img.shields.io/badge/macOS-10.11--27.*-brightgreen.svg?style=flat-square&logo=apple)](https://eng.lalitaalaalitah.com/sanskrit-dictionary-files-for-mac-os/)
[![Release](https://img.shields.io/badge/Release-v1.0.0-blue.svg?style=flat-square)](https://github.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs/releases)

A massive collection of **260+ Sanskrit dictionary bundles (~14GB)** optimized for the native macOS Dictionary app. Compatible with high-quality sources from GoldenDict, ColorDict, and EBDic.

🔗 **Official Website:** [eng.lalitaalaalitah.com](https://eng.lalitaalaalitah.com/sanskrit-dictionary-files-for-mac-os/)
📖 **Detailed Guide:** [HOW_TO_USE.md](HOW_TO_USE.md)

---

### 💻 Compatibility
| OS Version | Status |
| :--- | :--- |
| **macOS 10.11 - 27.1** | ✅ Confirmed Working |
| **Older Versions** | ❓ Untested |

---

### 🚀 Quick Installation

Because the collection is ~14GB, dictionaries are distributed via **GitHub Releases** to save bandwidth and disk space.

#### Option 1: Quick Terminal Installer
Run this single command in your macOS Terminal:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs/refs/heads/master/installer_script_from_release.sh)"
```

#### Option 2: Python Installer Script
```bash
uv run sanskrit_dict_installer.py
# Or using standard python
python3 sanskrit_dict_installer.py
```

#### Option 3: Nix & Home Manager Flake (See [Nix Installation](HOW_TO_USE.md#method-3-nix--home-manager-integration))
```nix
programs.sanskrit-dictionary.enable = true;
```

---

### 📚 Available Dictionaries
This repository contains **268** dictionaries.

<details>
<summary><b>📦 Click to expand full dictionary list sample</b></summary>

* `84k-glossary`
* `abhidhaanamanjarii`
* `abhidhAnachintAmaNi`
* `abhidhAnaratnamAlA`
* `abhyankara-grammar`
* `apte-1957`
* `apte-english-sanskrit`
* `aShTAdhyAyI-english`
* `Bohtlingk-and-Roth`
* `kalpadruma-sa`
* `vAchaspatyam-sa`
* `WordNet_3`
*(... and 250+ more)*

</details>

---

### 🛠 How to Activate After Installation
1. Open the **Dictionary** app on your Mac.
2. Open **Settings** / **Preferences** (`Cmd + ,`).
3. Scroll to the bottom of the list.
4. **Check the boxes** for the newly installed Sanskrit dictionaries to enable them.

---

### 🌟 Credits
* **Author:** [lalitaalaalitah](https://github.com/lalitaalaalitah)
* **Website:** [lalitaalaalitah.com](https://www.lalitaalaalitah.com)
* **Source Data:** [indic-dict/stardict-sanskrit](https://github.com/indic-dict/stardict-sanskrit)
* **Converter Tool:** [pyGlossary](https://github.com/ilius/pyglossary)
