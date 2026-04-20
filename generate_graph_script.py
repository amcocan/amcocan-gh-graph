#!/usr/bin/env python3
import sys
from datetime import datetime, timedelta

# Exact filled positions extracted from the attached image (row 0 = top-left square = Jan 2 2000, columns go right)
filled_positions = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 6), (0, 10), (0, 12), (0, 13), (0, 14),
    (0, 15), (0, 16), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 24), (0, 25), (0, 26),
    (0, 27), (0, 28), (0, 30), (0, 31), (0, 32), (0, 33), (0, 34), (0, 36), (0, 40), (0, 43),
    (0, 44), (0, 46), (0, 47), (0, 48), (0, 49),
    (1, 0), (1, 4), (1, 6), (1, 10), (1, 12), (1, 16), (1, 18), (1, 22), (1, 24), (1, 28),
    (1, 30), (1, 34), (1, 36), (1, 40), (1, 43), (1, 44), (1, 46), (1, 47), (1, 48), (1, 49),
    (2, 0), (2, 4), (2, 6), (2, 7), (2, 9), (2, 10), (2, 12), (2, 18), (2, 22), (2, 24),
    (2, 30), (2, 34), (2, 36), (2, 37), (2, 40), (2, 46), (2, 47), (2, 48), (2, 49),
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 6), (3, 8), (3, 10), (3, 12), (3, 18),
    (3, 22), (3, 24), (3, 30), (3, 31), (3, 32), (3, 33), (3, 34), (3, 36), (3, 38), (3, 40),
    (3, 43), (3, 44), (3, 46), (3, 47), (3, 48), (3, 49),
    (4, 0), (4, 4), (4, 6), (4, 10), (4, 12), (4, 18), (4, 22), (4, 24), (4, 30), (4, 34),
    (4, 36), (4, 39), (4, 40), (4, 43), (4, 44),
    (5, 0), (5, 4), (5, 6), (5, 10), (5, 12), (5, 16), (5, 18), (5, 22), (5, 24), (5, 28),
    (5, 30), (5, 34), (5, 36), (5, 40), (5, 43), (5, 44), (5, 45), (5, 46), (5, 47), (5, 48),
    (5, 49),
    (6, 0), (6, 4), (6, 6), (6, 10), (6, 12), (6, 13), (6, 14), (6, 15), (6, 16), (6, 18),
    (6, 19), (6, 20), (6, 21), (6, 22), (6, 24), (6, 25), (6, 26), (6, 27), (6, 28), (6, 30),
    (6, 34), (6, 36), (6, 40), (6, 43), (6, 44), (6, 45), (6, 46), (6, 47), (6, 48), (6, 49),
]

print("#!/bin/bash")
print("echo 'Building GitHub contribution graph artwork...'")
print("mkdir -p amcocan-gh-graph")
print("cd amcocan-gh-graph")
print("git init")
print("git remote add origin https://github.com/amcocan/amcocan-gh-graph.git")
print("git pull origin main || true")
print("FILE=4e4fbf3ba7d3fa51fc18b76eafd6e8ec1c2e3aa1be30b25f78798af39906b71f9ac0842686e0b4baf28bf165a2cac1b3b9011c6305f88164a711cfc5162603ad")
print("touch $FILE")

# Sort positions chronologically so commits happen in date order (nice for git history)
positions = sorted(filled_positions, key=lambda p: p[1]*7 + p[0])

for r, c in positions:
    # Calculate exact date: top-left = Jan 10 2000 (row 0, col 0)
    days_offset = c * 7 + r
    dt = datetime(2000, 1, 10) + timedelta(days=days_offset)
    date_str = dt.strftime('%a %b %d %Y %H:%M:%S GMT-0500 (Eastern Standard Time)')
    
    for i in range(4):
        print(f"echo 'amcocan -> ({i})' > $FILE")
        print(f"git add $FILE")
        print(f"git commit --date='{date_str}' -m 'Building GitHub contribution graph artwork...'")

print("git push origin main --force")
print("echo 'Building GitHub contribution graph artwork complete!'")
print("# The graph will now exactly match the attached image (top-left square = Jan 10 2000, descending vertical columns)")