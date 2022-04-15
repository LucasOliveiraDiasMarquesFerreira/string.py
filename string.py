#programa para saber se uma palavra é Palíndromo
#se a mensagem for devolvida da mesma forma que foi digitada pelo usuário significa que éum Palíndromo
s=input("Digite a mensagem a ser verificada:")#string inicial
stringlenght=len (s) #Calcula o comprimento da lista
slicedString=s [stringlenght::-1]# fatiando
print(slicedString) #imprime a string invertida


print("Se a mensagem for devolvida da mesma maneira que o usuário digitou,significa que ela é um Palíndromo")

