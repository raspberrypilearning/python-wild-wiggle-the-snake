<h2 class="c-project-heading--task">Додати частини тіла</h2>

\--- task ---

Намалюйте друге зелене круг позаду голови змії, щоб створити частину її тіла.

\--- /task ---

<h2 class="c-project-heading--explainer">Розтягування</h2>

Додайте другий круг позаду голови. Тоді ваша змія здаватиметься довшою.

Вам знадобиться:

- Додайте `circle()`
- Зробіть його трохи меншим за голову
- Змістіть його трохи ліворуч

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

\--- /code ---

</div>

<div class="c-project-output">
![Two green circles, one smaller and behind the other, on a light blue background](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Спробуйте змінити положення або розмір другого круга, щоб побачити, як це змінить форму тіла змії.

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо тіло не проглядається:<br />

- Чи відрізняються розміри кругів?<br />
- Переконайтеся, що ви запустили код

</div>
