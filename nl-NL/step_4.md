<h2 class="c-project-heading--task">Maak de slang langer</h2>

\--- task ---

Voeg nog twee cirkels achter de slang toe om het volledige lichaam te vormen.

\--- /task ---

<h2 class="c-project-heading--explainer">Glij, glij...</h2>

Geef je slang een langer lichaam door er twee extra segmenten aan de achterkant aan toe te voegen.

Blijf de variabele `x` gebruiken en trek verschillende waarden af om elke cirkel op de juiste plek te plaatsen.

Ze moeten elk iets kleiner zijn en verder naar links worden geplaatst.

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
circle(x, 200, 50) # kop op x
circle(x - 35, 200, 40) # lichaam 1
circle(x - 65, 200, 35) # lichaam 2
circle(x - 90, 200, 30) # staart

    ```
    x += 2 # verhoog x met 2
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Een complete slang gemaakt van 4 groene cirkels van verschillende groottes](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Probeer de grootte van de cirkels te veranderen om een dikke of dunne slang te maken.<br />
- Je kunt ook de afstand tussen de segmenten aanpassen.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als sommige lichaamsdelen niet zichtbaar zijn:<br />

- Controleer of elke `circle()` 3 getallen bevat<br />
- Let op spelfouten of ontbrekende komma's<br />
- Onthoud: elk nieuw segment komt verder naar links (gebruik `x - ...`)

</div>
