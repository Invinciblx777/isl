#!/usr/bin/env python3
"""
Indian Sign Language Recognition System
Main Entry Point

Run with: python main.py
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.app import main

if __name__ == "__main__":
    main()
