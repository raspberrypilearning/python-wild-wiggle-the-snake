<h2 class="c-project-heading--task">Allonger le serpent</h2>

--- task ---

Ajoute deux cercles supplémentaires derrière le serpent pour former son corps entier.

--- /task ---

<h2 class="c-project-heading--explainer">Glisser, glisser...</h2>

Allonge le corps de ton serpent en ajoutant deux segments supplémentaires à l'arrière.

Continue à utiliser la variable `x` et soustrais des quantités différentes pour placer chaque cercle au bon endroit.

Chacun devrait être un peu plus petit, et se déplacer plus loin vers la gauche.

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
circle(x, 200, 50)        # tête à x
circle(x - 35, 200, 40)   # corps 1
circle(x - 65, 200, 35)   # corps 2
circle(x - 90, 200, 30)   # queue

    ```
    x += 2 # augmenter x de 2
    ```

run()

--- /code ---

</div>

<div class="c-project-output">
![Un serpent complet composé de 4 cercles verts de tailles différentes](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

- Change la taille des cercles pour faire un serpent dodu ou tout maigre.<br />
- Tu peux aussi changer la distance entre les segments.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si certaines parties du corps ne s'affichent pas :<br />

- Vérifie que chaque `circle()` contient 3 nombres<br />
- Attention aux fautes d'orthographe ou aux virgules manquantes<br />
- Rappelle-toi : chaque nouveau segment est décalé vers la gauche (utilise `x - ...`)

</div>
