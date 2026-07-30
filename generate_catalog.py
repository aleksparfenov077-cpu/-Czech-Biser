# -*- coding: utf-8 -*-
"""Generate catalog + product pages."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gen", ROOT / "generate_pages.py")
# Re-define helpers locally to avoid re-running page writes from generate_pages

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

def footer(prefix=""):
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

  <script src="{prefix}main.js"></script>
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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


PRODUCTS = [
    ("rocailles.html", "Круглый бисер", "PRECIOSA Rocailles — классический круглый бисер для украшений и вышивки.",
     "Самый распространённый вид стеклянных бусин. Производятся размерами от 1,5 до 8 мм (серия «нулей» от 16/0 до 1/0). Есть варианты без покрытия и с покрытием, а также гранёный рокайль.",
     "https://czechbiser.ru/rocailles_p/", "assets/beads.jpg"),
    ("cut.html", "Рубка", "Two Cut и Three Cut Beads Preciosa — бисер с гранями для игры света.",
     "Рубка с шестиугольным профилем и круглое отверстие. Линейки 2Cuts, Bevelled, Extra, Cut и 3Cuts — для декоративных и ювелирных работ.",
     "https://czechbiser.ru/tcb_p/", "assets/jewelry.jpg"),
    ("bugles.html", "Стеклярус", "Bugles Preciosa — стеклярус разных длин и сечений.",
     "Круглый, квадратный, шестиугольный и кручёный стеклярус длиной от 0.5″ до 15.6″. Удобен для вышивки, бижутерии и декора.",
     "https://czechbiser.ru/bugles_p/", "assets/beads.jpg"),
    ("big-packs.html", "Большие пакеты", "Оптовая фасовка круглого бисера и стекляруса по 500 г.",
     "Крупные пакеты для студий и производств. Заказывайте через бланки на странице «Наличие / Заказ».",
     "https://czechbiser.ru/big-packs/", "assets/catalog.jpg"),
    ("mixes.html", "Миксы бусин", "Готовые миксы бусин Preciosa для декора и творчества.",
     "Подобранные сочетания цветов и форм — удобно для розницы и мастер-классов.",
     "https://czechbiser.ru/beads_mixes_p/", "assets/jewelry.jpg"),
    ("twin.html", "Twin", "Бисер Twin 2.5×5 мм с двумя отверстиями.",
     "Овальный профиль и два круглых отверстия — для сложных техник плетения и многослойных украшений.",
     "https://czechbiser.ru/twin_p/", "assets/beads.jpg"),
    ("pressed.html", "Прессованные бусины", "Прессованные бусины Preciosa разных форм и размеров.",
     "Фасовка по 10 г. В бланках цена указана за 1 пакет 10 г.",
     "https://czechbiser.ru/pressed_beads/", "assets/gems.jpg"),
    ("pearls.html", "Жемчужные бусины", "Бусины под жемчуг Preciosa.",
     "Имитация жемчуга для украшений и декора. В наличии и под заказ — уточняйте по бланку.",
     "https://czechbiser.ru/ip/", "assets/pearls.jpg"),
    ("maxima.html", "Жемчуг Maxima Premium", "Preciosa Maxima Premium — премиальный жемчуг.",
     "Высокое качество покрытия и стабильный цвет. Идеален для ювелирных и свадебных коллекций.",
     "https://czechbiser.ru/maxima-premium-pearls/", "assets/pearls.jpg"),
    ("chatons.html", "Шатоны в цапах", "Шатоны Preciosa в цапах: ss12, ss16, ss29, матовые ss39.",
     "Серебро, золото, чёрные оправы. Матовые шатоны 8 mm (ss39) — от 0,17 €/шт. Фото: на czechbiser.ru.",
     "https://czechbiser.ru/ss16/", "assets/crystals.jpg"),
    ("bicones.html", "Биконусы", "Биконусы / rondelle Preciosa.",
     "Классические кристаллы для сережек, браслетов и вышивки. Заказ по бланку.",
     "https://czechbiser.ru/rondell/", "assets/gems.jpg"),
    ("rivoli.html", "Rivoli", "Ювелирные вставки и камни Rivoli.",
     "Вставки для брошей, серег и кулонов. Под заказ и со склада.",
     "https://czechbiser.ru/rivoli/", "assets/crystals.jpg"),
    ("brooch.html", "Основы для брошей", "Японские основы для брошей.",
     "Надёжная фурнитура под бисерную и кристальную вышивку.",
     "https://czechbiser.ru/brb-2/", "assets/atelier.jpg"),
    ("sequins.html", "Пайетки", "Декоративные пайетки для вышивки и декора.",
     "Дополняют бисерные и стразовые работы. Заказ через бланк.",
     "https://czechbiser.ru/paillette-2/", "assets/jewelry.jpg"),
    ("rhinestones.html", "Стразы Preciosa", "Стразы холодной и горячей фиксации, размеры ss5–ss12.",
     "Для одежды, аксессуаров и декора. Холодная и горячая фиксация.",
     "https://czechbiser.ru/rhinestones/", "assets/crystals.jpg"),
]

PARTNERS = [
    ("TOHO", "https://busina.shop/cat/toho"),
    ("MIYUKI", "https://busina.shop/cat/miyuki"),
    ("MATUBO", "https://busina.shop/cat/matubo"),
    ("RUTKOVSKY", "https://busina.shop/cat/rutkovsky"),
    ("CRYSTALS", "https://busina.shop/cat/pios"),
    ("CzechMates", "https://busina.shop/cat/czechmates"),
    ("Cotton Pearls", "https://busina.shop/cat/cotton-pearls-shinko"),
]

# Catalog page
product_cards = "\n".join(
    f'''        <a class="product-link" href="products/{slug}">
          <strong>{name}</strong>
          <span>{lead[:90]}{'…' if len(lead)>90 else ''}</span>
          <span class="ext">Открыть →</span>
        </a>'''
    for slug, name, lead, *_ in PRODUCTS
)

partner_cards = "\n".join(
    f'''        <a class="partner-link" href="{url}" target="_blank" rel="noopener">{name}<small>busina.shop</small></a>'''
    for name, url in PARTNERS
)

write(ROOT / "catalog.html", HEAD.format(
    desc="Каталог чешского бисера Preciosa, стразов, бусин. Ссылки на czechbiser.ru и busina.shop.",
    title="Каталог — Czech Biser",
    css="styles.css",
) + header(current="catalog") + '''
  <main>
''' + page_hero(
    ['<a href="index.html">Главная</a>', "Каталог"],
    "Каталог товаров",
    "Preciosa на нашем сайте и czechbiser.ru · бренды TOHO, Miyuki и другие — на busina.shop."
) + f'''
    <div class="content-wrap">
      <h2 class="block-title">Наши товары Preciosa</h2>
      <div class="product-links">
{product_cards}
      </div>

      <h2 class="block-title" style="margin-top:3rem">Другие бренды на busina.shop</h2>
      <p class="section-lead" style="margin-bottom:1.2rem">TOHO, Miyuki, Matubo, CzechMates, Cotton Pearls и другие позиции — на партнёрском каталоге.</p>
      <div class="partner-grid">
{partner_cards}
      </div>

      <div class="cta-row" style="margin-top:2.5rem">
        <a class="btn btn-primary" href="order.html">Наличие / бланки заказа</a>
        <a class="btn btn-ghost dark" href="https://czechbiser.ru/" target="_blank" rel="noopener">Открыть czechbiser.ru</a>
        <a class="btn btn-ghost dark" href="https://busina.shop/" target="_blank" rel="noopener">Открыть busina.shop</a>
      </div>
    </div>
  </main>
''' + footer())

# Product pages
for slug, name, lead, body, external, img in PRODUCTS:
    extra = ""
    if slug == "chatons.html":
        extra = '''
          <p>Также: <a href="https://czechbiser.ru/ss39m/" target="_blank" rel="noopener">матовые шатоны ss39</a> ·
          <a href="https://czechbiser.ru/chtns_photo/" target="_blank" rel="noopener">фото шатонов</a></p>'''
    if slug == "rocailles.html":
        extra = '''
          <ul class="why-list">
            <li><strong>Размеры 1–34</strong><span>Традиционная «нулевая» серия Preciosa</span></li>
            <li><strong>10/0 — 1 и 2 категория</strong><span>Популярный размер для опта</span></li>
          </ul>'''

    html = HEAD.format(
        desc=lead,
        title=f"{name} — Czech Biser",
        css="../styles.css",
    ) + header(prefix="../", current="catalog") + '''
  <main>
''' + page_hero(
        [f'<a href="../index.html">Главная</a>', f'<a href="../catalog.html">Каталог</a>', name],
        name,
        lead,
    ) + f'''
    <div class="content-wrap">
      <div class="content-split">
        <div class="prose">
          <div class="why-visual" style="min-height:320px;margin-bottom:1.5rem;position:relative;overflow:hidden">
            <img src="../{img}" alt="{name}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" />
          </div>
          <h2>Описание</h2>
          <p>{body}</p>
          {extra}
          <div class="cta-row">
            <a class="btn btn-primary" href="../order.html">Заказать по бланку</a>
            <a class="btn btn-ghost dark" href="{external}" target="_blank" rel="noopener">Смотреть на czechbiser.ru</a>
            <a class="btn btn-ghost dark" href="https://wa.me/79272102531" target="_blank" rel="noopener">WhatsApp</a>
          </div>
        </div>
        <aside class="side-panel">
          <h3>Связанные разделы</h3>
          <ul>
            <li><a href="../types.html">Виды бисера</a></li>
            <li><a href="../order.html">Наличие / Заказ</a></li>
            <li><a href="../payment.html">Оплата/Доставка</a></li>
            <li><a href="{external}" target="_blank" rel="noopener">czechbiser.ru</a></li>
          </ul>
          <a class="btn btn-primary full" href="mailto:biseropt63@gmail.com?subject=Заказ:%20{name}">Запросить прайс</a>
        </aside>
      </div>
    </div>
  </main>
''' + footer(prefix="../")
    write(ROOT / "products" / slug, html)

print("catalog + products done")
