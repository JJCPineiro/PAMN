import os

matriz = []

print "\n" + 80*"*"
print 5*" " + "Hola soy trampostio, puedo ayudarte a transponer una matriz. Seguimos?"
print 20*" " + "Presiona cualquier tecla para continuar "
print 80*"*"
raw_input()

os.system("cls")

print ("\nMe quieres complicar la vida?")


fil = int(raw_input("\n\nIngrese el numero de renglones de su matriz: "))
col = int(raw_input("\n\nIngrese el numero de columnas de su matriz:  "))

for i in range(fil) :
	matriz.append([0]*col)

for f in range(fil) :
	for c in range(col) :
		matriz[f][c] = float(raw_input("\nEl elemento [%d] [%d] es :"%(f+1,c+1)))
		

print ("\n\nLa matriz es:\n\n") 
for a in matriz:
	print(a)

print("\n\nLa transpuesta es:\n\n")
for b in zip(*matriz):
	print(b)

print zip(*matriz)

//SoloAlbertoG
