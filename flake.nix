{
  description = "Sanskrit Dictionary files for macOS Dictionary.app";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        packages.default = pkgs.callPackage ./default.nix {};
      }
    ) // {
      homeManagerModules.default = { config, lib, pkgs, ... }:
        let
          cfg = config.programs.sanskrit-dictionary;
          appPkg = self.packages.${pkgs.stdenv.hostPlatform.system}.default;
        in
        {
          options.programs.sanskrit-dictionary = {
            enable = lib.mkEnableOption "Sanskrit Dictionary for macOS";
          };

          config = lib.mkIf cfg.enable {
            home.packages = [ appPkg ];
          };
        };
    };
}
