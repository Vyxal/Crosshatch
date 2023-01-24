from rich.columns import Columns
from rich.text import Text

from functools import partial
from sys import version as pyVersion

from crosshatch.const import VYXAL_VERSION, HELP, GOODBYE, __version__

COMMANDS = {}

class WrongArgsException(Exception):
    def __init__(self, name, supplied, expected):
        super().__init__(name, supplied, expected)
        self.name = name
        self.supplied = supplied
        self.expected = expected

def command(name, description, nargs = 0):
    def register(name, description, nargs, function):
        def call(function, name, nargs, repl, *args):
            if len(args) != nargs:
                raise WrongArgsException(name, len(args), nargs)
            return function(repl, *args)
        wrapper = partial(call, function, name, nargs)
        COMMANDS[name] = (wrapper, description)
        return wrapper
    return partial(register, name, description, nargs)

@command("help", "Prints this text.")
def help(repl):
    repl.console.rule()
    repl.console.print(HELP.format(
        vyxal_version = VYXAL_VERSION
    ))
    for name, command in COMMANDS.items():
        repl.console.print(Text("##" + name, style = "dim"), "-", command[1])
    repl.console.print()
@command("exit", "Exit the REPL.")
def exitCommand(repl):
    repl.console.print(GOODBYE)
    exit(0)
@command("version", "Print version information")
def version(repl):
    repl.console.print(f"[bold purple]Vyxal {VYXAL_VERSION}")
    repl.console.print(f"[blue]Crosshatch {__version__}")
    repl.console.print(f"Python {pyVersion}\n")