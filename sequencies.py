palavra = "banana"

lista = [2,5,2,8,5]

print(lista [3])

serie = range(0,10)

print(serie[0])

dias = ["S","T","Q","Q","S","S","D"]

#to add element to the list
dias.append("D2")

print(dias)

dias.pop() #to get rid of the last element of the list

print(dias)


# O Tuple e uma lista que vc nao pode mudar vc nao quer mudar exemplo dados de endereco no Brasil e fixo nao quer mudar
# esses parametros

# O tuple e uma estrutura de dados inalteravel


dias_tuple = ("S","T","Q","Q","S","S","D")

print(dias_tuple)

print(type(dias_tuple))

print(len(dias_tuple))

# tuple de 2 valores x e y por exemplo

ponto = (3,5)

# data types que sao considerados sequencias tuple, string, list

#Uma sequência é nada mais do que um conjunto de valores ordenados.
# Essa ordem é definida pelo índice. Por isso podemos acessar listas,
# tuples ou strings através dos [] (colchetes), por exemplo:

palavra = "alura"
print(palavra[3])

#Ou usando uma tuple:

letras = ("p", "y", "t", "h", "o", "n")
print(letras[2])

#Além disso, as sequências possuem várias funções em comuns

#Importante saber que existem algumas funções que funcionam com
# todos os tipos de sequências como os built-ins: len, min e max.
#O del também é uma função built-in, mas só funciona para sequências
#mutáveis como listas. Como o tuple é imutável, não podemos remover seus elementos, e logo o código dá erro.
#Veja o mesmo exemplo correto usando uma lista:

valores = ["a","b","c","d","e"]
del(valores[0]) #funciona pois é lista

#Uma diferença que encontramos entre list e tuple é na hora de criá-las, em que usamos [] ou ():

lista = [4,3,2,1]

tuple = (4,3,2,1)

#Outra diferença é a questão de podermos alterar a sequência ou não. Listas podem ser alteradas, podendo
#adicionar ou remover elementos. Tuples, uma vez criadas, não podem ser alteradas. Tuples são imutáveis .


#Já vimos as sequências str (strings), tuple, list e range.

#Entre essas sequências, list é a única que é mutável. tuple, str e range são imutáveis.

#Não falamos explicitamente que range é imutável, mas saiba que ele se comporta como tuples e strs.

ponto = (3,5)

p1 = (3,5)

p2 = (4,6)

p3 = (5,7)

line = [p1,p2,p3]

print(line)

p1 = ("Nico",39)

p2 = ("Flavio",37)

instrutores = [p1,p2]

print(instrutores)

print(instrutores[0])

print(instrutores[0][1])

palavras = []

palavras.append("banana")

palavras.append("abacaxi")

print(palavras)

palavras_tuple = (*palavras,)

print(palavras_tuple)

print(type(palavras_tuple))


mando = ["Mandalorian", "Grogu", "Ahsoka Tano", "Bo Katan", "Boba Fett"]
print(mando)
print(type(mando))

mando_tuple = (*mando,)
print(mando_tuple)
print(type(mando_tuple))









