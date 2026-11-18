import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('D:/PALATA_NEW/primer2.html', 'rb') as f:
    content = f.read()

idx = content.find(b'desktop-icons')
if idx >= 0:
    snippet = content[idx:idx+6000]
    print(snippet.decode('utf-8', errors='replace'))
