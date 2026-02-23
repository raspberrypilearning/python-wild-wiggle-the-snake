<h2 class="c-project-heading--task">Dessiner la tête du serpent</h2>

--- task ---

Dessine un cercle vert au milieu de l'écran pour faire la tête de ton serpent.

--- /task ---

<h2 class="c-project-heading--explainer">Salut, serpent !</h2>

Dans ce projet, tu vas créer un serpent animé qui se tortille en utilisant Python et p5.  
Commence par dessiner un cercle vert pour la tête du serpent.

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

x = 0 # position de départ du serpent

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
![Un cercle vert sur fond bleu clair](images/step_1.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de modifier la taille du cercle ou sa couleur.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si tu ne vois rien :<br />

- Assure-toi que la fonction `circle()` comporte **trois nombres** : x, y et size<br />
- Exécute à nouveau ton code après l'avoir enregistré

</div>