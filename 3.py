#YURI NAGHIRNIAC DE STEFANI
import random
import turtle
def forc(tartaruga):
    tartaruga.speed(7)
    tartaruga.penup()
    tartaruga.setpos(-300,-250)
    tartaruga.pendown()
    dist = 500
    angulo = 90
    tartaruga.left(angulo)
    tartaruga.forward(dist)
    dist = 200
    angulo = -90
    tartaruga.left(angulo)
    tartaruga.forward(dist)
    dist = 100
    angulo = -90
    tartaruga.left(angulo)
    tartaruga.forward(dist)
def calcerro(erro):
                    if erro==1:
                        tartaruga.setpos(-100,120)
                        tartaruga.penup()
                        cor(tartaruga)
                        tartaruga.right(90)
                        tartaruga.forward(30)
                        tartaruga.right(270)
                        tartaruga.pendown()
                        tartaruga.circle(30)
                    elif erro==2:
                        tartaruga.penup()
                        cor(tartaruga)
                        tartaruga.setpos(-100,90)
                        tartaruga.pendown()
                        tartaruga.left(0)
                        tartaruga.forward(100)   
                    elif erro==3:
                        tartaruga.penup()
                        cor(tartaruga)
                        tartaruga.pendown()
                        tartaruga.left(45)
                        tartaruga.forward(100)
                    elif erro==4:
                        tartaruga.penup()
                        cor(tartaruga)
                        tartaruga.pendown()
                        tartaruga.left(180)
                        tartaruga.forward(100)
                        tartaruga.left(90)
                        tartaruga.forward(100)
                    elif erro==5:
                        tartaruga.penup()
                        cor(tartaruga)
                        tartaruga.pendown()
                        tartaruga.left(180)
                        tartaruga.forward(100) 
                        tartaruga.left(45)
                        tartaruga.forward(90) 
                        tartaruga.left(135)
                        tartaruga.forward(90)
                    elif erro==6:
                        tartaruga.penup()
                        cor(tartaruga)
                        tartaruga.pendown()
                        tartaruga.left(180) 
                        tartaruga.forward(90)
                        tartaruga.left(-90)
                        tartaruga.forward(90)
palavras=list()#todas as palavras da lista
lixo=list()#para onde ficas as palavras usadas
atual2=list()#lista formada com as letras da palavra
formado=list()#a palavra atual com as letras usadas
posicao=list()#local do gráfico para colocar a letra
usada=list()#letras usadas
cont=0
perm=0
tartaruga   = turtle.Turtle()
letraa= turtle.Turtle()
f = open("entrada.txt", encoding="utf-8")
for linha in f.readlines():
    if linha!="":
        pal=""
        for j in range(0,len(linha)-1):
            pal=pal+linha[j]
        if pal!="":
            palavras.append(pal)
    cont+=1
func=1
func2=1
window = turtle.Screen()
while func==1:#para trocar de palavras
    while func==1:#para trocar de letra
        perm=0
        while perm==0:
            perm=1
            letra= window.textinput("Jenela mágica", "Digita ae!")
            if len(letra)==1:
                for jjj in range (len(usada)):
                    if letra in usada[jjj] and len(usada[jjj])>0:
                        perm=0
                        print("Você já usou essa letra!")
                        break
                if letra in "AaÀàáÁâÂãÃEeéÊÉêECcÇçIiíÍOoóÓôÔQqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxVvBbNnMmUuúÚ":
                        letra=letra
                else:
                        perm=0
                        print("Você usou letra proibida")
            elif len(letra)>len(atual):
                perm=0
                print("A palavra que você digitou é maior que a palavra atual!")
            elif len(letra)<len(atual):
                
                perm=0
                print("A palavra que você digitou é menor que a palavra atual!")
            elif len(letra)==len(atual):
                 mens=0
                 for i in range (len(atual)):
                     if formado[i] in "AaÀàáÁâÂãÃEeéÊÉêECcÇçIiíÍOoóÓôÔQqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxVvBbNnMmUuúÚ":
                         if letra[i] in formado [i]:
                             i=i
                         else:
                             perm=0
                             if mens==0:
                                 print("A sua palavra não encaixa na palavra atual!")
                             mens=1
                     for j in range (len(usada)):
                         if letra[i] in usada[j] and "1" in usada[j]:
                             perm=0
                             if mens==0:
                                 print("A sua palavra contém letras que não podem ser usadas!")
                             mens=1