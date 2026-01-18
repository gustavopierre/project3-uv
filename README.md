# project3-uv

A learning project to demonstrate the capabilities of [uv](https://github.com/astral-sh/uv), a modern Python package and project manager.

## What is uv?

`uv` is an extremely fast Python package installer and resolver, written in Rust. It's designed as a drop-in replacement for pip and pip-tools, but with significantly better performance and user experience.

## Features Demonstrated

This project showcases:
- 📦 **Dependency Management**: Using `pyproject.toml` for project configuration
- 🚀 **Fast Installation**: Lightning-fast package installation with uv
- 🛠️ **CLI Development**: Building command-line tools with Click
- 🌐 **HTTP Requests**: Making API calls with the requests library
- 🧪 **Testing**: Using pytest for unit tests
- ✨ **Code Quality**: Linting with ruff

## Prerequisites

Install uv by following the [official installation guide](https://github.com/astral-sh/uv#installation):

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Using pip
pip install uv
```

## Getting Started

### 1. Create a Virtual Environment

```bash
# Create a virtual environment with uv
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install all project dependencies
uv pip install -e .

# Install with development dependencies
uv pip install -e ".[dev]"
```

### 3. Run the Application

```bash
# Using Python module
python -m uv_learning.main --help

# Or if installed with entry point
uv-learning --help
```

## Usage Examples

### Hello Command

```bash
# Say hello
uv-learning hello

# Say hello to a specific person
uv-learning hello Alice
```

### Fetch Command

```bash
# Fetch data from GitHub API
uv-learning fetch

# Fetch from a custom URL
uv-learning fetch --url https://api.github.com/users/github
```

### Info Command

```bash
# Display project information
uv-learning info
```

## Common uv Commands

### Installing Packages

```bash
# Install a package
uv pip install requests

# Install a specific version
uv pip install requests==2.31.0

# Install from requirements.txt
uv pip install -r requirements.txt
```

### Managing Dependencies

```bash
# Sync dependencies from pyproject.toml
uv pip sync

# Compile dependencies to a lockfile
uv pip compile pyproject.toml -o requirements.txt
```

### Creating Virtual Environments

```bash
# Create a new virtual environment
uv venv

# Create with a specific Python version
uv venv --python 3.11

# Create in a custom location
uv venv my-env
```

## Development

### Running Tests

```bash
# Install dev dependencies first
uv pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Code Linting

```bash
# Run ruff linter
ruff check src/

# Auto-fix issues
ruff check --fix src/
```

## Project Structure

```
project3-uv/
├── src/
│   └── uv_learning/
│       ├── __init__.py      # Package initialization
│       └── main.py          # CLI application
├── tests/                   # Test files
├── pyproject.toml          # Project configuration and dependencies
├── .gitignore              # Git ignore patterns
└── README.md               # This file
```

## Why Use uv?

1. **Speed**: 10-100x faster than pip for package installation
2. **Reliability**: Better dependency resolution algorithm
3. **Simplicity**: Single tool for multiple workflows
4. **Compatibility**: Drop-in replacement for pip and pip-tools
5. **Modern**: Built with Rust for performance and safety

## Learning Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [Python Packaging Guide](https://packaging.python.org/)
- [Click Documentation](https://click.palletsprojects.com/)
- [Requests Documentation](https://requests.readthedocs.io/)

## License

This is a learning project for demonstration purposes.