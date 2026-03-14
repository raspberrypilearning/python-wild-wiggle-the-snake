<h2 class="c-project-heading--task">Намалюйте голову змії</h2>

\--- task ---

Намалюйте зелений круг посередині екрану, щоб створити вашу змію.

\--- /task ---

<h2 class="c-project-heading--explainer">Привіт, змійко!</h2>

У цьому проєкті ви створите анімовану змію, що ковзає, за допомогою Python та p5.  
Почніть з малювання зеленого круга для голови змії.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 14, 15
---

з p5 імпорт \*
з математичного імпорту sin

x = 0 # початкова позиція змії

def setup():
size(400, 400)
background('lightblue')
no_stroke()

def draw():
fill('green')
circle(200, 200, 50)

run()

\--- /code ---

</div>

<div class="c-project-output">![A single green circle on a light blue background](images/step_1.png)</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Спробуйте змінити розмір або колір кругу.

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо нічого не відбувається: <br />

- Переконайтеся, що `circle()` має **три числа**: x, y та розмір<br />
- Запустіть свій код ще раз після збереження

</div>