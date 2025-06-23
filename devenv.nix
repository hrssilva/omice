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
    pkgs.podman
  ];

  languages.python.enable = true;
  #languages.python.version = "3.12";

  # Define custom commands
  scripts = {
    shacl-validate.exec = ''
    podman run --rm -v ./:/data ghcr.io/ashleycaselli/shacl:latest validate -datafile /data/omice.ttl -shapesfile /data/omice.ttl
    '';

    shacl-infer.exec = ''
    podman run --rm -v ./:/data ghcr.io/ashleycaselli/shacl:latest infer -datafile /data/omice.ttl -shapesfile /data/omice.ttl
    '';
  };


  enterShell = ''
    echo "🐍 Python 3.12 dev environment ready!"
    echo "✔ rdflib, matplotlib, networkx pre-installed"
    echo "🛠 Custom commands available:"
    echo "  - shacl-validate"
    echo "  - shacl-infer"
  '';
}

