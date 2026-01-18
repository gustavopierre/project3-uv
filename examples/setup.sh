#!/bin/bash
# Example script showing basic uv workflow

set -e

echo "=== UV Learning Project Setup ==="
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✓ uv is installed"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
uv venv
echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "🔧 To activate the virtual environment, run:"
echo "   source .venv/bin/activate    # On macOS/Linux"
echo "   .venv\\Scripts\\activate      # On Windows"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
source .venv/bin/activate
uv pip install -e .
echo "✓ Dependencies installed"
echo ""

# Run the application
echo "🚀 Running the application..."
echo ""
python -m uv_learning.main hello
echo ""
python -m uv_learning.main info
echo ""

echo "✅ Setup complete! You can now use the uv-learning CLI."
echo ""
echo "Try these commands:"
echo "   uv-learning hello YourName"
echo "   uv-learning fetch"
echo "   uv-learning info"
