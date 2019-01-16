# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print('\n')
print('Selecione o número da operação desejada')
print('\n')
print(' 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão')
print('\n')
#v = 2
while bool(1):
	o = input('Digite sua opção (1/2/3/4): ')
	print('\n')
	if o != '1' and o != '2' and o != '3' and o != '4':
		print('Digite apenas números de 1 a 4!')
		print('\n')
	else:
		break
		#v=-1
n1 = int(input('Digite o primeiro número: '))
print('\n')
n2 = int(input('Digite o segundo número: '))
if o == '1':
	print(n1, " + ", n2, " = ", n1+n2)
elif o == '2':
	print(n1, " - ", n2, " = ", n1-n2)
elif o == '3':
	print(n1, " * ", n2, " = ", n1*n2)
elif o == '4':
	print(n1, " / ", n2, " = ", n1/n2)
