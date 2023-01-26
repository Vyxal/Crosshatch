import importlib.metadata
import sys

__version__ = "0.1.0"
VYXAL_VERSION = importlib.metadata.version("vyxal")

GREETING = f"""[bold purple]Vyxal {VYXAL_VERSION}[/bold purple] using Python {sys.version} on {sys.platform}. 
Type [dim]##help[/dim] for more information.
EOF or [dim]##exit[/dim] to exit.\n"""

GOODBYE = "\n[dim italic]See you, space cowboy..."

HELP = """Welcome to [bold purple]Vyxal {vyxal_version}[/bold purple]!
To run Vyxal code, simply enter it into the prompt. It will be run automatically.
If you want to run multiline code, put two spaces at the end of a line. Enter a blank line to run.

List of commands:
"""
