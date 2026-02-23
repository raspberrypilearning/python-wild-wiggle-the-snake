<h2 class="c-project-heading--task">Donner du style à ton serpent</h2>

--- task ---

Ajoute des yeux, des couleurs ou des décorations pour personnaliser ton serpent.

--- /task ---

<h2 class="c-project-heading--explainer">Personnaliser</h2>

Ton serpent rampe tranquillement — il est temps de lui donner de la personnalité !

Tu peux :

- Ajouter des yeux blancs avec des pupilles noires
- Changer la couleur du corps ou de chaque segment
- Ajouter des rayures, une langue, ou même un chapeau de fête !

Voici un exemple :

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 25-27, 29-31
---

    ```
    circle(x, 200, 50)               # tête à x
    circle(x - 35, 200 + offset, 40) # corps 1
    circle(x - 65, 200 - offset, 35) # corps 2
    circle(x - 90, 200 + offset, 30) # queue
    
    fill('white')
    circle(x + 10, 190, 10)
    circle(x + 25, 190, 10)
    
    fill('black')
    circle(x + 10, 190, 5)
    circle(x + 25, 190, 5)
    ```

--- /code ---

</div>

<div class="c-project-output">
![Un serpent vert qui tortille avec des yeux de dessin animé](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Envie de créativité ?

- Essaie d'ajouter des `circle()`s rouges pour les joues
- Utilise `fill('blue')` ou toute autre couleur de ton choix
- Fais cligner des yeux le serpent ou habille-le d'une couronne !

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si quelque chose disparaît :<br />

- As-tu **défini `fill()`** avant chaque cercle ?<br />
- Les nombres x et y sont-ils près de la tête du serpent ?<br />
- N'oublie pas : les cercles situés près du bas de ton code apparaissent **au-dessus**

</div>

<div class="c-project-callout c-project-callout--tip">

### Avis

Il s'agit d'un projet bêta, ce qui signifie qu'il est tout nouveau et pas encore largement disponible. Si tu as testé ce projet individuellement ou avec ton club, n'hésite pas à nous faire part de ton avis.

<a href="https://form.raspberrypi.org/4874054?tfa_6933=python-wild-wiggle-the-snake" style="
display: inline-block;
padding: 10px 20px;
border: 2px solid black;
border-radius: 999px;
font-weight: bold;
font-size: 16px;
background-color: white;
color: black;
text-align: center;
text-decoration: none;
transition: background-color 0.2s;
" onmouseover="this.style.backgroundColor='#f0f0f0';" onmouseout="this.style.backgroundColor='white';">
Donner ton avis </a>

</div>

***
Ce projet a été traduit par des bénévoles:

[name]

[name]

[name]

Grâce aux bénévoles, nous pouvons donner aux gens du monde entier la chance d'apprendre dans leur propre langue. Vous pouvez nous aider à atteindre plus de personnes en vous portant volontaire pour la traduction - plus d'informations sur [rpf.io/translate](https://rpf.io/translate).
