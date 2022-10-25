#Exercício 1
nome = input('Entre com seu nome: ')
print(nome.upper())
print(nome.lower())
print(len(nome))
print(nome.replace("Ribeiro", "do Inatel"))

#Exercício 2
num = int(input('Entre com o número: '))
inicio = int(input('Entre com o inicio: '))
fim = int(input('Entre com o final: '))

for c in range(inicio, fim+1):
    print(f'{num} x {c} = {num*c}')

#Exercício 3
sexo = ''
while (sexo != 'M') or (sexo != 'F'):
    sexo = input('Entre com o sexo da pessoa: [M/F]')
    if(sexo == "M"):
        print("A pessoa é homem.")
        break
    elif(sexo == "F"):
        print('A pessoa é mulher')
        break