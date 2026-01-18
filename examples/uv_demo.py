#!/usr/bin/env python3
"""
Example script showing how to use uv programmatically.

This demonstrates common uv workflows through Python code.
"""

import subprocess
import sys


def run_command(cmd, description):
    """Run a command and display its output."""
    print(f"\n{'='*60}")
    print(f"📍 {description}")
    print(f"{'='*60}")
    print(f"Running: {' '.join(cmd)}")
    print()
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(e.stderr)
        return False


def main():
    """Demonstrate various uv commands."""
    print("""
    ╔════════════════════════════════════════════╗
    ║   UV Package Manager - Usage Examples     ║
    ╚════════════════════════════════════════════╝
    """)
    
    # Check if uv is installed
    try:
        subprocess.run(["uv", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ uv is not installed. Please install it first:")
        print("   pip install uv")
        print("   OR")
        print("   curl -LsSf https://astral.sh/uv/install.sh | sh")
        sys.exit(1)
    
    # Example 1: Check uv version
    run_command(["uv", "--version"], "Check UV version")
    
    # Example 2: Show pip version
    run_command(["uv", "pip", "--version"], "Check pip version through uv")
    
    # Example 3: List installed packages
    run_command(["uv", "pip", "list"], "List installed packages")
    
    # Example 4: Show package info
    run_command(["uv", "pip", "show", "click"], "Show info for 'click' package")
    
    print(f"\n{'='*60}")
    print("✅ UV demonstration complete!")
    print(f"{'='*60}")
    print("\nFor more examples, see the README.md file.")


if __name__ == "__main__":
    main()
