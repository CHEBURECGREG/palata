#!/usr/bin/env python3
"""
Generator script for the reimagined PALATA single-page site.
Parses gallery.html for image data, curates content, and outputs index.html.
"""

import json
from pathlib import Path

# ============================================================
# SOURCE DATA: Load clean curated data from curated_data.json
# (extracted from gallery.html with proper UTF-8 decoding)
# ============================================================

BASE_URL = "https://xn----7sbaa5baqdtkc7agh5e.xn--p1ai/wp-content/uploads/2024/10/"

with open(Path(r"D:\PALATA\curated_data.json"), "r", encoding="utf-8") as f:
    CURATED_GALLERY = json.load(f)

# ============================================================
# CONTENT: Aphorisms, copy, historical hook
# ============================================================

APHORISMS = [
    {
        "text": "Слава — тень добродетели",
        "author": "Цицерон",
        "note": "Настоящая слава следует за делом, а не гонится за ним"
    },
    {
        "text": "Жажда славы — это признак величия души",
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
        "note": "Орден — это не билет в будущее, а квитанция из прошлого"
    },
    {
        "text": "Кто не рискует своим именем, не достоин им владеть",
        "author": "",
        "note": "Имя — это не ярлык. Это контракт с историей"
    },
]

# TikTok-style Table of Ranks historical hook
TABLE_OF_RANKS_HOOK = {
    "title": "Табель о рангах: как Imperio строил идеальную méritократию",
    "sections": [
        {
            "headline": "1722 год. Петр I подписывает документ, который перевернул понимание статуса в России на 200 лет вперёд.",
            "body": "До Табеля о рангах — хаос. Князь мог быть ничем, дворянин — ничтожеством, а талантливый сын кубария — навсегда застрять внизу. Петр ввёл жёсткую систему: 14 классов (рангов), жёстко привязанных к военной, гражданской и придворной службе. Всё — до запятой. Кто есть кто, кому что положено, какая карета, какой лакей, какой ряд в храме. Никакой «блин, я князь, а вы кто?». Есть ранг — есть права. Нет ранга — сиди тихо."
        },
        {
            "headline": "Князь ≠ Ранг. Это главная ловушка.",
            "body": "Титул «князь» в Российской империи — это часто просто родовое звание (как фамилия, только помпезнее). А реальная власть, доступ кцарю, земля, крестьяне, почет — всё это давали не кровь, а *служба*. Князь без ранга — просто красивое имя в списке гостей. А подпоручик 14 класса, пробившийся до полковника (6 класс) — уже личный дворянин, а через шаг — наследственный. И вот он уже решает судьбы губерний."
        },
        {
            "headline": "Почему это круто сейчас?",
            "body": "Потому что Табель — это первый в истории масштабный *skill tree* для целой нации. Чёткие уровни. Прозрачные правила апгрейда. Никаких «знает кого-то». Хочешь статус — отслужи. Хочешь знать — учись. Хочешь орден — сделай подвиг. Это геймификация социального лифта в чистом виде. И именно эту логику — «сделал → получил → зафиксировал» — мы переносим в современный формат наград. Без приворотов. Без связей. Только merit."
        }
    ]
}

# Hero/mission copy
HERO_COPY = {
    "tagline": "Международная палата личности",
    "subtitle": "Ордены. Честь. Масштаб личности.",
    "mission": "Мы не раздаём медали за красивые глаза. Мы фиксируем моменты, когда человек преодолел себя. Когда амбиция встретилась с действием. Когда имя стало историей."
}

ABOUT_COPY = {
    "title": "Что такое Палата — за 30 секунд",
    "bullets": [
        "Международная общественная организация, объединяющая кавалеров орденов и наград",
        "Ведём орденскую хронику: каждая награда — документ, каждая церемония — факт истории",
        "10+ лет работы, 100+ кавалеров, 10+ стран — география от Сиэтла до Одессы, от Токио до Стокгольма",
        "Патриарх Кирилл, Императорский дом, главы государств и регионов — те, кто знает цену чести, стоят с нами",
        "Не коммерция. Не политика. Только признание заслуг и сохранение памяти о тех, кто меняет мир"
    ]
}

CONTACT_INFO = {
    "address": "191014, Санкт-Петербург, ул. Маяковского, 19/29",
    "addressee": "Палате Личности, Малыхин Юрию",
    "chairman": "Председатель: Юрий Малыхин"
}

# ============================================================
# HTML GENERATION
# ============================================================

def generate_html():
    html = '''<!DOCTYPE html>
<html lang="ru-RU" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0A0A0F">
<title>Международная палата личности — Ордены. Честь. Масштаб.</title>
<meta name="description" content="Официальный сайт Международной палаты личности. Орденные награды, церемонии, история Табеля о рангах, кавалеры. Признание заслуг без политики и коммерции.">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏅</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  theme: {
    extend: {
      colors: {
        void: '#0D0D12',
        'void-soft': '#14141A',
        'void-card': '#1A1A22',
        'void-border': '#2A2A35',
        slate: '#4A5568',
        'slate-light': '#8B9AA8',
        gold: '#E8B82E',
        'gold-light': '#F0C84D',
        'gold-dim': '#C8A020',
        pearl: '#F5F0E8',
        'pearl-soft': '#D4C9B8',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
        serif: ['Playfair Display', 'Georgia', 'serif'],
      },
      fontSize: {
        'display-xl': ['clamp(3rem, 8vw, 5.5rem)', { lineHeight: '1.02', letterSpacing: '-0.03em' }],
        'display-lg': ['clamp(2.5rem, 6vw, 4rem)', { lineHeight: '1.05', letterSpacing: '-0.02em' }],
        'display-md': ['clamp(1.75rem, 4vw, 2.5rem)', { lineHeight: '1.1', letterSpacing: '-0.01em' }],
        'body-lg': ['1.125rem', { lineHeight: '1.8' }],
        'body-base': ['1rem', { lineHeight: '1.7' }],
        'caption': ['0.8125rem', { lineHeight: '1.6', letterSpacing: '0.02em' }],
      },
      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
        '26': '6.5rem',
        '30': '7.5rem',
      },
      boxShadow: {
        'premium': '0 25px 50px -12px rgba(0, 0, 0, 0.5)',
        'premium-hover': '0 35px 70px -15px rgba(0, 0, 0, 0.6)',
        'gold-glow': '0 0 40px rgba(212, 168, 42, 0.18)',
        'gold-glow-strong': '0 0 60px rgba(212, 168, 42, 0.3)',
        'inner-gold': 'inset 0 1px 0 rgba(212, 168, 42, 0.15)',
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
        '3xl': '2rem',
        '4xl': '3rem',
      },
      transitionTimingFunction: {
        'premium': 'cubic-bezier(0.22, 1, 0.36, 1)',
        'snappy': 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
      backgroundImage: {
        'gold-gradient': 'linear-gradient(135deg, #E8B82E 0%, #F0C84D 50%, #E8B82E 100%)',
        'void-gradient': 'radial-gradient(ellipse at 50% 0%, rgba(232, 184, 46, 0.1) 0%, transparent 60%)',
      }
    }
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap');

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  background-color: #0D0D12;
  color: #F5F0E8;
  font-feature-settings: "cv02", "cv03", "cv04", "cv11";
  scroll-behavior: smooth;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* ===== CUSTOM UTILITIES ===== */
.glass-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

.glass-card:hover {
  transform: translateY(-6px);
  border-color: rgba(232, 184, 46, 0.4);
  box-shadow: 0 35px 70px -15px rgba(0, 0, 0, 0.4), 0 0 40px rgba(232, 184, 46, 0.15);
}

.glass-strong {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
}

.text-gradient-gold {
  background: linear-gradient(135deg, #E8B82E 0%, #F5E6A0 50%, #E8B82E 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-gradient-pearl {
  background: linear-gradient(135deg, #F5F0E8 0%, #D4C9B8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.nav-glass {
  background: rgba(13, 13, 18, 0.8);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.btn-primary {
  background: linear-gradient(135deg, #E8B82E 0%, #F0C84D 100%);
  color: #0D0D12;
  font-weight: 600;
  transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 40px -10px rgba(232, 184, 46, 0.35);
}

.btn-primary:active { transform: translateY(0); }

.btn-ghost {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #F5F0E8;
  transition: all 0.3s cubic-bezier(0.22, 1, 0.36, 1);
}

.btn-ghost:hover {
  border-color: rgba(232, 184, 46, 0.5);
  background: rgba(232, 184, 46, 0.1);
  color: #F0C84D;
}

.divider-gold {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(232, 184, 46, 0.4), transparent);
}

.divider-gold-short {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #E8B82E, #F0C84D);
  border-radius: 2px;
}

/* ===== ANIMATIONS ===== */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideInRight {
  from { opacity: 0; transform: translateX(20px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes pulseGlow {
  0%, 100% { box-shadow: 0 0 30px rgba(232, 184, 46, 0.2); }
  50% { box-shadow: 0 0 50px rgba(232, 184, 46, 0.35); }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.animate-fade-in-up {
  animation: fadeInUp 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  opacity: 0;
}

.animate-fade-in {
  animation: fadeIn 0.6s ease forwards;
  opacity: 0;
}

.animate-slide-in-right {
  animation: slideInRight 0.6s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  opacity: 0;
}

.stagger-1 { animation-delay: 80ms; }
.stagger-2 { animation-delay: 160ms; }
.stagger-3 { animation-delay: 240ms; }
.stagger-4 { animation-delay: 320ms; }
.stagger-5 { animation-delay: 400ms; }
.stagger-6 { animation-delay: 480ms; }

/* Reveal on scroll */
.reveal { opacity: 0; transform: translateY(24px); transition: all 0.8s cubic-bezier(0.22, 1, 0.36, 1); }
.reveal.visible { opacity: 1; transform: translateY(0); }

/* Focus visible */
*:focus-visible {
  outline: 2px solid #E8B82E;
  outline-offset: 3px;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #0D0D12; }
::-webkit-scrollbar-thumb { background: #2A2A35; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #E8B82E; }

/* Selection */
::selection { background: rgba(232, 184, 46, 0.3); color: #F5F0E8; }

/* Lightbox */
.lightbox {
  position: fixed; inset: 0; z-index: 10000;
  background: rgba(13, 13, 18, 0.98);
  backdrop-filter: blur(8px);
  display: none; align-items: center; justify-content: center;
  padding: 2rem; opacity: 0; transition: opacity 0.3s ease;
}

.lightbox.open { display: flex; opacity: 1; }

.lightbox-content {
  position: relative; max-width: 90vw; max-height: 85vh;
  display: flex; flex-direction: column; align-items: center;
  transform: scale(0.92); transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1);
}

.lightbox.open .lightbox-content { transform: scale(1); }

.lightbox-img { max-width: 100%; max-height: 75vh; border-radius: 1rem; box-shadow: 0 40px 80px -20px rgba(0,0,0,0.7); object-fit: contain; }

.lightbox-caption {
  margin-top: 1.5rem; color: #D4C9B8; font-size: 1.125rem;
  font-family: 'Playfair Display', serif; font-style: italic;
  text-align: center; max-width: 700px; line-height: 1.7;
}

.lightbox-close, .lightbox-prev, .lightbox-next {
  width: 52px; height: 52px; border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.15);
  background: rgba(13, 13, 18, 0.85); color: #F5F0E8;
  display: flex; align-items: center; justify-content: center;
  backdrop-filter: blur(8px); transition: all 0.2s ease;
}

.lightbox-close { position: absolute; top: -70px; right: 0; }
.lightbox-prev { position: absolute; top: 50%; left: -80px; transform: translateY(-50%); }
.lightbox-next { position: absolute; top: 50%; right: -80px; transform: translateY(-50%); }

.lightbox-close:hover, .lightbox-prev:hover, .lightbox-next:hover {
  background: rgba(232, 184, 46, 0.2); border-color: #E8B82E; color: #F0C84D;
}

@media (max-width: 1024px) {
  .lightbox-prev { left: 1rem; }
  .lightbox-next { right: 1rem; }
  .lightbox-close { top: -65px; right: 0; }
}

.lightbox-counter {
  position: absolute; bottom: -55px; left: 50%; transform: translateX(-50%);
  color: #64748B; font-size: 0.8125rem; font-weight: 500; letter-spacing: 0.05em;
}

/* Category filter pills */
.filter-pill {
  padding: 0.5rem 1.125rem; border-radius: 9999px;
  font-size: 0.8125rem; font-weight: 500; letter-spacing: 0.02em;
  transition: all 0.25s cubic-bezier(0.22, 1, 0.36, 1);
  border: 1px solid transparent; background: transparent; color: #8B9AA8;
  white-space: nowrap;
}

.filter-pill:hover { color: #F5F0E8; border-color: rgba(255,255,255,0.2); background: rgba(255,255,255,0.04); }

.filter-pill.active {
  background: linear-gradient(135deg, #E8B82E 0%, #F0C84D 100%);
  color: #0D0D12; border-color: #E8B82E;
  box-shadow: 0 4px 20px -4px rgba(232, 184, 46, 0.4);
}

/* Gallery grid */
.gallery-grid {
  display: grid; grid-template-columns: repeat(1, 1fr); gap: 1.25rem;
}

@media (min-width: 640px) { .gallery-grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .gallery-grid { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 1440px) { .gallery-grid { grid-template-columns: repeat(4, 1fr); } }

/* Aphorism cards */
.aphorism-card {
  background: linear-gradient(145deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0.02) 100%);
  border: 1px solid rgba(255,255,255,0.06);
  border-left: 3px solid transparent;
  background-image: linear-gradient(145deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02)), linear-gradient(180deg, #E8B82E, #F0C84D);
  background-origin: border-box;
  background-clip: padding-box, border-box;
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

.aphorism-card:hover {
  border-left-color: #E8B82E;
  background-color: rgba(232, 184, 46, 0.05);
  transform: translateX(4px);
}

/* TikTok card */
.tiktok-card {
  background: linear-gradient(160deg, #14141A 0%, #1A1A22 100%);
  border: 1px solid rgba(232, 184, 46, 0.2);
  position: relative; overflow: hidden;
}

.tiktok-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #E8B82E, #F0C84D, #E8B82E);
  background-size: 200% 100%; animation: goldShift 3s linear infinite;
}

@keyframes goldShift { 0% { background-position: 0% 50%; } 100% { background-position: 200% 50%; } }

/* Stats counter */
.stat-number {
  font-family: 'Playfair Display', serif; font-weight: 600;
  background: linear-gradient(135deg, #F0C84D 0%, #E8B82E 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

/* Mobile menu */
.mobile-menu { transform: translateX(100%); transition: transform 0.4s cubic-bezier(0.22, 1, 0.36, 1); }
.mobile-menu.open { transform: translateX(0); }
.mobile-overlay { opacity: 0; pointer-events: none; transition: opacity 0.3s ease; }
.mobile-overlay.open { opacity: 1; pointer-events: auto; }

/* Accessibility mode */
body[data-accessibility="true"] {
  background: #FFFFFF !important; color: #000000 !important;
}
body[data-accessibility="true"] .glass-card,
body[data-accessibility="true"] .nav-glass,
body[data-accessibility="true"] .tiktok-card,
body[data-accessibility="true"] .aphorism-card {
  background: #FFFFFF !important; border: 2px solid #000 !important; backdrop-filter: none !important;
}
body[data-accessibility="true"] .btn-primary { background: #000 !important; color: #FFF !important; }
body[data-accessibility="true"] .btn-ghost { border-color: #000 !important; color: #000 !important; }
body[data-accessibility="true"] .text-gradient-gold,
body[data-accessibility="true"] .text-gradient-pearl,
body[data-accessibility="true"] .stat-number { -webkit-text-fill-color: #000 !important; color: #000 !important; }
body[data-accessibility="true"] .filter-pill { border-color: #000 !important; color: #000 !important; }
body[data-accessibility="true"] .filter-pill.active { background: #000 !important; color: #FFF !important; }
body[data-accessibility="true"] * { animation: none !important; transition: none !important; }

/* Print */
@media print {
  .nav-glass, .mobile-menu-btn, .lightbox, .filter-pill, .btn-primary, .btn-ghost { display: none !important; }
  body { background: #FFF !important; color: #000 !important; }
  .glass-card { border: 1px solid #CCC !important; background: #FFF !important; box-shadow: none !important; }
}

</style>
</head>
<body class="bg-void text-pearl antialiased min-h-screen flex flex-col">

<!-- Skip link -->
<a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-gold focus:text-void focus:rounded focus:font-semibold">Перейти к основному содержимому</a>

<!-- Navigation -->
<nav id="main-nav" class="fixed top-0 left-0 right-0 z-50 nav-glass">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <!-- Brand -->
      <a href="#top" class="flex items-center gap-3 group" aria-label="Международная палата личности — главная">
        <span class="w-10 h-10 rounded-xl bg-gradient-to-br from-gold to-gold-light flex items-center justify-center text-void font-bold text-lg group-hover:scale-105 transition-transform duration-300" aria-hidden="true">🏅</span>
        <span class="text-xl font-serif font-semibold text-pearl leading-tight group-hover:text-gold transition-colors duration-300 hidden sm:block">Международная палата личности</span>
      </a>

      <!-- Desktop nav -->
      <div class="hidden md:flex items-center gap-10">
        <a href="#about" class="text-sm font-medium text-slate-light hover:text-gold transition-colors duration-200">О Палате</a>
        <a href="#aphorisms" class="text-sm font-medium text-slate-light hover:text-gold transition-colors duration-200">Философия</a>
        <a href="#history" class="text-sm font-medium text-slate-light hover:text-gold transition-colors duration-200">История</a>
        <a href="#gallery" class="text-sm font-medium text-slate-light hover:text-gold transition-colors duration-200">Галерея</a>
        <a href="#contacts" class="text-sm font-medium text-slate-light hover:text-gold transition-colors duration-200">Контакты</a>
      </div>

      <!-- Controls -->
      <div class="flex items-center gap-2">
        <button id="access-toggle" class="p-2.5 rounded-xl text-slate-light hover:text-pearl transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gold focus:ring-offset-2 focus:ring-offset-void border border-gold/20" aria-label="Версия для слабовидящих" title="Доступность">
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
        </button>
        <button id="mobile-menu-btn" class="md:hidden p-2.5 rounded-xl text-slate-light hover:text-pearl transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gold focus:ring-offset-2 focus:ring-offset-void" aria-label="Открыть меню" aria-expanded="false">
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>
        </button>
      </div>
    </div>
  </div>
</nav>

<!-- Mobile menu panel -->
<div id="mobile-menu" class="mobile-menu fixed inset-0 z-40 bg-void/98 backdrop-blur-md lg:hidden">
  <div class="flex flex-col h-full pt-14 pb-8 px-6">
    <div class="flex items-center justify-between mb-10 border-b border-white/10 pb-6">
      <a href="#top" class="flex items-center gap-3">
        <span class="w-10 h-10 rounded-xl bg-gradient-to-br from-gold to-gold-light flex items-center justify-center text-void font-bold text-lg">🏅</span>
        <span class="text-lg font-serif font-bold text-pearl">Международная палата личности</span>
      </a>
      <button id="mobile-menu-close" class="text-slate-light hover:text-pearl transition-colors" aria-label="Закрыть меню">
        <svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
    </div>
    <nav class="flex-1 space-y-3">
      <a href="#about" class="block px-4 py-4 rounded-2xl text-base font-medium text-slate-light hover:text-pearl hover:bg-white/5 transition-all duration-200">О Палате</a>
      <a href="#aphorisms" class="block px-4 py-4 rounded-2xl text-base font-medium text-slate-light hover:text-pearl hover:bg-white/5 transition-all duration-200">Философия</a>
      <a href="#history" class="block px-4 py-4 rounded-2xl text-base font-medium text-slate-light hover:text-pearl hover:bg-white/5 transition-all duration-200">История (Табель о рангах)</a>
      <a href="#gallery" class="block px-4 py-4 rounded-2xl text-base font-medium text-slate-light hover:text-pearl hover:bg-white/5 transition-all duration-200">Галерея</a>
      <a href="#contacts" class="block px-4 py-4 rounded-2xl text-base font-medium text-slate-light hover:text-pearl hover:bg-white/5 transition-all duration-200">Контакты</a>
    </nav>
    <div class="mt-auto space-y-3 border-t border-white/10 pt-6">
      <button id="mobile-access-toggle" class="w-full flex items-center justify-between px-4 py-4 rounded-2xl text-base font-medium text-slate-light hover:text-pearl hover:bg-white/5 transition-all duration-200 border border-gold/20">
        <span>Версия для слабовидящих</span>
        <svg class="w-5 h-5 text-slate-light" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
      </button>
    </div>
  </div>
</div>

<div id="mobile-menu-overlay" class="mobile-overlay fixed inset-0 z-30 bg-black/80 backdrop-blur-sm lg:hidden"></div>

<!-- ============================================
     MAIN CONTENT
     ============================================ -->
<main id="main-content" class="flex-1 pt-16">

<!-- ----- HERO ----- -->
<section id="top" class="relative min-h-[90vh] flex items-center justify-center overflow-hidden">
  <!-- Background atmosphere -->
  <div class="absolute inset-0 -z-20 bg-void-gradient"></div>
  <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[900px] h-[900px] rounded-full bg-gold/5 blur-[150px] -translate-y-1/4 animate-float" aria-hidden="true"></div>
  <div class="absolute bottom-0 right-1/4 w-[600px] h-[600px] rounded-full bg-slate/5 blur-[120px] translate-y-1/3" aria-hidden="true"></div>
  <div class="absolute inset-0 -z-10" aria-hidden="true">
    <svg width="100%" height="100%" viewBox="0 0 1440 900" preserveAspectRatio="none">
      <defs>
        <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
          <path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(232,184,46,0.04)" stroke-width="0.5"/>
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill="url(#grid)"/>
    </svg>
  </div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 py-20">
    <div class="text-center max-w-4xl mx-auto">
      <!-- Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 mb-8 animate-fade-in-up">
        <span class="w-2 h-2 rounded-full bg-gold animate-pulse"></span>
        <span class="text-caption font-medium text-gold tracking-wider uppercase">Официальный ресурс · منذ 2014</span>
      </div>

      <!-- Main headline -->
      <h1 class="text-display-xl font-serif font-bold text-pearl tracking-tight leading-tight mb-6 animate-fade-in-up stagger-1">
        Международная<br><span class="text-gradient-gold">палата личности</span>
      </h1>

      <!-- Subtitle -->
      <p class="text-display-md font-serif font-normal text-pearl-soft leading-relaxed mb-10 animate-fade-in-up stagger-2 max-w-2xl mx-auto">
        Ордены. Честь. Масштаб личности.
      </p>

      <!-- Mission statement -->
      <div class="glass-strong rounded-3xl p-6 md:p-8 mb-12 animate-fade-in-up stagger-3 max-w-2xl mx-auto border border-white/10">
        <p class="text-body-lg text-pearl-soft leading-relaxed font-light italic">
          "Мы не раздаём медали за красивые глаза. Мы фиксируем моменты, когда человек преодолел себя. Когда амбиция встретилась с действием. Когда имя стало историей."
        </p>
      </div>

      <!-- CTA buttons -->
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 animate-fade-in-up stagger-4">
        <a href="#gallery" class="btn-primary px-10 py-4 rounded-2xl text-lg flex items-center justify-center gap-2 w-full sm:w-auto">
          Открыть галерею наград
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
        </a>
        <a href="#about" class="btn-ghost px-10 py-4 rounded-2xl text-lg flex items-center justify-center gap-2 w-full sm:w-auto">
          О Палате
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 3a1 1 0 011-1h14a1 1 0 011 1v16a1 1 0 01-1 1H5a1 1 0 01-1-1V3zM4 7l16 0" /></svg>
        </a>
      </div>

      <!-- Scroll indicator -->
      <div class="absolute bottom-8 left-1/2 -translate-x-1/2 animate-fade-in stagger-5" aria-hidden="true">
        <svg class="w-6 h-6 text-slate-light animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" /></svg>
      </div>
    </div>
  </div>
</section>

<!-- ----- ABOUT / STATS ----- -->
<section id="about" class="py-22 lg:py-30 bg-void-soft/50 border-y border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-[1fr_1.2fr] gap-16 items-start">
      <!-- Left: About text -->
      <div class="reveal space-y-8">
        <div class="inline-flex items-center gap-3 px-4 py-1.5 rounded-full bg-white/5 border border-white/10">
          <span class="text-caption font-medium text-gold tracking-wider uppercase">О Палате</span>
        </div>
        <h2 class="text-display-lg font-serif font-bold text-pearl tracking-tight leading-tight">Что такое Палата — за 30 секунд</h2>
        <div class="divider-gold-short"></div>
        <p class="text-body-lg text-pearl-soft leading-relaxed">
          Международная общественная организация, объединяющая кавалеров орденов и наград. Не коммерция. Не политика. Только признание заслуг и сохранение памяти о тех, кто меняет мир.
        </p>

        <ul class="space-y-4" role="list">
'''

    for i, bullet in enumerate(ABOUT_COPY["bullets"]):
        html += f'''          <li class="flex items-start gap-4 text-body-base text-pearl-soft reveal" style="transition-delay: {100 + i * 80}ms">
            <span class="w-8 h-8 rounded-xl bg-gold/10 flex items-center justify-center flex-shrink-0 mt-0.5" aria-hidden="true">
              <svg class="w-5 h-5 text-gold" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
            </span>
            <span>{bullet}</span>
          </li>
'''

    html += '''        </ul>
      </div>

      <!-- Right: Stats cards -->
      <div class="grid sm:grid-cols-2 gap-4 reveal" style="transition-delay: 200ms">
'''

    stats = [
        {"num": "10+", "label": "Лет работы", "icon": "📅"},
        {"num": "100+", "label": "Кавалеров", "icon": "🏅"},
        {"num": "10+", "label": "Стран", "icon": "🌍"},
        {"num": "∞", "label": "Уважения", "icon": "♾️"},
    ]

    for i, stat in enumerate(stats):
        html += f'''        <article class="glass-card rounded-3xl p-6 md:p-8 text-center group" style="transition-delay: {i * 80}ms">
          <div class="text-4xl mb-3" aria-hidden="true">{stat["icon"]}</div>
          <div class="stat-number text-4xl md:text-5xl lg:text-6xl font-bold mb-2">{stat["num"]}</div>
          <div class="text-sm font-medium text-slate-light uppercase tracking-wider">{stat["label"]}</div>
          <div class="divider-gold-short mx-auto mt-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </article>
'''

    html += '''      </div>
    </div>

    <!-- Chairman card -->
    <div class="reveal mt-16" style="transition-delay: 400ms">
      <div class="glass-strong rounded-4xl p-8 md:p-12 relative overflow-hidden group">
        <div class="absolute inset-0 bg-gradient-to-tr from-gold/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
        <div class="relative z-10 grid md:grid-cols-3 gap-8 items-center">
          <div class="md:col-span-1">
            <div class="w-24 h-24 md:w-32 md:h-32 rounded-2xl bg-gradient-to-br from-gold to-gold-light flex items-center justify-center mx-auto md:mx-0" aria-hidden="true">
              <span class="text-4xl md:text-6xl font-bold text-void">🏅</span>
            </div>
          </div>
          <div class="md:col-span-2 text-center md:text-left space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gold/10 border border-gold/20 text-gold text-caption font-semibold uppercase tracking-wider">Председатель Палаты</div>
            <h3 class="text-2xl md:text-3xl font-serif font-bold text-pearl">Юрий Малыхин</h3>
            <p class="text-body-base text-pearl-soft">Основатель и идеолог Палаты. Делает честь и награды понятными, прозрачными и достойными для нового поколения.</p>
            <div class="flex flex-wrap items-center justify-center md:justify-start gap-3 mt-6">
              <span class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-sm font-medium text-pearl-soft">10+ лет миссии</span>
              <span class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-sm font-medium text-pearl-soft">Международное признание</span>
              <span class="px-4 py-2 rounded-xl bg-gold/10 border border-gold/30 text-sm font-semibold text-gold">Честность ante omnia</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ----- APHORISMS / PHILOSOPHY ----- -->
<section id="aphorisms" class="py-22 lg:py-30">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-16 reveal">
      <div class="inline-flex items-center gap-3 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 mb-6">
        <span class="text-caption font-medium text-gold tracking-wider uppercase">Философия</span>
      </div>
      <h2 class="text-display-lg font-serif font-bold text-pearl tracking-tight leading-tight mb-4">Афоризмы о чести, славе и награде</h2>
      <p class="text-body-lg text-pearl-soft">Не пафос. Не бюрократия. Твёрдые истины, проверенные веками. Читай — и бери на вооружение.</p>
    </div>

    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6" role="list">
'''

    for i, aph in enumerate(APHORISMS):
        html += f'''      <article class="aphorism-card rounded-3xl p-6 md:p-8 reveal group" role="listitem" style="transition-delay: {i * 100}ms">
        <blockquote class="text-body-lg font-serif font-medium text-pearl leading-relaxed mb-4">«{aph["text"]}»</blockquote>
'''

        if aph["author"]:
            html += f'''        <footer class="flex items-center gap-3 text-sm">
          <cite class="font-serif text-gold not-italic">{aph["author"]}</cite>
          <span class="w-12 h-px bg-gold/30"></span>
        </footer>
'''

        html += f'''        <p class="text-caption text-slate-light mt-4 leading-relaxed">{aph["note"]}</p>
      </article>
'''

    html += '''    </div>
  </div>
</section>

<!-- ----- TIKTOK-STYLE HISTORY: TABLE OF RANKS ----- -->
<section id="history" class="py-22 lg:py-30 bg-void-soft/30 border-y border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-16 reveal">
      <div class="inline-flex items-center gap-3 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 mb-6">
        <span class="text-caption font-medium text-gold tracking-wider uppercase">История · TikTok-format</span>
      </div>
      <h2 class="text-display-lg font-serif font-bold text-pearl tracking-tight leading-tight mb-4">{TABLE_OF_RANKS_HOOK["title"]}</h2>
      <p class="text-body-lg text-pearl-soft">Почему система Петра I всё ещё круче любого современного HR-бренда.</p>
    </div>

    <div class="space-y-8" role="list">
'''

    for i, section in enumerate(TABLE_OF_RANKS_HOOK["sections"]):
        html += f'''      <article class="tiktok-card rounded-4xl p-8 md:p-12 reveal group" role="listitem" style="transition-delay: {i * 150}ms">
        <div class="flex items-start gap-4 md:gap-8">
          <div class="w-14 h-14 md:w-16 md:h-16 rounded-2xl bg-gold/10 border border-gold/20 flex items-center justify-center flex-shrink-0 mt-1" aria-hidden="true">
            <span class="text-2xl md:text-3xl font-bold text-gold">{i + 1}</span>
          </div>
          <div class="flex-1 min-w-0">
            <h3 class="text-display-md font-serif font-bold text-pearl tracking-tight mb-4">{section["headline"]}</h3>
            <div class="prose prose-invert max-w-none text-body-base text-pearl-soft leading-relaxed space-y-4">
              <p>{section["body"]}</p>
            </div>
          </div>
        </div>
        <div class="divider-gold mt-8 opacity-50 group-hover:opacity-100 transition-opacity duration-500"></div>
      </article>
'''

    html += '''    </div>

    <!-- Bridge to modern awards -->
    <div class="reveal mt-12 text-center" style="transition-delay: 600ms">
      <div class="glass-strong rounded-4xl p-8 md:p-12 max-w-3xl mx-auto">
        <h3 class="text-display-md font-serif font-bold text-pearl tracking-tight mb-4">Именно эту логику мы перенесли в XXI век</h3>
        <p class="text-body-lg text-pearl-soft mb-6">Прозрачные критерии. Открытая хроника. Никаких «своих». Только merit — действие, зафиксированное орденом.</p>
        <a href="#gallery" class="btn-primary px-8 py-3 rounded-2xl text-lg inline-flex items-center gap-2">
          Увидеть, как это выглядит сейчас
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- ----- GALLERY ----- -->
<section id="gallery" class="py-22 lg:py-30">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-8 mb-12 reveal">
      <div>
        <div class="inline-flex items-center gap-3 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 mb-4">
          <span class="text-caption font-medium text-gold tracking-wider uppercase">Галерея</span>
        </div>
        <h2 class="text-display-lg font-serif font-bold text-pearl tracking-tight leading-tight">Награды, церемонии, история в деталях</h2>
        <p class="text-body-base text-pearl-soft mt-2 max-w-md">Курируемая подборка. Без «стены старых мужчин». Только регалии, знаки отличия и моменты, когда честь становилась видимой.</p>
      </div>
      <div class="reveal" style="transition-delay: 200ms">
        <span class="text-caption text-slate-light" id="gallery-counter">Показано <span id="visible-count">0</span> из {len(CURATED_GALLERY)}</span>
      </div>
    </div>

    <!-- Category filter -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-10 reveal" role="tablist" aria-label="Фильтр по категориям" style="transition-delay: 150ms">
'''

    categories = ["Все", "Ордена", "Церемонии", "Историческое", "Международное", "Патриарх", "Прочее"]
    for i, cat in enumerate(categories):
        active = 'active' if cat == "Все" else ''
        selected = 'true' if cat == "Все" else 'false'
        html += f'''      <button class="filter-pill {active}" data-filter="{cat}" role="tab" aria-selected="{selected}" aria-controls="gallery-grid">{cat}</button>
'''

    html += '''    </div>

    <!-- Gallery grid -->
    <div class="gallery-grid" id="gallery-grid" role="list" aria-label="Галерея наград">
'''

    for i, item in enumerate(CURATED_GALLERY):
        full_url = BASE_URL + item['file']
        stagger = (i % 6) + 1
        html += f'''      <article class="glass-card rounded-3xl overflow-hidden group cursor-pointer aspect-[4/5] reveal stagger-{stagger}" data-category="{item['category']}" role="listitem" tabindex="0" onclick="openLightbox({i})" onkeydown="if(event.key==='Enter'||event.key===' '){{event.preventDefault();openLightbox({i})}}">
        <div class="relative h-full bg-slate/20 overflow-hidden">
          <img src="{full_url}" alt="{item['alt']}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 500%22%3E%3Crect fill=%22%231A1A24%22 width=%22400%22 height=%22500%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 dominant-baseline=%22middle%22 text-anchor=%22middle%22 fill=%22%23334155%22 font-family=%22system-ui%22 font-size=%2214%22%3E%F0%9F%8F%85%3C/text%3E%3C/svg%22'">
          <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-all duration-500"></div>
          <div class="absolute bottom-0 left-0 w-full p-5 bg-gradient-to-t from-black/90 via-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
            <span class="text-sm font-medium text-pearl block truncate">{item['caption']}</span>
          </div>
          <span class="absolute top-3 left-3 px-3 py-1 rounded-full bg-gold/20 text-gold text-[10px] font-bold tracking-tighter uppercase border border-gold/30 backdrop-blur-sm">{item['category']}</span>
          <div class="absolute top-3 right-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
            <button class="w-10 h-10 rounded-full bg-void/80 backdrop-blur-sm border border-white/10 text-pearl flex items-center justify-center hover:bg-gold/20 hover:text-gold hover:border-gold/30 transition-all duration-200" aria-label="Открыть в полноэкранном режиме">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" /></svg>
            </button>
          </div>
        </div>
      </article>
'''

    html += '''    </div>

    <!-- Load more / CTA -->
    <div class="text-center mt-12 reveal" style="transition-delay: 300ms">
      <p class="text-body-base text-pearl-soft mb-4">В архиве Палаты — сотни уникальных снимков, документов и регалий.</p>
      <a href="gallery.html" class="btn-ghost px-8 py-3 rounded-2xl text-lg inline-flex items-center gap-2">
        Полная галерея на отдельной странице
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
      </a>
    </div>
  </div>
</section>

<!-- ----- CONTACTS ----- -->
<section id="contacts" class="py-22 lg:py-30 bg-void-soft/30 border-y border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-16 items-start">
      <!-- Left: Contact info -->
      <div class="reveal space-y-8">
        <div class="inline-flex items-center gap-3 px-4 py-1.5 rounded-full bg-white/5 border border-white/10">
          <span class="text-caption font-medium text-gold tracking-wider uppercase">Контакты</span>
        </div>
        <h2 class="text-display-lg font-serif font-bold text-pearl tracking-tight leading-tight">Свяжитесь с Палатой</h2>
        <div class="divider-gold-short"></div>
        <p class="text-body-lg text-pearl-soft leading-relaxed">Пишите, если хотите предложить кандидата на награду, узнать о партнёрстве или просто сказать: «Респект за миссию».</p>

        <div class="space-y-6 pt-4 border-t border-white/10">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-xl bg-gold/10 border border-gold/20 flex items-center justify-center flex-shrink-0" aria-hidden="true">
              <svg class="w-6 h-6 text-gold" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
            </div>
            <div>
              <h3 class="font-semibold text-pearl mb-1">Адрес</h3>
              <address class="text-pearl-soft not-italic text-body-base leading-relaxed">{CONTACT_INFO["address"]}<br>Адресат: {CONTACT_INFO["addressee"]}</address>
            </div>
          </div>

          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-xl bg-gold/10 border border-gold/20 flex items-center justify-center flex-shrink-0" aria-hidden="true">
              <svg class="w-6 h-6 text-gold" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
            </div>
            <div>
              <h3 class="font-semibold text-pearl mb-1">Руководство</h3>
              <p class="text-pearl-soft text-body-base">{CONTACT_INFO["chairman"]}</p>
            </div>
          </div>

          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-xl bg-gold/10 border border-gold/20 flex items-center justify-center flex-shrink-0" aria-hidden="true">
              <svg class="w-6 h-6 text-gold" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
            </div>
            <div>
              <h3 class="font-semibold text-pearl mb-1">Предложить candidatura</h3>
              <p class="text-pearl-soft text-body-base">Напишите на официальную почту Палаты с пометкой «Кандидат». Рассмотрим за 14 дней.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Right: Contact form / CTA card -->
      <div class="reveal" style="transition-delay: 200ms">
        <div class="glass-strong rounded-4xl p-8 md:p-12 h-full">
          <h3 class="text-display-md font-serif font-bold text-pearl tracking-tight mb-6">Хотите стать кавалером?</h3>
          <p class="text-body-lg text-pearl-soft mb-8">Нет анкет, нет взяток, нет связей. Есть только дела, которые говорят сами за себя. Если вы (или кто-то, кого вы знаете) сделали подвиг — мы его зафиксируем.</p>

          <div class="space-y-4">
            <button class="btn-primary w-full py-4 rounded-2xl text-lg font-semibold" onclick="window.open('mailto:palata@personalitet.org?subject=Кандидат%20на%20награду','_blank')">
              Предложить кандидата
            </button>
            <button class="btn-ghost w-full py-4 rounded-2xl text-lg font-semibold" onclick="window.open('https://t.me/palata_lichnosti','_blank')">
              Написать в Telegram
            </button>
          </div>

          <div class="mt-10 pt-8 border-t border-white/10">
            <p class="text-caption text-slate-light mb-4 uppercase tracking-wider">Партнёры и поддержка</p>
            <div class="flex flex-wrap items-center gap-4">
              <span class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-sm font-medium text-pearl-soft">Патриархия</span>
              <span class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-sm font-medium text-pearl-soft">Императорский дом</span>
              <span class="px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-sm font-medium text-pearl-soft">Гос. структуры</span>
              <span class="px-4 py-2 rounded-xl bg-gold/10 border border-gold/30 text-sm font-semibold text-gold">Международныеorgs</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

</main>

<!-- ----- FOOTER ----- -->
<footer class="border-t border-white/10 bg-void/50 py-12 lg:py-16 backdrop-blur-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <span class="w-10 h-10 rounded-xl bg-gradient-to-br from-gold to-gold-light flex items-center justify-center text-void font-bold text-lg" aria-hidden="true">🏅</span>
        <span class="text-xl font-serif font-bold text-pearl">«Международная палата личности»</span>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-6 text-sm text-slate-light">
        <a href="#about" class="hover:text-pearl transition-colors">О Палате</a>
        <a href="#aphorisms" class="hover:text-pearl transition-colors">Философия</a>
        <a href="#history" class="hover:text-pearl transition-colors">История</a>
        <a href="#gallery" class="hover:text-pearl transition-colors">Галерея</a>
        <a href="#contacts" class="hover:text-pearl transition-colors">Контакты</a>
      </div>

      <div class="text-xs text-slate-light/60">
      </div>
    </div>
  </div>
</footer>

<!-- ----- LIGHTBOX ----- -->
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Полноэкранный просмотр изображения">
  <div class="lightbox-content">
    <button class="lightbox-close" id="lightbox-close" aria-label="Закрыть">
      <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
    </button>
    <button class="lightbox-prev" id="lightbox-prev" aria-label="Предыдущее изображение">
      <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 18l-6-6 6-6" /></svg>
    </button>
    <img class="lightbox-img" id="lightbox-img" alt="" src="" loading="lazy">
    <p class="lightbox-caption" id="lightbox-caption"></p>
    <span class="lightbox-counter" id="lightbox-counter"></span>
    <button class="lightbox-next" id="lightbox-next" aria-label="Следующее изображение">
      <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 18l6-6-6-6" /></svg>
    </button>
  </div>
</div>

<!-- ----- JAVASCRIPT ----- -->
<script>
// ============================================
// GALLERY DATA (embedded for lightbox)
// ============================================
const galleryData = [
'''

    for i, item in enumerate(CURATED_GALLERY):
        full_url = BASE_URL + item['file']
        html += f'''  {{"file": "{item['file']}", "alt": "{item['alt'].replace('"', '\\"')}", "caption": "{item['caption'].replace('"', '\\"')}", "full_url": "{full_url}", "category": "{item['category']}"}},
'''

    html += '''];

const BASE_URL = "https://xn----7sbaa5baqdtkc7agh5e.xn--p1ai/wp-content/uploads/2024/10/";

// ============================================
// LIGHTBOX SYSTEM
// ============================================
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

function prevImage() {
  currentIndex = (currentIndex - 1 + galleryData.length) % galleryData.length;
  updateLightbox();
}

function nextImage() {
  currentIndex = (currentIndex + 1) % galleryData.length;
  updateLightbox();
}

// Event listeners
lightboxClose.addEventListener('click', closeLightbox);
lightboxPrev.addEventListener('click', prevImage);
lightboxNext.addEventListener('click', nextImage);

// Close on background click
lightbox.addEventListener('click', (e) => {
  if (e.target === lightbox) closeLightbox();
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
  if (!lightbox.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') prevImage();
  if (e.key === 'ArrowRight') nextImage();
});

// ============================================
// CATEGORY FILTER
// ============================================
const filterButtons = document.querySelectorAll('.filter-pill');
const galleryItems = document.querySelectorAll('[data-category]');
const visibleCount = document.getElementById('visible-count');

function updateVisibleCount() {
  let count = 0;
  galleryItems.forEach(item => {
    if (item.style.display !== 'none') count++;
  });
  if (visibleCount) visibleCount.textContent = count;
}

filterButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;

    // Update active button
    filterButtons.forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-selected', 'false');
    });
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');

    // Filter items with animation
    galleryItems.forEach((item, i) => {
      const category = item.dataset.category;
      if (filter === 'Все' || category === filter) {
        item.style.display = 'block';
        item.style.animation = 'fadeInUp 0.5s cubic-bezier(0.22, 1, 0.36, 1) forwards';
        item.style.opacity = '1';
        item.style.transform = 'translateY(0)';
      } else {
        item.style.animation = 'fadeInUp 0.3s cubic-bezier(0.22, 1, 0.36, 1) reverse forwards';
        setTimeout(() => { item.style.display = 'none'; }, 300);
      }
    });

    setTimeout(updateVisibleCount, 350);
  });
});

// Initial count
setTimeout(updateVisibleCount, 100);

// ============================================
// ACCESSIBILITY TOGGLE
// ============================================
const ACCESS_KEY = 'palata-accessibility';
const accessToggle = document.getElementById('access-toggle');
const mobileAccessToggle = document.getElementById('mobile-access-toggle');

function setAccessibility(enabled) {
  if (enabled) {
    document.body.setAttribute('data-accessibility', 'true');
    document.body.classList.add('accessibility-mode');
    localStorage.setItem(ACCESS_KEY, 'true');
    updateAccessIcon(true);
  } else {
    document.body.removeAttribute('data-accessibility');
    document.body.classList.remove('accessibility-mode');
    localStorage.setItem(ACCESS_KEY, 'false');
    updateAccessIcon(false);
  }
}

function updateAccessIcon(enabled) {
  [accessToggle, mobileAccessToggle].forEach(btn => {
    if (btn) {
      if (enabled) {
        btn.classList.add('text-gold', 'ring-1', 'ring-gold', 'bg-white/10');
        btn.classList.remove('border-gold/20');
      } else {
        btn.classList.remove('text-gold', 'ring-1', 'ring-gold', 'bg-white/10');
        btn.classList.add('border-gold/20');
      }
    }
  });
}

accessToggle?.addEventListener('click', () => {
  const enabled = document.body.getAttribute('data-accessibility') === 'true';
  setAccessibility(!enabled);
});
mobileAccessToggle?.addEventListener('click', () => {
  const enabled = document.body.getAttribute('data-accessibility') === 'true';
  setAccessibility(!enabled);
});

// Restore accessibility preference
const savedAccess = localStorage.getItem(ACCESS_KEY);
if (savedAccess === 'true') {
  setAccessibility(true);
}

// ============================================
// MOBILE MENU
// ============================================
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenuClose = document.getElementById('mobile-menu-close');
const mobileMenu = document.getElementById('mobile-menu');
const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');

mobileMenuBtn?.addEventListener('click', () => {
  mobileMenu?.classList.add('open');
  mobileMenuOverlay?.classList.add('open');
  document.body.style.overflow = 'hidden';
  mobileMenuBtn.setAttribute('aria-expanded', 'true');
});

function closeMobileMenu() {
  mobileMenu?.classList.remove('open');
  mobileMenuOverlay?.classList.remove('open');
  document.body.style.overflow = '';
  mobileMenuBtn?.setAttribute('aria-expanded', 'false');
}

mobileMenuClose?.addEventListener('click', closeMobileMenu);
mobileMenuOverlay?.addEventListener('click', closeMobileMenu);

mobileMenu?.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', closeMobileMenu);
});

// ============================================
// SCROLL REVEAL (IntersectionObserver)
// ============================================
const revealElements = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
});

revealElements.forEach(el => revealObserver.observe(el));

// ============================================
// NAV SCROLL EFFECT
// ============================================
const nav = document.getElementById('main-nav');
let lastScroll = 0;
window.addEventListener('scroll', () => {
  const currentScroll = window.scrollY;
  if (currentScroll > 100) {
    nav.classList.add('bg-void/90', 'border-white/10');
    nav.classList.remove('bg-void/75');
  } else {
    nav.classList.remove('bg-void/90', 'border-white/10');
    nav.classList.add('bg-void/75');
  }
  lastScroll = currentScroll;
}, { passive: true });

// ============================================
// SMOOTH SCROLL FOR ANCHORS
// ============================================
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

console.log('Международная палата личности — Premium unified site initialized with ' + galleryData.length + ' curated images');
</script>
</body>
</html>
'''

    return html

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    output_path = Path(r"D:\PALATA\index.html")
    html_content = generate_html()
    output_path.write_text(html_content, encoding='utf-8')
    print(f"Generated: {output_path}")
    print(f"Size: {len(html_content):,} characters")
    print(f"Curated images: {len(CURATED_GALLERY)}")
    print("Categories represented:", sorted(set(item['category'] for item in CURATED_GALLERY)))