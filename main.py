'''--->COMENTARIO DE BLOCO
Título:revisão de Python
Autor :profe.Berssa
Data:2024.07.02
'''
#-->comentario de linha
#objetivo: Revisar os fundamentos

print("hello world!")


#saida -->print()
print("100+100") #"string/str"
print(100+100) #operação

#entrada-->input()
nome = input('digite seu nome:')
print('Voce dise', nome)
valor1 = int(input ('digite um valor: '))
valor2 = int(input ('digite outro valor: '))
total = valor1 + valor2
print('soma dos valores digitados é:', total)

#variaveis -->espaço de memoria que arnazena valores temporariamente
#str--> arnazena textos e cacteres--> %s ou %c
nome='ariadine'
print(type(nome))
#int--> arnazena numeros inteiros positivos e negativos--> %d
valorX=-81
print('a variavel valorX é do tipo', type(valorX), 'e tem armazenado o valor :%d' %valorX)
#float--> armazena numeros de ponto flutuante positivos e negativos-->NÃO USE , USA .--> #f
pi = 3.14159
print('a variavel pi é do tipo', type(pi), 'e tem armazenado o valor :%.2f' %pi)
#bool--> armazena se é true ou false--> ?
teste = 10 > 50
print('a variavel teste é do tipo', type(teste), 'e tem armazenado o valor :', teste)

#operadores
#aritimeticos --> calculos +, -, *, /, **, //, %
print(5*5)
print(15/4) #resultado float
print(10//3) # --> resultado numero inteiro
print(10%4)
# -->atribuição
A = 10 # --> = (recebe)
A +=1  # --> = incremento soma 1
A -=1  # --> = descremento diminui 1
#relacionais --> fazem comparações e retornam true ou false
A == 10 # ==é igual == true
A != 10 # != diferentes == false
# >; <; >=; <=
# logicos --> concatenação de operadores relacionas
# and ==e; or==ou; not==não

#repetições
#loço for --> quando eu sei quantas vezes vai repetir
for i in range(1,11):
  print(i)
palavra='programação'
for letra in palavra:
  print(letra)

tecla = 1
while tecla !=0: #--> repete até a condição ser false
  tecla= int(input('digite um numero:'))
#condições -->if;  else; elif
idade = int(input('digite sua idade'))
if idade >= 18: #testa e faz se o resultado true
  print('pode ir pro bailão')
elif idade >= 16: #faz se i if == false e i elif == true
  print('vai pro bailão com a mãe ou pai')
else:# se o resultado do if for == a false
  print('não vai pro bailão')
#funções --> def
def soma(x, y):
  R = x + y
  return R
print(soma(10 , 5))
print(soma(100, 50))
A=int(input('digite um valor:'))
B= int(input('digite outro valor:'))
print('soma de %d e %d é igual a %d '%(A, B,(soma (A ,B))))