{   
  pkgs ? import (fetchTarball 
    https://github.com/NixOS/nixpkgs/archive/refs/tags/21.11.tar.gz
  ) {}
}:
with pkgs.python39Packages;

pkgs.mkShell {
  buildInputs = [
    pandas numpy requests scikit-learn azure-storage-blob jupyter
    matplotlib seaborn
  ];
  shellHook = ''
    # Set environment variables
    export BPEXT_DATASETS_SAS_URL="$HOME/secret/azure/bpext-datasets-sas-url"

    # Fix vscode python settings
    mkdir -p .vscode
    cat > .vscode/settings.json <<EOF
    {
      "python.defaultInterpreterPath": "''$(which python)",
      "python.analysis.extraPaths": [ "''${PYTHONPATH//:/'", "'}" ],
    }
    EOF
    export PYTHONPATH="$PYTHONPATH:$PWD"
  '';
}
