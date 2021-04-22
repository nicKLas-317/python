nir15 = input("NIR15 ? ")
nir13 = nir15[:13]
s = nir13[0]
mm = int(nir13[3:5])
dd = int(nir13[5:7])
tiret = nir15[13]
cc = int(nir15[14:])
if s != '1' and s != '2':
	print("S incorrect !")
elif mm<1 or mm>12:
	print("MM incorrect !")
elif dd>95 and dd<99:
	print("DD incorrect !")
elif tiret!='-':
	print("Tiret absent !")
elif cc!=97-(int(nir13)%97):
	print("CC incorrect !")
else:
	print("NIR15 valide")
