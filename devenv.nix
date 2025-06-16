# devenv.nix
{ pkgs, ... }:

let
  my-python = pkgs.python312.withPackages (ps: with ps; [
    rdflib
    matplotlib
    networkx
  ]);
in
{
  name = "omice";

  packages = [
    my-python
    pkgs.git
  ];

  languages.python.enable = true;
  #languages.python.version = "3.12";

  enterShell = ''
    echo "🐍 Python 3.12 dev environment ready!"
    echo "✔ rdflib, matplotlib, networkx pre-installed"
  '';
}

