#programa que lê uma string e devolve ela inverida
s=input("Digite a mensagem a ser invertida:")#string inicial
stringlenght=len (s) #Calcula o comprimento da lista
slicedString=s [stringlenght::-1]# fatiando
print(slicedString) #imprime a string invertida
