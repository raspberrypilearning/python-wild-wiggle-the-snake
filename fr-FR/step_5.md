<h2 class="c-project-heading--task">Ajouter un tortillement</h2>

--- task ---

Utilise un décalage oblique pour faire glisser ton serpent d'un côté à l'autre.

--- /task ---

<h2 class="c-project-heading--explainer">Gigotte !</h2>

Donne l'illusion que ton serpent **rampe** en ajoutant un mouvement de va-et-vient fluide à son corps.

Crée une nouvelle variable appelée `offset`. Cela changera un peu à chaque fois que ton code s'exécutera — comme une vague qui monte ou descend lentement.

Tu l'utiliseras pour déplacer les segments du corps de haut en bas de manière fluide.  
Tu utiliseras une fonction appelée `sin()`, qui fait partie des outils mathématiques de Python.

Ne te préoccupe pas de son fonctionnement — ça nous donne juste une belle courbe lisse que nous pouvons utiliser pour l’animation.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13
line_highlights: 18, 21-23
---

def draw():
    global x
    background('lightblue')
    fill('green')

    offset = sin(x * 0.1) * 10
    
    circle(x, 200, 50)               # tête à x
    circle(x - 35, 200 + offset, 40) # corps 1
    circle(x - 65, 200 - offset, 35) # corps 2
    circle(x - 90, 200 + offset, 30) # queue

    x += 2  # augmenter x de 2

--- /code ---

</div>

<div class="c-project-output">
![Un serpent à quatre parties se tortillant de gauche à droite en se déplaçant](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de changer les nombres dans `offset = sin(x * 0.1) * 10` :

- Le `0.1` contrôle la **vitesse** du tortillement
- Le `10` contrôle l’**amplitude** du tortillement

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si le tortillement ne fonctionne pas :<br />

- As-tu utilisé `offset` pour modifier les positions **y** des cercles ?<br />
- Tes parenthèses et ton orthographe sont-elles correctes ?<br />
- Vérifie si tes lignes `circle()` correspondent à l'exemple

</div>
