import json
import re
from pathlib import Path

ROOT = Path(r'D:\PALATA_NEW')

with open(ROOT / 'data' / 'gallery.json', 'r', encoding='utf-8') as f:
    GALLERY_SOURCE = json.load(f)['gallery']

CURATED_FILES = [
    'whatsapp-image-2024-10-30-at-21.14.48-e1730375910347.jpeg',
    'whatsapp-image-2024-10-30-at-21.29.41-e1730376191532.jpeg',
    'whatsapp-image-2024-10-30-at-21.19.15.jpeg',
    'whatsapp-image-2024-10-30-at-21.20.44.jpeg',
    'whatsapp-image-2024-10-30-at-21.27.18.jpeg',
    'whatsapp-image-2024-10-30-at-22.06.26.jpeg',
    'whatsapp-image-2024-10-30-at-22.10.03.jpeg',
    'whatsapp-image-2024-10-30-at-21.31.30.jpeg',
    'whatsapp-image-2024-10-30-at-21.56.38.jpeg',
    'whatsapp-image-2024-10-30-at-22.48.21.jpeg',
    'whatsapp-image-2024-10-30-at-22.51.38.jpeg',
    'whatsapp-image-2024-10-30-at-21.36.43.jpeg',
    'whatsapp-image-2024-10-30-at-22.50.07-e1730377550353.jpeg',
    'whatsapp-image-2024-10-30-at-22.54.53.jpeg',
    'whatsapp-image-2024-10-30-at-21.38.53.jpeg',
    'whatsapp-image-2024-10-30-at-21.57.42.jpeg',
    'whatsapp-image-2024-10-30-at-22.01.23-e1730377363598.jpeg',
    'whatsapp-image-2024-10-30-at-21.44.24.jpeg',
]

CATEGORY_MAP = {}
for item in GALLERY_SOURCE:
    if item['file'] in CURATED_FILES:
        CATEGORY_MAP[item['category']] = item['category']

BASE_URL = 'https://xn----7sbaa5baqdtkc7agh5e.xn--p1ai/wp-content/uploads/2024/10/'

def is_konstantin(item):
    blob = ' '.join([item.get('file', ''), item.get('alt', ''), item.get('caption', ''), item.get('category', '')])
    return bool(re.search(r'\bКонстантин\b|\bКонстантина\b|\bКонстантину\b|Константину', blob, re.IGNORECASE))

CURATED_GALLERY = []
for item in GALLERY_SOURCE:
    if item['file'] not in CURATED_FILES:
        continue
    if is_konstantin(item):
        continue
    cat = CATEGORY_MAP.get(item['category'], item['category'])
    CURATED_GALLERY.append({
        'file': item['file'],
        'alt': item['alt'],
        'caption': item['caption'],
        'category': cat,
    })

print('Curated:', len(CURATED_GALLERY))

ORG = {
    'name': '«Международная палата личности»',
    'chairman': 'Малыхин Юрий Иванович',
    'established': '18 июня 1999 года, Санкт-Петербург',
    'address': '191014, Санкт-Петербург, ул. Маяковского, 19/29',
    'manufacturing': 'Ордена отчеканены на Государственном Монетном Дворе Санкт-Петербурга',
}

CONTACT_INFO = {
    'address': '191014, Санкт-Петербург, ул. Маяковского, 19/29',
    'addressee': 'Палате Личности, Малыхин Юрию',
    'chairman': 'Председатель: Юрий Малыхин',
}

def esc(s):
    return str(s).replace('&', '&').replace('<', '<').replace('>', '>').replace('"', '"')

ORG_NAME = esc(ORG['name'])
ORG_CHAIRMAN = esc(ORG['chairman'])
ORG_ADDRESS = esc(ORG['address'])
ORG_ADDRESSEE = esc(CONTACT_INFO['addressee'])
ORG_MANUFACTURING = esc(ORG['manufacturing'])
ORG_ESTABLISHED = esc(ORG['established'])

print('ORG_ADDRESS:', repr(ORG_ADDRESS))
print('ORG_ADDRESSEE:', repr(ORG_ADDRESSEE))
print('ORG_CHAIRMAN:', repr(ORG_CHAIRMAN))

# Now test the f-string
html = f'''
<address>{ORG_ADDRESS}<br>АДРЕСАТ: {ORG_ADDRESSEE}</address>
<div>{ORG_CHAIRMAN}</div>
'''

print('Generated:')
print(html)