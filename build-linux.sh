#!/bin/bash

cargo build --release
mkdir -p ./package
cp ./target/release/libsudokux_minlex.so ./package/sudokux_minlex.so
