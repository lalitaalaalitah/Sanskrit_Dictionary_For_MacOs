# 🕉️ Sanskrit Dictionaries for macOS

[![macOS Compatibility](https://img.shields.io/badge/macOS-10.11--13.1-brightgreen.svg?style=flat-square&logo=apple)](https://eng.lalitaalaalitah.com/sanskrit-dictionary-files-for-mac-os/)
[![Release](https://img.shields.io/badge/Release-v1.0.0-blue.svg?style=flat-square)](https://github.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs/releases)

A massive collection of Sanskrit dictionary bundles optimized for the native macOS Dictionary app. These are compatible with the high-quality sources used in GoldenDict, ColorDict, and EBDic.

🔗 **Official Website:** [eng.lalitaalaalitah.com](https://eng.lalitaalaalitah.com/sanskrit-dictionary-files-for-mac-os/)

---

### 💻 Compatibility
| OS Version | Status |
| :--- | :--- |
| **macOS 10.11 - 27.1** | ✅ Confirmed Working |
| **Older Versions** | ❓ Untested (No promises) |

---

### 🚀 Quick Installation (New Method)
Because the collection has grown to **14GB**, the previous Python and Nix installers are deprecated. Use the new high-speed shell uploader/downloader.

**To install all dictionaries at once, run this in your Terminal:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs/refs/heads/master/installer_script_from_release.sh)"
```
**Note:** This will install all dictionaries, which is approximately 14GB of data. Please ensure you have enough disk space.
You may easily delete those which you don't want to keep later from `~/Library/Dictionaries`

---

### ⚠️ Deprecation Notice
> [!CAUTION]
> **Traditional Git-based installation is currently deprecated.**
> Due to the massive size (14GB+), dictionaries are now distributed via **GitHub Releases** as compressed `.zip` files.

<details>
<summary><b>View Deprecated Installation Methods (Python / Nix)</b></summary>

#### 1. Automated Installer Script
```bash
uv run sanskrit_dict_installer.py
# Or using standard python
python3 sanskrit_dict_installer.py
```

#### 2. Nix & Home Manager Integration
```nix
programs.sanskrit-dictionary.enable = true;
```
</details>

---

### 📚 Available Dictionaries
This repository contains **268** dictionaries. Click the button below to see the full list.

<details>
<summary><b>📦 Click to expand the full list of dictionaries</b></summary>

| Dictionary Name | Type |
| :--- | :--- |
| `84k-glossary` | Apple Dict |
| `abhidhaanamanjarii` | Apple Dict |
| `abhidhAnachintAmaNi` | Apple Dict |
| `abhidhAnaratnamAlA` | Apple Dict |
| `abhyankara-grammar` | Apple Dict |
| `apte-1957` | Apple Dict |
| `apte-english-sanskrit` | Apple Dict |
| `aShTAdhyAyI-english` | Apple Dict |
| `Bohtlingk-and-Roth` | Apple Dict |
| `kalpadruma-sa` | Apple Dict |
| `vAchaspatyam-sa` | Apple Dict |
| `WordNet_3` | Apple Dict |

*(... and 250+ more)*

**Full file list:**
```text
* 84k-glossary_apple_dict.dictionary
* abhidhaanamanjarii_apple_dict.dictionary
* abhidhAnachintAmaNi_apple_dict.dictionary
* abhidhAnachintAmaNiparishiShTa_apple_dict.dictionary
* abhidhAnachintAmaNishilonCha_apple_dict.dictionary
* abhidhAnaratnamAlA_apple_dict.dictionary
* abhyankara-grammar_apple_dict.dictionary
* abhyankara-grammar_apple_dict_roman.dictionary
* abhyankara-grammar_devanagari.dictionary
* AHD_Indo-European_and_Semitic_Roots_Supplement_apple_dict.dictionary
* AkhyAtachandrikA_apple_dict.dictionary
* AkhyAtachandrikA_devanagari.dictionary
* alar_apple_dict.dictionary
* amara-onto_apple_dict.dictionary
* American_Heritage_Dictionary_4th_Ed_apple_dict.dictionary
* American_Idioms_2nd_Ed_apple_dict.dictionary
* apte-1890_apple_dict.dictionary
* apte-1957_apple_dict.dictionary
* apte-bi_apple_dict.dictionary
* apte-english-sanskrit-cologne_apple_dict.dictionary
* aShTAdhyAyI-english_apple_dict.dictionary
* aufrecht-catalogus-catalogorum_apple_dict.dictionary
* Bohtlingk-and-Roth-Grosses-Petersburger-Worterbuch_apple_dict.dictionary
* Bohtlingk-Sanskrit-Worterbuch-in-kurzerer-Fassung_apple_dict.dictionary
* bopp_apple_dict.dictionary
* burnouf_apple_dict.dictionary
* capeller-sanskrit-english_apple_dict.dictionary
* Collins_Thesaurus_apple_dict.dictionary
* dictionnaire-heritage_du_sanskrit_san-fra_apple_dict.dictionary
* edgerton-buddhist-hybrid_apple_dict.dictionary
* hi-shabdasagar_apple_dict.dictionary
* kashika_apple_dict.dictionary
* macdonell_apple_dict.dictionary
* mw-cologne_apple_dict.dictionary
* Oxford_Advanced_Learner_s_Dictionary_apple_dict.dictionary
* pts_pali_apple_dict.dictionary
* vAchaspatyam-sa.dictionary
* whitney-roots_apple_dict.dictionary
* wilson_apple_dict.dictionary
* winslow_apple_dict.dictionary
* WordNet_3_apple_dict.dictionary
* yates_apple_dict.dictionary
* अभिधानमञ्जरी_apple_dict_devanagari.dictionary
```
</details>

---

### 🛠 How to Activate After Installation
1.  Open the **Dictionary** app on your Mac.
2.  Open **Settings** (Press `Cmd + ,`).
3.  Scroll to the bottom of the list.
4.  **Check the boxes** for the newly installed Sanskrit dictionaries to enable them.

---

### 🌟 Credits
*   **Source Data:** [indic-dict/stardict-sanskrit](https://github.com/indic-dict/stardict-sanskrit) for the high-quality source StarDict files.
* **Converter CLO**: [pyGlossary](https://github.com/ilius/pyglossary)
*   **Maintenance:** [lalitaalaalitah](https://github.com/lalitaalaalitah)

---
**[Back to top ↑](#sanskrit_dictionary_for_macos)**
