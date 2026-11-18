with open('D:/PALATA_NEW/index.html', 'rb') as f:
    content = f.read()

# Check for template literal artifacts
issues = []
if b'{esc(' in content:
    issues.append('Unescaped Python esc() calls found')
if b'{len(CURATED_GALLERY)}' in content:
    issues.append('Unescaped len() found')
if b'{ORG_' in content:
    issues.append('Unescaped ORG_ vars found')
if b'${' in content:
    issues.append('Unescaped JS template literals found')
if b'text-accent' not in content:
    issues.append('Missing text-accent class')

# Check content
checks = [
    ('ЯрСайт'.encode('utf-8'), 'Yarsite mention'),
    ('Константин'.encode('utf-8'), 'Konstantin'),
    (b'gold', 'Gold color'),
    (b'#E8B82E', 'Gold hex'),
    (b'🏅', 'Medal emoji'),
    (b'display-mega', 'Display mega'),
    (b'marquee', 'Marquee'),
    (b'rank-card', 'Rank cards'),
    (b'gallery__item', 'Gallery items'),
    (b'filter__btn', 'Filter tabs'),
    (b'stat__num', 'Stat numbers'),
    (b'lightbox', 'Lightbox'),
    (b'btn--primary', 'Primary buttons'),
    (b'footer__copy', 'Footer copy'),
    ('Создание сайта'.encode('utf-8'), 'Footer credit'),
]

print('=== ISSUES ===')
for issue in issues:
    print(f'FAIL: {issue}')
if not issues:
    print('OK: No template artifacts')

print()
print('=== CONTENT CHECKS ===')
for check, label in checks:
    found = check in content
    if 'Konstantin' in label or 'Gold' in label or 'Yarsite' in label or 'Footer credit' in label:
        if found:
            print(f'FAIL: {label} present')
        else:
            print(f'OK: {label} absent')
    else:
        if found:
            print(f'OK: {label} present')
        else:
            print(f'MISSING: {label}')

# Gallery count
import re
items = re.findall(b'gallery__item', content)
print(f'Gallery items: {len(items)}')

# File size
print(f'File size: {len(content):,} bytes')