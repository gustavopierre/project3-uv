"""Tests for the main CLI application."""

import pytest
from click.testing import CliRunner

from uv_learning.main import cli


@pytest.fixture
def runner():
    """Create a Click CLI runner."""
    return CliRunner()


def test_cli_help(runner):
    """Test that the CLI help works."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "UV Learning" in result.output


def test_hello_default(runner):
    """Test hello command with default argument."""
    result = runner.invoke(cli, ["hello"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output
    assert "uv" in result.output


def test_hello_with_name(runner):
    """Test hello command with custom name."""
    result = runner.invoke(cli, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.output


def test_info_command(runner):
    """Test info command displays project information."""
    result = runner.invoke(cli, ["info"])
    assert result.exit_code == 0
    assert "UV Learning Project" in result.output
    assert "Version:" in result.output
    assert "uv" in result.output


def test_fetch_command_with_invalid_url(runner):
    """Test fetch command with an invalid URL."""
    result = runner.invoke(cli, ["fetch", "--url", "http://invalid-url-that-does-not-exist.local"])
    assert result.exit_code != 0
    assert "Error:" in result.output
