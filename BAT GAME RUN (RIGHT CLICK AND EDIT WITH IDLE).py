#Gerekli kütüphanelerin projeye eklenmesi
import turtle, random, math, winsound, time

#Ekrandaki karakterlerin projeye eklenmesi
gerekligif=turtle.Screen()


#YARASALAR
gerekligif.register_shape("yarasaresimkirmizi.gif")
gerekligif.register_shape("yarasaresimapembe.gif")
gerekligif.register_shape("yarasaresimkmor.gif")
gerekligif.register_shape("yarasaresimyesil.gif")
gerekligif.register_shape("yarasaresimkahverengi.gif")
gerekligif.register_shape("yarasaresimsari.gif")


###KARAKTERİN HIZ DEĞERİ###
hiz = 1

#İLGİLİ FONKSİYON İÇİNDE PROJENİN ÇALIŞTIRILMASI
def launcher():
    #OYUN LAUNCHER'A BACKGROUND EKLEME VE OYUN İSMİNİ BELİRLEME
    girismenu=turtle.Screen()
    girismenu.title("YARASA AVCISI")
    girismenu.bgpic("startmenu.gif")
    

    #YARASA AVCISI YAZIMI
    launcher=turtle.Turtle()
    launcher.hideturtle()
    launcher.penup()
    launcher.goto(0,300)
    launcher.pendown()
    
    launcher.color("deep pink")
    style = ("Game Over", 120, "bold")
    launcher.write("YARASA AVCISI", font=style, align="center")
    
    #LAUNCHER YAZIMI
    launcher.penup()
    launcher.goto(0,240)
    launcher.pendown()
    
    launcher.color("pink")
    style = ("Game Over", 80, "bold")
    launcher.write("LAUNCHER", font=style, align='center')

    launcher.penup()
    launcher.goto(0,-220)
    launcher.pendown()

    launcher.color("Dark Orange1")
    style = ("Game Over", 50, "bold")
    launcher.write("Start Menu icin 'w' tusuna basiniz.", font=style, align='center')

    launcher.penup()
    launcher.goto(0,-260)
    launcher.pendown()

    launcher.color("Dark Orange1")
    style = ("Game Over", 50, "bold")
    launcher.write("Exit icin 's' tusuna basiniz.", font=style, align='center')


    #START MENU, EXİT
    launcher.penup()
    launcher.goto(0,30)
    launcher.pendown()
    launcher.color("deep pink")
    style = ("Game Over", 70, "bold")
    launcher.write("Start Menu", font=style, align="center")

    launcher.penup()
    launcher.goto(0,-40)
    launcher.pendown()
    launcher.color("deep pink")
    style = ("Game Over", 70, "bold")
    launcher.write("Exit", font=style, align="center")

    launcher.penup()
    launcher.goto(0,-130)
    launcher.pendown()
    launcher.color("brown1")
    style = ("Game Over", 70, "bold")
    launcher.write("By Furkan Ayaz", font=style, align="center")
    
    



    #MENU'DE İLERİ GERİ YAPACAK CURSOR'UN BELİRLENMESİ
    cursor=turtle.Turtle()
    cursor.hideturtle()
    cursor.penup()
    cursor.goto(0,300)
    cursor.pendown()
    cursor.penup()
    cursor.backward(120)
    cursor.pendown()
    cursor.color("black","deep pink")
    cursor.shapesize(2, 2, 1)
    
    

    #İLERİ GERİ TUŞLARININ MENUDE KULLANIMI
    tus=turtle.Turtle()
    tus.hideturtle()
    tus2=turtle.Screen()
    tus.penup()
    tus.goto(0,30)
    tus.pendown()

    tus.color("pink")
    style = ("Game Over", 70, "bold")
    tus.write("Start Menu", font=style, align="center")
    tus.penup()
    tus.backward(120)
    tus.left(90)
    tus.forward(20)
    tus.right(90)
    tus.pendown()
    tus.shapesize(2,2,1)
    tus.showturtle()

        

    def f(): #AŞAĞIYA YÖN TUŞU
        winsound.PlaySound("zapsplatatari.wav", winsound.SND_ASYNC)
        tus.penup()
        tus.pencolor("aquamarine")
        tus.right(90)
        tus.forward(70)
        tus.left(90)
        tus.pendown()

        launcher.penup() 
        launcher.goto(0,30)
        launcher.color("deep pink")
        style = ("Game Over", 70, "bold")
        launcher.write("Start Menu", font=style, align="center")
        launcher.pendown()

        launcher.penup()
        launcher.goto(0,-40)
        launcher.pendown()
        launcher.color("pink")
        style = ("Game Over", 70, "bold")
        launcher.write("Exit", font=style, align="center")
        
        

        #(-120.00,-20.00)

        if tus.position()<(-120.00,50.00):
            tus.penup()
            tus.goto(-120,-20)
            tus.pendown()
        tus.showturtle()
        
            
            

        

  

    def b(): #YUKARIYA YÖN TUŞU
        winsound.PlaySound("zapsplatatari.wav", winsound.SND_ASYNC)
        launcher.penup()
        launcher.pencolor("aquamarine")
        launcher.goto(0,-40)
        launcher.pendown()
        launcher.color("deep pink")
        style = ("Game Over", 70, "bold")
        launcher.write("Exit", font=style, align="center")
        
        #START MENU'DEN YUKARIYA GİTMESİNİ ENGELLEME
        if tus.position()>=(-120,-20): #Positionlar (x,y) ikilisine göre kıyaslar
            tus.hideturtle()
            tus.penup()
            tus.goto(-120,-20)
            tus.pendown()
        tus.showturtle()
        
        
        tus.penup()
        tus.left(90)
        tus.forward(70)
        tus.right(90)
        tus.pendown()


        launcher.penup() 
        launcher.goto(0,30)
        launcher.color("pink")
        style = ("Game Over", 70, "bold")
        launcher.write("Start Menu", font=style, align="center")
        launcher.pendown()

    def startgiris(): #START'A BASILDIĞINDA MOD EKRANINA GİRME TUŞU
        winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
        time.sleep(1)
        if tus.position()==(-120.00,50.00):
            girismenu.clear()
            tus.clear()
            launcher.clear()
            tus2.clear()

            #Start Menu'ye basıldıktan sonra açılan yeni ekran
            fa=turtle.Turtle()
            fa.shapesize(2,2,1)
            modresim=turtle.Screen()
            fa.color("brown1")
            fa.penup()
            fa.goto(-580,-100)
            fa.pendown()

            modresim.bgpic("modtercih.png")

            fa.pu()
            fa.goto(-153.81,0.45)
            fa.pd()

            def right():
                winsound.PlaySound("zapsplatatari.wav", winsound.SND_ASYNC)
                fa.pencolor("white")
                fa.pu()
                fa.forward(355)
                fa.pd()
                #(201.19,0.45)

                if fa.position()>(201.19,0.45):
                    fa.pu()
                    fa.goto(201.19,0.45)
                    fa.pd()
                    

            modresim.listen()    
            modresim.onkey(right, "Right")


            def modsecimiyap1():
                winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
                time.sleep(1)
                if fa.position()==(201.19,0.45):
                    modresim.clear()
                    yz1=turtle.Turtle()
                    yz1.pu()
                    yz1.home()
                    yz1.pd()

                    #MOD SEÇİLDİKTEN SONRA OYUN EKRANININ AÇILMASI
                    modresim.bgpic("yarasayıldızay.png")
                    winsound.PlaySound("zapsplatatari2.wav", winsound.SND_ASYNC)

                    #İMLEÇ KOORDİNATININ BELİRLENMESİ
                    yz1.pu()
                    yz1.color("brown1")
                    yz1.shapesize(2,2,1)
                    yz1.left(90)
                    yz1.pd()

                    

                    

                    #SKOR VE CAN OLUŞTURMA
                    can = 3
                    skor = 0



                    #Hedef oluşturucu
                    maxHedef=6
                    hedefler = []
                    
                    yarasarenk = ["yellow","green","pink","red","purple4","wheat4"]
                    
                    for miktar in range (maxHedef):
                        #HEDEF OLUŞTURMA
                        renksecici = random.choice(yarasarenk)
                        hedefler.append(turtle.Turtle())
                        hedeflery=random.randrange(-320,320)
                        hedeflerx=random.randrange(-600,600)
                        hedefler[miktar].pu()
                        hedefler[miktar].speed(1000)
                        hedefler[miktar].setposition(hedeflerx,hedeflery)
                        hedefler[miktar].pd()
                    
                        hedefler[miktar].color(renksecici)
                        if hedefler[miktar].color()==('red', 'red'):
                            hedefler[miktar].shape("yarasaresimkirmizi.gif")
                        if hedefler[miktar].color()==('purple4', 'purple4'):
                            hedefler[miktar].shape("yarasaresimkmor.gif")
                        if hedefler[miktar].color()==('wheat4', 'wheat4'):
                            hedefler[miktar].shape("yarasaresimkahverengi.gif")
                        if hedefler[miktar].color()==('pink', 'pink'):
                            hedefler[miktar].shape("yarasaresimapembe.gif")
                        if hedefler[miktar].color()==('green', 'green'):
                            hedefler[miktar].shape("yarasaresimyesil.gif")
                        if hedefler[miktar].color()==('yellow', 'yellow'):
                            hedefler[miktar].shape("yarasaresimsari.gif")
                            


                        hedefler[miktar].shapesize(2,2,1)
                        hedefler[miktar].pu()
                        hedefler[miktar].speed(0)
                        hedefler[miktar].pd()


                    def solacevir():
                        yz1.left(30)
                    def sagacevir():
                        yz1.right(30)
                    def hizartir():
                        global hiz
                        hiz+=1
                    def hizazalt():
                        global hiz
                        hiz-=1
                    def carpisma(x1,x2):
                        x = math.sqrt(math.pow(x1.xcor()-x2.xcor(),2) + math.pow(x1.ycor()-x2.ycor(),2))
                        if x < 20:
                            return True
                        
                        else:
                            return False


                    hareket=turtle.Screen()
                    hareket.tracer(2)
                    hareket.onkey(solacevir, "Left")
                    hareket.onkey(sagacevir, "Right")
                    hareket.onkey(hizartir, "Up")
                    hareket.onkey(hizazalt, "Down")


                    while True:
                        yz1.shape("arrow")
                        yz1.pu()
                        yz1.forward(hiz)
                        yz1.pd()
                        

                        #X VE Y KOORDİNATINDAN DIŞARI ÇIKMASINI ENGELLEME
                        if yz1.ycor() > 355 or yz1.ycor()<-355:
                            yz1.right(180)
                            winsound.PlaySound("fire.wav", winsound.SND_ASYNC)
                            
                        if yz1.xcor() > 630 or yz1.xcor()<-630:
                            yz1.right(180)
                            winsound.PlaySound("fire.wav", winsound.SND_ASYNC)

                        



                        #HEDEFİ TAŞIMA
                        for miktar in range(maxHedef):
                            hedefler[miktar].pu()
                            hedefler[miktar].forward(2)

                            #X VE Y KOORDİNATINDAN DIŞARI ÇIKMASINI ENGELLEME
                            if hedefler[miktar].ycor() > 345 or hedefler[miktar].ycor()<-345:
                                hedefler[miktar].right(180)
                                winsound.PlaySound("fire.wav", winsound.SND_ASYNC)
                                
                            if hedefler[miktar].xcor() > 620 or hedefler[miktar].xcor()<-620:
                                hedefler[miktar].right(180)
                                winsound.PlaySound("fire.wav", winsound.SND_ASYNC)


                            #çarpışma kontrolü (DOST, DÜŞMAN YARASA VS İMLEC)
                            if carpisma(yz1, hedefler[miktar]):
                                hedefler[miktar].pu()
                                hedefler[miktar].setposition(random.randint(-630,630), random.randint(-355,355))
                                hedefler[miktar].right(random.randint(0,360))
                                hedefler[miktar].pd()
                                   
                                muzik="zapsplatatari.wav"
                                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                                skor += 10


                                    
                                #CAN AZALTMA VE SKOR ARTTIRMA ALGORİTMASI
                                if (hedefler[miktar].color()==('red', 'red') or hedefler[miktar].color()==('purple4', 'purple4') or hedefler[miktar].color()==('wheat4', 'wheat4')):
                                    skor-=30

                                    can-=1

                                
                                    
                                    if can==-1:
                                        turtle.clear()
                                        turtle.reset()
                                        hareket.clear()
                                        hareket.reset()
                                        modresim.clear()
                                        modresim.reset()
                                        
                                        
                                        
                                        
                                        #SKOR TABLOSU ÇİZİMİ
                                        skortablosuuarkaplan=turtle.Screen()
                                        skortablosuuarkaplan.bgpic("startmenu.gif")
                                        skortablosu=turtle.Turtle()
                                        skortablosu.color('deep pink')
                                        skortablosu.pu()
                                        skortablosu.setposition(-300,-300)
                                        skortablosu.pd()
                                        skortablosu.pensize(8)

                                        for i in range(4):
                                            skortablosu.dot(20,"brown1")
                                            skortablosu.fd(600)
                                            skortablosu.lt(90)


                                        skortablosu.pu()
                                        skortablosu.hideturtle()
                                        skortablosu.goto(0,0)
                                        skortablosu.left(90)
                                        skortablosu.fd(210)
                                        skortablosu.color('deep pink')
                                        style = ('Courrier', 50, 'bold')
                                        skortablosu.write('SKOR TABLOSU', font=style, align='center')
                                        skortablosu.goto(0,80)
                                        skortablosu.right(90)
                                        skortablosu.backward(270)
                                        skortablosu.pd()
                                        

                                        if (skor<=0):
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
 
                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)

                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)


                                        if (skor==10):
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
 
                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()

                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)


                                        if (skor>=20):
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
 
                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()

                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)






                                        
                                            

                                        

                                        #SKOR DEĞERLENDİRMESİ
                                        skortablosu.pu()
                                        skortablosu.goto(0,-150)
                                        skorsonucyaz="SKOR DEĞERLENDİRMENİZ: "
                                        toplamskor=skorsonucyaz+str(skor)
                                        skortablosu.color("brown1")
                                        style = ('Courrier', 25, 'bold')
                                        skortablosu.write(toplamskor, font=style, align='center')
                                        time.sleep(1)
                                        canyazici.hideturtle()
                                        skortablosu.home()
                                        skortablosu.pd()
                                        exit()
                                        








                                        
                                    canyazici=turtle.Turtle()
                                    canyazici.pu()
                                    
                                    canyazici.hideturtle()
                                    konum=canyazici.pos()
                                    canyazici.setposition(-595,320)
                                    canyazicistring = "CAN: %s" %can
                                    canyazici.color("red")
                                    canyazici.write(canyazicistring, False, align="left", font=("Arial",18, "bold"))
                                    canyazici.color("black")
                                    time.sleep(1)
                                    canyazici.clear()
                                    canyazici.goto(konum)

 

                                #EKRANDA SKORUN YAZDIRILMASI
                                skoryazici=turtle.Turtle()
                                
                                skoryazici.pu()
                                skoryazici.hideturtle()
                                konum=skoryazici.pos()
                                skoryazici.setposition(-595,300)
                                
                                skoryazicistring = "SKOR: %s" %skor
                                skoryazici.color("red")
                                skoryazici.write(skoryazicistring, False, align="left", font=("Arial",18, "bold"))
                                skoryazici.color("black")
                                time.sleep(1)
                                skoryazici.clear()
                                
                                skoryazici.goto(konum)
                                skoryazici.showturtle()

                              

                                #5 Skora ulaşınca ekranın rastgele yerinde kombo dairesi çıksın ve onu yiyince skora+10 eklesin




            modresim.onkey(modsecimiyap1, "s")
            

            def left():
                winsound.PlaySound("zapsplatatari.wav", winsound.SND_ASYNC)
                fa.pencolor("white")
                fa.pu()
                fa.backward(355)
                fa.pd()
                #(-153.81,0.45)

                if fa.position()<(-153.81,0.45):
                    fa.penup()
                    fa.goto(-153.81,0.45)
                    fa.pendown()


            modresim.listen()
            modresim.onkey(left, "Left")

            def modsecimiyap():
                winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
                time.sleep(1)
                if fa.position()==(-153.81,0.45):
                    modresim.clear()
                    yz=turtle.Turtle()
                    yz.pu()
                    yz.home()
                    yz.pd()

                    #MOD SEÇİLDİKTEN SONRA OYUN EKRANININ AÇILMASI
                    modresim.bgpic("yarasabackground.png")
                    winsound.PlaySound("zapsplatatari2.wav", winsound.SND_ASYNC)

                    

                    #İMLEÇ KOORDİNATININ BELİRLENMESİ
                    yz.pu()
                    yz.color("brown1")
                    yz.shapesize(2,2,1)
                    yz.left(90)
                    yz.pd()

                    

                    

                    
                    

                    #SKOR VE CAN OLUŞTURMA
                    can = 3
                    skor = 0
                    

                    #Hedef oluşturucu
                    maxHedef=6
                    hedefler = []
                    
                    yarasarenk = ["yellow","green","pink","red","purple4","wheat4"]
                    
                    for miktar in range (maxHedef):
                        #HEDEF OLUŞTURMA
                        renksecici = random.choice(yarasarenk)
                        hedefler.append(turtle.Turtle())
                        hedeflery=random.randrange(-320,320)
                        hedeflerx=random.randrange(-600,600)
                        hedefler[miktar].pu()
                        hedefler[miktar].speed(1000)
                        hedefler[miktar].setposition(hedeflerx,hedeflery)
                        hedefler[miktar].pd()
                    
                        hedefler[miktar].color(renksecici)
                        if hedefler[miktar].color()==('red', 'red'):
                            hedefler[miktar].shape("yarasaresimkirmizi.gif")
                        if hedefler[miktar].color()==('purple4', 'purple4'):
                            hedefler[miktar].shape("yarasaresimkmor.gif")
                        if hedefler[miktar].color()==('wheat4', 'wheat4'):
                            hedefler[miktar].shape("yarasaresimkahverengi.gif")
                        if hedefler[miktar].color()==('pink', 'pink'):
                            hedefler[miktar].shape("yarasaresimapembe.gif")
                        if hedefler[miktar].color()==('green', 'green'):
                            hedefler[miktar].shape("yarasaresimyesil.gif")
                        if hedefler[miktar].color()==('yellow', 'yellow'):
                            hedefler[miktar].shape("yarasaresimsari.gif")
                        
                        hedefler[miktar].shapesize(2,2,1)
                        hedefler[miktar].pu()
                        hedefler[miktar].speed(0)
                        hedefler[miktar].pd()


                    def solacevir():
                        yz.left(30)
                    def sagacevir():
                        yz.right(30)
                    def hizartir():
                        global hiz
                        hiz+=1
                    def hizazalt():
                        global hiz
                        hiz-=1
                    def carpisma(x1,x2):
                        x = math.sqrt(math.pow(x1.xcor()-x2.xcor(),2) + math.pow(x1.ycor()-x2.ycor(),2))
                        if x < 20:
                            return True
                        else:
                            return False
                        

                    hareket=turtle.Screen()
                    hareket.tracer(2)
                    hareket.onkey(solacevir, "Left")
                    hareket.onkey(sagacevir, "Right")
                    hareket.onkey(hizartir, "Up")
                    hareket.onkey(hizazalt, "Down")


                    while True:
                        yz.shape("arrow")
                        yz.pu()
                        yz.forward(hiz)
                        yz.pd()

                        #X VE Y KOORDİNATINDAN DIŞARI ÇIKMASINI ENGELLEME
                        if yz.ycor() > 355 or yz.ycor()<-355:
                            yz.right(180)
                            winsound.PlaySound("fire.wav", winsound.SND_ASYNC)
                            
                        if yz.xcor() > 630 or yz.xcor()<-630:
                            yz.right(180)
                            winsound.PlaySound("fire.wav", winsound.SND_ASYNC)



                        #HEDEFİ TAŞIMA
                        for miktar in range(maxHedef):
                            hedefler[miktar].pu()
                            hedefler[miktar].forward(2)

                            #X VE Y KOORDİNATINDAN DIŞARI ÇIKMASINI ENGELLEME
                            if hedefler[miktar].ycor() > 345 or hedefler[miktar].ycor()<-345:
                                hedefler[miktar].right(180)
                                winsound.PlaySound("fire.wav", winsound.SND_ASYNC)
                                
                            if hedefler[miktar].xcor() > 620 or hedefler[miktar].xcor()<-620:
                                hedefler[miktar].right(180)
                                winsound.PlaySound("fire.wav", winsound.SND_ASYNC)


                            #çarpışma kontrolü
                            if carpisma(yz, hedefler[miktar]):
                                hedefler[miktar].pu()
                                hedefler[miktar].setposition(random.randint(-630,630), random.randint(-355,355))
                                hedefler[miktar].right(random.randint(0,360))
                                hedefler[miktar].pd()
                                   
                                muzik="zapsplatatari.wav"
                                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                                skor += 10
                                

                                
                                    
                                #CAN AZALTMA VE SKOR ARTTIRMA ALGORİTMASI
                                if (hedefler[miktar].color()==('red', 'red') or hedefler[miktar].color()==('purple4', 'purple4') or hedefler[miktar].color()==('wheat4', 'wheat4')):
                                    skor-=30

                                    can-=1
                                    
                                    if can==-1:
                                        turtle.clear()
                                        turtle.reset()
                                        hareket.clear()
                                        hareket.reset()
                                        modresim.clear()
                                        modresim.reset()
                                        
                                        
                                        
                                        #SKOR TABLOSU ÇİZİMİ
                                        skortablosuarkaplan=turtle.Screen()
                                        skortablosuarkaplan.bgpic("startmenu.gif")
                                        skortablosu=turtle.Turtle()
                                        skortablosu.hideturtle()
                                        skortablosu.color('deep pink')
                                        skortablosu.pu()
                                        skortablosu.setposition(-300,-300)
                                        skortablosu.pd()
                                        skortablosu.pensize(8)

                                        for i in range(4):
                                            skortablosu.dot(20,"brown1")
                                            skortablosu.fd(600)
                                            skortablosu.lt(90)


                                        skortablosu.pu()
                                        skortablosu.goto(0,0)
                                        skortablosu.left(90)
                                        skortablosu.fd(210)
                                        skortablosu.color('deep pink')
                                        style = ('Courrier', 50, 'bold')
                                        skortablosu.write('SKOR TABLOSU', font=style, align='center')
                                        skortablosu.goto(0,80)
                                        skortablosu.right(90)
                                        skortablosu.backward(270)
                                        skortablosu.pd()


                                        if (skor<=0):
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
 
                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)

                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)


                                        if (skor==10):
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
 
                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()

                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)


                                        if (skor>=20):
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
 
                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()

                                            skortablosu.penup()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
                                            skortablosu.forward(200)
                                            skortablosu.pendown()
                                            #YILDIZ
                                            skortablosu.begin_fill()
                                            for i in range(5):
                                                skortablosu.color("yellow")
                                                skortablosu.forward(150)
                                                skortablosu.right(144)
                                            skortablosu.end_fill()
                                            winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)


                                        #SKOR DEĞERLENDİRMESİ
                                        skortablosu.pu()
                                        skortablosu.goto(0,-150)
                                        skorsonucyaz="SKOR DEĞERLENDİRMENİZ: "
                                        toplamskor=skorsonucyaz+str(skor)
                                        skortablosu.color("brown1")
                                        style = ('Courrier', 25, 'bold')
                                        skortablosu.write(toplamskor, font=style, align='center')
                                        time.sleep(1)
                                        canyazici.hideturtle()
                                        skortablosu.home()
                                        skortablosu.pd()
                                        exit()
                                        








                                        
                                    canyazici=turtle.Turtle()
                                    canyazici.color("aquamarine")
                                    canyazici.pu()
                                    
                                    konum=canyazici.pos()
                                    canyazici.setposition(-595,320)
                                    canyazicistring = "CAN: %s" %can
                                    canyazici.color("red")
                                    canyazici.write(canyazicistring, False, align="left", font=("Arial",18, "bold"))
                                    canyazici.color("aquamarine")
                                    time.sleep(1)
                                    canyazici.clear()
                                    canyazici.goto(konum)

 

                                #EKRANDA SKORUN YAZDIRILMASI
                                skoryazici=turtle.Turtle()
                                
                                skoryazici.pu()
                                skoryazici.hideturtle()
                                konum=skoryazici.pos()
                                skoryazici.setposition(-595,300)
                                
                                skoryazicistring = "SKOR: %s" %skor
                                skoryazici.color("red")
                                skoryazici.write(skoryazicistring, False, align="left", font=("Arial",18, "bold"))
                                skoryazici.color("aquamarine")
                                time.sleep(1)
                                skoryazici.clear()
                                
                                skoryazici.goto(konum)
                                skoryazici.showturtle()

                              

                                #5 Skora ulaşınca ekranın rastgele yerinde kombo dairesi çıksın ve onu yiyince skora+10 eklesin

            modresim.onkey(modsecimiyap, "w")
            

#İLGİLİ FONKSİYON İÇİNDE PROJENİN KAPATILMASI          
    def exitgiris():
        winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
        time.sleep(1)
        if tus.position()==(-120,-20.00):
            exit()

        
    tus2.onkey(b, "Up")
    tus2.onkey(f, "Down")
    tus2.onkey(startgiris, "w")
    tus2.onkey(exitgiris, "s")
    
    tus2.listen()
    
    
    
        
launcher()


       
    

