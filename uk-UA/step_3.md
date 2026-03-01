<h2 class="c-project-heading--task">Порухаємо змію!</h2>

\--- task ---

Використайте змінну, щоб ваша змія ковзала по екрану.

\--- /task ---

<h2 class="c-project-heading--explainer">Вона ожила!</h2>

Ви на шляху до того, щоб ваша змійка почала рухатися по екрану.

Використайте змінну під назвою `x`, щоб відстежувати, де знаходиться голова змії.  
Щоразу, коли виконується `draw()`, ми додаватимемо трохи до `x`, щоб змістити все праворуч.

Функція `draw()` виконується безліч разів на секунду. Ось чому ми кожного разу робимо фон - він очищає екран, тому змія не залишає за собою слід.

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
circle(x, 200, 50)  # голова на x
circle(x - 35, 200, 40)  # круг x - 35

    ```
    x += 2 # щоб збільшити х вдвічі
    ```

\--- /code ---

</div>

<div class="c-project-output">
![The head and body of the snake moving to the right](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Спробуйте змінити швидкість руху змії, використовуючи більше або менше число в `x += 2`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо змія не порухалась:<br />

- Ви використовували `global x` всередині `draw()`?<br />
- Чи удосконалили `x` на `x += 2`?

</div>
