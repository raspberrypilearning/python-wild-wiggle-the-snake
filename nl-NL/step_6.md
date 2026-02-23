<h2 class="c-project-heading--task">Geef je slang wat stijl</h2>

--- task ---

Voeg ogen, kleuren of versieringen toe om je slang te personaliseren.

--- /task ---

<h2 class="c-project-heading--explainer">Maak het je eigen</h2>

Je slang kronkelt lekker voort, nu is het tijd om hem wat persoonlijkheid te geven!

Je kunt:

- Voeg witte ogen met zwarte pupillen toe
- Verander de kleur van het lichaam of van elk segment
- Voeg strepen, een tong of zelfs een feestmuts toe!

Hier is een voorbeeld:

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
    circle(x, 200, 50) # kop op x
    circle(x - 35, 200 + afstand, 40) # lichaam 1
    circle(x - 65, 200 - afstand, 35) # lichaam 2
    circle(x - 90, 200 + afstand, 30) # staart
    
    fill('white')
    circle(x + 10, 190, 10)
    circle(x + 25, 190, 10)
    
    fill('black')
    circle(x + 10, 190, 5)
    cirkel(x + 25, 190, 5)
    ```

--- /code ---

</div>

<div class="c-project-output">
![Een kronkelende groene slang met cartoonogen](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Wil je creatief worden?

- Probeer rode `circle()`-tekens toe te voegen voor de wangen
- Gebruik `fill('blue')` of een andere kleur naar keuze
- Laat de slang knipperen of een kroon dragen!

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als iets verdwijnt:<br />

- Heb je **de functie `fill()`** vóór elke circle ingesteld?<br />
- Liggen de x- en y-waarden dicht bij de kop van de slang?<br />
- Onthoud: cirkels onderaan je code verschijnen **bovenop**

</div>

<div class="c-project-callout c-project-callout--tip">

### Terugkoppeling

Dit is een bètaproject, wat betekent dat het gloednieuw is en nog niet algemeen beschikbaar. Als je dit project zelf of met je club hebt getest, laat ons dan weten wat je ervan vindt.

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
Geef feedback </a>

</div>

***
Dit project werd vertaald door vrijwilligers:

[name]

[name]

[name]

Dankzij vrijwilligers kunnen we mensen over de hele wereld de kans geven om in hun eigen taal te leren. Jij kunt ons helpen meer mensen te bereiken door vrijwillig te starten met vertalen - meer informatie op [rpf.io/translate](https://rpf.io/translate).
