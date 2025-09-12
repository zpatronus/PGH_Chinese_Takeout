#!/bin/bash

set -euo pipefail

python3 generate.py

git add .
git commit -m "Update on $(date)"
git push