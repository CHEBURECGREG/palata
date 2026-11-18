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

print('=== ISSUES ===')
for issue in issues:
    print('FAIL: ' + issue)
if not issues:
    print('OK: No template artifacts')

# Check content
yarsite = 'ЯрСайт'.encode('utf-8')
konstantin = 'Константин'.encode('utf-8')
sozdanie = 'Создание сайта'.encode('utf-8')
gold_hex = b'#E8B82E'

checks = [
    (yarsite, 'Yarsite mention'),
    (konstantin, 'Konstantin'),
    (sozdanie, 'Footer credit'),
    (gold_hex, 'Gold hex'),
    (b'display-mega', 'Display mega'),
    (b'marquee', 'Marquee'),
    (b'rank-card', 'Rank cards'),
    (b'gallery__item', 'Gallery items'),
    (b'filter__btn', 'Filter tabs'),
    (b'stat__num', 'Stat numbers'),
    (b'lightbox', 'Lightbox'),
    (b'btn--primary', 'Primary buttons'),
    (b'footer__copy', 'Footer copy'),
]

print()
print('=== CONTENT CHECKS ===')
for check, label in checks:
    found = check in content
    if 'Konstantin' in label or 'Gold' in label or 'Yarsite' in label or 'Footer credit' in label:
        if found:
            print('FAIL: ' + label + ' present')
        else:
            print('OK: ' + label + ' absent')
    else:
        if found:
            print('OK: ' + label + ' present')
        else:
            print('MISSING: ' + label)

# Gallery count
import re
items = re.findall(b'gallery__item', content)
print('Gallery items: ' + str(len(items)))

# File size
print('File size: ' + str(len(content)) + ' bytes')