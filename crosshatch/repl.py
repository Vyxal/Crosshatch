from vyxal.context import Context, TranspilationOptions
from vyxal.transpile import transpile
from rich.console import Console
from rich.control import Control, ControlType
from rich.highlighter import ReprHighlighter

import vyxal.elements
import vyxal.helpers

import sys
import readline
import traceback

from crosshatch.highlighter import VYXAL_DEFAULT, VyxalHighlighter
from crosshatch.const import GREETING, GOODBYE
from crosshatch.commands import COMMANDS

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

    def prepareLocals(self):
        return {
            "stack": self.stack,
            "ctx": self.ctx
        } | vyxal.elements.__dict__ | vyxal.helpers.__dict__
    def highlightCommand(self, command: str):
        self.console.print(Control((ControlType.CURSOR_UP, 1), (ControlType.ERASE_IN_LINE, 2)))
        self.console.print(f"[bold purple]{self.lineno}[/bold purple] <= ", end = "")
        self.console.print(self.vyxalHighlighter(command), end = "")
        self.console.print(Control((ControlType.CURSOR_MOVE_TO_COLUMN, 0), (ControlType.CURSOR_DOWN, 1),))
    def printErrorTraceback(self, tb, vyxal, code):
        self.console.print(f"[bold red]{self.lineno}[/bold red] <= {self.vyxalHighlighter(vyxal)}")
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
        vyxal = "\n".join(vyxal)
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
                    self.console.print(f"[bold green]{self.lineno}[/bold green] => ", end = "")
                    self.console.print(line)
            self.lineno += 1
            self.stack.clear()

    def runCommand(self, command):
        self.console.print(Control((ControlType.CURSOR_UP, 1), (ControlType.ERASE_IN_LINE, 2), (ControlType.CURSOR_MOVE_TO_COLUMN, 0)))
        self.console.print(f"<= [dim]{command}")
        command, *args = command.lstrip("#").split(" ")
        if command not in COMMANDS:
            self.console.print(f"[red]Unknown command {command}")
            return
        return COMMANDS[command][0](self, *args)

    def run(self):
        self.console.print(GREETING)
        commandList = []
        while True:
            try:
                command = input(f"[{self.lineno}] ..." if len(commandList) else f"[{self.lineno}] vyxal> ")
            except KeyboardInterrupt:
                self.console.print(Control((ControlType.ERASE_IN_LINE, 2), (ControlType.CURSOR_MOVE_TO_COLUMN, 0)), end = "")
                continue
            except EOFError:
                self.console.print(GOODBYE)
                break
            else:
                
                if command == "lyxal":
                    self.console.print("we do a little trolling")
                    import webbrowser
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                    continue
                if command.startswith("##"):
                    self.runCommand(command)
                else:
                    if len(commandList):
                        if command == "":
                            self.console.print(Control((ControlType.CURSOR_UP, 1), (ControlType.ERASE_IN_LINE, 2), (ControlType.CURSOR_MOVE_TO_COLUMN, 0)))
                            self.runVyxal(commandList)
                            commandList.clear()
                        else:
                            commandList.append(command)
                            self.highlightCommand(command)
                    else:
                        self.highlightCommand(command)
                        commandList.append(command)
                        if not command.endswith("  "):
                            self.runVyxal(commandList)
                            commandList.clear()
                        
                    