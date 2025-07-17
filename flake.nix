{
  description = "omice dev environment with Python 3.12 and SHACL tools";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        my-python = pkgs.python312.withPackages (ps: with ps; [
          rdflib
          matplotlib
          networkx
        ]);
      in {
        devShells.default = pkgs.mkShell {
          name = "omice";

          packages = [
            my-python
            pkgs.git
            pkgs.podman
            pkgs.pyright
          ];

          shellHook = ''
            echo "🐍 Python 3.12 dev environment ready!"
            echo "✔ rdflib, matplotlib, networkx pre-installed"
            echo "🛠 Custom commands available:"
            echo "  - shacl-validate [datafile] [shapesfile]"
            echo "  - shacl-infer [datafile] [shapesfile]"

            shacl-validate() {
              local datafile="''${1:-omice.ttl}"
              local shapesfile="''${2:-omice.ttl}"
              podman run --rm -v "$PWD":/data ghcr.io/ashleycaselli/shacl:latest \
                validate -datafile "/data/$datafile" -shapesfile "/data/$shapesfile"
            }

            shacl-infer() {
              local datafile="''${1:-omice.ttl}"
              local shapesfile="''${2:-omice.ttl}"
              podman run --rm -v "$PWD":/data ghcr.io/ashleycaselli/shacl:latest \
                infer -datafile "/data/$datafile" -shapesfile "/data/$shapesfile"
            }
          '';
        };
      });
}

