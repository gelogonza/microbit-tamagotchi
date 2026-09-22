# micro:bit — MakeCode Python

Notes for `makecode.microbit.org`. Only relevant if you are building on micro:bit.

## MakeCode Python is not MicroPython

Two different Python dialects target this board.

| | MakeCode Python | MicroPython |
|---|---|---|
| Import | none — `basic`, `input`, `led` are global | `from microbit import *` |
| Converts to blocks | yes | **no** |
| Where | makecode.microbit.org Python tab | python.microbit.org, Mu |

Code from tutorials, forums, or an LLM is very often MicroPython. It will not
convert to blocks, and the error will not say "wrong dialect."

## Block conversion is all-or-nothing

One unsupported construct anywhere in the file hides **every** block, not just
the offending one. If the Blocks tab greys out, you are looking for a single
line, not a general problem.

Constructs with no block equivalent:

- ternary expressions — `x if cond else y`
- `is` / `is None`
- docstrings (a bare string as a function's first statement)
- f-strings
- dictionaries
- list comprehensions
- `try` / `except`

## Namespace collisions

A variable named after an existing namespace produces a **type error**, not a
naming complaint. The message will look unrelated to your variable.

Avoid: `light`, `text`, `input`, `game`, `led`, `music`, `radio`, `pins`,
`control`, `serial`, `basic`, `images`.

Symptom: `types not compatible: light and number` on the assignment line and on
every later use.

## Getting an identifier right

**Drag the block onto the canvas, switch to the Python tab, read what MakeCode
generated.** That is the authority.

API names have changed between editor versions — `music.begin_melody` became
`music.start_melody`, and the V2 logo-touch enum is easy to get wrong. A name
from documentation, memory, or an LLM may be from a different version and will
fail confusingly.

## Known-unverified in this repo

`code/reference/block_tour.py` section 9 (micro:bit V2 only) contains two
identifiers that have **not** been checked against a current editor:

- `TouchButtonEvent.PRESSED`
- `soundExpression.giggle.play()`

Left unverified deliberately. Trial IND-01 in
`testing/individual/TEMPLATE-resilience-trials.md` walks through checking
them against the editor's own output. Do not "fix" them by guessing.

## V1 vs V2

Section 9 of the tour file is V2-only: microphone, speaker, logo touch. On a V1
board, delete it. Everything above it runs on both.
