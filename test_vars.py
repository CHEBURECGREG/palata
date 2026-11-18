ORG = {'address': '191014, Санкт-Петербург, ул. Маяковского, 19/29'}
CONTACT_INFO = {'addressee': 'Палате Личности, Малыхин Юрию'}

def esc(s):
    return str(s).replace('&', '&').replace('<', '<').replace('>', '>').replace('"', '"')

ORG_ADDRESS = esc(ORG['address'])
ORG_ADDRESSEE = esc(CONTACT_INFO['addressee'])
ORG_CHAIRMAN = esc('Малыхин Юрий Иванович')

print('ORG_ADDRESS repr:', repr(ORG_ADDRESS))
print('ORG_ADDRESSEE repr:', repr(ORG_ADDRESSEE))
print('ORG_CHAIRMAN repr:', repr(ORG_CHAIRMAN))