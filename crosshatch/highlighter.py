from rich.highlighter import RegexHighlighter
from rich.theme import Theme

VYXAL_DEFAULT = {
    "vyxal.number": "bright_green",
    "vyxal.comment": "green",
    "vyxal.variable": "bright_blue",
    "vyxal.string": "red",
    "vyxal.function": "magenta",
    "vyxal.function_end": "magenta",
    "vyxal.constant": "blue",
    "vyxal.digraph": "bright_cyan",
    "vyxal.modchar": "cyan",
    "vyxal.list": "bright_magenta"
}
VYXAL_DEFAULT |= {
    "vyxal.list_sep": VYXAL_DEFAULT["vyxal.list"],
    "vyxal.list_end": VYXAL_DEFAULT["vyxal.list"]
}
VYXAL_DEFAULT = Theme(VYXAL_DEFAULT)

class VyxalHighlighter(RegexHighlighter):
    base_style = "vyxal."
    highlights = [
        r"(?P<comment>(#.*$))",
        
        r"(?P<variable>([→|←][a-zA-Z_]+))",
        r"(?P<constant>[₀₁₄₆₇₈¶¤ð×u])",
        r"(?P<digraph>[∆ø↔Þ¨k].)",
        r"(?P<modchar>[vß⁺₌₍~&ƒɖ])",
        
        r"(?P<function>[λƛ⟑µ⁽‡≬']|(¨3)|(¨2)|(¨₂)|(¨₃)).*(?P<function_end>;)",
        r"(?P<function>@[a-zA-Z_]+(\:([a-zA-Z_]|\d)+)*\|).*(?P<function_end>;)",
        r"(?P<function>[a-zA-Z_]+;)",

        r"(?P<list>⟨)[^|]+?((?P<list_sep>\|)[^|]+?)*(?P<list_end>⟩)",
        
        r"(?P<number>[0123456789.°]*)",
        r"(?P<string>`(.*?(?<!\\))`|(`.*)|(‛..)|(\\.))"
    ]