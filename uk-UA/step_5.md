<h2 class="c-project-heading--task">Додамо руху</h2>

\--- task ---

Щоб заставити змію рухатись зі сторони в сторону використовуйте рухомий offset

\--- /task ---

<h2 class="c-project-heading--explainer">Заставимо її ковзати!</h2>

Зробіть свою змію **ковзати**, додавши її тілу плавне погойдування вгору-вниз.

Створіть нову змінну з назвою `offset`. Це трохи змінюватиметься кожного разу, коли ваш код виконується — щось на кшталт хвилі, яка повільно піднімається та опускається.

Ви використаєте його для плавного переміщення частин тіла вгору і вниз.  
Ви використовуватимете функцію під назвою `sin()`, яка є частиною математичних інструментів Python.

Не хвилюйтеся, як це працює — це просто дає нам гарну плавну криву, яку ми можемо використовувати для анімації.

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
    offset = sin(x * 0.1) * 10
    
    circle(x, 200, 50)               # голова на x
    circle(x - 35, 200 + offset, 40) # круг 1
    circle(x - 65, 200 - offset, 35) # круг 2
    circle(x - 90, 200 + offset, 30) # хвіст
    
    x += 2  # збільшити х вдвічі
    ```

\--- /code ---

</div>

<div class="c-project-output">
![A four-part snake wriggling side to side as it moves](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Порада

Спробуйте змінити числа в `offset = sin(x * 0.1) * 10`:

- `0.1` контролює **швидкість** ковзання
- «10» контролює **величину** коливання

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо ковзання не працює:<br />

- Чи використовували ви `offset`, щоб змінити **y** розміщенні круга?<br />
- Чи правильні ваші дужки та орфографія?<br />
- Перевірте, чи відповідають ваші рядки `circle()` прикладу

</div>
