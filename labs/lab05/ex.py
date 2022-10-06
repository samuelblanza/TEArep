texto = "X-DSPAM-Confidence:0.8475"
inicio = texto.find(":") + 1
final = len(texto)
número = texto[inicio:final]
print(número)
print(type(número))
