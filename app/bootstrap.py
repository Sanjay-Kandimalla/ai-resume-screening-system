# bootstrap.py
import os
import sys

# Go from /app or /app/pages → project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)