"""
Main CLI application for uv-learning project.

This demonstrates a simple CLI tool with external dependencies (click, requests).
"""

import click
import requests

from uv_learning import __version__ as package_version


@click.group()
@click.version_option()
def cli():
    """UV Learning - A demo project for learning uv package manager."""
    pass


@cli.command()
@click.argument("name", default="World")
def hello(name):
    """Say hello to NAME."""
    click.echo(f"Hello, {name}!")
    click.echo("This project uses uv for dependency management.")


@cli.command()
@click.option("--url", default="https://api.github.com", help="URL to fetch")
def fetch(url):
    """Fetch data from a URL using requests library."""
    try:
        click.echo(f"Fetching {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        click.echo(f"Status Code: {response.status_code}")
        click.echo(f"Response length: {len(response.text)} characters")
        click.echo("✓ Successfully fetched data")
    except requests.RequestException as e:
        click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort()


@cli.command()
def info():
    """Display project information."""
    click.echo("UV Learning Project")
    click.echo(f"Version: {package_version}")
    click.echo("\nThis project demonstrates:")
    click.echo("  • Using uv for Python package management")
    click.echo("  • Managing dependencies with pyproject.toml")
    click.echo("  • Creating CLI applications with Click")
    click.echo("  • Making HTTP requests with requests library")


if __name__ == "__main__":
    cli()
