import vyxal

from rich.console import Console

import importlib.metadata
import readline
import sys

__version__ = importlib.metadata.version("vyxal")
GREETING = f'''[bold purple]Vyxal {__version__}[/bold purple] using Python {sys.version} on {sys.platform}. 
Type [dim]!!/help[/dim] for more information.\n'''

class CrosshatchREPL:
    def __init__(self):
        self.console = Console(highlight=False)

    def run(self):
        self.console.print(GREETING)
        while True:
            try:
                self.console.input("vyxal> ")
            except (EOFError, KeyboardInterrupt):
                self.console.print("\n[dim italic]See you, space cowboy...")
                break

def run():
    repl = CrosshatchREPL()
    repl.run()
