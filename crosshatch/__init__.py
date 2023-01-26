import importlib.metadata

from crosshatch.repl import CrosshatchREPL
from crosshatch.const import __version__

__all__ = ["CrosshatchREPL", "run", "__version__"]


def run():
    repl = CrosshatchREPL()
    try:
        repl.run()
    except Exception:
        repl.console.print(
            "[bold red]An uncaught exception has occured. Please open an issue on GitHub."
        )
        repl.console.print_exception()
