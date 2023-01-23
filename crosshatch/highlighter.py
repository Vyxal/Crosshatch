from rich.highlighter import RegexHighlighter
from rich.theme import Theme

VYXAL_DEFAULT = Theme({
    "vyxal.number": "bright_green",
    "vyxal.comment": "green",
    "vyxal.variable": "bright_blue",
    "vyxal.string": "red",
    "vyxal.lambda": "purple",
    "vyxal.constant": "blue",
    "vyxal.digraph": "bright_cyan",
    "vyxal.modchar": "cyan"
})

class VyxalHighlighter(RegexHighlighter):
    base_style = "vyxal."
    highlights = [
        r"(?P<number>[0123456789.°])",
        r"(?P<comment>(#.*$))",
        r"(?P<variable>([→|←][a-zA-Z_]+))",
        r"(?P<lambda>[λƛ⟑µ⁽‡≬']|(¨3)|(¨2)|(¨₂)|(¨₃))",
        r"(?P<constant>[₀₁₄₆₇₈¶¤ð×u])",
        r"(?P<digraph>[∆ø↔Þ¨k].)",
        r"(?P<modchar>[vß⁺₌₍~&ƒɖ])",
        r"(?P<string>`(.*?(?<!\\))`|(`.*)|(‛..)|(\\.))"
    ]