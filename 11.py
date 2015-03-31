#YURI NAGHIRNIAC DE STEFANI
import random
import turtle
def impr(letraa, valor, qjogo,qacerto,qerro,qperda):
        letraa.speed(9)
        letraa.penup()
        letraa.setpos(valor,260)
        letraa.pendown()
        letraa.penup()
        letraa.write("Número de jogos: " + str(qjogo), font=("Arial", 12, "normal"))
        letraa.setpos(valor,240)
        letraa.pendown()
        letraa.penup()
        letraa.write("Jogos ganhados: " + str(qacerto), font=("Arial", 12, "normal"))
        letraa.setpos(valor,220)
        letraa.pendown()
        letraa.penup()
        letraa.write("Jogos perdidos: " + str(qperda), font=("Arial", 12, "normal"))
        letraa.setpos(valor,200)
        letraa.pendown()
        letraa.penup()
        mmedia=qerro/(qjogo)
        mmedia=int(mmedia*10)
        mmedia=float(mmedia/10)
        letraa.write("Média de erros: " + str(mmedia), font=("Arial", 12, "normal"))

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
def traço(angulo, tartaruga, posicao, pos, i, dist, atual):
        if atual[i] != " ":
            if i>0:
                angulo = 0
            tartaruga.penup()
            cor(tartaruga)
            tartaruga.setpos(pos,-250)
            tartaruga.pendown()
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
def palavrada(atual2, i):
        if atual2[i] in "AaÀàáÁâÂãÃ":
            atual2[i]="AaÀàáÁâÂãÃ"
        if atual2[i] in "EeéÊÉêE":
            atual2[i]="EeéÊÉêE"
        if atual2[i] in "CcÇç":
            atual2[i]="CcÇç"
        if atual2[i] in "OoóÓôÔ":
            atual2[i]="OoóÓôÔ"
        if atual2[i] in "IiíÍ":
            atual2[i]="IiíÍ"
        if atual2[i] in "UuúÚ":
            atual2[i]="UuúÚ"
        if atual2[i] in "Bb":
            atual2[i]="Bb"
        if atual2[i] in "Dd":
            atual2[i]="Dd"
        if atual2[i] in "Ff":
            atual2[i]="Ff"
        if atual2[i] in "Gg":
            atual2[i]="Gg"
        if atual2[i] in "Hh":
            atual2[i]="Hh"
        if atual2[i] in "Jj":
            atual2[i]="Jj"
        if atual2[i] in "Kk":
            atual2[i]="Kk"
        if atual2[i] in "Ll":
            atual2[i]="Ll"
        if atual2[i] in "Mm":
            atual2[i]="Mm"
        if atual2[i] in "Nn":
            atual2[i]="Nn"
        if atual2[i] in "Pp":
            atual2[i]="Pp"
        if atual2[i] in "Qq":
            atual2[i]="Qq"
        if atual2[i] in "Rr":
            atual2[i]="Rr"
        if atual2[i] in "Ss":
            atual2[i]="Ss"
        if atual2[i] in "Tt":
            atual2[i]="Tt"
        if atual2[i] in "Vv":
            atual2[i]="Vv"
        if atual2[i] in "Ww":
            atual2[i]="Ww"
        if atual2[i] in "Xx":
            atual2[i]="Xx"
        if atual2[i] in "Yy":
            atual2[i]="Yy"
        if atual2[i] in "Zz":
            atual2[i]="Zz"
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

modalidade=3
posicao2=-240
letra=""
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
func=1
erro=0
func2=1
perm=0
perm3=1
disterro=-50
tamanho=0
perm4=0
mmedia=float(0)
pal=""
jogadas=0
errdado=1
disterro2=100
mens=0
mens2=0
atual3=""
qjogo=0
qerro=0
qacerto=0
qperda=0
qjogo1=0
qerro1=0
qacerto1=0
qperda1=0
qjogo2=0
qerro2=0
qacerto2=0
qperda2=0
jogador1=0
jogador2=0
perm6=0
perm7=""

func2=1
window = turtle.Screen()
while modalidade!=1 and modalidade!=2:
    modalidade=int(window.textinput("Janela mágica", "Digita a modalidade: 1 contra o computador ou 2 contra outro jogador!"))
while func==1:#para trocar de palavras
    if jogador1==0:
        jogador1=1
        jogador2=0
    else:
        jogador1=0
        jogador2=1
    mens2=0
    atual3=""
    mens=0
    errado=1
    jogadas+=1
    atual=""
    func=1
    letra=""
    posicao=list()
    usada=list()
    erro=0
    func2=1
    perm=0  
    disterro=-50
    disterro2=100
    window.bgcolor("white")
    window.reset()
    if qjogo>=1 and modalidade ==1:
        impr(letraa, -50, qjogo,qacerto,qerro,qperda)
    if qjogo1>=1 and modalidade ==2:
        impr(letraa, -50, qjogo1,qacerto1,qerro1,qperda1)
        letraa.speed(9)
        letraa.penup()
        letraa.setpos(-50,180)
        letraa.pendown()
        letraa.penup()
        letraa.write("(Jogador 1)", font=("Arial", 12, "normal"))
    if qjogo2>=1 and modalidade ==2:
        impr(letraa, 120, qjogo2,qacerto2,qerro2,qperda2)
        letraa.speed(9)
        letraa.penup()
        letraa.setpos(120,180)
        letraa.pendown()
        letraa.penup()
        letraa.write("(Jogador 2)", font=("Arial", 12, "normal"))
    if modalidade==2:
        if jogador1==1:
            qjogo1+=1
        else:
            qjogo2+=1
    if modalidade==1:
            valor = random.randint(0,len(palavras)-1)
            atual=palavras[valor]
    atual2=[""]*len(atual)
    atual3=atual
    for i in range (len(atual2)):
        atual2[i]=atual[i]
    for i in range (len(atual2)):
        palavrada(atual2,i)
    if modalidade==1:
        lixo.append(palavras[valor])
        del palavras[valor]
    formado=[" "]*len(atual)
    pos=-275
    dist = 17
    angulo = 90
    posicao.append(pos)
    for i in range (0, len(atual)):
        traço(angulo, tartaruga, posicao, pos, i, dist, atual)
        if atual[i] != " ":
            pos=pos+30 
            posicao.append(pos)
        if atual[i] == " ":
            pos=pos+15
            posicao.append(pos)
    tartaruga.penup()
    tartaruga.setpos(-100,150)
    tartaruga.left(-90)
    func2=1
    qjogo+=1
    window.title("Forca")
    forc(tartaruga)
    if modalidade==1:
        if palavras==[]:
            palavras=lixo
            lixo=[]
    if modalidade==1:
            valor = random.randint(0,len(palavras)-1)
            atual=palavras[valor]
    perm6=0
    if modalidade==2:
        if jogador1==1:
            while perm6==0:
                perm6=1
                atual=window.textinput("Jogador 1", "Digita a palavra para o oponente!")
                for l in range (len(atual)):
                    if atual[l] in "AaÀàáÁâÂãÃEeéÊÉêECcÇçIiíÍOoóÓôÔQqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxVvBbNnMmUuúÚ":
                        l=l
                    else:
                        perm6=0
                if perm6==0:
                    print("Sua palavra tem caractere proibido!")
        else:
            while perm6==0:
                perm6=1
                atual=window.textinput("Jogador 1", "Digita a palavra para o oponente!")
                for l in range (len(atual)):
                    if atual[l] in "AaÀàáÁâÂãÃEeéÊÉêECcÇçIiíÍOoóÓôÔQqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxVvBbNnMmUuúÚ":
                        l=l
                    else:
                        perm6=0
                if perm6==0:
                    print("Sua palavra tem caractere proibido!")
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
            if errado==1:
                erro+=1
                calcerro(erro)
                disterro+=50
                letraa.speed(7)
                letraa.penup()
                letraa.setpos(disterro,150)
                letraa.pendown()
                letraa.write(letra, font=("Arial", 20, "normal"))
                if letra in "AaÀàáÁâÃÂã":
                    usada.append("AaÀàáÁâÃÂã1")
                    errado=0
                if letra in "EeéÊÉêE":
                    usada.append("EeéÊÉêE1")
                    errado=0
                if letra in "bB":
                    usada.append("bB1")
                    errado=0
                if  letra in "CcÇç":
                    usada.append("CcÇç1")
                    errado=0
                if letra in "Dd":
                    usada.append("Dd1")
                    errado=0
                if  letra in "Ff":
                    usada.append("Ff1")
                    errado=0
                if  letra in "Gg":
                    usada.append("Gg1")
                    errado=0
                if letra in "Hh":
                    usada.append("Hh1")
                    errado=0
                if  letra in "IiíÍ":
                    usada.append("IiíÍ1")
                    errado=0
                if  letra in "Jj":
                    usada.append("Jj1")
                    errado=0
                if letra in "Kk":
                    usada.append("Kk1")
                    errado=0
                if  letra in "Ll":
                    usada.append("Ll1")
                    errado=0
                if   letra in "Mm1":
                    usada.append("Mm1")
                    errado=0
                if   letra in "Nn":
                    usada.append("nN1")
                    errado=0
                if  letra in "OoóÓôÔ": 
                    usada.append("OoóÓôÔ1")
                    errado=0
                if   letra in "pP":
                    usada.append("Pp1")
                    errado=0
                if  letra in "qQ":
                    usada.append("Qq1")
                    errado=0
                if   letra in "Rr":
                    usada.append("Rr1")
                    errado=0
                if  letra in "Ss":
                    usada.append("Ss1")
                    errado=0
                if  letra in "Tt":
                    usada.append("Tt1")
                    errado=0
                if letra in "UuúÚ":
                    usada.append("UuúÚ1")
                    errado=0
                if   letra in "Vv":
                    usada.append("Vv1")
                    errado=0
                if  letra in "Ww":
                    usada.append("Ww1")
                    errado=0
                if   letra in "Xx":
                    usada.append("Xx1")
                    errado=0
                if  letra in "yY":
                    usada.append("Yy1")
                    errado=0
                if  letra in "zZ":
                    usada.append("zZ1")
                    errado=0
mens2=1
        perm3=1
        if len(letra)!=1:
            perm3=0
            mens2=0
            func2=0
            for i in range (len(atual)):
                if letra[i] in atual2[i]:
                    i=i
                else:
                    mens2=1
                    perm3=1
                    func2=1
            perm4=3
            for k in range (len(usada)):
                    if len(usada[k])==len(letra):
                        perm4=2
                        for t in range (len(usada[k])):
                            if letra[t] in usada[k][t]:
                                t=t
                            else:
                                perm4=3
                        if perm4==2:
                            break
            if perm4==2:
                print ("Você já usou essa palavra!")
            if mens2==1 and mens2!=0 and perm4==3:
                                erro+=1
                                usada.append([""]*len(letra))
                                for l in range (len(letra)):
                                    usada[-1][l]=letra[l]
                                    palavrada(usada[-1],l)
                                usada.append(letra)
                                calcerro(erro)
                                disterro2-=30
                                letraa.speed(99)
                                letraa.penup()
                                letraa.setpos(-30,disterro2)
                                letraa.pendown()
                                letraa.write(letra, font=("Arial", 20, "normal"))
if atual.replace(" ", "")==""or mens2==0:
            window.reset()
            tartaruga.speed(99999) 
            tartaruga.penup()
            tartaruga.setpos(-9999,-9999)
            tartaruga.pendown()
            letraa.speed(1)
            letraa.penup()
            letraa.setpos(-300,0)
            letraa.pendown()
            letraa.write("VOCÊ WIN!!!!!!!!", font=("Arial", 50, "normal"))
            letraa.penup()
            letraa.setpos(-300,-500)
            func2=0
            qacerto+=1
            qerro+=erro
            if modalidade==2:
                if jogador1==1:
                    qerro1+=erro
                    qacerto1+=1
                else:
                    qerro2+=erro
                    qacerto2+=1
        elif erro==6:
            func2=0
            qerro+=erro
            window.reset()
            tartaruga.speed(99999)
            tartaruga.penup()
            tartaruga.setpos(-9999,-9999)
            tartaruga.pendown()
            letraa.speed(1)
            letraa.penup()
            letraa.setpos(-300,200)
            letraa.pendown()
            letraa.write("A palavra é: " + atual3, font=("Arial", 20, "normal"))
            letraa.penup()
            letraa.setpos(-300,100)
            letraa.pendown()
            letraa.write("VOCÊ LOSE!!!!!!!!", font=("Arial", 50, "normal"))
            letraa.penup()
            letraa.setpos(-300,-500)
            qperda+=1
            if modalidade==2:
                if jogador1==1:
                    qperda1+=1
                else:
                    qperda2+=1
        
        letra=""
    perm7=window.textinput("Jogador 1", "Deseje jogar novamente? 'N' para nâo ou 'S' para sim!")
    if perm7=="n" or perm7=="N":
            func=0