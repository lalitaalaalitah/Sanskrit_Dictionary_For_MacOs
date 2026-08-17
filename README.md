# Sanskrit_Dictionary_For_MacOs

https://eng.lalitaalaalitah.com/sanskrit-dictionary-files-for-mac-os/


These are dictionary files for Mac OS dictionary app. These are similar to those which are being used with GoldenDict or ColorDict or EBDic.

* These work for 10.11-13.1(confirmed). I don't have access to older Mac OS versions, so no promises for them.

## Installation Options

You can install these dictionaries using the automated installer script or integrate them declaratively using Nix and Home Manager. See [HOW_TO_USE.md](file:///Volumes/Cablet_WD_2TB_20251206/05_Development/Github/02_Sanskrit_Dev/03_Sanskrit_Dictionary_For_MacOs/01_Sanskrit_Dictionary_For_MacOs/HOW_TO_USE.md) for detailed instructions.

### 1. Automated Installer Script

Run the following command in the cloned repository to install the dictionaries:

```bash
uv run sanskrit_dict_installer.py
# Or using standard python
python3 sanskrit_dict_installer.py
```

### 2. Nix & Home Manager Integration

If you use Nix-Darwin and Home Manager, you can enable the dictionaries in your custom applications configuration:

```nix
programs.sanskrit-dictionary.enable = true;
```

## These Dictionaries are working correctly:
```
* abhyankara-grammar_apple_dict_roman.dictionary
* abhyankara-grammar_devanagari.dictionary
* AHD_Indo-European_and_Semitic_Roots_Supplement_apple_dict_roman.dictionary
* AkhyAtachandrikA_apple_dict_roman.dictionary
* AkhyAtachandrikA_devanagari.dictionary
* AkhyAtachandrikA_dict_devanagari.dictionary
* amara-ont_apple_dict_roman.dictionary
* amara-onto_devanagari.dictionary
* American_Heritage_Dictionary_4th_Ed_apple_dict.dictionary
* American_Idioms_2nd_Ed_apple_dict.dictionary
* apte-sa_apple_dict_roman.dictionary
* aShTAdhyAyI-anuvRtt_apple_dict_roman_devanagari.dictionary
* aShTAdhyAyI-english_apple_dict_roman_devanagari.dictionary
* balamanorama_apple_dict_devanagari.dictionary
* bloomfield-vedic-sa_apple_dict_roman_devanagari.dictionary
* bopp_apple_dict_roman_devanagari.dictionary
* Chandas_apple_dict_roman_devanagari.dictionary
* Collins_Thesaurus_apple_dict_eng_roman.dictionary
* computer-shrIkAnta_apple_dict_eng_san_roman.dictionary
* dcs-frequency_apple_dict_roman_devanagari.dictionary
* Declension-A-01_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-02_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-03_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-04_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-05_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-06_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-07_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-08_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-09_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A-10_10-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-A1-heritage_du_sanskrit_san-san_apple_dict_roman_devanagari.dictionary
* Declension-A2-heritage_du_sanskrit_san-san_apple_dict_roman_devanagari.dictionary
* Declension-A3-heritage_du_sanskrit_san-san_apple_dict_roman_devanagari.dictionary
* Declension-A4-heritage_du_sanskrit_san-san_apple_dict_roman_devanagari.dictionary
* Declension-A5-heritage_du_sanskrit_san-san_apple_dict_roman_devanagari.dictionary
* Declension-B-1_3-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-B-2_3-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-B-3_3-heritage_du_sanskrit_san-eng_apple_dict_roman_devanagari.dictionary
* Declension-B-heritage_du_sanskrit_san-san_apple_dict_roman_devanagari.dictionary
* dhAtu-pATha-kRShNAchArya_apple_dict_roman_devanagari.dictionary
* dhAtupATha-sa_apple_dict.dictionary
* ekAkSharanAmamAlA_apple_dict.dictionary
* jnu-tiNanta_apple_dict.dictionary
* kalpadruma-sa.dictionary
* kalpadruma-sa_apple_dict.dictionary
* mw-bi-itrans-dev.dictionary
* mw-sa_apple_dict.dictionary
* padamanjari-apple.dictionary
* padamanjarI.dictionary
* padamanjarI_apple_dict.dictionary
* pali-en-pa_apple_dict.dictionary
* siddhAnta-kaumudI.dictionary
* siddhAnta-kaumudI_apple_dict.dictionary
* vAchaspatyam-sa.dictionary
* vedic-rituals-h_apple_dict.dictionary
* अभिधानमञ्जरी_apple_dict_devanagari.dictionary
```
## Credits:

* https://github.com/indic-dict/stardict-sanskrit for source stardict files
