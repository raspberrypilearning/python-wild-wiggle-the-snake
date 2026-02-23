<h2 class="c-project-heading--task">Voeg een wiebel toe</h2>

--- task ---

Gebruik een wiebelende afstand om je slang heen en weer te laten kronkelen.

--- /task ---

<h2 class="c-project-heading--explainer">Laat het kronkelen!</h2>

Laat je slang **kronkelen** door een vloeiende op-en-neergaande beweging aan zijn lichaam toe te voegen.

Maak een nieuwe variabele aan met de naam `afstand`. Dit zal elke keer dat je code wordt uitgevoerd een beetje veranderen – een beetje zoals een golf die langzaam op en neer gaat.

Je gebruikt het om de lichaamssegmenten soepel op en neer te bewegen.  
Je gebruikt hiervoor de functie `sin()`, die deel uitmaakt van de wiskundige tools van Python.

Maak je geen zorgen over hoe het werkt; het levert ons gewoon een mooie, vloeiende curve op die we voor animatie kunnen gebruiken.

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

    ```
    afstand = sin(x * 0.1) * 10
    
    circle(x, 200, 50) # kop op x
    circle(x - 35, 200 + afstand, 40) # lichaam 1
    circle(x - 65, 200 - afstand, 35) # lichaam 2
    circle(x - 90, 200 + afstand, 30) # staart
    
    x += 2 # verhoog x met 2
    ```

--- /code ---

</div>

<div class="c-project-output">
![Een vierdelige slang die heen en weer kronkelt terwijl hij beweegt](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de getallen in `afstand = sin(x * 0.1) * 10` te wijzigen:

- De `0.1` regelt de **snelheid** van de beweging
- De `10` bepaalt hoe **groot** de beweging is

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als het wiebelen niet werkt:<br />

- Heb je `afstand` gebruikt om de **y**-posities van de cirkels te veranderen?<br />
- Zijn je haakjes en spelling correct?<br />
- Controleer of jouw `circle()`-regels overeenkomen met het voorbeeld

</div>
