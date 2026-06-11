<h2 class="c-project-heading--task">Додай частину тулуба</h2>

--- task ---

Намалюй ще один зелений круг позаду голови змії, — це буде частина її тулуба.

--- /task ---

<h2 class="c-project-heading--explainer">Розтягуємо</h2>

Додай позаду голови ще один круг. Так твоя змія здаватиметься довшою.

Тобі потрібно буде:
- Знову використати `circle()` і намалювати круг
- Зробити цей круг трохи меншим за голову
- Посунути його трохи ліворуч

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
![Два зелених круги, одне менше та розташоване позаду іншого, на блакитному тлі.](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Спробуй змінити положення або розмір другого круга. Як змінилася форма тіла змії?

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо тіло не видно:<br />
- Чи відрізняються розміри двох кругів?<br />
- Запусти код ще раз

</div>
