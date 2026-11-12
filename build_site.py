#!/usr/bin/env python3
"""
PALATA — Industrial Brutalist Single-Page Builder (v3 fixed)
Desktop (>=1024px): fixed left sidebar only (top header hidden).
Mobile (<=1023px): native-app UX — sticky top bar, bottom dock, 2x2 grids,
swipeable ranks, horizontal filter chips, zero overflow.
"""
import json
import re
from pathlib import Path

ROOT = Path(r"D:\PALATA_NEW")

# ------------------------------------------------------------------
# Load source data
# ------------------------------------------------------------------
with open(ROOT / "data" / "gallery.json", "r", encoding="utf-8") as f:
    GALLERY_SOURCE = json.load(f)["gallery"]

CURATED_FILES = [
    "whatsapp-image-2024-10-30-at-21.14.48-e1730375910347.jpeg",
    "whatsapp-image-2024-10-30-at-21.29.41-e1730376191532.jpeg",
    "whatsapp-image-2024-10-30-at-21.19.15.jpeg",
    "whatsapp-image-2024-10-30-at-21.20.44.jpeg",
    "whatsapp-image-2024-10-30-at-21.27.18.jpeg",
    "whatsapp-image-2024-10-30-at-21.31.30.jpeg",
    "whatsapp-image-2024-10-30-at-21.36.43.jpeg",
    "whatsapp-image-2024-10-30-at-21.38.53.jpeg",
    "whatsapp-image-2024-10-30-at-21.56.38.jpeg",
    "whatsapp-image-2024-10-30-at-21.57.42.jpeg",
    "whatsapp-image-2024-10-30-at-22.06.26.jpeg",
    "whatsapp-image-2024-10-30-at-22.10.03.jpeg",
    "whatsapp-image-2024-10-30-at-22.48.21.jpeg",
    "whatsapp-image-2024-10-30-at-22.50.07-e1730377550353.jpeg",
    "whatsapp-image-2024-10-30-at-22.51.38.jpeg",
    "whatsapp-image-2024-10-30-at-22.54.53.jpeg",
    "whatsapp-image-2024-10-30-at-21.44.24.jpeg",
]

CATEGORY_MAP = {}
for item in GALLERY_SOURCE:
    if item["file"] in CURATED_FILES:
        CATEGORY_MAP[item["category"]] = item["category"]

BASE_URL = "https://xn----7sbaa5baqdtkc7agh5e.xn--p1ai/wp-content/uploads/2024/10/"

# ------------------------------------------------------------------
# Stop-Konstantin filter (no Konstantin anywhere in output)
# ------------------------------------------------------------------
def is_konstantin(item):
    blob = " ".join([item.get("file", ""), item.get("alt", ""), item.get("caption", ""), item.get("category", "")])
    return bool(re.search(r"\bКонстантин\b|\bКонстантина\b|\bКонстантину\b|Константину", blob, re.IGNORECASE))

CURATED_GALLERY = []
for item in GALLERY_SOURCE:
    if item["file"] not in CURATED_FILES:
        continue
    if is_konstantin(item):
        continue
    cat = CATEGORY_MAP.get(item["category"], item["category"])
    CURATED_GALLERY.append({
        "file": item["file"],
        "alt": item["alt"],
        "caption": item["caption"],
        "category": cat,
    })

print(f"Curated images: {len(CURATED_GALLERY)}")

all_text = json.dumps(CURATED_GALLERY, ensure_ascii=False)
if re.search(r"Константин", all_text, re.IGNORECASE):
    raise SystemExit("FAIL: Konstantin still present in curated data!")
if "ЯрСайт" in all_text:
    raise SystemExit("FAIL: YarSite still present in curated data!")

# ------------------------------------------------------------------
# Content (dry, factual, Russian-only — slop stop applied)
# ------------------------------------------------------------------
APHORISMS = [
    "Слава — тень добродетели.",
    "Жажда славы — это признак величия души.",
    "Честь — единственная валюта, которая не обесценивается.",
]

TABLE_OF_RANKS = [
    {
        "num": "1722",
        "headline": "Петр I подписывает Табель о рангах.",
        "body": "До Табеля — хаос. Князь мог быть ничем, дворянин — ничтожеством. Петр ввёл 14 классов, жёстко привязанных к службе. Всё — до запятой. Есть ранг — есть права. Нет — сиди тихо.",
    },
    {
        "num": "Князь ≠ Ранг",
        "headline": "Титул не даёт власти.",
        "body": "Титул «князь» — часто просто родовое звание. Реальная власть — от службы, а не от крови. Подпоручик 14 класса, пробившийся до полковника (6 класс), становится личным дворянином, затем — наследственным. Решает судьбы губерний.",
    },
    {
        "num": "Ранг VI",
        "headline": "Социальный лифт.",
        "body": "Шестой класс (полковник / коллежский советник) даёт наследственную дворянскую честь. Чёткие уровни, прозрачные правила апгрейда. Хочешь статус — отслужи. Хочешь орден — сделай подвиг.",
    },
    {
        "num": "XXI век",
        "headline": "Логика Табеля сегодня.",
        "body": "Прозрачные критерии. Открытая хроника. Только merit — действие, зафиксированное орденом. Без приворотов. Без связей.",
    },
]

ORG = {
    "name": "«Международная палата личности»",
    "chairman": "Малыхин Юрий Иванович",
    "established": "18 июня 1999 года",
    "city": "Санкт-Петербург",
    "address": "191014, Санкт-Петербург, ул. Маяковского, 19/29",
    "manufacturing": "Ордена отчеканены на Государственном Монетном Дворе Санкт-Петербурга",
}

CONTACT_INFO = {
    "address": "191014, Санкт-Петербург, ул. Маяковского, 19/29",
    "addressee": "Палате Личности, Малыхин Юрию",
    "chairman": "Малыхин Юрий Иванович",
}

# ------------------------------------------------------------------
# Escaping
# ------------------------------------------------------------------
def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def esc_attr(s):
    return esc(s)

# ------------------------------------------------------------------
# HTML Generation
# ------------------------------------------------------------------
def generate_html():
    C = CURATED_GALLERY
    GALLERY_COUNT = len(C)
    ORG_CHAIRMAN = esc(ORG["chairman"])
    ORG_ADDRESS = esc(ORG["address"])
    ORG_ADDRESSEE = esc(CONTACT_INFO["addressee"])
    ORG_MANUFACTURING = esc(ORG["manufacturing"])
    ORG_ESTABLISHED = esc(ORG["established"])

    parts = []
    append = parts.append

    append("<!DOCTYPE html>")
    append("<html lang=\"ru-RU\">")
    append("<head>")
    append("<meta charset=\"UTF-8\">")
    append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\">")
    append("<meta name=\"theme-color\" content=\"#000000\">")
    append("<title>" + ORG["name"] + " \u2014 Ордена. Честь. Масштаб.</title>")
    append("<meta name=\"description\" content=\"Официальный сайт Международной палаты личности. Ордена, церемонии, Табель о рангах, кавалеры.\">")
    append("<meta name=\"author\" content=\"" + ORG_CHAIRMAN + "\">")
    append("<link rel=\"icon\" type=\"image/svg+xml\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='45' fill='none' stroke='white' stroke-width='4'/%3E%3C/svg%3e\">")
    append("<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">")
    append("<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>")
    append("<link href=\"https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap\" rel=\"stylesheet\">")
    append("<style>")

    css = """
:root {
  --black: #000000;
  --charcoal: #0A0A0A;
  --graphite: #141414;
  --graphite-2: #1E1E1E;
  --border: #262626;
  --border-bright: #3A3A3A;
  --white: #FFFFFF;
  --white-90: #E6E6E6;
  --white-70: #B3B3B3;
  --white-50: #808080;
  --white-30: #4D4D4D;
  --accent: #22c55e;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html {
  scroll-behavior: smooth;
  background: var(--black);
  overflow-x: hidden;
  max-width: 100vw;
}

html, body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  max-width: 100vw;
}

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--black);
  color: var(--white);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  font-variant-numeric: lining-nums tabular-nums;
  font-feature-settings: "lnum" 1, "tnum" 1;
}

body, h1, h2, h3, h4, h5, h6, span, div, p, td, th {
  font-variant-numeric: lining-nums tabular-nums;
  font-feature-settings: "lnum" 1, "tnum" 1;
}

.mono { font-family: 'JetBrains Mono', 'Courier New', monospace; }

/* ===== TYPOGRAPHY ===== */
.display-mega {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: -0.04em;
  text-transform: uppercase;
}
.display-xl {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  line-height: 0.92;
  letter-spacing: -0.03em;
  text-transform: uppercase;
}
.display-lg {
  font-family: 'Syne', sans-serif;
  font-weight: 600;
  line-height: 0.96;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}
.display-md {
  font-family: 'Syne', sans-serif;
  font-weight: 500;
  line-height: 1.05;
  letter-spacing: -0.01em;
}
.body-lg { font-size: clamp(1rem, 1.5vw, 1.25rem); line-height: 1.7; }
.body { font-size: 1rem; line-height: 1.65; }
.body-sm { font-size: 0.875rem; line-height: 1.6; }
.caption { font-size: 0.75rem; line-height: 1.5; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 500; }

/* ===== UTILITIES ===== */
.container { width: 100%; max-width: 1440px; margin: 0 auto; padding: 0 2rem; }
@media (max-width: 1023px) { .container { padding: 0 1rem; } }

.section { padding: 5rem 0; }
@media (max-width: 1023px) { .section { padding: 3rem 0; } }

.grid { display: grid; gap: 1rem; }
.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }
@media (max-width: 1024px) { .grid-4 { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 1023px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 640px) { .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; } }

.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.gap-1 { gap: 0.5rem; }
.gap-2 { gap: 1rem; }
.gap-3 { gap: 1.5rem; }
.gap-4 { gap: 2rem; }

.text-center { text-align: center; }
.text-left { text-align: left; }

.w-full { width: 100%; }

.relative { position: relative; }
.absolute { position: absolute; }
.fixed { position: fixed; }
.sticky { position: sticky; }
.inset-0 { inset: 0; }
.z-10 { z-index: 10; }
.z-20 { z-index: 20; }
.z-50 { z-index: 50; }
.z-1000 { z-index: 1000; }

.overflow-hidden { overflow: hidden; }

.border { border: 1px solid var(--border); }
.border-b { border-bottom: 1px solid var(--border); }

.bg-charcoal { background: var(--charcoal); }
.bg-graphite { background: var(--graphite); }

.p-4 { padding: 1.5rem; }
.p-6 { padding: 2rem; }
.px-4 { padding-left: 1.5rem; padding-right: 1.5rem; }

.mb-4 { margin-bottom: 1.5rem; }
.mb-6 { margin-bottom: 2rem; }
.mb-8 { margin-bottom: 3rem; }

.opacity-50 { opacity: 0.5; }

.text-white { color: var(--white); }
.text-accent { color: var(--accent); }
.text-white-50 { color: var(--white-50); }
.text-white-70 { color: var(--white-70); }
.text-white-30 { color: var(--white-30); }

/* ===== MOBILE: zero horizontal overflow (320-430px) ===== */
@media (max-width: 430px) {
  html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    width: 100% !important;
  }
  body { margin-left: 0 !important; padding-left: 0 !important; }
  h1, h2, h3, .display-mega, .display-lg, .display-xl {
    word-break: normal !important;
    overflow-wrap: break-word !important;
    hyphens: auto !important;
  }
  .display-mega { font-size: clamp(1.6rem, 10vw, 2.6rem) !important; line-height: 1.05; }
  .display-lg { font-size: clamp(1.2rem, 8vw, 1.8rem) !important; }
  .display-md { font-size: clamp(1rem, 7vw, 1.4rem) !important; }
}

/* ===== MARQUEE (seamless, always running) ===== */
.marquee {
  overflow: hidden;
  white-space: nowrap;
  display: flex;
  background: #ffffff;
  color: #000000;
  height: 38px;
  align-items: center;
  border-bottom: 1px solid #222;
  font-family: 'Syne', sans-serif;
  font-weight: 600;
  font-size: clamp(0.8rem, 1.2vw, 1rem);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}
.marquee-track {
  display: inline-flex;
  align-items: center;
  width: max-content;
  will-change: transform;
  animation: palataMarquee 28s linear infinite !important;
}
.marquee:hover .marquee-track { animation-play-state: paused; }
@keyframes palataMarquee {
  0% { transform: translate3d(0, 0, 0); }
  100% { transform: translate3d(-50%, 0, 0); }
}
.marquee__item { display: inline-flex; align-items: center; gap: 2.5rem; padding-right: 2.5rem; }
.marquee__dot { width: 5px; height: 5px; background: var(--black); border-radius: 50%; flex-shrink: 0; }

/* ===== DESKTOP LAYOUT: fixed left sidebar only ===== */
.desktop-layout {
  display: flex;
  min-height: 100vh;
}
.sidebar {
  position: fixed;
  top: 0; left: 0; bottom: 0;
  width: 300px;
  z-index: 40;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #0a0a0a;
  border-right: 1px solid #1f1f1f;
  padding: 28px 24px;
}
.main-content {
  margin-left: 300px;
  width: calc(100% - 300px);
  min-height: 100vh;
}

.sidebar__title {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.05em;
  color: var(--white);
  margin-bottom: 2.5rem;
}
.sidebar__nav {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}
.sidebar__link {
  color: var(--white-70);
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.05rem !important;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  text-decoration: none;
  transition: color 0.2s;
  display: block;
  padding: 14px 0;
  border-bottom: 1px solid #1a1a1a;
}
.sidebar__link:hover { color: var(--white); }
.sidebar__apply {
  background: var(--white);
  color: var(--black);
  border: 1px solid var(--white);
  padding: 16px 20px;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 0.95rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  text-decoration: none;
  text-align: center;
  border-radius: 0;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 24px;
}
.sidebar__order {
  margin-top: auto;
  padding-top: 2rem;
  border-top: 1px solid var(--border);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--white-50);
  line-height: 1.5;
}
.sidebar__order .sidebar__order-text {
  color: var(--white);
  display: block;
  margin-bottom: 0.5rem;
}

/* ===== DESKTOP: hide top header & mobile bars ===== */
@media (min-width: 1024px) {
  .header, .mobile-topbar, .mobile-dock, .mobile-menu-btn,
  .rank-story, .about-grid-mobile, .stat-mobile, .fact-card-mobile,
  .filter-mobile-wrap { display: none !important; }
  .desktop-layout { display: flex; }
  .main-content { margin-left: 300px; width: calc(100% - 300px); }
  .sidebar { display: flex !important; }
}

/* ===== DESKTOP: massive first screen centered vertically + type scale ===== */
@media (min-width: 1024px) {
  .hero {
    margin-left: 300px !important;
    width: calc(100% - 300px) !important;
    min-height: calc(100vh - 38px) !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    padding: 0 40px !important;
    box-sizing: border-box !important;
    max-width: none !important;
  }
  .hero__content {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    padding: 0 !important;
    max-width: none !important;
    width: 100% !important;
    margin: 0 auto !important;
  }
  .hero__badge,
  .hero__title,
  .hero__lead,
  .hero__cta {
    margin-left: auto !important;
    margin-right: auto !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
  }
  .hero__title .h1-text {
    font-size: clamp(4.2rem, 6vw, 7rem) !important;
    line-height: 0.96 !important;
    letter-spacing: -0.035em !important;
  }
  h2.display-lg { font-size: clamp(2.8rem, 4.2vw, 4.5rem) !important; line-height: 1.02 !important; }
  .body, .body-lg { font-size: 1.2rem !important; line-height: 1.65 !important; }
  .caption { font-size: 0.9rem !important; font-weight: 600 !important; }
  .card > div.caption { font-size: 0.9rem !important; }
  .card > div.body, .card > div.body-lg { font-size: 1.25rem !important; font-weight: 600 !important; }
  .hero__cta .btn { padding: 18px 36px !important; font-size: 1rem !important; font-weight: 700 !important; }
  .hero__lead {
    font-size: 1.35rem !important;
    line-height: 1.5 !important;
    color: #a3a3a3 !important;
    max-width: 720px !important;
    margin: 24px 0 36px 0 !important;
  }
  .hero__glow {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 30% 50%, rgba(34, 197, 94, 0.08), transparent 65%);
    pointer-events: none;
    z-index: 0;
  }
}

/* ===== MOBILE: hide sidebar, full-width content ===== */
@media (max-width: 1023px) {
  .sidebar { display: none !important; width: 0 !important; }
  .main-content { margin-left: 0 !important; width: 100% !important; max-width: 100vw !important; overflow-x: hidden !important; padding: 72px 16px 96px 16px !important; box-sizing: border-box !important; }
  .desktop-layout { display: block !important; }

  /* Marquee visible right under the top bar on mobile */
  .marquee { margin-top: 56px !important; }

  /* Hero: strict vertical centering, content starts under marquee/top bar */
  .hero {
    min-height: 100svh !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    text-align: center !important;
    padding: 24px 16px 40px 16px !important;
    box-sizing: border-box !important;
  }
  .hero__content { padding: 0 !important; max-width: 100% !important; text-align: center !important; align-items: center !important; width: 100% !important; }
  .hero__title .h1-text {
    font-size: clamp(1.5rem, 6.2vw, 2.4rem) !important;
    line-height: 1.04 !important;
    letter-spacing: -0.03em;
    word-break: normal !important;
    overflow-wrap: break-word !important;
    hyphens: auto !important;
  }
  .hero__lead {
    font-size: 1.05rem !important;
    color: #a3a3a3 !important;
    margin: 16px 0 24px 0 !important;
    max-width: 100% !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
    hyphens: auto !important;
  }
  .hero__cta .btn { width: 100% !important; justify-content: center !important; }
}

/* ===== MOBILE STICKY TOP BAR ===== */

/* ===== MOBILE STICKY TOP BAR ===== */
.mobile-topbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  height: 56px;
  z-index: 50;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 16px;
  background: rgba(10,10,10,0.9);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid #1f1f1f;
}
.mobile-topbar__title {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  color: var(--white);
}
.mobile-topbar__rank-btn {
  background: transparent;
  border: 1px solid var(--border-bright);
  color: var(--white);
  padding: 0.35rem 0.9rem;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
  font-size: 0.7rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  text-decoration: none;
  border-radius: 0;
  cursor: pointer;
  transition: all 0.2s;
}
.mobile-topbar__rank-btn:hover, .mobile-topbar__rank-btn:active {
  background: #22c55e;
  color: #000000;
  box-shadow: 0 0 25px rgba(34, 197, 94, 0.4);
  border-color: #22c55e;
}

/* ===== MOBILE BOTTOM DOCK BAR ===== */
.mobile-dock {
  position: fixed;
  bottom: 0; left: 0; right: 0;
  height: 64px;
  z-index: 50;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  padding: 8px 12px calc(8px + env(safe-area-inset-bottom));
  background: rgba(10,10,10,0.95);
  backdrop-filter: blur(16px);
  border-top: 1px solid #1f1f1f;
}
.mobile-dock__tab {
  display: flex; flex-direction: column; align-items: center; gap: 0.25rem;
  color: #e5e5e5 !important;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
  font-size: 0.78rem !important;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.35rem 0.5rem;
  border-radius: 0;
  transition: color 0.2s;
}
.mobile-dock__tab:hover, .mobile-dock__tab.active { color: var(--white); }
.mobile-dock__tab--accent {
  background: #22c55e;
  color: #000000;
  min-width: auto;
  padding: 0.5rem 1rem;
}
.mobile-dock__tab--accent:hover, .mobile-dock__tab--accent:active {
  background: #22c55e;
  color: #000000;
  box-shadow: 0 0 25px rgba(34, 197, 94, 0.4);
  border-color: #22c55e;
}

/* ===== HERO ===== */
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  position: relative;
  padding-top: 72px;
}
.hero__glow { position: absolute; inset: 0; background: radial-gradient(circle at 30% 50%, rgba(34, 197, 94, 0.08), transparent 65%); pointer-events: none; z-index: 0; }
.hero__content { position: relative; z-index: 1; text-align: left; max-width: 900px; padding: 2rem; }
.hero__badge { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--white-50); margin-bottom: 2rem; }
.hero__badge::before { content: ''; width: 8px; height: 8px; background: var(--accent); border-radius: 50%; animation: pulse 2s infinite; }
@keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
.hero__title { margin-bottom: 1.5rem; }
.hero__title .accent { color: var(--accent); }
.hero__cta { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 4rem; }

/* H1 sizes per spec */
.hero__title .h1-text {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: clamp(3rem, 5.2vw, 5.5rem);
  line-height: 1.02;
  letter-spacing: -0.03em;
}
@media (min-width: 1024px) {
  .hero__title .h1-text {
    font-size: clamp(4.2rem, 6vw, 7rem) !important;
    line-height: 0.96 !important;
    letter-spacing: -0.035em !important;
  }
}
@media (max-width: 768px) {
  .hero__title .h1-text {
    font-size: clamp(1.85rem, 7.2vw, 2.8rem) !important;
    line-height: 1.04 !important;
    letter-spacing: -0.03em;
  }
}

/* ===== BUTTONS ===== */
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 0.75rem; padding: 1rem 2rem; border-radius: 0; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 0.75rem; letter-spacing: 0.05em; text-transform: uppercase; text-decoration: none; transition: all 0.2s; border: 1px solid transparent; cursor: pointer; }
.btn--primary { background: var(--white); color: var(--black); border-color: var(--white); }
.btn--primary:hover { background: var(--white-90); }
.btn--ghost { background: transparent; color: var(--white); border-color: var(--border-bright); }
.btn--ghost:hover { border-color: var(--white); background: rgba(255,255,255,0.05); }
.btn--apply {
  background: var(--white);
  color: var(--black);
  border: 1px solid var(--white);
  transition: all 0.2s;
}
.btn--apply:hover, .btn--apply:active {
  background: #22c55e;
  color: #000000;
  box-shadow: 0 0 25px rgba(34, 197, 94, 0.4);
  border-color: #22c55e;
}

/* Mobile: hero buttons full width */
@media (max-width: 1023px) {
  .hero__cta { flex-direction: column; align-items: stretch; }
  .hero__cta .btn { width: 100%; justify-content: center; }
}

/* ===== CARDS ===== */
.card { background: var(--graphite); border: 1px solid var(--border); padding: 2rem; transition: border-color 0.3s, transform 0.3s; }
.card:hover { border-color: var(--white); transform: translateY(-4px); }

/* ===== STATS (large numbers) ===== */
.stat { text-align: center; }
.stat__num {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 800;
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  color: #ffffff;
  font-variant-numeric: lining-nums tabular-nums;
  font-feature-settings: "lnum" 1, "tnum" 1;
  line-height: 1;
}
.stat__label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--white-50);
  margin-top: 0.5rem;
}

/* ===== MOBILE ABOUT: 2x2 fact grid + 2x2 stats ===== */
@media (max-width: 1023px) {
  .about-grid-mobile { grid-template-columns: repeat(2, 1fr); gap: 10px; }
  .stat-mobile__num {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 800;
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    color: #22c55e;
    font-variant-numeric: lining-nums tabular-nums;
    font-feature-settings: "lnum" 1, "tnum" 1;
    line-height: 1;
  }
  .stat-mobile__label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--white-50);
  }
  .fact-card-mobile { background: var(--graphite); border: 1px solid var(--border); padding: 1rem 0.75rem; text-align: center; }
  .fact-card-mobile__caption { font-family: 'JetBrains Mono', monospace; font-size: 0.625rem; letter-spacing: 0.05em; text-transform: uppercase; color: var(--white-50); margin-bottom: 0.5rem; }
  .fact-card-mobile__value { font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: clamp(1rem, 5vw, 1.25rem); color: var(--white); word-break: break-word; overflow-wrap: break-word; }
}

/* ===== EPIGRAPH ===== */
.epigraph { text-align: center; padding: 3rem 0; font-family: 'Syne', sans-serif; font-weight: 500; font-size: clamp(1.1rem, 2vw, 1.4rem); color: var(--white-30); font-style: italic; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.epigraph__text { margin-bottom: 0.5rem; }
.epigraph__author { font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--white-50); }

/* ===== ABOUT ===== */
.about-dossier { max-width: 500px; }

/* ===== TABLE OF RANKS ===== */
.rank-card { background: var(--graphite); border: 1px solid var(--border); padding: 2.5rem; position: relative; overflow: hidden; }
.rank-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, var(--white), var(--white-50), var(--white)); background-size: 200% 100%; animation: shimmer 4s linear infinite; }
@keyframes shimmer { 0% { background-position: 0% 50%; } 100% { background-position: 200% 50%; } }
.rank-card__num { font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 1.25rem; color: var(--white-50); margin-bottom: 1rem; }
.rank-card__headline { font-family: 'Syne', sans-serif; font-weight: 600; font-size: clamp(1.1rem, 2vw, 1.5rem); line-height: 1.15; margin-bottom: 1rem; }
.rank-card__body { color: var(--white-70); line-height: 1.8; }

/* MOBILE ranks: fixed-height swipeable story cards */
@media (max-width: 1023px) {
  .rank-story { height: 340px; display: flex; flex-direction: column; }
  .rank-card { padding: 1.5rem; height: 100%; display: flex; flex-direction: column; justify-content: center; }
  .rank-card__headline { font-size: clamp(1.1rem, 5vw, 1.35rem); }
  .rank-card__body { font-size: 0.9rem; line-height: 1.6; margin-bottom: 0; }
  .rank-card__num { font-size: 1rem; margin-bottom: 0.75rem; }
}
.rank-swipe-hint {
  font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: var(--white-30);
  text-transform: uppercase; letter-spacing: 0.08em; margin-top: 0.75rem;
}

/* ===== GALLERY CATALOG ===== */
.gallery-header { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem; align-items: center; }
.gallery-counter { font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--white-50); }

.gallery { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }
@media (max-width: 1024px) { .gallery { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 1023px) { .gallery { grid-template-columns: repeat(2, 1fr); gap: 10px; } }

.gallery__item { position: relative; aspect-ratio: 4/5; background: var(--graphite-2); border: 1px solid var(--border); overflow: hidden; cursor: pointer; transition: border-color 0.2s; }
.gallery__item:hover { border-color: var(--white); }
.gallery__img { width: 100%; height: 100%; object-fit: cover; display: block; }
.gallery__index { position: absolute; top: 0.75rem; left: 0.75rem; background: rgba(0,0,0,0.8); border: 1px solid var(--border-bright); padding: 0.25rem 0.6rem; font-family: 'JetBrains Mono', monospace; font-size: 0.625rem; font-weight: 700; color: var(--white); z-index: 2; }
.gallery__cat { position: absolute; top: 0.75rem; right: 0.75rem; background: rgba(0,0,0,0.8); border: 1px solid var(--border-bright); padding: 0.25rem 0.6rem; font-size: 0.625rem; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: var(--white-70); z-index: 2; }
.gallery__caption { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(transparent, rgba(0,0,0,0.9)); padding: 1rem; font-family: 'Inter', sans-serif; font-size: 0.8125rem; color: var(--white); z-index: 2; }

/* MOBILE filter chips: single horizontal row, swipeable, no scrollbar */
.filter-mobile-wrap {
  display: flex; gap: 0.5rem; margin-bottom: 1.5rem; overflow-x: auto; white-space: nowrap;
  scrollbar-width: none; -webkit-overflow-scrolling: touch;
}
.filter-mobile-wrap::-webkit-scrollbar { display: none; }
.filter {
  display: inline-flex; flex-wrap: nowrap; gap: 0.5rem;
}
.filter__btn { background: transparent; border: 1px solid var(--border); color: var(--white-50); padding: 0.4rem 1rem; font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; cursor: pointer; transition: all 0.2s; white-space: nowrap; }
.filter__btn:hover { border-color: var(--white-50); color: var(--white); }
.filter__btn.active { background: var(--white); color: var(--black); border-color: var(--white); }

.show-more { text-align: center; margin-top: 2rem; }

/* ===== FOOTER ===== */
.footer { border-top: 1px solid var(--border); background: var(--charcoal); padding: 3rem 2rem; }
.footer__grid { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 2rem; max-width: 1440px; margin: 0 auto; }
.footer__nav { display: flex; flex-wrap: wrap; gap: 2rem; }
.footer__link { color: var(--white-50); font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 500; letter-spacing: 0.04em; text-decoration: none; transition: color 0.2s; }
.footer__link:hover { color: var(--white); }
.footer__copy { font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: var(--white-30); }

/* ===== LIGHTBOX (dossier window) ===== */
.lightbox { position: fixed; inset: 0; z-index: 10000; background: rgba(0,0,0,0.98); backdrop-filter: blur(10px); display: none; align-items: center; justify-content: center; padding: 2rem; opacity: 0; transition: opacity 0.3s; }
.lightbox.open { display: flex; opacity: 1; }
@media (max-width: 1023px) {
  .lightbox { padding: 0; align-items: flex-start; justify-content: center; max-height: 100dvh; overflow-y: auto; }
  .lightbox__dossier { width: 100vw; max-height: 100dvh; overflow-y: auto; max-width: none; border: none; border-radius: 0; margin: 0; }
}
.lightbox__dossier__body {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  width: 100% !important;
  height: 100% !important;
  box-sizing: border-box !important;
  margin: auto !important;
  padding: 1.5rem !important;
  overflow-y: visible !important;
}
.lightbox__img {
  max-width: 100% !important;
  max-height: 62vh !important;
  object-fit: contain !important;
  display: block !important;
  margin: 0 auto !important;
  border-radius: 4px !important;
  border: none !important;
}
.lightbox__caption {
  text-align: center !important;
  margin-top: 10px !important;
  width: 100% !important;
}
.lightbox__dossier__footer {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  max-width: 440px !important;
  margin: 14px auto 0 auto !important;
}
@media (max-width: 1023px) {
  .lightbox__dossier__footer {
    position: fixed; bottom: 0; left: 0; right: 0; z-index: 60;
    padding: 0.75rem 1rem env(safe-area-inset-bottom) 1rem;
    background: var(--charcoal);
    border-top: 1px solid var(--border);
    display: flex; flex-direction: column; gap: 0.75rem; align-items: stretch;
  }
  .lightbox__nav-panel {
    display: flex; align-items: center; justify-content: space-between; gap: 8px; width: 100%; margin-top: 16px;
  }
  .lightbox__nav-btn {
    padding: 12px 16px; font-size: 0.9rem; background: #171717; border: 1px solid #262626; color: #ffffff; border-radius: 6px; flex: none;
  }
  .lightbox__nav-btn:hover { border-color: var(--white); background: rgba(255,255,255,0.05); }
  .lightbox__nav-btn--prev { text-align: left; }
  .lightbox__nav-btn--next { text-align: right; }
  .lightbox__counter {
    font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: var(--white); letter-spacing: 0.04em;
  }
}
.lightbox__nav-btn { background: transparent; border: 1px solid var(--border); color: var(--white); padding: 0.5rem 1rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; cursor: pointer; transition: all 0.2s; flex: 1; text-align: center; }
@media (max-width: 1023px) {
  .lightbox__nav-btn { font-size: 0.85rem; padding: 0.75rem 1rem; border-radius: 0; }
}
.lightbox__nav-btn:hover { border-color: var(--white); background: rgba(255,255,255,0.05); }
.lightbox__nav-btn--prev { text-align: left; }
.lightbox__nav-btn--next { text-align: right; }
.lightbox__counter { font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--white-30); }

/* ===== REVEAL ===== */
.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.8s cubic-bezier(0.16,1,0.3,1), transform 0.8s cubic-bezier(0.16,1,0.3,1); }
.reveal.visible { opacity: 1; transform: translateY(0); }
.stagger-1 { transition-delay: 60ms; }
.stagger-2 { transition-delay: 120ms; }
.stagger-3 { transition-delay: 180ms; }
.stagger-4 { transition-delay: 240ms; }

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--black); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 0; }

/* ===== SELECTION ===== */
::selection { background: var(--accent); color: var(--black); }

/* ===== ENTRANCE ANIMATION ===== */
@keyframes heroReveal {
  0% { opacity: 0; transform: translateY(28px) scale(0.985); filter: blur(6px); }
  100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
}
.hero__badge.reveal { animation: heroReveal 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.08s both !important; }
.hero-line { display: block; }
.hero-line.reveal.stagger-1 { animation: heroReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.18s both !important; }
.hero-line.reveal.stagger-2 { animation: heroReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.28s both !important; }
.hero-line.reveal.stagger-3 { animation: heroReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.38s both !important; }
.hero__lead.reveal { animation: heroReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.5s both !important; }
.hero__cta.reveal { animation: heroReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.62s both !important; }

html, body {
.hero__lead.reveal { animation: heroReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.5s both !important; }
.hero__cta.reveal { animation: heroReveal 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.62s both !important; }
"""
    append(css)
    append("</style>")
    append("</head>")
    append("<body>")

    # ---- MARQUEE (aphorisms woven in) ----
    marquee_items = list(APHORISMS) + [
        "МЕЖДУНАРОДНАЯ ПАЛАТА ЛИЧНОСТИ",
        "ОРДЕНА. ЧЕСТЬ. МАСШТАБ.",
        "ГОСУДАРСТВЕННЫЙ МОНЕТНЫЙ ДВОР СПБ",
        "ТАБЕЛЬ О РАНГАХ · 1722",
        "МЕРИТОКРАЦИЯ БЕЗ ПРИВОРОТОВ",
    ]
    append("""<!-- MARQUEE TICKER -->
<div class="marquee" aria-hidden="true">
  <div class="marquee-track">""")
    for item in marquee_items:
        append('    <span class="marquee__item"><span class="marquee__dot"></span><span>' + esc(item) + '</span><span class="marquee__dot"></span>')
    append('    <span class="marquee__item"><span class="marquee__dot"></span><span>' + esc(marquee_items[0]) + '</span><span class="marquee__dot"></span>')
    append("""  </div>
</div>""")

    # ---- MOBILE STICKY TOP BAR ----
    append("""<div class="mobile-topbar">
  <div class="mobile-topbar__title">ПАЛАТА ЛИЧНОСТИ</div>
  <button class="mobile-topbar__rank-btn" id="mobile-topbar-rank">НА РАНГ</button>
</div>""")

    # ---- DESKTOP LAYOUT (sidebar + main) ----
    append("""<div class="desktop-layout">
  <aside class="sidebar">
    <div class="sidebar__title">ПАЛАТА ЛИЧНОСТИ • 1999</div>
    <nav class="sidebar__nav">
      <a href="#about" class="sidebar__link">О Палате</a>
      <a href="#history" class="sidebar__link">Табель о рангах</a>
      <a href="#gallery" class="sidebar__link">Регалии и архив</a>
      <a href="#contacts" class="sidebar__link">Контакты</a>
    </nav>
    <a href="#contacts" class="sidebar__apply btn--apply">ПОДАТЬ ЗАЯВКУ НА РАНГ</a>
    <div class="sidebar__order">
      <span class="sidebar__order-text">Орден Палаты</span>
      191014, СПб, ул. Маяковского, 19/29
    </div>
  </aside>

  <div class="main-content">""")

    # ---- HERO ----
    append("""<section class="hero" id="top" aria-labelledby="hero-title">
  <div class="hero__content">
    <div class="hero__badge reveal">
      <span>ОФИЦИАЛЬНЫЙ РЕСУРС • С 1999</span>
    </div>
    <h1 class="display-mega reveal stagger-1" id="hero-title">
      <span class="h1-text">
        <span class="hero-line reveal stagger-1">МЕЖДУНАРОДНАЯ</span>
        <span class="hero-line reveal stagger-2">ПАЛАТА</span>
        <span class="hero-line reveal stagger-3"><span class="accent">ЛИЧНОСТИ</span></span>
      </span>
    </h1>
    <p class="hero__lead reveal stagger-2">Учреждена в Санкт-Петербурге 18 июня 1999 года. Ордена и знаки отличия чеканятся на Государственном Монетном Дворе.</p>
    <div class="hero__cta reveal stagger-3">
      <a href="#gallery" class="btn btn--primary">ОТКРЫТЬ ДОСЬЕ НАГРАД</a>
      <a href="#about" class="btn btn--ghost">О ПАЛАТЕ</a>
    </div>
  </div>
</section>""")

    # ---- Epigraph divider ----
    append("""<div class="epigraph reveal">
  <div class="epigraph__text">«""" + esc(APHORISMS[0]) + """»</div>
  <div class="epigraph__author">Цицерон</div>
</div>""")

    # ---- ABOUT ----
    append("""<section class="section" id="about" aria-labelledby="about-title">
  <div class="container">
    <div class="grid grid-2 gap-4" style="align-items: start;">
      <div class="reveal">
        <span class="caption text-accent">01 / ДОСЬЕ</span>
        <h2 class="display-lg mb-4" id="about-title">О ПАЛАТЕ</h2>
        <p class="body-lg text-white-70 mb-6" style="max-width: 500px;">
          Международная общественная организация, объединяющая кавалеров орденов. Ведём орденскую хронику: каждая награда — документ, каждая церемония — факт.
        </p>
""")

    # Mobile: 2x2 fact grid + stats stacked
    append("""        <div class="about-grid-mobile">
          <div class="fact-card-mobile reveal stagger-1">
            <div class="fact-card-mobile__caption">ОСНОВАНА</div>
            <div class="fact-card-mobile__value">""" + ORG_ESTABLISHED + """</div>
          </div>
          <div class="fact-card-mobile reveal stagger-2">
            <div class="fact-card-mobile__caption">ПРЕДСЕДАТЕЛЬ</div>
            <div class="fact-card-mobile__value">""" + ORG_CHAIRMAN + """</div>
          </div>
          <div class="fact-card-mobile reveal stagger-3">
            <div class="fact-card-mobile__caption">ИЗГОТОВЛЕНИЕ</div>
            <div class="fact-card-mobile__value">""" + ORG_MANUFACTURING + """</div>
          </div>
          <div class="fact-card-mobile reveal stagger-4">
            <div class="fact-card-mobile__caption">АДРЕС</div>
            <div class="fact-card-mobile__value">""" + ORG_ADDRESS + """</div>
          </div>
        </div>

        <div class="grid grid-2 gap-3 stat-mobile reveal" style="margin-top: 1.5rem;">
          <article class="stat stagger-1">
            <div class="stat-mobile__num">27+</div>
            <div class="stat-mobile__label">ЛЕТ РАБОТЫ</div>
          </article>
          <article class="stat stagger-2">
            <div class="stat-mobile__num">100+</div>
            <div class="stat-mobile__label">КАВАЛЕРОВ</div>
          </article>
          <article class="stat stagger-3">
            <div class="stat-mobile__num">1999</div>
            <div class="stat-mobile__label">ГОД ОСНОВАНИЯ</div>
          </article>
        </div>
""")

    append("""      </div>
      <div class="grid grid-2 gap-2">
        <div class="card reveal stagger-1">
          <div class="caption text-accent">ОСНОВАНА</div>
          <div class="body text-white-70" style="margin-top: 0.5rem;">""" + ORG_ESTABLISHED + """</div>
        </div>
        <div class="card reveal stagger-2">
          <div class="caption text-accent">ПРЕДСЕДАТЕЛЬ</div>
          <div class="body text-white-70" style="margin-top: 0.5rem;">""" + ORG_CHAIRMAN + """</div>
        </div>
        <div class="card reveal stagger-3">
          <div class="caption text-accent">ИЗГОТОВЛЕНИЕ</div>
          <div class="body text-white-70" style="margin-top: 0.5rem;">""" + ORG_MANUFACTURING + """</div>
        </div>
        <div class="card reveal stagger-4">
          <div class="caption text-accent">АДРЕС</div>
          <div class="body text-white-70" style="margin-top: 0.5rem;">""" + ORG_ADDRESS + """</div>
        </div>
      </div>
      <div class="grid grid-2 gap-2">
        <article class="stat reveal stagger-1">
          <div class="stat__num">27+</div>
          <div class="stat__label">ЛЕТ РАБОТЫ</div>
        </article>
        <article class="stat reveal stagger-2">
          <div class="stat__num">100+</div>
          <div class="stat__label">КАВАЛЕРОВ</div>
        </article>
        <article class="stat reveal stagger-3">
          <div class="stat__num">1999</div>
          <div class="stat__label">ГОД ОСНОВАНИЯ</div>
        </article>
      </div>
    </div>
  </div>
</section>""")

    # ---- Epigraph divider ----
    append("""<div class="epigraph reveal">
  <div class="epigraph__text">«""" + esc(APHORISMS[1]) + """»</div>
  <div class="epigraph__author">Платон</div>
</div>""")

    # ---- TABLE OF RANKS ----
    append("""<section class="section" id="history" aria-labelledby="history-title">
  <div class="container">
    <div class="reveal mb-6" style="max-width: 600px;">
      <span class="caption text-accent">02 / ТАБЕЛЬ О РАНГАХ</span>
      <h2 class="display-lg mb-2" id="history-title">ТАБЕЛЬ О РАНГАХ: СИСТЕМА ПЕТРА I</h2>
      <p class="body text-white-50 mb-6">Почему система Петра I остаётся эталоном прозрачной карьерной лестницы.</p>
    </div>
    <div class="grid grid-2 gap-3 rank-story" role="list">""")

    for i, section in enumerate(TABLE_OF_RANKS):
        stagger = (i % 4) + 1
        append("""      <article class="rank-card reveal stagger-""" + str(stagger) + """\" role="listitem" style="transition-delay: """ + str(i * 100) + """ms;">
        <div class="rank-card__num">""" + esc(section["num"]) + """</div>
        <h3 class="rank-card__headline">""" + esc(section["headline"]) + """</h3>
        <p class="rank-card__body">""" + esc(section["body"]) + """</p>
      </article>""")

    append("""    </div>
    <div class="rank-swipe-hint reveal">Свайпните карточку влево / вправо • тап по краю</div>
  </div>
</section>""")

    # ---- Epigraph divider ----
    append("""<div class="epigraph reveal">
  <div class="epigraph__text">«""" + esc(APHORISMS[2]) + """»</div>
  <div class="epigraph__author">Бизантийская мудрость</div>
</div>""")

    # ---- GALLERY (first 12 visible, rest behind "Раскрыть полный архив") ----
    VISIBLE_COUNT = min(12, len(C))
    append("""<section class="section" id="gallery" aria-labelledby="gallery-title">
  <div class="container">
    <div class="gallery-header reveal">
      <div>
        <span class="caption text-accent">03 / РЕГАЛИИ И АРХИВ</span>
        <h2 class="display-lg mb-1" id="gallery-title">НАГРАДЫ И АРТЕФАКТЫ ПАЛАТЫ</h2>
        <p class="body text-white-50">Курируемая подборка. Только регалии, знаки отличия и моменты, когда честь становилась видимой.</p>
      </div>
      <div class="gallery-counter">ПОКАЗАНО <span id="visible-count">""" + str(VISIBLE_COUNT) + """</span> ИЗ """ + str(GALLERY_COUNT) + """</div>
    </div>
    <div class="filter-mobile-wrap reveal" role="tablist" aria-label="Фильтр по категориям" style="transition-delay: 100ms;">
      <div class="filter">
        <button class="filter__btn active" data-filter="Все" role="tab" aria-selected="true" aria-controls="gallery-grid">Все</button>
        <button class="filter__btn" data-filter="Ордена и знаки" role="tab" aria-selected="false" aria-controls="gallery-grid">Ордена и знаки</button>
        <button class="filter__btn" data-filter="Церемонии" role="tab" aria-selected="false" aria-controls="gallery-grid">Церемонии</button>
        <button class="filter__btn" data-filter="История" role="tab" aria-selected="false" aria-controls="gallery-grid">История</button>
      </div>
    </div>
    <div class="gallery" id="gallery-grid" role="list" aria-label="Галерея наград">""")

    for i, item in enumerate(C[:VISIBLE_COUNT]):
        full_url = BASE_URL + item['file']
        cat_map = {
            "Портреты": "Ордена и знаки",
            "Награды": "Ордена и знаки",
            "Церемонии": "Церемонии",
            "История": "История",
            "Артефакты": "Артефакты",
            "Документы": "Документы",
            "Международное": "Ордена и знаки",
        }
        display_cat = cat_map.get(item["category"], "Ордена и знаки")
        append("      <article class=\"gallery__item reveal\" data-category=\"" + esc_attr(display_cat) + "\" role=\"listitem\" tabindex=\"0\" onclick=\"openLightbox(" + str(i) + ")\" onkeydown=\"if(event.key==='Enter'||event.key===' '){event.preventDefault();openLightbox(" + str(i) + ")}\">")
        append('        <img class="gallery__img" src="' + esc_attr(full_url) + '" alt="' + esc_attr(item['alt']) + '" loading="lazy">')
        append('        <span class="gallery__index">АРТЕФАКТ №' + str(i + 1) + '</span>')
        append('        <span class="gallery__cat">' + esc_attr(display_cat) + '</span>')
        append('        <span class="gallery__caption">' + esc_attr(item['caption']) + '</span>')
        append("      </article>")

    append("""    </div>
    <div class="show-more reveal mt-8">
      <button class="btn btn--ghost" id="show-more-btn">Раскрыть полный архив Палаты</button>
    </div>
  </div>
</section>""")

    # ---- CONTACTS ----
    append("""<section class="section" id="contacts" aria-labelledby="contacts-title">
  <div class="container">
    <div class="grid grid-2 gap-4">
      <div class="reveal">
        <span class="caption text-accent">04 / СВЯЗЬ</span>
        <h2 class="display-lg mb-6" id="contacts-title">СВЯЖИТЕСЬ С ПАЛАТОЙ</h2>
        <p class="body-lg text-white-70 mb-8">Пишите, если хотите предложить кандидата на награду или узнать о партнёрстве.</p>
        <div class="space-y-4">
          <div class="card">
            <div class="flex gap-3">
              <div style="width: 48px; height: 48px; background: var(--charcoal); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              </div>
              <div>
                <div class="caption text-white-50">АДРЕС</div>
                <address class="body text-white-70" style="font-style: normal; margin-top: 0.25rem;">""" + ORG_ADDRESS + """<br>АДРЕСАТ: """ + ORG_ADDRESSEE + """</address>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="flex gap-3">
              <div style="width: 48px; height: 48px; background: var(--charcoal); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/></svg>
              </div>
              <div>
                <div class="caption text-white-50">ПРЕДСЕДАТЕЛЬ</div>
                <div class="body text-white-70" style="margin-top: 0.25rem;">""" + ORG_CHAIRMAN + """</div>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="flex gap-3">
              <div style="width: 48px; height: 48px; background: var(--charcoal); border: 1px solid var(--border); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              </div>
              <div>
                <div class="caption text-accent">ПРЕДЛОЖИТЬ КАНДИДАТА</div>
                <div class="body text-white-70" style="margin-top: 0.25rem;">Напишите на официальную почту Палаты с пометкой «Кандидат». Рассмотрим за 14 дней.</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="reveal" style="transition-delay: 200ms;">
        <div class="card" style="height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 class="display-md mb-4">ХОЧЕТЕ СТАТЬ КАВАЛЕРОМ?</h3>
            <p class="body-lg text-white-70 mb-8">Нет анкет, нет взяток, нет связей. Есть только дела, которые говорят сами за себя. Если вы (или кто-то, кого вы знаете) сделали подвиг — мы его зафиксируем.</p>
            <div class="flex flex-col gap-3 mb-8">
              <button class="btn btn--primary btn--apply" onclick="window.open('mailto:palata@personalitet.org?subject=Кандидат%20на%20награду','_blank')">ПОДАТЬ ЗАЯВКУ НА РАНГ</button>
              <button class="btn btn--ghost" onclick="window.open('https://t.me/palata_lichnosti','_blank')">НАПИСАТЬ В TELEGRAM</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>""")

    # ---- FOOTER ----
    append("""<footer class="footer" role="contentinfo">
  <div class="footer__grid">
    <nav class="footer__nav" aria-label="Навигация по подвалу">
      <a href="#about" class="footer__link">О Палате</a>
      <a href="#history" class="footer__link">Табель о рангах</a>
      <a href="#gallery" class="footer__link">Регалии и архив</a>
      <a href="#contacts" class="footer__link">Контакты</a>
    </nav>
    <div class="footer__copy">«МЕЖДУНАРОДНАЯ ПАЛАТА ЛИЧНОСТИ» · ОФИЦИАЛЬНЫЙ РЕСУРС</div>
  </div>
</footer>""")

    # ---- MOBILE BOTTOM DOCK ----
    append("""<nav class="mobile-dock" aria-label="Мобильная навигация">
  <a href="#about" class="mobile-dock__tab" id="dock-dossier">О Палате</a>
  <a href="#history" class="mobile-dock__tab" id="dock-ranks">Ранги</a>
  <a href="#gallery" class="mobile-dock__tab" id="dock-regalia">Регалии</a>
  <a href="#contacts" class="mobile-dock__tab mobile-dock__tab--accent" id="dock-rank">Заявка</a>
</nav>""")

    # ---- LIGHTBOX ----
    append("""<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Просмотр досье артефакта">
  <div class="lightbox__dossier">
    <div class="lightbox__dossier__header">
      <div class="lightbox__dossier__title" id="lightbox-title">ДОСЬЕ АРТЕФАКТА</div>
      <button class="lightbox__dossier__close" id="lightbox-close">Закрыть [Esc]</button>
    </div>
    <div class="lightbox__dossier__body">
      <span class="lightbox__cat" id="lightbox-cat"></span>
      <img class="lightbox__img" id="lightbox-img" alt="" src="" loading="lazy">
      <p class="lightbox__caption" id="lightbox-caption"></p>
    </div>
    <div class="lightbox__dossier__footer">
      <div class="lightbox__nav-panel">
        <button class="lightbox__nav-btn lightbox__nav-btn--prev" id="lightbox-prev">← Назад</button>
        <span class="lightbox__counter" id="lightbox-counter">1 / 1</span>
        <button class="lightbox__nav-btn lightbox__nav-btn--next" id="lightbox-next">Далее →</button>
      </div>
      <button class="lightbox__dossier__close" id="lightbox-close-mobile">Закрыть</button>
    </div>
  </div>
</div>""")

    # ---- JAVASCRIPT ----
    append("""<script>
const galleryData = [""")

    for i, item in enumerate(C):
        full_url = BASE_URL + item['file']
        append("""  {"file": \"""" + esc_attr(item['file']) + """\", "alt": \"""" + esc_attr(item['alt']) + """\", "caption": \"""" + esc_attr(item['caption']) + """\", "full_url": \"""" + esc_attr(full_url) + """\", "category": \"""" + esc_attr(item['category']) + """\"},""")

    append("""];
const VISIBLE_COUNT = """ + str(VISIBLE_COUNT) + """;
const BASE_URL = \"""" + BASE_URL + """\";

// Lightbox
let currentIndex = 0;
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.getElementById('lightbox-caption');
const lightboxCat = document.getElementById('lightbox-cat');
const lightboxCounter = document.getElementById('lightbox-counter');
const lightboxTitle = document.getElementById('lightbox-title');
const lightboxClose = document.getElementById('lightbox-close');
const lightboxCloseMobile = document.getElementById('lightbox-close-mobile');
const lightboxPrev = document.getElementById('lightbox-prev');
const lightboxNext = document.getElementById('lightbox-next');

function openLightbox(index) {
  currentIndex = index;
  updateLightbox();
  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
  lightboxClose.focus();
}
function closeLightbox() {
  lightbox.classList.remove('open');
  document.body.style.overflow = '';
}
function updateLightbox() {
  const item = galleryData[currentIndex];
  lightboxImg.src = item.full_url;
  lightboxImg.alt = item.alt;
  lightboxCaption.textContent = item.caption;
  lightboxCat.textContent = item.category.toUpperCase();
  lightboxTitle.textContent = 'АРТЕФАКТ №' + (currentIndex + 1);
  lightboxCounter.textContent = (currentIndex + 1) + ' / ' + galleryData.length;
}
function prevImage() { currentIndex = (currentIndex - 1 + galleryData.length) % galleryData.length; updateLightbox(); }
function nextImage() { currentIndex = (currentIndex + 1) % galleryData.length; updateLightbox(); }

lightboxClose.addEventListener('click', closeLightbox);
lightboxCloseMobile.addEventListener('click', closeLightbox);
lightboxPrev.addEventListener('click', prevImage);
lightboxNext.addEventListener('click', nextImage);
lightbox.addEventListener('click', (e) => { if (e.target === lightbox) closeLightbox(); });
document.addEventListener('keydown', (e) => {
  if (!lightbox.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') prevImage();
  if (e.key === 'ArrowRight') nextImage();
});

// Lightbox touch swipe
let lbTouchStartX = 0;
let lbTouchEndX = 0;
lightbox.addEventListener('touchstart', (e) => { lbTouchStartX = e.changedTouches[0].screenX; }, { passive: true });
lightbox.addEventListener('touchend', (e) => {
  lbTouchEndX = e.changedTouches[0].screenX;
  const diff = lbTouchStartX - lbTouchEndX;
  if (Math.abs(diff) > 40) { diff > 0 ? nextImage() : prevImage(); }
}, { passive: true });

// Category filter
const filterButtons = document.querySelectorAll('.filter__btn');
const galleryItems = document.querySelectorAll('[data-category]');
const visibleCount = document.getElementById('visible-count');
let allVisible = false;

function updateVisibleCount() {
  let count = 0;
  galleryItems.forEach(item => { if (item.style.display !== 'none') count++; });
  if (visibleCount) visibleCount.textContent = count;
}

filterButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;
    filterButtons.forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');
    galleryItems.forEach((item) => {
      const cat = item.dataset.category;
      if (filter === 'Все' || cat === filter) {
        item.style.display = 'block';
        item.style.animation = 'none';
        item.style.opacity = '1';
        item.style.transform = 'translateY(0)';
      } else {
        item.style.display = 'none';
      }
    });
    setTimeout(updateVisibleCount, 50);
  });
});

// Show more: reveal all gallery items
const showMoreBtn = document.getElementById('show-more-btn');
if (showMoreBtn) {
  showMoreBtn.addEventListener('click', () => {
    galleryItems.forEach(item => { item.style.display = 'block'; });
    allVisible = true;
    setTimeout(updateVisibleCount, 50);
    showMoreBtn.style.display = 'none';
  });
}
setTimeout(updateVisibleCount, 100);

// Smooth scroll anchors
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href');
    if (targetId === '#') return;
    const target = document.querySelector(targetId);
    if (target) {
      e.preventDefault();
      const targetPosition = target.getBoundingClientRect().top + window.scrollY;
      window.scrollTo({ top: targetPosition, behavior: 'smooth' });
    }
  });
});

// Mobile dock tab activation on scroll
const dockTabs = document.querySelectorAll('.mobile-dock__tab');
const sections = ['#about', '#history', '#gallery', '#contacts'];
function setActiveDock() {
  let current = sections[0];
  sections.forEach(sec => {
    const el = document.querySelector(sec);
    if (el && window.scrollY >= el.offsetTop - 100) current = sec;
  });
  dockTabs.forEach(tab => {
    tab.classList.remove('active');
    if (tab.getAttribute('href') === current) tab.classList.add('active');
  });
}
window.addEventListener('scroll', setActiveDock, { passive: true });
setActiveDock();

// TABLE OF RANKS mobile swipe (stories feel)
const rankCards = document.querySelectorAll('.rank-card');
let currentRank = 0;
const rankWrap = document.querySelector('.rank-story');
function showRank(index) {
  rankCards.forEach((c, i) => { c.style.display = (i === index) ? 'block' : 'none'; });
}
if (rankWrap && rankCards.length) {
  showRank(0);
  let touchStartX = 0;
  let touchEndX = 0;
  rankWrap.addEventListener('touchstart', (e) => { touchStartX = e.changedTouches[0].screenX; }, { passive: true });
  rankWrap.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 40) {
      currentRank = diff > 0 ? (currentRank + 1) % rankCards.length : (currentRank - 1 + rankCards.length) % rankCards.length;
      showRank(currentRank);
    }
  }, { passive: true });
  rankWrap.addEventListener('click', (e) => {
    const rect = rankWrap.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    if (clickX < rect.width / 2) {
      currentRank = (currentRank - 1 + rankCards.length) % rankCards.length;
    } else {
      currentRank = (currentRank + 1) % rankCards.length;
    }
    showRank(currentRank);
  });
}

// IntersectionObserver reveal
const revealElements = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
revealElements.forEach(el => revealObserver.observe(el));

console.log('МЕЖДУНАРОДНАЯ ПАЛАТА ЛИЧНОСТЬ — сайт инициализирован с ' + galleryData.length + ' артефактами');
</script>
</body>
</html>""")

    return "\n".join(parts)


if __name__ == "__main__":
    output_path = ROOT / "index.html"
    html_content = generate_html()
    output_path.write_text(html_content, encoding="utf-8")
    print(f"Generated: {output_path}")
    print(f"Size: {len(html_content):,} characters")
    print(f"Curated images: {len(CURATED_GALLERY)}")

    # Verification
    checks = [
        ("Konstantin", "Константин" in html_content),
        ("YarSite", "ЯрСайт" in html_content),
        ("Unprocessed braces", "{esc" in html_content or "{ORG" in html_content or "{GALLERY" in html_content),
        ("Stat 27+", "27+ ЛЕТ РАБОТЫ" in html_content),
        ("Old 10+ years", "10+ ЛЕТ РАБОТЫ" in html_content),
        ("Header apply button", "ПОДАТЬ ЗАЯВКУ НА РАНГ" in html_content),
        ("Nav items", "Регалии и архив" in html_content),
        ("Lining nums", "lining-nums" in html_content),
        ("Tabular nums", "tabular-nums" in html_content),
        ("Header nav", "Табель о рангах" in html_content),
        ("Mobile topbar", "ПАЛАТА ЛИЧНОСТИ" in html_content),
        ("Mobile topbar rank", "НА РАНГ" in html_content),
        ("Mobile dock", "mobile-dock" in html_content),
        ("Dock tabs", "О Палате" in html_content and "Ранги" in html_content and "Регалии" in html_content and "Заявка" in html_content),
        ("SVH hero", "100svh" in html_content),
        ("Grid 2x2", "repeat(2, 1fr)" in html_content),
        ("Touch swipe", "touchstart" in html_content and "touchend" in html_content),
        ("Lightbox fullscreen", "100dvh" in html_content),
        ("Desktop guard", "@media (min-width: 1024px)" in html_content),
        ("Mobile guard", "@media (max-width: 1023px)" in html_content),
        ("Zero overflow", "overflow-x: hidden" in html_content),
        ("Safe area", "env(safe-area-inset-bottom)" in html_content),
        ("Sidebar width 280", "width: 280px;" in html_content),
        ("Main margin 280", "margin-left: 280px;" in html_content),
        ("H1 mobile clamp", "clamp(1.5rem, 6.2vw, 2.4rem)" in html_content),
        ("H1 desktop clamp", "clamp(4.2rem, 6vw, 7rem)" in html_content),
        ("Neon green apply", "#22c55e" in html_content),
    ]

    print("\n=== VERIFICATION ===")
    all_pass = True
    for name, found in checks:
        status = "FAIL" if found else "OK"
        if name in ("Konstantin", "YarSite", "Unprocessed braces", "Old 10+ years"):
            status = "FAIL" if found else "OK"
            if found:
                all_pass = False
        else:
            status = "OK" if found else "FAIL"
            if not found:
                all_pass = False
        print(f"  {status}: {name}")
    print(f"\nOverall: {'PASS' if all_pass else 'FAIL'}")
