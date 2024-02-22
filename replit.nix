{ pkgs }: {
  deps = [
    pkgs.magic-vlsi
    pkgs.stow
    pkgs.zsh
    pkgs.python311Packages.flake8
    pkgs.httpie
  ];
}