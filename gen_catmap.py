with open('data/gallery.json', 'rb') as f:
    content = f.read()
decoded = content.decode('utf-8')
import json
data = json.loads(decoded)

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

cat_map = {}
for item in data['gallery']:
    if item['file'] in CURATED_FILES:
        cat_map[item['category']] = item['category']

def esc_for_source(s):
    result = []
    for c in s:
        o = ord(c)
        if o > 127:
            result.append('\\u{:04x}'.format(o))
        else:
            result.append(c)
    return ''.join(result)

lines = ['CATEGORY_MAP = {']
for k, v in cat_map.items():
    lines.append('    "{}": "{}",'.format(esc_for_source(k), esc_for_source(v)))
lines.append('}')

with open('cat_map_fixed.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written cat_map_fixed.py')
with open('cat_map_fixed.py', 'r', encoding='utf-8') as f:
    print(f.read())