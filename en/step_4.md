<h2 class="c-project-heading--task">Make the snake longer</h2>

--- task ---

Add two more circles behind the snake to make its full body.

--- /task ---

<h2 class="c-project-heading--explainer">Slither, slither...</h2>

Give your snake a longer body by adding two more segments behind it.

Keep using the `x` variable and subtract different amounts to place each circle in the right spot.

Each one should be a little smaller, and moved further to the left.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13
line_highlights: 19-20
---

def draw():
    global x
    background('lightblue')
    fill('green')
    circle(x, 200, 50)        # head at x
    circle(x - 35, 200, 40)   # body 1
    circle(x - 65, 200, 35)   # body 2
    circle(x - 90, 200, 30)   # tail

    x += 2  # increase x by 2


run()

--- /code ---
</div>

<div class="c-project-output">
![A full snake made from 4 green circles of different sizes](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Try changing the sizes of the circles to make a chunky or skinny snake.<br />
- You can also change how far apart the segments are.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If some parts of the body don’t show up:<br />
- Check each `circle()` has 3 numbers<br />
- Look out for spelling errors or missing commas<br />
- Remember: every new segment is further left (use `x - ...`)

</div>
