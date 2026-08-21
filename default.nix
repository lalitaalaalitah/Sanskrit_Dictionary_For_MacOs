{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation rec {
  pname = "sanskrit-dictionary-for-macos";
  version = "1.0.0";

  src = ./.;

  nativeBuildInputs = [ pkgs.makeWrapper ];
  buildInputs = [ pkgs.python3 pkgs.curl pkgs.unzip ];

  dontConfigure = true;
  dontBuild = true;

  installPhase = ''
    mkdir -p $out/bin

    # Copy the installer script
    cp sanskrit_dict_installer.py $out/bin/sanskrit-dict-installer
    chmod +x $out/bin/sanskrit-dict-installer

    # Convert the uv run shebang to env python3 and patch shebangs
    sed -i 's|#!/usr/bin/env uv run|#!/usr/bin/env python3|' $out/bin/sanskrit-dict-installer
    patchShebangs $out/bin/sanskrit-dict-installer

    # Wrap binary to ensure curl and unzip are in PATH if needed at runtime
    wrapProgram $out/bin/sanskrit-dict-installer \
      --prefix PATH : ${pkgs.lib.makeBinPath [ pkgs.curl pkgs.unzip pkgs.python3 ]}
  '';

  meta = with pkgs.lib; {
    description = "Sanskrit Dictionary files for macOS Dictionary.app with an automated installer";
    homepage = "https://github.com/lalitaalaalitah/Sanskrit_Dictionary_For_MacOs";
    license = licenses.mit;
    platforms = platforms.darwin;
    maintainers = [ "lalitaalaalitah" ];
  };
}
