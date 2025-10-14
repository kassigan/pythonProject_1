"""
Генератор одностраничного сайта "Find your best Pet".

Скрипт создаёт файл find_your_best_pet.html в текущей папке.
Открой файл в браузере (double-click) или запусти простой сервер:
  python -m http.server 8000
и открой http://localhost:8000/find_your_best_pet.html

Замечания:
- Это статическая страница. Поля загрузки фотографий и форма — только вёрстка; чтобы сохранять данные/файлы, нужно добавить серверную часть (Flask/Django/Node и т.д.).
- В коде есть явные места, помеченные <!-- PLACEHOLDER -->, где можно заполнять данные о животных и добавлять изображения.
"""

html_content = '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Find your best Pet</title>
  <style>
    /* Базовая стилизация */
    html,body{height:100%;margin:0;font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial}
    body{
      /* Фоновая фотография счастливых людей с собаками и кошками (Unsplash) */
      background-image: url('https://images.unsplash.com/photo-1507149833265-60c372daea22?auto=format&fit=crop&w=1650&q=80');
      background-size: cover; background-position: center; background-attachment: fixed;
      color:#111;
      display:flex;align-items:flex-start;justify-content:center;padding:40px 20px;
    }
    /* Полупрозрачная карточка-обёртка для контента */
    .container{
      width:100%;max-width:1100px;background:rgba(255,255,255,0.92);backdrop-filter:blur(6px);border-radius:12px;padding:28px;box-shadow:0 8px 30px rgba(0,0,0,0.2);
    }
    header{text-align:center;margin-bottom:18px}
    h1{margin:0;font-size:34px;letter-spacing:0.4px}
    .subtitle{margin-top:10px;color:#333;line-height:1.45}
    nav{display:flex;gap:12px;justify-content:center;margin:18px 0}
    .btn{padding:10px 18px;border-radius:8px;text-decoration:none;font-weight:600;border:1px solid rgba(0,0,0,0.08);background:linear-gradient(180deg,#fff,#f2f2f2);box-shadow:0 2px 6px rgba(0,0,0,0.06)}
    .divider{height:1px;background:linear-gradient(90deg,#0000, #0002, #0000);margin:22px 0}

    /* Секции с карточками */
    .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    .card{background:#fff;border-radius:10px;padding:14px;min-height:150px;box-shadow:0 6px 18px rgba(0,0,0,0.06);display:flex;flex-direction:column}
    .card h3{margin:6px 0 8px}
    .card p{flex:1;margin:0;color:#444}
    .card a{margin-top:10px;display:inline-block}

    /* Секции подробного просмотра */
    section.detail{margin-top:20px;padding:16px;border-radius:10px;background:linear-gradient(180deg,rgba(250,250,250,0.9),#fff);box-shadow:inset 0 0 0 1px rgba(0,0,0,0.02)}
    .pet-form{display:grid;grid-template-columns:1fr 360px;gap:20px;align-items:start}
    .pet-info{display:flex;flex-direction:column;gap:10px}
    label{font-weight:600;font-size:14px}
    input[type=text], textarea, select{width:100%;padding:10px;border:1px solid #ddd;border-radius:8px;font-size:14px}
    textarea{min-height:140px;resize:vertical}
    .photo-placeholder{border:2px dashed #dcdcdc;border-radius:8px;height:220px;display:flex;align-items:center;justify-content:center;color:#888}
    .small-note{font-size:13px;color:#666}
    .actions{display:flex;gap:10px;margin-top:8px}
    .muted{color:#666;font-size:14px}

    footer{margin-top:18px;text-align:center;color:#555;font-size:14px}

    /* Mobile */
    @media (max-width:880px){
      .grid{grid-template-columns:1fr}
      .pet-form{grid-template-columns:1fr}
      .photo-placeholder{height:180px}
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Find your best Pet</h1>
      <p class="subtitle">Это агрегатор бездомных животных, которые ищут хозяев. Тут вы сможете прочитать историю животного, узнать про его характер, его привычки и предпочтения, связаться с волонтёром или приютом, где сейчас находится животное.</p>
    </header>

    <nav>
      <a class="btn" href="#cats">Кошки</a>
      <a class="btn" href="#dogs">Собаки</a>
      <a class="btn" href="#other">Другие животные</a>
    </nav>

    <div class="divider"></div>

    <!-- Блок карточек: места для добавления конкретных животных -->
    <div class="grid" aria-label="Категории животных">
      <article class="card">
        <h3>Кошки</h3>
        <p>Короткое описание: здесь вы сможете найти кошек разного возраста и характера — от ласковых до независимых. Нажмите "Подробнее", чтобы перейти к списку и карточкам.</p>
        <a href="#cats">Подробнее →</a>
      </article>

      <article class="card">
        <h3>Собаки</h3>
        <p>Короткое описание: собаки разного размера и темперамента, от активных до спокойных. Нажмите "Подробнее", чтобы перейти к списку и карточкам.</p>
        <a href="#dogs">Подробнее →</a>
      </article>

      <article class="card">
        <h3>Другие животные</h3>
        <p>Кролики, хорьки, птицы и другие — маленькие и необычные питомцы, которые тоже ищут дом.</p>
        <a href="#other">Подробнее →</a>
      </article>
    </div>

    <div class="divider"></div>

    <!-- Секции с якорями, где можно размещать подробные карточки животных -->
    <section id="cats" class="detail">
      <h2>Кошки</h2>
      <p class="muted">Ниже — шаблон карточки питомца. Скопируйте блок, чтобы добавить ещё животных. Места для заполнения отмечены <!-- PLACEHOLDER -->.</p>

      <!-- Пример карточки / форма заполнения -->
      <div class="pet-form">
        <div class="pet-info">
          <label>Имя</label>
          <input type="text" placeholder="Например: Мурка" />

          <label>Возраст</label>
          <input type="text" placeholder="Например: 2 года" />

          <label>Короткая история</label>
          <textarea placeholder="Расскажите, как животное оказалось в приюте / на улице, особенности биографии..."></textarea>

          <label>Характер и привычки</label>
          <textarea placeholder="Например: ласковая, любит играть с мячиком, немного застенчива"></textarea>

          <label>Предпочтения (корм, режим, совместимость с детьми/кошками/собаками)</label>
          <input type="text" placeholder="Например: сухой корм, аккуратна с детьми, ладит с кошками" />

          <label>Контакты волонтёра / приюта</label>
          <input type="text" placeholder="Телефон или email волонтёра" />

          <div class="actions">
            <button class="btn" type="button">Сохранить (макет)</button>
            <button class="btn" type="button">Поделиться</button>
          </div>
        </div>

        <div>
          <label>Фотографии</label>
          <div class="photo-placeholder"> <!-- PLACEHOLDER: сюда можно вставить уменьшенное превью фото или картинку -->
            Перетащите или выберите фото
          </div>
          <p class="small-note">Вы можете добавить несколько фотографий. В статическом варианте поле ниже не загрузит файл на сервер — для этого нужна серверная часть.</p>
          <input type="file" accept="image/*" multiple />
        </div>
      </div>

    </section>

    <div class="divider"></div>

    <section id="dogs" class="detail">
      <h2>Собаки</h2>
      <p class="muted">Шаблон карточки для собак — скопируйте и заполните информацию про конкретного питомца.</p>

      <!-- PLACEHOLDER: повторите структуру карточки как выше для добавления собак -->
      <div class="pet-form">
        <div class="pet-info">
          <label>Имя</label>
          <input type="text" placeholder="Например: Бим" />

          <label>Возраст</label>
          <input type="text" placeholder="Например: 4 года" />

          <label>Короткая история</label>
          <textarea placeholder="Коротко о судьбе собаки..."></textarea>

          <label>Характер и привычки</label>
          <textarea placeholder="Например: активный, любит прогулки, подходит к тренировкам"></textarea>

          <label>Предпочтения</label>
          <input type="text" placeholder="Например: корм, прогулки, отношение к другим животным" />

          <label>Контакты волонтёра / приюта</label>
          <input type="text" placeholder="Телефон или email" />

        </div>

        <div>
          <label>Фотографии</label>
          <div class="photo-placeholder">Место для фото собаки</div>
          <input type="file" accept="image/*" multiple />
        </div>
      </div>

    </section>

    <div class="divider"></div>

    <section id="other" class="detail">
      <h2>Другие животные</h2>
      <p class="muted">Здесь можно разместить информацию о кроликах, хорьках, птицах и пр. Формат карточки тот же — имя, история, характер, фото, контакты.</p>

      <!-- PLACEHOLDER for other animals -->
      <div class="pet-form">
        <div class="pet-info">
          <label>Вид / Имя</label>
          <input type="text" placeholder="Например: Кролик — Пух" />

          <label>Возраст</label>
          <input type="text" placeholder="Например: 1 год" />

          <label>История</label>
          <textarea placeholder="Коротко о животном..."></textarea>

          <label>Характер</label>
          <textarea placeholder="Например: спокойный, любит лакомства"></textarea>

          <label>Контакты</label>
          <input type="text" placeholder="Телефон / email" />
        </div>

        <div>
          <label>Фотографии</label>
          <div class="photo-placeholder">Место для фото</div>
          <input type="file" accept="image/*" multiple />
        </div>
      </div>

    </section>

    <footer>
      <p>Если захотите — могу превратить этот статический макет в рабочее приложение на Flask (с загрузкой фотографий и сохранением карточек).</p>
    </footer>
  </div>
</body>
</html>
'''

# Создаём файл
with open('find_your_best_pet.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Файл find_your_best_pet.html успешно создан в текущей папке.')
print('Откройте его в браузере или запустите: python -m http.server 8000')
