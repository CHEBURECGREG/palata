with open('D:/PALATA_NEW/index.html', 'rb') as f:
    content = f.read()

import re

# Search for chairman (using bytes)
chairman_bytes = 'МАЛЫХИН'.encode('utf-8')
idx = content.find(chairman_bytes)
if idx >= 0:
    print(f'Chairman found at {idx}: {content[idx:idx+80]}')
else:
    print('Chairman NOT found')

# Search for mayakovskogo
mayak_bytes = 'МАЯКОВСКОГО'.encode('utf-8')
idx = content.find(mayak_bytes)
if idx >= 0:
    print(f'Mayakovskogo found at {idx}: {content[idx:idx+80]}')
else:
    print('Mayakovskogo NOT found')

# Search for aphorism
aph_bytes = 'ЖАЖДА СЛАВЫ'.encode('utf-8')
idx = content.find(aph_bytes)
if idx >= 0:
    print(f'Aphorism found at {idx}: {content[idx:idx+80]}')
else:
    print('Aphorism NOT found')

# Search for Cicero
cic_bytes = 'ЦИЦЕРОН'.encode('utf-8')
idx = content.find(cic_bytes)
if idx >= 0:
    print(f'Cicero found at {idx}: {content[idx:idx+80]}')
else:
    print('Cicero NOT found')

# Search for Plato
pla_bytes = 'ПЛАТОН'.encode('utf-8')
idx = content.find(pla_bytes)
if idx >= 0:
    print(f'Plato found at {idx}: {content[idx:idx+80]}')
else:
    print('Plato NOT found')