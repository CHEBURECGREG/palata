with open('D:/PALATA_NEW/index.html', 'rb') as f:
    content = f.read()

# Check for key content
checks = [
    ('ГОСУДАРСТВЕННЫЙ МОНЕТНЫЙ ДВОР', 'Mint mention'),
    ('1722', 'Table of Ranks year'),
    ('МЕРИТОКРАЦИЯ', 'Meritocracy'),
    ('МАЛЫХИН ЮРИЙ ИВАНОВИЧ', 'Chairman full name'),
    ('МАЯКОВСКОГО', 'Address street'),
    ('1999', 'Established year'),
    ('🏅', 'Medal emoji'),
    ('01 /', 'Section numbering'),
    ('05 /', 'Section numbering'),
    ('ЖАЖДА СЛАВЫ', 'Aphorism'),
    ('ЦИЦЕРОН', 'Cicero'),
    ('ПЛАТОН', 'Plato'),
]
for check, label in checks:
    if check.encode('utf-8') in content:
        print(f'OK: {label}')
    else:
        print(f'MISSING: {label}')

# Verify mobile responsiveness
if b'@media (max-width: 768px)' in content:
    print('OK: Mobile breakpoints')
if b'@media (max-width: 1024px)' in content:
    print('OK: Tablet breakpoints')
if b'@media (max-width: 1200px)' in content:
    print('OK: Desktop breakpoints')

# Check no gold
if b'gold' in content.lower() or b'#E8B82E' in content or b'#F0C84D' in content:
    print('WARNING: Gold colors detected')
else:
    print('OK: No gold colors')

# Check no Konstantin
konstantin_bytes = 'Константин'.encode('utf-8')
if konstantin_bytes in content:
    print('FAIL: Konstantin found')
else:
    print('OK: No Konstantin')