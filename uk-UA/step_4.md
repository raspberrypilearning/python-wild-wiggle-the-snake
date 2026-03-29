<h2 class="c-project-heading--task">Зробіть змію довшою</h2>

\--- task ---

Додамо ще два круги позаду змії, щоб зробити її повне тіло.

\--- /task ---

<h2 class="c-project-heading--explainer">Ковзь, ковзь...</h2>

Видовжте свою змію, додавши ще два круги позаду

Продовжуйте використовувати змінну `x` та віднімайте різні суми, щоб розмістити кожний круг в потрібному місці.

Кожен з них має бути трохи меншим і зміщеним лівіше.

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
circle(x, 200, 50)        # голова на x
circle(x - 35, 200, 40)   # круг 1
circle(x - 65, 200, 35)   # круг 2
circle(x - 90, 200, 30)   # хвіст

    ```
    x += 2 # щоб збільшити х вдвічі
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![A full snake made from 4 green circles of different sizes](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

- Спробуйте різні розміри кругів, щоб зробити вгодовану або тонку змійку.<br />
- Ви також можете змінити відстань між кругами.

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо деякі частини тіла не відображаються:<br />

- Перевірте, чи кожне `circle()` має 3 числа<br />
- Звертайте увагу на орфографічні помилки або пропущені коми<br />
- Пам'ятайте: кожен новий відрізок знаходиться все лівіше, і лівіше (використовуйте `x - ...`)

</div>
