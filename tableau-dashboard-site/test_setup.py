#!/usr/bin/env python3
"""
Quick test to verify Python environment setup
"""

import sys
import flask
import gunicorn

def test_setup():
    print("=" * 50)
    print("Python Environment Setup Verification")
    print("=" * 50)
    print(f"Python version: {sys.version}")
    print(f"Flask version: {flask.__version__}")
    print(f"Gunicorn version: {gunicorn.__version__}")
    print("=" * 50)
    print("✓ All packages imported successfully!")
    print("✓ Python environment is ready!")
    print("=" * 50)

if __name__ == "__main__":
    test_setup()
