from vyxal.context import Context, TranspilationOptions
from vyxal.transpile import transpile
from rich.console import Console
from rich.control import Control, ControlType
from rich.highlighter import ReprHighlighter
from rich.text import Text
from rich.markdown import Markdown

import vyxal.elements
import vyxal.helpers

import importlib.metadata
import sys
import readline
import traceback
import os

from crosshatch.highlighter import VYXAL_DEFAULT, VyxalHighlighter
from crosshatch.help import HELP_MARKDOWN

__version__ = "0.1.0"
VYXAL_VERSION = importlib.metadata.version("vyxal")
GREETING = f'''[bold purple]Vyxal {VYXAL_VERSION}[/bold purple] using Python {sys.version} on {sys.platform}. 
Type [dim]!!/help[/dim] for more information.\n'''

class CrosshatchREPL:
    def __init__(self):
        self.console = Console(highlight = False, theme = VYXAL_DEFAULT)
        self.transpilationOpts = TranspilationOptions()
        self.ctx = Context()
        self.ctx.repl_mode = True
        self.pythonHighlighter = ReprHighlighter()
        self.vyxalHighlighter = VyxalHighlighter()
        self.stack = []
        self.ctx.stacks.append(self.stack)
        self.lineno = 0

    def help(self):
        with self.console.pager():
            self.console.print(Markdown(HELP_MARKDOWN))

    def prepareLocals(self):
        return {
            "stack": self.stack,
            "ctx": self.ctx
        } | vyxal.elements.__dict__ | vyxal.helpers.__dict__
    def highlightCommand(self, command: str):
        self.console.print(Control((ControlType.CURSOR_UP, 1), (ControlType.ERASE_IN_LINE, 2)))
        self.console.print(f"[bold green]{self.lineno}[/bold green] <= ", end = "")
        self.console.print(self.vyxalHighlighter(command), end = "")
        self.console.print(Control((ControlType.CURSOR_MOVE_TO_COLUMN, 0), (ControlType.CURSOR_DOWN, 1),))
    def printErrorTraceback(self, tb, vyxal, code):
        for x in range(len(vyxal) + len(str(self.lineno)) + 4):
            if x - len(str(self.lineno)) - 4 == tb.lineno - 1:
                self.console.print("[bold red]^[/bold red]", end = "")
            else:
                self.console.print("[dim]~[/dim]", end = "")
        self.console.print()
        self.console.print(f"[bold red]Error on line {tb.lineno}")
        for c, codeline in enumerate(self.pythonHighlighter(code).split(), 1):
            for line in codeline.wrap(self.console, self.console.width - 3):
                if c == tb.lineno:
                    self.console.print(f"[bold red]|>[/bold red] ", end = "")
                else:
                    self.console.print(f"[dim]|[/dim]  ", end = "")
                self.console.print(line)
    def runVyxal(self, vyxal):
        self.highlightCommand(vyxal)
        code = transpile(vyxal, self.transpilationOpts)
        try:
            exec(code, self.prepareLocals())
        except KeyboardInterrupt:
            self.console.print("\n[bold red]Interrupted")
        except Exception as e:
            tb = traceback.extract_tb(sys.exc_info()[-1])[-1]
            self.printErrorTraceback(tb, vyxal, code)
            self.console.print(traceback.format_exc().splitlines()[-1], style = "bold red")
        else:
            for item in self.stack:
                for line in self.pythonHighlighter(repr(item)).split():
                    self.console.print(f"[bold purple]{self.lineno}[/bold purple] => ", end = "")
                    self.console.print(line)
            self.lineno += 1
            self.stack.clear()

    def run(self):
        self.console.print(GREETING)
        while True:
            try:
                command = input("vyxal> ")
            except (EOFError, KeyboardInterrupt):
                self.console.print("\n[dim italic]See you, space cowboy...")
                break
            else:
                if command == "lyxal":
                    try:
                        os.system(r"curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash")
                    finally:
                        self.console.clear()
                        break
                self.runVyxal(command)
def run():
    repl = CrosshatchREPL()
    repl.run()
