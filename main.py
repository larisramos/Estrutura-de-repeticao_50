'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.'''

acumuladorSoma = 0
cont = 0
cont2 = 0
for num in range (0,6):
  cont += 1
  valor = int(input(f'Digite o {cont}° valor: '))
  if valor%2==0:
    cont2 += 1
    acumuladorSoma += valor
print(f'Entre os {cont} valores informados, {cont2} números são pares e a soma destes é igual a {acumuladorSoma}.')