          #TUPLAS estrutura de dados semelhante a listas e são imutaveis(EX: CPF, RG)
#Tupla usa parenteses [], Lista usam ()

tuple = (1,2,3,4,5)
index = tuple[0]
print(index)

          # Coverter tupla em lista
tuple = (1,2,3,45,78,52)
x = list(tuple)
print (x)
       #For n in tuple
for n in tuple:
  print(tuple)

          #Desempacotar elementos da tupla
list = (1,3)
x, y = list
print('coordenada',x)
print('coordenada',y)

          #FUNÇÕES - chama-se def. O nome da função deve ser semantico (Levar o nome do que faz)
      # 1primira chamada
Exemplo: def nome():
  print('Olá mundo')
nome()

      #Exemplo2 parametro função pura

name4 = 'Caio'
def display():
  # Local - dentro da função
  name = 'Gabriel'
  name2 = 'Bia'
  name3 = 'Ben'
  print('Ola', name)
  print('Ola', name2)
  print('Ola', name3)
print('Ola', name4)
display()

def soma():
  n = int(input('Digite um numero'))
  x = int(input('Digite outro numero'))
  print(n+x)
soma()
soma()

                    # **EXERCÍCIOS:**

#1 -  Crie uma tupla chamada `frutas` com pelo menos 5 frutas diferentes. Em seguida, acesse e imprima o terceiro elemento da tupla. 

tuple = ('Maça', 'Banana', 'Pêra', 'Uva',  'Mamão')
elemento = tuple
print(elemento[3])

# #- Crie uma tupla chamada `numeros` com alguns números inteiros. Em seguida, converta essa tupla em uma lista e imprima a lista resultante.

tuple = (2,4,29,34)
numeros = list(tuple)
print (numeros)

#3 - Crie uma tupla chamada `meses` com os nomes dos meses do ano até Setembro. Use um loop `for` para imprimir cada mês em uma linha separada.

tuple = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro')
for meses in tuple:
  print(meses)


#4 - Crie uma lista chamada `notas` com algumas notas de alunos. Em seguida, converta essa lista em uma tupla e imprima a tupla resultante.

notas = [2,5,7,9,10]
tuple_notas = tuple(notas)
print(tuple_notas)

#5 - Crie uma lista chamada `ponto` que represente as coordenadas (x, y) de um ponto. Em seguida, desempacote os elementos da lista em duas variáveis separadas (x e y) e imprima os valores.

ponto = (1,3)
x,y = ponto
print(x)
print(y)



                    #desafio calculadora
                    #4 OPÇÕES DE OPERAÇÃO, CONDICIONAIS**, FOR** , VARIAVEIS**,SINAIS DE COMPARAÇÃO (==)**  

Função para realizar a operação de adição
def adicao(x, y):
    return x + y

# Função para realizar a operação de subtração
def subtracao(x, y):
    return x - y

# Função para realizar a operação de multiplicação
def multiplicacao(x, y):
    return x * y

# Função para realizar a operação de divisão
def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

# Função principal da calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite a opção (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado: ", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1, num2))
    else:
        print("Opção inválida")

Chamando a função da calculadora
calculadora()

# Sistema para restaurante que mostre um menu que tenha como opção:
# Pratos - pizza / macarronada / lanche
# Bebidas - Agua / suco ; refrigerante / vinha

def atendimento():
     print("O que você deseja, comer ou beber?")
     escolha01 = int(input("Digte 1 para comer, Digite 2 para beber ->"))
     if escolha01 == 1:
          escolha_prato()
     else:
        escolha_drinks()


def escolha_drinks():
  escolha_drink =int(input("Digite 1 para Refri, Digite 2 para Suco"))
  if escolha_drink == 1:
      print("Opa você escolheu Refri")
  else:
      print("Você escolheu suco")


def escolha_prato():
  escolha = input("Escolha uma opção: a -salada, b - churrasco, c - Pizza ->")
  if escolha =='a':
     print("Sua salada está a caminho")
  elif escolha == 'b':
     print('Poxa, sensacional, já foi pedido seu Churrasco')
  elif escolha  == 'c':
      print('Show, sua Pizza já esta no forno *.*')
  else:
    print("Não temos essa")



atendimento()

                                    ## Dicionario

boy = {
'Nome': 'Gabriel',
'idade': '25',
'cpf': 123456789,
'RG' :456789,
'Cidade': 'Guarulhos'
}
print (boy)

if 'idade' in boy:
 print ("Idade do garoto")


notas_declaradas ={
"José": 9,
"Maria": 10,
"Felipe":7
}

c = 10

while c <=10:
    nome_que_vai_entrar = input("digite o nome do aluno >> ")
    nota = float(input("Digite a nota do aluno >> "))


    if notas_declaradas.get(nome_que_vai_entrar):
        print("Já existe o aluno", nome_que_vai_entrar)
    else: 
        notas_declaradas[nome_que_vai_entrar] = nota
        print(notas_declaradas)




#Crie um dicionário que represente um 
#dicionário de sinônimos. Em seguida, 
#peça ao usuário para digitar uma palavra e, 
#se a palavra estiver no dicionário, 
#mostre o seu sinônimo.
#crie um dicionário com 5 letras, e acesse 
#o 3º indice

p1 ={
  'alegre': 'animado',
  'morto': 'falecer',
  'tranquilo':'calmo',
  'rapido':'veloz',
  'lento':'devagar'
  }

p2 = input("Digite uma palavra para saber o sinonimo : ") 
if p2 in p1:
  print (p1[p2])

d1 = {'A','B','C','D','E'}
if  i3 in d1:
 print(d1)
  

#Return

def funcao_com_condicao(valor):
    if valor < 0:
        return "Valor negativo"
    # O código abaixo só é executado se o valor for maior ou igual a 0
    return "Valor não-negativo"


# #soma +=
# #subt -=

def soma_lista(lista):
  soma = 0
for numero in lista:
    soma += numero
    return soma

#_______________________________________________________________________

 #Exercício 1: Escreva uma função que calcule 
# a soma dos números de 1 a N, 
# onde N é um número inteiro dado. 

numero = int(input('Digite um numero inteiro:'))
print(numero)
def soma_num(numero):
    soma = 0 # Initialize soma variable to 0
    for i in range(1,numero+1):
        soma += numero
    print(soma)
soma_num(numero)

correção
def soma(N):
      soma = 0
for i in range(1,N+1):
  soma = soma + i
  print (soma)
  soma(2)

# Exercício 2: Escreva uma função que 
# conte quantas vezes uma letra 
# específica aparece em uma palavra.

def contar_letra (palavra, letra):
  contador = 0
  for char in palavra:
      if  char == letra:
          contador += 1

print (f'Tem essa quantidade de letra {letra}:', contador)
achados = contar_letra ('pneumutramicrospiosilicovulcanicoconiotico', 'a')

# Exercício 3: Escreva uma função que calcule 
# o fatorial de um número 
# inteiro não negativo N.

3! = 3 * 2 * 1 = 6 produto da multiplicação dos numeros anteriores.
N = int(input('fat:'))
resultado = 1
count = 1
while count <=N:
 count +=1 #count + count + 1
print(resultado)

