#!/usr/bin/env bash
# Launch the Houssam Ascension control center (GUI with CLI fallback).
# Adjust PYTHON to point to your interpreter or virtual environment.
PYTHON=${PYTHON:-python3}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$SCRIPT_DIR"
$PYTHON main.py
