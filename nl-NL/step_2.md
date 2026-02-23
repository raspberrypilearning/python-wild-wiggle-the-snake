<h2 class="c-project-heading--task">Voeg een lichaamssegment toe</h2>

--- task ---

Teken een tweede groene cirkel achter de kop van de slang om een deel van zijn lichaam te vormen.

--- /task ---

<h2 class="c-project-heading--explainer">Uitrekken</h2>

Voeg een tweede cirkel achter de kop toe. Hierdoor zal de slang er langer uitzien.

Je moet het volgende doen:

- Gebruik een andere `circle()`
- Maak het iets kleiner dan het hoofd
- Schuif het een beetje naar links

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

--- /code ---

</div>

<div class="c-project-output">
![Twee groene cirkels, de ene kleiner en achter de andere, op een lichtblauwe achtergrond](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de positie of grootte van de tweede cirkel te veranderen om te zien hoe dit de lichaamsvorm van de slang beïnvloedt.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als het lichaam niet verschijnt:<br />

- Zijn de getallen voor de twee cirkels verschillend?<br />
- Zorg ervoor dat je op 'Run' hebt geklikt

</div>
