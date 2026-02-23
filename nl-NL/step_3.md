<h2 class="c-project-heading--task">Laat de slang bewegen</h2>

--- task ---

Gebruik een variabele om je slang over het scherm te laten kronkelen.

--- /task ---

<h2 class="c-project-heading--explainer">Het leeft!</h2>

Je gaat je slang over het scherm laten bewegen.

Gebruik een variabele genaamd `x` om bij te houden waar de kop van de slang zich bevindt.  
Telkens wanneer `draw()` wordt uitgevoerd, tellen we een beetje bij `x` op om alles naar rechts te verschuiven.

De functie `draw()` wordt vele malen per seconde uitgevoerd. Daarom tekenen we de achtergrond elke keer opnieuw — dat maakt het scherm leeg, zodat de slang geen spoor achterlaat.

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
    circle(x, 200, 50) # hoofd op x
    circle(x - 35, 200, 40) # lichaam op x - 35

    x += 2 # verhoog x met 2

--- /code ---

</div>

<div class="c-project-output">
![De kop en het lichaam van de slang bewegen naar rechts](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Probeer de snelheid waarmee de slang beweegt te veranderen door een groter of kleiner getal te gebruiken in `x += 2`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als de slang niet beweegt:<br />

- Heb je `global x` gebruikt binnen `draw()`?<br />
- Werk je `x` bij met `x += 2`?

</div>
