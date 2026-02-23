<h2 class="c-project-heading--task">Teken de kop van de slang</h2>

--- task ---

Teken een groene cirkel in het midden van het scherm om de kop van je slang te maken.

--- /task ---

<h2 class="c-project-heading--explainer">Hallo, slang!</h2>

In dit project ga je een kronkelende animatieslang maken met Python en p5.  
Begin met het tekenen van een groene cirkel voor de kop van de slang.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 14, 15
---

from p5 import *
from math import sin

x = 0 # startpositie van de slang

def setup():
    size(400, 400)
    background('lightblue')
    no_stroke()

def draw():
    fill('green')
    circle(200, 200, 50)

run()

--- /code ---

</div>

<div class="c-project-output">
![Een enkele groene cirkel op een lichtblauwe achtergrond](images/step_1.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de grootte van de cirkel of de kleur te veranderen.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als je niets ziet:<br />

- Zorg ervoor dat de `circle()` **drie getallen** heeft: x, y en grootte<br />
- Voer je code opnieuw uit na het opslaan

</div>