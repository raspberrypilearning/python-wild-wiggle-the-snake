<h2 class="c-project-heading--task">Make the snake move</h2>
--- task ---
Use a variable to make your snake slither across the screen.
--- /task ---

<h2 class="c-project-heading--explainer">It’s alive!</h2>

You’re about to make your snake move across the screen.

We’ll use a variable called `x` to keep track of where the snake's head is.  
Each time `draw()` runs, we’ll add a little to `x` to move everything to the right.

This is called **animation** — and it works just by changing positions over time!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4,11-13
---
from p5 import *
from math import sin

x = 0  # starting position of the snake


def setup():
    size(400, 400)
    background('lightblue')
    no_stroke()


def draw():
    global x
    background('lightblue')
    fill('green')
    circle(x, 200, 50)  # head at x
    circle(x - 35, 200, 40)  # body at x - 35

    x += 2  # increase x by 2


run()
--- /code ---
</div>

<div class="c-project-output">
![The head and body of the snake moving to the right](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try changing how fast the snake moves by using a bigger or smaller number in `x += 2`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If the snake doesn’t move:<br />
- Make sure `x = 0` comes **before** your functions<br />
- Did you use `global x` inside `draw()`?<br />
- Are you updating `x` with `x += 2`?

</div>
