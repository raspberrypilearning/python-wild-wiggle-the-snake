<h2 class="c-project-heading--task">Faire bouger le serpent</h2>

--- task ---

Utilise une variable pour faire ramper ton serpent sur l'écran.

--- /task ---

<h2 class="c-project-heading--explainer">Il est vivant !</h2>

Tu vas maintenant faire bouger ton serpent à l’écran.

Utilise une variable appelée `x` pour suivre l'emplacement de la tête du serpent.  
À chaque exécution de `draw()`, nous ajouterons un petit peu à `x` pour déplacer tout vers la droite.

La fonction `draw()` s'exécute plusieurs fois par seconde. C’est pourquoi nous dessinons l’arrière-plan à chaque fois — il efface l’écran de sorte que le serpent ne laisse pas de trace.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13
line_highlights: 14-15, 17-18, 20
---

def draw():
global x
background('lightblue')
fill('green')
circle(x, 200, 50)  # tête à x
circle(x - 35, 200, 40)  # coprs à x - 35

    ```
    x += 2 # augmenter x de 2
    ```

--- /code ---

</div>

<div class="c-project-output">
![La tête et le corps du serpent se déplacent vers la droite](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de changer à quelle vitesse le serpent se déplace en utilisant un nombre plus grand ou plus petit dans `x += 2`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si le serpent ne bouge pas :<br />

- As-tu utilisé `global x` à l'intérieur de `draw()` ?<br />
- Mets-tu à jour `x` avec `x += 2` ?

</div>
