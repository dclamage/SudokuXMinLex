@echo off
cargo build --release
if not exist ".\package" mkdir ".\package"
copy ".\target\release\sudokux_minlex.dll" ".\package\sudokux_minlex.pyd"
