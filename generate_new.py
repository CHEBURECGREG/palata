#!/usr/bin/env python3
"""
Generator for the reimagined PALATA site — modern, light, rebellious youth aesthetic.
Single-page, clean, green accent, sharp living copy.
"""

import json
from pathlib import Path

# ============================================================
# CLEAN CURATED DATA
# ============================================================

BASE_URL = "https://xn----7sbaa5baqdtkc7agh5e.xn--p1ai/wp-content/uploads/2024/10/"

with open(Path(r"D:\PALATA\curated_data.json"), "r", encoding="utf-8") as f:
    CURATED_GALLERY = json.load(f)

# ============================================================
# CONTENT — SHARP, REBELLIOUS, ALIVE
# ============================================================

APHORISMS = [
    {
        "text": "Слава — тень добродетели",
        "author": "Цицерон",
        "note": "Настоящая слава следует за делом, а не гонится за ним"
    },
    {
        "text": "Жажда славы — признак величия души",
        "author": "Платон",
        "note": "Только сильные стремятся оставить след в истории"
    },
    {
        "text": "Честь — единственная валюта, которая не обесценивается",
        "author": "",
        "note": "Ранги дают власть, а честь — уважение веков"
    },
    {
        "text": "Награда не делает героя. Она лишь зафиксирует, что он им уже был",
        "author": "",
        "note": "Орден — не билет в будущее, а квитанция из прошлого"
    },
    {
        "text": "Кто не рискует своим именем, не достоин им владеть",
        "author": "",
        "note": "Имя — не ярлык. Контракт с историей"
    },
]

# Table of Ranks — living story, no labels
TABLE_OF_RANKS = [
    {
        "headline": "1722. Петр I подписывает документ, перевернувший понимание статуса в России на 200 лет вперёд.",
        "body": "До Табеля — хаос. Князь мог быть ничем, дворянин — ничтожеством, талантливый сын кубария — навсегда внизу. Петр ввёл 14 классов, жёстко привязанных к службе. Всё — до запятой. Кто есть кто, кому что положено. Никаких «я князь, а вы кто?». Есть ранг — есть права. Нет — сиди тихо."
    },
    {
        "headline": "Князь ≠ Ранг. Главная ловушка.",
        "body": "Титул «князь» — часто просто родовое звание. Реальная власть, доступ к царю, земля, почет — давали не кровь, а служба. Князь без ранга — красивое имя в списке гостей. Подпоручик 14 класса, пробившийся до полковника (6 класс) — уже личный дворянин, через шаг — наследственный. И решает судьбы губерний."
    },
    {
        "headline": "Почему это круто сейчас?",
        "body": "Табель — первый в истории масштабный skill tree для целой нации. Чёткие уровни. Прозрачные правила апгрейда. Никаких «знает кого-то». Хочешь статус — отслужи. Хочешь знать — учись. Хочешь орден — сделай подвиг. Геймификация соцлифта в чистом виде. Именно эту логику — «сделал → получил → зафиксировал» — мы переносим в XXI век. Без приворотов. Без связей. Только merit."
    }
]

HERO = {
    "tagline": "Международная палата личности",
    "subtitle": "Ордены. Честь. Масштаб личности.",
    "mission": "Мы не раздаём медали за красивые глаза. Фиксируем моменты, когда человек преодолел себя. Когда амбиция встретилась с действием. Когда имя стало историей."
}

ABOUT = {
    "title": "Что такое Палата — за 30 секунд",
    "bullets": [
        "Международная общественная организация, объединяющая кавалеров орденов",
        "Орденская хроника: каждая награда — документ, каждая церемония — факт",
        "10+ лет, 100+ кавалеров, 10+ стран — от Сиэтла до Одессы, от Токио до Стокгольма",
        "Патриарх Кирилл, Императорский дом, главы регионов — те, кто знает цену чести, с нами",
        "Не коммерция. Не политика. Только признание заслуг и память о тех, кто меняет мир"
    ]
}

CONTACT = {
    "address": "191014, Санкт-Петербург, ул. Маяковского, 19/29",
    "addressee": "Палате Личности, Малыхин Юрию",
    "chairman": "Председатель: Юрий Малыхин"
}

# ============================================================
# HTML GENERATION
# ============================================================

def generate_html():
    html = '''<!DOCTYPE html>
<html lang="ru-RU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#F2F2F2">
<title>Международная палата личности — Ордены. Честь. Масштаб.</title>
<meta name="description" content="Официальный сайт Международной палаты личности. Орденные награды, церемонии, история Табеля о рангах, кавалеры. Признание заслуг без политики и коммерции.">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏅</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #F2F2F2;
  --bg-elevated: #FFFFFF;
  --fg: #1A1A1A;
  --fg-muted: #6B6B6B;
  --fg-subtle: #9B9B9B;
  --accent: #05EB33;
  --accent-dim: #04C02A;
  --border: #E0E0E0;
  --card-shadow: 0 2px 12px rgba(0,0,0,0.04);
  --card-shadow-hover: 0 12px 32px rgba(0,0,0,0.08);
  --radius: 16px;
  --radius-lg: 24px;
  --transition: 0.3s cubic-bezier(0.22, 1, 0.36, 1);
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-serif: 'Playfair Display', Georgia, serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
  }
}

body {
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--fg);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-feature-settings: "cv02", "cv03", "cv04", "cv11";
}

a { color: inherit; text-decoration: none; }
img { max-width: 100%; height: auto; display: block; }
button { font: inherit; background: none; border: none; cursor: pointer; }

/* Skip link */
.skip-link {
  position: absolute; top: -100%; left: 16px; z-index: 10000;
  padding: 12px 20px; background: var(--accent); color: var(--fg);
  border-radius: 8px; font-weight: 600; font-size: 14px;
}
.skip-link:focus { top: 16px; }

/* Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

::selection { background: rgba(5, 235, 51, 0.3); color: var(--fg); }

/* ===== LAYOUT ===== */
.container {
  width: 100%; max-width: 1280px; margin: 0 auto; padding: 0 24px;
}
@media (min-width: 1024px) { .container { padding: 0 40px; } }

.section { padding: 80px 0; }
@media (min-width: 768px) { .section { padding: 120px 0; } }

/* ===== TYPOGRAPHY ===== */
.display-xl {
  font-family: var(--font-serif); font-weight: 600;
  font-size: clamp(48px, 7vw, 80px); line-height: 1.02; letter-spacing: -0.03em;
}
.display-lg {
  font-family: var(--font-serif); font-weight: 500;
  font-size: clamp(36px, 5vw, 56px); line-height: 1.05; letter-spacing: -0.02em;
}
.display-md {
  font-family: var(--font-serif); font-weight: 400;
  font-size: clamp(28px, 4vw, 40px); line-height: 1.1; letter-spacing: -0.01em;
}
.body-lg { font-size: 20px; line-height: 1.8; }
.body { font-size: 16px; line-height: 1.7; }
.body-sm { font-size: 14px; line-height: 1.6; }
.caption { font-size: 12px; line-height: 1.5; letter-spacing: 0.05em; text-transform: uppercase; font-weight: 500; }

.text-gradient {
  background: linear-gradient(135deg, var(--fg) 0%, var(--accent) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

.fg-muted { color: var(--fg-muted); }
.fg-subtle { color: var(--fg-subtle); }

/* ===== BUTTONS ===== */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 10px;
  padding: 16px 32px; border-radius: 100px; font-weight: 600; font-size: 16px;
  transition: var(--transition); white-space: nowrap;
}
.btn-primary {
  background: var(--accent); color: var(--fg);
  box-shadow: 0 2px 8px rgba(5, 235, 51, 0.3);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(5, 235, 51, 0.4); }
.btn-primary:active { transform: translateY(0); }

.btn-ghost {
  background: transparent; color: var(--fg); border: 1px solid var(--border);
}
.btn-ghost:hover { border-color: var(--accent); color: var(--accent); background: rgba(5, 235, 51, 0.06); }

/* ===== NAV ===== */
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  transition: var(--transition);
}
.nav.scrolled { background: rgba(255, 255, 255, 0.95); box-shadow: 0 4px 24px rgba(0,0,0,0.04); }

.nav-inner {
  display: flex; align-items: center; justify-content: space-between; height: 72px;
}
.nav-brand {
  display: flex; align-items: center; gap: 12px;
  font-family: var(--font-serif); font-weight: 600; font-size: 22px; color: var(--fg);
}
.nav-brand:hover { color: var(--accent); }
.nav-logo {
  width: 40px; height: 40px; border-radius: 12px;
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent-dim) 100%);
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 18px; color: var(--fg);
}

.nav-menu { display: none; gap: 40px; }
@media (min-width: 768px) { .nav-menu { display: flex; } }
.nav-link { font-weight: 500; font-size: 14px; color: var(--fg-muted); transition: var(--transition); }
.nav-link:hover { color: var(--accent); }

.nav-actions { display: flex; align-items: center; gap: 12px; }

/* Mobile menu */
.mobile-menu-btn { display: flex; align-items: center; justify-content: center; width: 44px; height: 44px; border-radius: 12px; color: var(--fg-muted); }
@media (min-width: 768px) { .mobile-menu-btn { display: none; } }
.mobile-menu-btn:hover { background: var(--border); color: var(--fg); }

.mobile-menu {
  position: fixed; inset: 0; z-index: 999;
  background: var(--bg-elevated); transform: translateX(100%); transition: transform 0.4s var(--transition);
  display: flex; flex-direction: column; padding: 80px 24px 32px; overflow-y: auto;
}
.mobile-menu.open { transform: translateX(0); }
.mobile-menu-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 40px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
.mobile-menu-close { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--fg-muted); }
.mobile-menu-close:hover { background: var(--border); color: var(--fg); }
.mobile-nav { display: flex; flex-direction: column; gap: 8px; }
.mobile-nav-link { padding: 16px 20px; border-radius: 12px; font-weight: 500; font-size: 16px; color: var(--fg-muted); transition: var(--transition); }
.mobile-nav-link:hover { background: var(--border); color: var(--fg); }

.mobile-overlay {
  position: fixed; inset: 0; z-index: 998; background: rgba(0,0,0,0.5); opacity: 0; pointer-events: none; transition: opacity 0.3s;
}
.mobile-overlay.open { opacity: 1; pointer-events: auto; }

/* ===== HERO ===== */
.hero {
  min-height: 100vh; display: flex; align-items: center; justify-content: center;
  position: relative; overflow: hidden; padding-top: 72px;
}
.hero-bg {
  position: absolute; inset: 0; z-index: -2;
  background:
    radial-gradient(ellipse 60% 50% at 50% 0%, rgba(5, 235, 51, 0.08) 0%, transparent 60%),
    radial-gradient(ellipse 40% 30% at 80% 100%, rgba(5, 235, 51, 0.04) 0%, transparent 50%);
}
.hero-grid {
  position: absolute; inset: 0; z-index: -1; opacity: 0.03;
  background-image:
    linear-gradient(rgba(0,0,0,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,0,0,0.04) 1px, transparent 1px);
  background-size: 60px 60px;
}

.hero-content { text-align: center; max-width: 800px; padding: 40px 0; }
.hero-badge {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 8px 16px; border-radius: 100px; background: var(--bg-elevated); border: 1px solid var(--border);
  margin-bottom: 32px; font-size: 13px; font-weight: 500; color: var(--fg-muted);
}
.hero-badge::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--accent); animation: pulse 2s infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }

.hero-title { margin-bottom: 24px; }
.hero-title .accent { color: var(--accent); }

.hero-subtitle { margin-bottom: 40px; color: var(--fg-muted); }

.hero-mission {
  background: var(--bg-elevated); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 32px 40px; margin-bottom: 48px; text-align: left; font-style: italic;
  font-size: 20px; line-height: 1.8; color: var(--fg-muted);
}
@media (max-width: 640px) { .hero-mission { padding: 24px; font-size: 18px; } }

.hero-cta { display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; margin-bottom: 60px; }

.hero-scroll {
  position: absolute; bottom: 32px; left: 50%; transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: 8px;
  color: var(--fg-subtle); font-size: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em;
}
.hero-scroll svg { animation: bounce 2s infinite; width: 24px; height: 24px; }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(8px); } }

/* ===== GREEN ACCENT BAR ===== */
.accent-bar {
  height: 3px; background: linear-gradient(90deg, var(--accent) 0%, var(--accent-dim) 100%);
  margin: 40px 0; border-radius: 2px;
}
.accent-bar-short {
  width: 80px; height: 4px; background: linear-gradient(90deg, var(--accent), var(--accent-dim));
  border-radius: 2px; margin: 16px 0 32px;
}

/* ===== ABOUT / STATS ===== */
.about-grid {
  display: grid; gap: 48px; align-items: start;
}
@media (min-width: 1024px) { .about-grid { grid-template-columns: 1fr 1.2fr; } }

.about-title { margin-bottom: 8px; }
.about-text { color: var(--fg-muted); margin-bottom: 32px; font-size: 20px; }

.about-list { display: flex; flex-direction: column; gap: 20px; }
.about-item {
  display: flex; gap: 16px; padding: 20px; background: var(--bg-elevated);
  border: 1px solid var(--border); border-radius: var(--radius);
  transition: var(--transition);
}
.about-item:hover { border-color: var(--accent); box-shadow: var(--card-shadow-hover); }
.about-icon {
  width: 48px; height: 48px; border-radius: 12px; flex-shrink: 0;
  background: rgba(5, 235, 51, 0.1); color: var(--accent);
  display: flex; align-items: center; justify-content: center; font-size: 20px;
}
.about-item-text { color: var(--fg-muted); }

.stats-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px;
}
@media (min-width: 640px) { .stats-grid { grid-template-columns: repeat(4, 1fr); } }
.stat-card {
  background: var(--bg-elevated); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 32px 24px; text-align: center; transition: var(--transition);
}
.stat-card:hover { border-color: var(--accent); box-shadow: var(--card-shadow-hover); }
.stat-icon { font-size: 32px; margin-bottom: 12px; }
.stat-number {
  font-family: var(--font-serif); font-weight: 600; font-size: 48px; line-height: 1.1; color: var(--fg);
}
@media (min-width: 768px) { .stat-number { font-size: 64px; } }
.stat-label { font-size: 13px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; color: var(--fg-muted); margin-top: 8px; }

.chairman-card {
  margin-top: 48px; background: var(--bg-elevated); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 40px; display: grid; gap: 24px;
}
@media (min-width: 768px) { .chairman-card { grid-template-columns: auto 1fr; align-items: center; } }
.chairman-avatar {
  width: 96px; height: 96px; border-radius: var(--radius-lg);
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent-dim) 100%);
  display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: 700; color: var(--fg);
  margin: 0 auto;
}
@media (min-width: 768px) { .chairman-avatar { margin: 0; } }
.chairman-badge {
  display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px;
  background: rgba(5, 235, 51, 0.1); color: var(--accent); border-radius: 100px;
  font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; width: fit-content;
}
.chairman-name { font-family: var(--font-serif); font-weight: 600; font-size: 32px; line-height: 1.2; }
.chairman-desc { color: var(--fg-muted); font-size: 18px; }
.chairman-tags { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }
.tag {
  padding: 8px 16px; border-radius: 100px; font-size: 13px; font-weight: 500;
  background: var(--bg); border: 1px solid var(--border); color: var(--fg-muted); transition: var(--transition);
}
.tag:hover { border-color: var(--accent); color: var(--accent); }
.tag-primary { background: rgba(5, 235, 51, 0.1); border-color: var(--accent); color: var(--accent); }

/* ===== APHORISMS ===== */
.aphorisms-grid {
  display: grid; gap: 24px;
}
@media (min-width: 768px) { .aphorisms-grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .aphorisms-grid { grid-template-columns: repeat(3, 1fr); } }

.aphorism-card {
  background: var(--bg-elevated); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 32px; position: relative; transition: var(--transition);
  border-left: 4px solid transparent;
}
.aphorism-card::before {
  content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px;
  background: linear-gradient(180deg, var(--accent), var(--accent-dim));
  opacity: 0; transition: var(--transition);
}
.aphorism-card:hover {
  border-color: var(--accent); box-shadow: var(--card-shadow-hover); transform: translateX(4px);
}
.aphorism-card:hover::before { opacity: 1; }
.aphorism-text { font-family: var(--font-serif); font-weight: 500; font-size: 22px; line-height: 1.4; margin-bottom: 16px; }
.aphorism-author { font-family: var(--font-serif); font-size: 16px; color: var(--accent); margin-bottom: 12px; }
.aphorism-divider { width: 40px; height: 2px; background: var(--accent); border-radius: 1px; margin-bottom: 16px; }
.aphorism-note { font-size: 14px; color: var(--fg-muted); line-height: 1.6; }

/* ===== HISTORY / TABLE OF RANKS ===== */
.history-list { display: flex; flex-direction: column; gap: 32px; }
.history-card {
  background: var(--bg-elevated); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 40px; position: relative; overflow: hidden; transition: var(--transition);
}
.history-card::before {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent), var(--accent-dim), var(--accent));
  background-size: 200% 100%; animation: accent-shift 4s linear infinite;
}
@keyframes accent-shift { 0% { background-position: 0% 50%; } 100% { background-position: 200% 50%; } }
.history-card:hover { border-color: var(--accent); box-shadow: var(--card-shadow-hover); }
.history-number {
  width: 48px; height: 48px; border-radius: 12px; flex-shrink: 0;
  background: rgba(5, 235, 51, 0.1); color: var(--accent);
  display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 20px;
}
.history-content { flex: 1; min-width: 0; }
.history-headline { font-family: var(--font-serif); font-weight: 600; font-size: 24px; line-height: 1.3; margin-bottom: 16px; }
@media (min-width: 768px) { .history-headline { font-size: 28px; } }
.history-body { color: var(--fg-muted); line-height: 1.8; }
.history-divider { height: 1px; background: linear-gradient(90deg, transparent, var(--border), transparent); margin-top: 32px; }

.bridge-card {
  background: var(--bg-elevated); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 48px; text-align: center; margin-top: 40px;
}
.bridge-title { font-family: var(--font-serif); font-weight: 600; font-size: 32px; line-height: 1.2; margin-bottom: 16px; }
.bridge-text { color: var(--fg-muted); font-size: 20px; margin-bottom: 32px; max-width: 600px; margin-left: auto; margin-right: auto; }

/* ===== GALLERY ===== */
.gallery-header {
  display: flex; flex-direction: column; gap: 16px; align-items: flex-start; justify-content: space-between; margin-bottom: 40px;
}
@media (min-width: 768px) { .gallery-header { flex-direction: row; align-items: center; } }
.gallery-title { font-family: var(--font-serif); font-weight: 600; font-size: 36px; line-height: 1.2; }
.gallery-subtitle { color: var(--fg-muted); max-width: 400px; }

.filter-bar {
  display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 32px;
}
.filter-btn {
  padding: 10px 20px; border-radius: 100px; font-size: 13px; font-weight: 500;
  background: transparent; border: 1px solid var(--border); color: var(--fg-muted);
  transition: var(--transition); white-space: nowrap;
}
.filter-btn:hover { border-color: var(--accent); color: var(--accent); background: rgba(5, 235, 51, 0.06); }
.filter-btn.active { background: var(--accent); border-color: var(--accent); color: var(--fg); }

.gallery-grid {
  display: grid; grid-template-columns: 1fr; gap: 20px;
}
@media (min-width: 640px) { .gallery-grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .gallery-grid { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 1440px) { .gallery-grid { grid-template-columns: repeat(4, 1fr); } }

.gallery-item {
  background: var(--bg-elevated); border: 1px solid var(--border); border-radius: var(--radius-lg);
  overflow: hidden; aspect-ratio: 4/5; position: relative; transition: var(--transition);
  cursor: pointer;
}
.gallery-item:hover { transform: translateY(-6px); border-color: var(--accent); box-shadow: var(--card-shadow-hover); }
.gallery-item.hidden { display: none; }

.gallery-image {
  width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s var(--transition);
}
.gallery-item:hover .gallery-image { transform: scale(1.05); }

.gallery-overlay {
  position: absolute; inset: 0; background: linear-gradient(180deg, transparent 50%, rgba(0,0,0,0.7) 100%);
  opacity: 0; transition: var(--transition); display: flex; flex-direction: column; justify-content: flex-end; padding: 24px;
}
.gallery-item:hover .gallery-overlay { opacity: 1; }
.gallery-caption { color: white; font-weight: 500; font-size: 15px; }
.gallery-category {
  position: absolute; top: 16px; left: 16px; z-index: 1;
  padding: 6px 12px; border-radius: 100px; font-size: 11px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.05em;
  background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); color: white; border: 1px solid rgba(255,255,255,0.3);
}
.gallery-expand {
  position: absolute; top: 16px; right: 16px; z-index: 1; opacity: 0; transition: var(--transition);
  width: 40px; height: 40px; border-radius: 50%; background: rgba(0,0,0,0.4); backdrop-filter: blur(8px);
  display: flex; align-items: center; justify-content: center; color: white;
}
.gallery-item:hover .gallery-expand { opacity: 1; }
.gallery-expand:hover { background: var(--accent); color: var(--fg); }

.gallery-more {
  text-align: center; margin-top: 48px; padding-top: 40px; border-top: 1px solid var(--border);
}
.gallery-more-text { color: var(--fg-muted); margin-bottom: 20px; }

/* ===== LIGHTBOX ===== */
.lightbox {
  position: fixed; inset: 0; z-index: 10000; background: rgba(0,0,0,0.95);
  display: none; align-items: center; justify-content: center; padding: 24px;
  opacity: 0; transition: opacity 0.3s; backdrop-filter: blur(8px);
}
.lightbox.open { display: flex; opacity: 1; }
.lightbox-content { position: relative; max-width: 90vw; max-height: 85vh; transform: scale(0.92); transition: transform 0.35s var(--transition); }
.lightbox.open .lightbox-content { transform: scale(1); }
.lightbox-img { max-width: 100%; max-height: 75vh; border-radius: 16px; box-shadow: 0 32px 64px rgba(0,0,0,0.5); object-fit: contain; }
.lightbox-caption { margin-top: 24px; color: rgba(255,255,255,0.8); font-family: var(--font-serif); font-style: italic; font-size: 20px; text-align: center; max-width: 700px; line-height: 1.6; }
.lightbox-close, .lightbox-prev, .lightbox-next {
  width: 56px; height: 56px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.15);
  background: rgba(0,0,0,0.5); color: white; display: flex; align-items: center; justify-content: center;
  transition: var(--transition); backdrop-filter: blur(8px);
}
.lightbox-close { position: absolute; top: -72px; right: 0; }
.lightbox-prev { position: absolute; top: 50%; left: -72px; transform: translateY(-50%); }
.lightbox-next { position: absolute; top: 50%; right: -72px; transform: translateY(-50%); }
@media (max-width: 1024px) {
  .lightbox-prev { left: 16px; } .lightbox-next { right: 16px; }
  .lightbox-close { top: -68px; right: 0; }
}
.lightbox-close:hover, .lightbox-prev:hover, .lightbox-next:hover {
  background: var(--accent); border-color: var(--accent); color: var(--fg);
}
.lightbox-counter { position: absolute; bottom: -50px; left: 50%; transform: translateX(-50%); color: rgba(255,255,255,0.4); font-size: 13px; font-weight: 500; letter-spacing: 0.05em; }

/* ===== CONTACTS ===== */
.contacts-grid {
  display: grid; gap: 48px;
}
@media (min-width: 1024px) { .contacts-grid { grid-template-columns: 1fr 1fr; } }

.contact-title { font-family: var(--font-serif); font-weight: 600; font-size: 36px; line-height: 1.2; margin-bottom: 16px; }
.contact-subtitle { color: var(--fg-muted); font-size: 20px; margin-bottom: 40px; }

.contact-list { display: flex; flex-direction: column; gap: 24px; }
.contact-item {
  display: flex; gap: 20px; padding: 24px; background: var(--bg-elevated);
  border: 1px solid var(--border); border-radius: var(--radius); transition: var(--transition);
}
.contact-item:hover { border-color: var(--accent); }
.contact-icon {
  width: 56px; height: 56px; border-radius: 14px; flex-shrink: 0;
  background: rgba(5, 235, 51, 0.1); color: var(--accent);
  display: flex; align-items: center; justify-content: center; font-size: 22px;
}
.contact-label { font-size: 13px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; color: var(--fg-muted); margin-bottom: 4px; }
.contact-value { color: var(--fg); font-size: 16px; line-height: 1.6; }

.cta-card {
  background: var(--bg-elevated); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 48px; display: flex; flex-direction: column; align-items: stretch; height: 100%;
}
.cta-title { font-family: var(--font-serif); font-weight: 600; font-size: 32px; line-height: 1.2; margin-bottom: 12px; }
.cta-text { color: var(--fg-muted); font-size: 20px; margin-bottom: 32px; flex: 1; }
.cta-buttons { display: flex; flex-direction: column; gap: 12px; margin-bottom: 40px; }
.cta-divider { height: 1px; background: var(--border); margin-bottom: 24px; }
.cta-partners { color: var(--fg-subtle); font-size: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 16px; }
.cta-tags { display: flex; flex-wrap: wrap; gap: 10px; }
.cta-tag { padding: 8px 16px; border-radius: 100px; font-size: 12px; font-weight: 500; background: var(--bg); border: 1px solid var(--border); color: var(--fg-muted); transition: var(--transition); }
.cta-tag:hover { border-color: var(--accent); color: var(--accent); }
.cta-tag-primary { background: rgba(5, 235, 51, 0.1); border-color: var(--accent); color: var(--accent); }

/* ===== FOOTER ===== */
.footer {
  border-top: 1px solid var(--border); background: var(--bg-elevated);
  padding: 40px 0; margin-top: 80px;
}
.footer-inner {
  display: flex; flex-direction: column; align-items: center; justify-content: space-between; gap: 24px; text-align: center;
}
@media (min-width: 768px) { .footer-inner { flex-direction: row; text-align: left; } }
.footer-brand { display: flex; align-items: center; gap: 12px; font-family: var(--font-serif); font-weight: 600; font-size: 22px; color: var(--fg); }
.footer-logo { width: 40px; height: 40px; border-radius: 12px; background: linear-gradient(135deg, var(--accent), var(--accent-dim)); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 18px; color: var(--fg); }
.footer-nav { display: flex; flex-wrap: wrap; gap: 24px; justify-content: center; }
@media (min-width: 768px) { .footer-nav { justify-content: flex-start; } }
.footer-link { font-size: 14px; color: var(--fg-muted); transition: var(--transition); }
.footer-link:hover { color: var(--accent); }
.footer-copy { font-size: 12px; color: var(--fg-subtle); }

/* ===== REVEAL ANIMATIONS ===== */
.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.8s var(--transition), transform 0.8s var(--transition); }
.reveal.visible { opacity: 1; transform: translateY(0); }
.stagger-1 { transition-delay: 80ms; } .stagger-2 { transition-delay: 160ms; }
.stagger-3 { transition-delay: 240ms; } .stagger-4 { transition-delay: 320ms; }
.stagger-5 { transition-delay: 400ms; } .stagger-6 { transition-delay: 480ms; }

/* ===== ACCESSIBILITY ===== */
@media (prefers-contrast: high) {
  :root { --border: #000; --fg-muted: #333; }
}
.focus-visible:focus { outline: 2px solid var(--accent); outline-offset: 3px; }

</style>
</head>
<body>

<!-- Skip link -->
<a href="#main" class="skip-link">Перейти к основному содержимому</a>

<!-- Navigation -->
<nav class="nav" id="nav" role="navigation" aria-label="Главное меню">
  <div class="container nav-inner">
    <a href="#top" class="nav-brand" aria-label="Международная палата личности — главная">
      <span class="nav-logo" aria-hidden="true">🏅</span>
      <span>Международная палата личности</span>
    </a>
    <div class="nav-menu" role="menubar">
      <a href="#about" class="nav-link" role="menuitem">О Палате</a>
      <a href="#aphorisms" class="nav-link" role="menuitem">Философия</a>
      <a href="#history" class="nav-link" role="menuitem">История</a>
      <a href="#gallery" class="nav-link" role="menuitem">Галерея</a>
      <a href="#contacts" class="nav-link" role="menuitem">Контакты</a>
    </div>
    <div class="nav-actions">
      <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Открыть меню" aria-expanded="false" aria-controls="mobileMenu">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 6h16M4 12h16M4 18h16" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</nav>

<!-- Mobile menu -->
<div class="mobile-menu" id="mobileMenu" role="dialog" aria-modal="true" aria-label="Меню">
  <div class="mobile-menu-header">
    <a href="#top" class="nav-brand">
      <span class="nav-logo" aria-hidden="true">🏅</span>
      <span>Международная палата личности</span>
    </a>
    <button class="mobile-menu-close" id="mobileMenuClose" aria-label="Закрыть меню">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 18L18 6M6 6l12 12" stroke-linecap="round"/></svg>
    </button>
  </div>
  <nav class="mobile-nav" role="navigation">
    <a href="#about" class="mobile-nav-link" role="menuitem">О Палате</a>
    <a href="#aphorisms" class="mobile-nav-link" role="menuitem">Философия</a>
    <a href="#history" class="mobile-nav-link" role="menuitem">История</a>
    <a href="#gallery" class="mobile-nav-link" role="menuitem">Галерея</a>
    <a href="#contacts" class="mobile-nav-link" role="menuitem">Контакты</a>
  </nav>
</div>
<div class="mobile-overlay" id="mobileOverlay"></div>

<!-- Main -->
<main id="main">

<!-- HERO -->
<section class="hero" id="top" aria-labelledby="hero-title">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="hero-grid" aria-hidden="true"></div>
  <div class="container">
    <div class="hero-content">
      <div class="hero-badge reveal">
        <span>Официальный ресурс · c 2014</span>
      </div>
      <h1 class="display-xl reveal stagger-1" id="hero-title">Международная<br><span class="accent">палата личности</span></h1>
      <p class="display-md reveal stagger-2 fg-muted">Ордены. Честь. Масштаб личности.</p>
      <div class="hero-mission reveal stagger-3">"''' + HERO["mission"] + '''"</div>
      <div class="hero-cta reveal stagger-4">
        <a href="#gallery" class="btn btn-primary">Открыть галерею наград <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M13 7l5 5m0 0l-5 5m5-5H6" stroke-linecap="round"/></svg></a>
        <a href="#about" class="btn btn-ghost">О Палате <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 3a1 1 0 011-1h14a1 1 0 011 1v16a1 1 0 01-1 1H5a1 1 0 01-1-1V3zM4 7l16 0" stroke-linecap="round"/></svg></a>
      </div>
      <div class="hero-scroll" aria-hidden="true">
        <span>Прокрути</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 14l-7 7m0 0l-7-7m7 7V3" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT -->
<section class="section" id="about" aria-labelledby="about-title">
  <div class="container">
    <div class="about-grid">
      <div>
        <div class="caption reveal fg-subtle">О Палате</div>
        <h2 class="display-lg reveal stagger-1" id="about-title">''' + ABOUT["title"] + '''</h2>
        <div class="accent-bar-short reveal stagger-2"></div>
        <p class="body-lg reveal stagger-2 fg-muted">''' + ABOUT["bullets"][0] + '''. Не коммерция. Не политика. Только признание заслуг и память о тех, кто меняет мир.</p>
        <ul class="about-list" role="list">
'''
    for i, bullet in enumerate(ABOUT["bullets"]):
        html += f'''          <li class="about-item reveal stagger-{3 + i}" style="transition-delay: {200 + i * 80}ms">
            <span class="about-icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 13l4 4L19 7" stroke-linecap="round"/></svg></span>
            <span class="about-item-text">{bullet}</span>
          </li>
'''
    html += '''        </ul>
      </div>
      <div>
        <div class="stats-grid" role="list">
'''
    stats = [
        {"num": "10+", "label": "Лет работы", "icon": "📅"},
        {"num": "100+", "label": "Кавалеров", "icon": "🏅"},
        {"num": "10+", "label": "Стран", "icon": "🌍"},
        {"num": "∞", "label": "Уважения", "icon": "♾️"},
    ]
    for i, stat in enumerate(stats):
        html += f'''          <article class="stat-card reveal stagger-1" style="transition-delay: {i * 80}ms" role="listitem">
            <div class="stat-icon" aria-hidden="true">{stat["icon"]}</div>
            <div class="stat-number">{stat["num"]}</div>
            <div class="stat-label">{stat["label"]}</div>
          </article>
'''
    html += '''        </div>
        <div class="chairman-card reveal" style="transition-delay: 400ms">
          <div class="chairman-avatar" aria-hidden="true">🏅</div>
          <div>
            <span class="chairman-badge">Председатель Палаты</span>
            <h3 class="chairman-name">Юрий Малыхин</h3>
            <p class="chairman-desc">Основатель и идеолог Палаты. Делает честь и награды понятными, прозрачными и достойными для нового поколения.</p>
            <div class="chairman-tags">
              <span class="tag">10+ лет миссии</span>
              <span class="tag">Международное признание</span>
              <span class="tag tag-primary">Честность ante omnia</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- APHORISMS -->
<section class="section" id="aphorisms" aria-labelledby="aphorisms-title">
  <div class="container">
    <div class="reveal" style="text-align: center; max-width: 600px; margin: 0 auto 60px;">
      <div class="caption fg-subtle">Философия</div>
      <h2 class="display-lg" id="aphorisms-title">Афоризмы о чести, славе и награде</h2>
      <p class="body-lg fg-muted" style="margin-top: 16px;">Не пафос. Не бюрократия. Твёрдые истины, проверенные веками. Читай — и бери на вооружение.</p>
    </div>
    <div class="aphorisms-grid" role="list">
'''
    for i, aph in enumerate(APHORISMS):
        html += f'''      <article class="aphorism-card reveal stagger-{(i % 6) + 1}" role="listitem" style="transition-delay: {i * 100}ms">
        <blockquote class="aphorism-text">«{aph["text"]}»</blockquote>
'''
        if aph["author"]:
            html += f'''        <cite class="aphorism-author">{aph["author"]}</cite>
        <div class="aphorism-divider"></div>
'''
        html += f'''        <p class="aphorism-note">{aph["note"]}</p>
      </article>
'''
    html += '''    </div>
  </div>
</section>

<!-- HISTORY / TABLE OF RANKS -->
<section class="section" id="history" aria-labelledby="history-title">
  <div class="container">
    <div class="reveal" style="text-align: center; max-width: 600px; margin: 0 auto 60px;">
      <div class="caption fg-subtle">История</div>
      <h2 class="display-lg" id="history-title">Табель о рангах: как Империя построила идеальную méritократию</h2>
      <p class="body-lg fg-muted" style="margin-top: 16px;">Почему система Петра I всё ещё круче любого современного HR-бренда.</p>
    </div>
    <div class="history-list" role="list">
'''
    for i, section in enumerate(TABLE_OF_RANKS):
        html += f'''      <article class="history-card reveal stagger-{(i % 6) + 1}" role="listitem" style="transition-delay: {i * 150}ms">
        <div style="display: flex; gap: 24px; align-items: flex-start;">
          <span class="history-number" aria-hidden="true">{i + 1}</span>
          <div class="history-content">
            <h3 class="history-headline">{section["headline"]}</h3>
            <div class="history-body">{section["body"]}</div>
          </div>
        </div>
        <div class="history-divider"></div>
      </article>
'''
    html += '''    </div>
    <div class="bridge-card reveal" style="transition-delay: 600ms;">
      <h3 class="bridge-title">Именно эту логику мы перенесли в XXI век</h3>
      <p class="bridge-text">Прозрачные критерии. Открытая хроника. Никаких «своих». Только merit — действие, зафиксированное орденом.</p>
      <a href="#gallery" class="btn btn-primary">Увидеть, как это выглядит сейчас <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M13 7l5 5m0 0l-5 5m5-5H6" stroke-linecap="round"/></svg></a>
    </div>
  </div>
</section>

<!-- GALLERY -->
<section class="section" id="gallery" aria-labelledby="gallery-title">
  <div class="container">
    <div class="gallery-header">
      <div>
        <div class="caption reveal fg-subtle">Галерея</div>
        <h2 class="display-lg reveal stagger-1" id="gallery-title">Награды, церемонии, история в деталях</h2>
        <p class="body reveal stagger-2 fg-muted">Курируемая подборка. Без «стены старых мужчин». Только регалии, знаки отличия и моменты, когда честь становилась видимой.</p>
      </div>
      <div class="reveal stagger-3" style="transition-delay: 200ms;">
        <span class="caption fg-subtle" id="gallery-counter">Показано <span id="visible-count">0</span> из {len(CURATED_GALLERY)}</span>
      </div>
    </div>
    <div class="filter-bar reveal stagger-2" role="tablist" aria-label="Фильтр по категориям" style="transition-delay: 150ms;">
'''
    categories = ["Все", "Ордена", "Церемонии", "Историческое", "Международное", "Патриарх", "Прочее", "Портреты"]
    for i, cat in enumerate(categories):
        active = 'active' if cat == "Все" else ''
        selected = 'true' if cat == "Все" else 'false'
        html += f'''      <button class="filter-btn {active}" data-filter="{cat}" role="tab" aria-selected="{selected}" aria-controls="gallery-grid">{cat}</button>
'''
    html += '''    </div>
    <div class="gallery-grid" id="gallery-grid" role="list" aria-label="Галерея наград">
'''
    for i, item in enumerate(CURATED_GALLERY):
        full_url = BASE_URL + item['file']
        stagger = (i % 6) + 1
        html += f'''      <article class="gallery-item reveal stagger-{stagger}" data-category="{item['category']}" role="listitem" tabindex="0" onclick="openLightbox({i})" onkeydown="if(event.key==='Enter'||event.key===' '){{event.preventDefault();openLightbox({i})}}">
        <img class="gallery-image" src="{full_url}" alt="{item['alt']}" loading="lazy" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 500%22%3E%3Crect fill=%22%23F2F2F2%22 width=%22400%22 height=%22500%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 dominant-baseline=%22middle%22 text-anchor=%22middle%22 fill=%22%239B9B9B%22 font-family=%22system-ui%22 font-size=%2214%22%3E%F0%9F%8F%85%3C/text%3E%3C/svg%22'">
        <div class="gallery-overlay">
          <span class="gallery-caption">{item['caption']}</span>
        </div>
        <span class="gallery-category">{item['category']}</span>
        <button class="gallery-expand" aria-label="Открыть в полноэкранном режиме"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" stroke-linecap="round"/></svg></button>
      </article>
'''
    html += '''    </div>
    <div class="gallery-more reveal" style="transition-delay: 300ms;">
      <p class="gallery-more-text">В архиве Палаты — сотни уникальных снимков, документов и регалий.</p>
      <a href="gallery.html" class="btn btn-ghost">Полная галерея на отдельной странице <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M13 7l5 5m0 0l-5 5m5-5H6" stroke-linecap="round"/></svg></a>
    </div>
  </div>
</section>

<!-- CONTACTS -->
<section class="section" id="contacts" aria-labelledby="contacts-title">
  <div class="container">
    <div class="contacts-grid">
      <div>
        <div class="caption reveal fg-subtle">Контакты</div>
        <h2 class="display-lg reveal stagger-1 contact-title" id="contacts-title">Свяжитесь с Палатой</h2>
        <p class="body reveal stagger-2 contact-subtitle fg-muted">Пишите, если хотите предложить кандидата на награду, узнать о партнёрстве или просто сказать: «Респект за миссию».</p>
        <div class="contact-list" role="list">
          <div class="contact-item reveal stagger-3" role="listitem">
            <span class="contact-icon" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
            <div>
              <span class="contact-label">Адрес</span>
              <address class="contact-value" style="font-style: normal;">''' + CONTACT["address"] + '''<br>Адресат: ''' + CONTACT["addressee"] + '''</address>
            </div>
          </div>
          <div class="contact-item reveal stagger-4" role="listitem">
            <span class="contact-icon" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/></svg></span>
            <div>
              <span class="contact-label">Руководство</span>
              <p class="contact-value">''' + CONTACT["chairman"] + '''</p>
            </div>
          </div>
          <div class="contact-item reveal stagger-5" role="listitem">
            <span class="contact-icon" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></span>
            <div>
              <span class="contact-label">Предложить кандидата</span>
              <p class="contact-value">Напишите на официальную почту Палаты с пометкой «Кандидат». Рассмотрим за 14 дней.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="cta-card reveal" style="transition-delay: 200ms;">
        <h3 class="cta-title">Хотите стать кавалером?</h3>
        <p class="cta-text">Нет анкет, нет взяток, нет связей. Есть только дела, которые говорят сами за себя. Если вы (или кто-то, кого вы знаете) сделали подвиг — мы его зафиксируем.</p>
        <div class="cta-buttons">
          <button class="btn btn-primary" onclick="window.open('mailto:palata@personalitet.org?subject=Кандидат%20на%20награду','_blank')">Предложить кандидата</button>
          <button class="btn btn-ghost" onclick="window.open('https://t.me/palata_lichnosti','_blank')">Написать в Telegram</button>
        </div>
        <div class="cta-divider"></div>
        <p class="cta-partners">Партнёры и поддержка</p>
        <div class="cta-tags">
          <span class="cta-tag">Патриархия</span>
          <span class="cta-tag">Императорский дом</span>
          <span class="cta-tag">Гос. структуры</span>
          <span class="cta-tag cta-tag-primary">Международные orgs</span>
        </div>
      </div>
    </div>
  </div>
</section>

</main>

<!-- FOOTER -->
<footer class="footer" role="contentinfo">
  <div class="container footer-inner">
    <div class="footer-brand">
      <span class="footer-logo" aria-hidden="true">🏅</span>
      <span>«Международная палата личности»</span>
    </div>
    <nav class="footer-nav" aria-label="Навигация по подвалу">
      <a href="#about" class="footer-link">О Палате</a>
      <a href="#aphorisms" class="footer-link">Философия</a>
      <a href="#history" class="footer-link">История</a>
      <a href="#gallery" class="footer-link">Галерея</a>
      <a href="#contacts" class="footer-link">Контакты</a>
    </nav>
    <p class="footer-copy">Создание сайта: ЯрСайт</p>
  </div>
</footer>

<!-- LIGHTBOX -->
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Полноэкранный просмотр изображения">
  <div class="lightbox-content">
    <button class="lightbox-close" id="lightbox-close" aria-label="Закрыть"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 18L18 6M6 6l12 12" stroke-linecap="round"/></svg></button>
    <button class="lightbox-prev" id="lightbox-prev" aria-label="Предыдущее"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 18l-6-6 6-6" stroke-linecap="round"/></svg></button>
    <img class="lightbox-img" id="lightbox-img" alt="" src="" loading="lazy">
    <p class="lightbox-caption" id="lightbox-caption"></p>
    <span class="lightbox-counter" id="lightbox-counter"></span>
    <button class="lightbox-next" id="lightbox-next" aria-label="Следующее"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 18l6-6-6-6" stroke-linecap="round"/></svg></button>
  </div>
</div>

<!-- JAVASCRIPT -->
<script>
// Gallery data for lightbox
const galleryData = [
'''
    for i, item in enumerate(CURATED_GALLERY):
        full_url = BASE_URL + item['file']
        html += f'''  {{"file": "{item['file']}", "alt": "{item['alt'].replace('"', '\\\\\"')}", "caption": "{item['caption'].replace('"', '\\\\\"')}", "full_url": "{full_url}", "category": "{item['category']}"}},
'''
    html += '''];

const BASE_URL = "https://xn----7sbaa5baqdtkc7agh5e.xn--p1ai/wp-content/uploads/2024/10/";

// Lightbox
let currentIndex = 0;
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.getElementById('lightbox-caption');
const lightboxCounter = document.getElementById('lightbox-counter');
const lightboxClose = document.getElementById('lightbox-close');
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
  lightboxCounter.textContent = `${currentIndex + 1} / ${galleryData.length}`;
}
function prevImage() { currentIndex = (currentIndex - 1 + galleryData.length) % galleryData.length; updateLightbox(); }
function nextImage() { currentIndex = (currentIndex + 1) % galleryData.length; updateLightbox(); }

lightboxClose.addEventListener('click', closeLightbox);
lightboxPrev.addEventListener('click', prevImage);
lightboxNext.addEventListener('click', nextImage);
lightbox.addEventListener('click', (e) => { if (e.target === lightbox) closeLightbox(); });
document.addEventListener('keydown', (e) => {
  if (!lightbox.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') prevImage();
  if (e.key === 'ArrowRight') nextImage();
});

// Category filter
const filterButtons = document.querySelectorAll('.filter-btn');
const galleryItems = document.querySelectorAll('[data-category]');
const visibleCount = document.getElementById('visible-count');

function updateVisibleCount() {
  let count = 0;
  galleryItems.forEach(item => { if (item.style.display !== 'none') count++; });
  if (visibleCount) visibleCount.textContent = count;
}

filterButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;
    filterButtons.forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
    btn.classList.add('active'); btn.setAttribute('aria-selected', 'true');
    galleryItems.forEach((item) => {
      const cat = item.dataset.category;
      if (filter === 'Все' || cat === filter) {
        item.style.display = 'block';
        item.style.animation = 'fadeInUp 0.4s var(--transition) forwards';
        item.style.opacity = '1'; item.style.transform = 'translateY(0)';
      } else {
        item.style.animation = 'fadeInUp 0.3s var(--transition) reverse forwards';
        setTimeout(() => { item.style.display = 'none'; }, 300);
      }
    });
    setTimeout(updateVisibleCount, 350);
  });
});
setTimeout(updateVisibleCount, 100);

// Mobile menu
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenuClose = document.getElementById('mobileMenuClose');
const mobileMenu = document.getElementById('mobileMenu');
const mobileOverlay = document.getElementById('mobileOverlay');

mobileMenuBtn?.addEventListener('click', () => {
  mobileMenu?.classList.add('open');
  mobileOverlay?.classList.add('open');
  document.body.style.overflow = 'hidden';
  mobileMenuBtn.setAttribute('aria-expanded', 'true');
});
function closeMobileMenu() {
  mobileMenu?.classList.remove('open');
  mobileOverlay?.classList.remove('open');
  document.body.style.overflow = '';
  mobileMenuBtn?.setAttribute('aria-expanded', 'false');
}
mobileMenuClose?.addEventListener('click', closeMobileMenu);
mobileOverlay?.addEventListener('click', closeMobileMenu);
mobileMenu?.querySelectorAll('a').forEach(link => { link.addEventListener('click', closeMobileMenu); });

// Nav scroll effect
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) nav.classList.add('scrolled');
  else nav.classList.remove('scrolled');
}, { passive: true });

// Smooth scroll for anchors
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href');
    if (targetId === '#') return;
    const target = document.querySelector(targetId);
    if (target) {
      e.preventDefault();
      const navHeight = nav.offsetHeight;
      const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight;
      window.scrollTo({ top: targetPosition, behavior: 'smooth' });
    }
  });
});

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

console.log('Международная палата личности — Modern site initialized with ' + galleryData.length + ' curated images');
</script>
</body>
</html>
'''
    return html

if __name__ == "__main__":
    output_path = Path(r"D:\PALATA\index.html")
    html_content = generate_html()
    output_path.write_text(html_content, encoding='utf-8')
    print(f"Generated: {output_path}")
    print(f"Size: {len(html_content):,} characters")
    print(f"Curated images: {len(CURATED_GALLERY)}")
    cats = sorted(set(item['category'] for item in CURATED_GALLERY))
    print(f"Categories: {cats}")