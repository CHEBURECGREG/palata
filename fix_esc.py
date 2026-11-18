with open('D:/PALATA_NEW/build_brutalist.py', 'rb') as f:
    content = f.read()

# Fix the esc function
old = b'return str(s).replace("&", "&").replace("<", "<").replace(">", ">").replace(\'"\', """'
new = b'return str(s).replace("&", "&").replace("<", "<").replace(">", ">").replace(\'"\', \'"\')'

fixed = content.replace(old, new)

with open('D:/PALATA_NEW/build_brutalist.py', 'wb') as f:
    f.write(fixed)

print('Fixed esc function')