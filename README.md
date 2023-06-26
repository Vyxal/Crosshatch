![Crosshatch Logo](banner.png)

Ever wanted to use [Vyxal](https://github.com/Vyxal/Vyxal), but found that the default REPL was lacking in features and that the online interpreter wasn't interactive enough? Well now there's a solution to all your read-execute-print-loop needs! Crosshatch is designed to be easy to use, visually appealing and highly interoperable with the Vyxal programming language. 

## Installation

<!-- Uncomment when on PyPi

To get Crosshatch, simply install it with pip:

```
pip install crosshatch
```
--> 
If you want to work on Crosshatch, you can also use poetry. First, download this repository and unzip it. Alternatively, you can open it with Github Desktop or clone it via git.

Then, you'll need to install [Poetry](https://python-poetry.org/), which is the packaging tool used for Crosshatch.

```
pip install poetry
```

Finally, run:

```
poetry install
```

and it will take care of installing all the required dependencies.

## Usage

To run Crosshatch:

```
crosshatch
```

Or if you want to do development work on it:

```
poetry run crosshatch
```

After starting Crosshatch, you'll see something like the following:

```
Vyxal 2.19.0 using Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32.
Type ##help for more information.
EOF or ##exit to exit.

[0] vyxal>
```

Enter your expressions after the `>` and they will be evaluated. The `[0]` indicates that this is expression 0.
