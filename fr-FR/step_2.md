<h2 class="c-project-heading--task">Ajouter un segment de corps</h2>

\--- task ---

Dessine un deuxième cercle vert derrière la tête du serpent pour représenter une partie de son corps.

\--- /task ---

<h2 class="c-project-heading--explainer">Étirer</h2>

Ajoute un deuxième cercle derrière la tête. Ça donnera que le serpent est plus long.

Tu auras besoin :

- Utiliser un autre `circle()`
- Le rendre légèrement plus petit que la tête
- Le déplacer légèrement vers la gauche

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13
line_highlights: 16
---

def draw():
fill('green')
circle(200, 200, 50)
circle(165, 200, 40)

run()

\--- /code ---

</div>

<div class="c-project-output">
![Deux cercles verts, l'un plus petit et derrière l'autre, sur un fond bleu clair](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de changer la position ou la taille du deuxième cercle pour voir comment il change la forme du corps du serpent.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si le corps ne s'affiche pas :<br />

- Les nombres des deux cercles sont-ils différents ?<br />
- Assure-toi d'avoir cliqué sur Run

</div>
