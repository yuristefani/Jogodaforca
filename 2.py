#YURI NAGHIRNIAC DE STEFANI
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
f = open("entrada.txt", encoding="utf-8")
for linha in f.readlines():
    if linha!="":
        pal=""
        for j in range(0,len(linha)-1):
            pal=pal+linha[j]
        if pal!="":
            palavras.append(pal)
    cont+=1