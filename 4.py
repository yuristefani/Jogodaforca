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
def cor(var):
    a=random.randint(0,8)
    if a==0:
        var.color("orange")
    if a==1:
        var.color("red")
    if a==2:
        var.color("yellow")
    if a==3:
        var.color("blue")
    if a==4:
        var.color("black")
    if a==5:
        var.color("green")
    if a==6:
        var.color("purple")
    if a==7:
        var.color("grey")
atual=""
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
    while func2==1:#para trocar de letra
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
        errado=1
        if len(letra)==1:
            for lll in range (0, len(atual)):
                letraa.speed(20)
                letraa.penup()
                cor(letraa)
                letraa.setpos(posicao[lll],-250)
                letraa.pendown()
                if atual[lll] in "AaÀàáÁâÂãÃ" and letra in "AaÀàáÁâÃÂã":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("AaÀàáÁâÂãÃ")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "EeéÊÉêE" and letra in "EeéÊÉêE":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("EeéÊÉêE")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Bb" and letra in "bB":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("bB")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "CcÇç" and letra in "CcÇç":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("CcÇç")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Dd" and letra in "Dd":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Dd")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Ff" and letra in "Ff":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Ff")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Gg" and letra in "Gg":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Gg")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Hh" and letra in "Hh":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Hh")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "IiíÍ" and letra in "IiíÍ":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("IiíÍ")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Jj" and letra in "Jj":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Jj")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Kk" and letra in "Kk":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Kk")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Ll" and letra in "Ll":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Ll")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Mm" and letra in "Mm":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Mm")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "nN" and letra in "Nn":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("nN")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "OoóÓôÔ" and letra in "OoóÓôÔ":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("OoóÓôÔ")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Pp" and letra in "Pp":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Pp")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Qq" and letra in "Qq":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Qq")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Rr" and letra in "Rr":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Rr")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Ss" and letra in "Ss":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Ss")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Tt" and letra in "Tt":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Tt")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "UuúÚ" and letra in "UuúÚ":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("UuúÚ")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "vV" and letra in "Vv":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("vV")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Ww" and letra in "Ww":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Ww")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Xx" and letra in "Xx":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Xx")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "Yy" and letra in "yY":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("Yy")
                    errado=0
                    formado[lll]=usada[-1]
                if atual[lll] in "zZ" and letra in "Zz":
                    letraa.write(atual[lll], font=("Arial", 20, "normal"))
                    atual =atual.replace(atual[lll]," ",1)
                    usada.append("zZ")
                    errado=0
                    formado[lll]=usada[-1]