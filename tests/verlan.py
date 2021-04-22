texte = input("Texte ? ")
texteVerlan = ''
for i in range(1, len(texte) + 1):
	texteVerlan += texte[-i]
print(texteVerlan)
