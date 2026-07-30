# -*- coding: utf-8 -*-
"""Generate multi-page Czech Biser site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HEAD = '''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{css}" />
</head>
<body>
  <div class="noise" aria-hidden="true"></div>
'''

def header(prefix="", current=""):
    def link(href, label, key):
        cur = ' aria-current="page"' if current == key else ""
        return f'      <a href="{prefix}{href}"{cur}>{label}</a>'
    links = "\n".join([
        link("index.html", "Главная", "home"),
        link("catalog.html", "Каталог", "catalog"),
        link("types.html", "Виды бисера", "types"),
        link("order.html", "Наличие / Заказ", "order"),
        link("payment.html", "Оплата/Доставка", "payment"),
        link("contacts.html", "Контакты", "contacts"),
    ])
    return f'''  <header class="header" id="header">
    <a class="logo" href="{prefix}index.html">
      <span class="logo-mark" aria-hidden="true"></span>
      <span class="logo-text">Czech <em>Biser</em></span>
    </a>
    <nav class="nav" id="nav" aria-label="Основная навигация">
{links}
    </nav>
    <a class="header-cta" href="https://wa.me/79272102531" target="_blank" rel="noopener">WhatsApp</a>
    <button class="menu-btn" id="menuBtn" type="button" aria-label="Открыть меню" aria-expanded="false">
      <span></span><span></span>
    </button>
  </header>
'''

def footer(prefix="", js="main.js"):
    return f'''  <footer class="footer">
    <div class="footer-brand">
      <span class="logo-mark" aria-hidden="true"></span>
      <div>
        <strong>Czech Biser</strong>
        <span>Чешский бисер Preciosa оптом</span>
        <div class="footer-links">
          <a href="{prefix}payment.html">Оплата/Доставка</a>
          <a href="{prefix}order.html">Наличие / Заказ</a>
          <a href="{prefix}contacts.html">Контакты</a>
          <a href="https://czechbiser.ru/" target="_blank" rel="noopener">czechbiser.ru</a>
          <a href="https://busina.shop/" target="_blank" rel="noopener">busina.shop</a>
        </div>
      </div>
    </div>
    <p>© <span id="year"></span> Czech Biser. Доставка по России.</p>
  </footer>

  <a class="whatsapp-float" href="https://wa.me/79272102531" target="_blank" rel="noopener" aria-label="Написать в WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.5 3.5A11.9 11.9 0 0 0 12.05 0C5.5 0 .15 5.35.15 11.9c0 2.1.55 4.15 1.6 5.95L0 24l6.3-1.65a11.9 11.9 0 0 0 5.75 1.45h.01c6.55 0 11.9-5.35 11.9-11.9 0-3.18-1.24-6.17-3.46-8.4zM12.05 21.15h-.01a9.9 9.9 0 0 1-5.05-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.5-5.22c0-5.45 4.44-9.88 9.9-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.9 7c0 5.45-4.44 9.88-9.89 9.88zm5.43-7.4c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.04-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.05 1.02-1.05 2.5s1.07 2.9 1.22 3.1c.15.2 2.11 3.22 5.11 4.52.71.31 1.27.49 1.7.63.72.23 1.37.2 1.89.12.58-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35z"/></svg>
  </a>

  <script src="{prefix}{js}"></script>
</body>
</html>
'''

def page_hero(crumbs, title, lead):
    crumbs_html = " <span>/</span> ".join(crumbs)
    return f'''  <section class="page-hero">
    <div class="page-hero-inner">
      <nav class="breadcrumb" aria-label="Хлебные крошки">{crumbs_html}</nav>
      <h1>{title}</h1>
      <p>{lead}</p>
    </div>
  </section>
'''

def write(path: Path, html: str):
    path.write_text(html, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


# --- payment.html ---
write(ROOT / "payment.html", HEAD.format(
    desc="Оплата и доставка чешского бисера Preciosa оптом по России.",
    title="Оплата/Доставка — Czech Biser",
    css="styles.css",
) + header(current="payment") + '''
  <main>
''' + page_hero(
    ['<a href="index.html">Главная</a>', "Оплата/Доставка"],
    "Оплата и доставка",
    "Прозрачный порядок заказа, варианты оплаты и отправка транспортными компаниями по всей России."
) + '''
    <div class="content-wrap">
      <div class="content-split">
        <div class="prose">
          <div class="notice">При большом объёме заказов на складе сроки отправки после оплаты могут увеличиться до 2 рабочих дней. Сроки сборки — до 5 рабочих дней.</div>

          <h2>Порядок оформления заказа</h2>
          <ol class="steps-plain">
            <li>
              <div>
                <strong>Заявка в бланке</strong>
                <span>Оформляете заявку через <a href="order.html">бланки заказа</a> и присылаете на <a href="mailto:biseropt63@gmail.com">biseropt63@gmail.com</a>.</span>
              </div>
            </li>
            <li>
              <div>
                <strong>Подтверждение менеджера</strong>
                <span>В течение 24 часов в рабочие дни менеджер свяжется с вами, уточнит оплату и доставку.</span>
              </div>
            </li>
            <li>
              <div>
                <strong>Резерв товара</strong>
                <span>После заявки товар резервируется. Если оплата не поступила за 3 рабочих дня — резерв снимается.</span>
              </div>
            </li>
            <li>
              <div>
                <strong>Отгрузка</strong>
                <span>После поступления оплаты товар отгружается с нашего склада.</span>
              </div>
            </li>
          </ol>

          <h2>Варианты доставки</h2>
          <div class="info-cards" style="grid-template-columns:1fr 1fr">
            <article>
              <h3>Транспортные компании</h3>
              <p>Доставка за счёт клиента. Работаем с ведущими ТК по России.</p>
            </article>
            <article>
              <h3>Почта России</h3>
              <p>Небольшие заказы: 1 место, не более 15 кг.</p>
            </article>
            <article>
              <h3>Самовывоз</h3>
              <p>г. Тольятти. Предварительно созвонитесь: <a href="tel:+79277799997">+7 927 779 99 97</a>.</p>
            </article>
            <article>
              <h3>Документы</h3>
              <p>Полный пакет сопроводительных документов к каждому заказу.</p>
            </article>
          </div>

          <h2 id="anchor">Варианты оплаты</h2>
          <ul class="why-list">
            <li>
              <strong>Криптовалютный счёт</strong>
              <span>Экономия 3–4%. Поможем с регистрацией на Bybit: <a href="https://wa.me/420728870811" target="_blank" rel="noopener">+420 728 870 811</a> (WhatsApp).</span>
            </li>
            <li>
              <strong>Карты российских банков</strong>
              <span>Для физлиц. При оплате на карту — скидка 10%.</span>
            </li>
            <li>
              <strong>Расчётный счёт ИП</strong>
              <span>Без НДС.</span>
            </li>
            <li>
              <strong>Расчётный счёт ООО</strong>
              <span>«Тольяттинская Кабельная Компания» — с НДС (+14% к сумме оплаты).</span>
            </li>
          </ul>

          <div class="cta-row">
            <a class="btn btn-primary" href="order.html">Перейти к бланкам заказа</a>
            <a class="btn btn-ghost dark" href="https://wa.me/79272102531" target="_blank" rel="noopener">WhatsApp</a>
          </div>
        </div>

        <aside class="side-panel">
          <h3>Важно знать</h3>
          <ul>
            <li>Минимум заказа — 10 кг</li>
            <li>Курс оплаты: 93 ₽</li>
            <li>Скидка 10% на карту</li>
            <li>Резерв — 3 рабочих дня</li>
          </ul>
          <a class="btn btn-primary full" href="mailto:biseropt63@gmail.com">Написать на email</a>
        </aside>
      </div>
    </div>
  </main>
''' + footer())


# --- contacts.html ---
write(ROOT / "contacts.html", HEAD.format(
    desc="Контакты Czech Biser: телефоны Россия и Чехия, email, склад в Тольятти.",
    title="Контакты — Czech Biser",
    css="styles.css",
) + header(current="contacts") + '''
  <main>
''' + page_hero(
    ['<a href="index.html">Главная</a>', "Контакты"],
    "Контакты",
    "По заказам и вопросам сотрудничества — Россия и Чехия."
) + '''
    <div class="content-wrap">
      <div class="content-split">
        <div>
          <div class="contact-list" style="margin-top:0">
            <a href="https://wa.me/420728870811" target="_blank" rel="noopener">
              <span>WhatsApp (предпочтительный)</span>
              <strong>+420 728 870 811</strong>
            </a>
            <a href="tel:+79272102531">
              <span>Телефон в России</span>
              <strong>+7 927 210 25 31</strong>
            </a>
            <a href="mailto:biseropt63@gmail.com">
              <span>Email для заказов</span>
              <strong>biseropt63@gmail.com</strong>
            </a>
            <a href="tel:+79277799997">
              <span>Самовывоз · Тольятти</span>
              <strong>+7 927 779 99 97</strong>
            </a>
          </div>

          <div class="info-cards" style="margin-top:2rem;grid-template-columns:1fr 1fr">
            <article>
              <h3>График склада</h3>
              <p>Пн–Пт: 8:30–16:30<br>Самарское время (МСК+1)<br>Сб–Вс: выходные</p>
            </article>
            <article>
              <h3>Мессенджеры</h3>
              <p>
                <a href="https://wa.me/79272102531" target="_blank" rel="noopener">WhatsApp РФ</a><br>
                <a href="https://wa.me/420728870811" target="_blank" rel="noopener">WhatsApp CZ</a>
              </p>
            </article>
          </div>

          <div class="legal-box">
            <h3>Сведения о юридическом лице</h3>
            <p>ООО «Тольяттинская Кабельная Компания»</p>
            <p>ИНН 6323061940</p>
            <p>Адрес для корреспонденции и возврата: 445000, г. Тольятти, Самарская обл., ул. Вокзальная, 44</p>
          </div>
        </div>

        <aside class="side-panel">
          <h3>Быстрая связь</h3>
          <p>Напишите — ответим по наличию, курсу и доставке.</p>
          <div class="cta-row" style="flex-direction:column">
            <a class="btn btn-primary full" href="https://wa.me/79272102531" target="_blank" rel="noopener">Открыть WhatsApp</a>
            <a class="btn btn-ghost dark full" href="mailto:biseropt63@gmail.com">Написать email</a>
            <a class="btn btn-ghost dark full" href="order.html">Бланки заказа</a>
          </div>
        </aside>
      </div>
    </div>
  </main>
''' + footer())


# --- types.html ---
write(ROOT / "types.html", HEAD.format(
    desc="Виды чешского бисера Preciosa: рокайль, рубка, стеклярус, Twin.",
    title="Виды чешского бисера — Czech Biser",
    css="styles.css",
) + header(current="types") + '''
  <main>
''' + page_hero(
    ['<a href="index.html">Главная</a>', "Виды чешского бисера"],
    "Виды чешского бисера",
    "Основные формы Preciosa: размеры, профиль и тип отверстия."
) + '''
    <div class="content-wrap">
      <div class="type-block" id="rocailles">
        <h2>Круглый бисер (Rocailles)</h2>
        <table class="data-table">
          <thead>
            <tr><th>Наименование / артикул</th><th>Размеры</th><th>Профиль / отверстие</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Rocailles-RH<br>311 19 001, 331 19 001</td>
              <td>1/0–16/0, 31/0–34/0</td>
              <td>Круглый / круглое</td>
            </tr>
            <tr>
              <td>Rocailles-SH<br>311 29 001, 331 29 001</td>
              <td>1/0–14/0, 31/0–34/0</td>
              <td>Круглый / квадратное</td>
            </tr>
            <tr>
              <td>Cut-Rocailles-RH<br>361 11 001</td>
              <td>8/0, 9/0, 10/0, 11/0, 13/0, 15/0</td>
              <td>Усечённый круг / круглое</td>
            </tr>
          </tbody>
        </table>
        <div class="cta-row">
          <a class="btn btn-ghost dark" href="products/rocailles.html">Подробнее о рокайле</a>
          <a class="btn btn-ghost dark" href="https://czechbiser.ru/rocailles_p/" target="_blank" rel="noopener">На czechbiser.ru</a>
        </div>
      </div>

      <div class="type-block" id="cut">
        <h2>Рубка (Two Cut / Three Cut)</h2>
        <table class="data-table">
          <thead>
            <tr><th>Наименование / артикул</th><th>Размеры</th><th>Профиль / отверстие</th></tr>
          </thead>
          <tbody>
            <tr><td>2Cuts-RH / 351 31 001</td><td>8/0–12/0, 32/0</td><td>Шестиугольник / круглое</td></tr>
            <tr><td>2cuts Bevelled-RH / 351 36 001</td><td>8/0, 9/0</td><td>Скошенный шестиугольник</td></tr>
            <tr><td>2cuts extra-RH / 351 51 001</td><td>9/0–11/0</td><td>Увеличенный диаметр</td></tr>
            <tr><td>2cuts Cut-RH / 361 81 001</td><td>9/0–11/0</td><td>Шестиугольник / круглое</td></tr>
            <tr><td>3cuts-RH / 361 31 001</td><td>8/0–12/0</td><td>Огранённый шестиугольник</td></tr>
          </tbody>
        </table>
        <div class="cta-row">
          <a class="btn btn-ghost dark" href="products/cut.html">Подробнее</a>
          <a class="btn btn-ghost dark" href="https://czechbiser.ru/tcb_p/" target="_blank" rel="noopener">На czechbiser.ru</a>
        </div>
      </div>

      <div class="type-block" id="bugles">
        <h2>Стеклярус (Bugles)</h2>
        <table class="data-table">
          <thead>
            <tr><th>Наименование / артикул</th><th>Длины</th><th>Особенности</th></tr>
          </thead>
          <tbody>
            <tr><td>Bugles-RH / 351 12 001</td><td>0.5″–15.6″</td><td>Круглый / круглое отверстие</td></tr>
            <tr><td>Bugles-SH / 351 22 001</td><td>0.5″–15.6″</td><td>Квадратное отверстие</td></tr>
            <tr><td>Bugles-SupTwSH / 351 28 001</td><td>1″, 2″</td><td>Супер-витое квадратное</td></tr>
            <tr><td>BuglesHex-RH / 351 32 001</td><td>0.5″–15.6″</td><td>Шестиугольник</td></tr>
            <tr><td>BuglesHex-TwRH / 351 38 001</td><td>3″–15.6″</td><td>Кручёный шестиугольник</td></tr>
          </tbody>
        </table>
        <div class="cta-row">
          <a class="btn btn-ghost dark" href="products/bugles.html">Подробнее</a>
          <a class="btn btn-ghost dark" href="https://czechbiser.ru/bugles_p/" target="_blank" rel="noopener">На czechbiser.ru</a>
        </div>
      </div>

      <div class="type-block" id="twin">
        <h2>Бисер Twin</h2>
        <table class="data-table">
          <thead>
            <tr><th>Наименование / артикул</th><th>Размер</th><th>Профиль / отверстие</th></tr>
          </thead>
          <tbody>
            <tr><td>Twin-2RH / 321 96 001</td><td>2.5 × 5 mm</td><td>Овальный, 2 круглых отверстия</td></tr>
          </tbody>
        </table>
        <div class="cta-row">
          <a class="btn btn-ghost dark" href="products/twin.html">Подробнее</a>
          <a class="btn btn-ghost dark" href="https://czechbiser.ru/twin_p/" target="_blank" rel="noopener">На czechbiser.ru</a>
        </div>
      </div>

      <div class="cta-row">
        <a class="btn btn-primary" href="catalog.html">Весь каталог</a>
        <a class="btn btn-ghost dark" href="order.html">Заказать по бланку</a>
      </div>
    </div>
  </main>
''' + footer())


# --- order.html ---
write(ROOT / "order.html", HEAD.format(
    desc="Наличие и заказ: бланки Excel для оптового заказа бисера Preciosa. Минимум 10 кг.",
    title="Наличие / Заказ — Czech Biser",
    css="styles.css",
) + header(current="order") + '''
  <main>
''' + page_hero(
    ['<a href="index.html">Главная</a>', "Наличие / Заказ"],
    "Наличие / Заказ",
    "Скачайте бланки, отметьте артикулы и отправьте заявку на email."
) + '''
    <div class="content-wrap">
      <div class="notice danger">
        <strong>Внимание!</strong> Мы не продаём чешский бисер в социальных сетях.
        Все заказы принимаются только в бланках MS Excel на почту
        <a href="mailto:biseropt63@gmail.com">biseropt63@gmail.com</a>.
        Минимальный объём — <strong>10 кг</strong>.
      </div>

      <div class="prose" style="margin-bottom:2rem">
        <p>Проставьте желаемое количество напротив нужных артикулов в графе «заказ» и вышлите заполненный бланк на email. Перед скачиванием нажмите <strong>Ctrl+F5</strong>, чтобы обновить кэш.</p>
        <p>Прайс-лист обновлён: 27.07.2026 · Курс оплаты: 93 ₽</p>
      </div>

      <h2 class="block-title">Бланки для заказа</h2>
      <div class="download-grid">
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Круглый%20бисер">
          <strong>Круглый бисер</strong>
          <span>Рокайль, размеры 1–34, фасовка в т.ч. 500 г</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Стеклярус">
          <strong>Стеклярус</strong>
          <span>Bugles, фасовка 500 г</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Большие%20пакеты">
          <strong>Большие пакеты</strong>
          <span>Круглый бисер и стеклярус по 500 г</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Шатоны">
          <strong>Шатоны в цапах</strong>
          <span>ss12, ss16, ss29, матовые ss39</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Биконусы">
          <strong>Биконусы</strong>
          <span>Rondelle / биконусы Preciosa</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Rivoli">
          <strong>Rivoli</strong>
          <span>Ювелирные вставки и камни</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Жемчуг">
          <strong>Бусины под жемчуг</strong>
          <span>Имитация жемчуга Preciosa</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Maxima%20Premium">
          <strong>Maxima Premium</strong>
          <span>Жемчуг Preciosa Maxima Premium</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Основы%20для%20брошей">
          <strong>Основы для брошей</strong>
          <span>Японские основы</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Шатоны%20без%20цап">
          <strong>Шатоны без цап</strong>
          <span>ss2,5 (pp6), ss16 (pp31)</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Пайетки">
          <strong>Пайетки</strong>
          <span>Декоративные пайетки</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Стразы">
          <strong>Стразы Preciosa</strong>
          <span>Горячая и холодная фиксация</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
        <a class="download-item" href="mailto:biseropt63@gmail.com?subject=Бланк:%20Прессованные%20бусины">
          <strong>Прессованные бусины</strong>
          <span>Фасовка 10 г, цена за пакет</span>
          <span class="cat-link">Запросить бланк →</span>
        </a>
      </div>

      <div class="cta-row">
        <a class="btn btn-primary" href="mailto:biseropt63@gmail.com">Отправить заявку на email</a>
        <a class="btn btn-ghost dark" href="payment.html">Условия оплаты</a>
        <a class="btn btn-ghost dark" href="https://wa.me/79272102531" target="_blank" rel="noopener">Уточнить наличие</a>
      </div>
    </div>
  </main>
''' + footer())

print("core pages done")
