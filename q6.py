n1 = float(input('Primeiro numero: '))
n2 = float(input('Segunda numero: '))
n3 = float(input('Terceiro numero: '))
media_a = (n1 + n2 + n3) / 3
if n1 != 0 and n2 != 0 and n3 != 0:
    media_h = 3/((1/n1) + (1/n2) + (1/n3))
else:
    media_h = 0
print(f'Media aritrimetrica: {media_a:.2f}')
print(f'Media harmonica: {media_h:.2f}')