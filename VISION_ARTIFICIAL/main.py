import cv2
import csv
import random
import pandas as pd
import time
#cap=cv2.VideoCapture("video.mp4")

cap=cv2.VideoCapture("carros.mp4")
deteccion = cv2.createBackgroundSubtractorMOG2(history=10000,varThreshold=12) #Extrae los objetos en movimiento de una camara estable
deteccion1= cv2.createBackgroundSubtractorMOG2(history=10000,varThreshold=12)
deteccion2= cv2.createBackgroundSubtractorMOG2(history=10000,varThreshold=12)
deteccion3=cv2.createBackgroundSubtractorMOG2(history=10000,varThreshold=12)
car_cascade = cv2.CascadeClassifier('cars.xml')
area1=0
area2=0
area3=0

while True:

    ret,frame=cap.read()
    #renderizado del frame para expandir
    #frame = cv2.resize(frame,(1280,720)) 
    hora_actual=time.strftime('%H:%M:%S',time.localtime())
    retiros=[
    ['Persona','Placa','Local','Lugar_Estacionamiento','Hora_reserva','Hora_estacionamiento','Hora_retiro'],
    ]


    frame = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    zona1=frame[0:720,85:385]
    zona2=frame[0:720,360:660] 
    zona3=frame[0:720,600:900] 
    #FRAME TOTAL
    mascara = deteccion.apply(frame)
    _,mascara=cv2.threshold(mascara,254,255,cv2.THRESH_BINARY)

    #PARA LA ZONA 1
    
    mascara1=deteccion1.apply(zona1)
    _,mascara1=cv2.threshold(mascara1,254,255,cv2.THRESH_BINARY)

        #PARA LA ZONA 2
    
    mascara2 = deteccion2.apply(zona2)
    _,mascara2=cv2.threshold(mascara2,254,255,cv2.THRESH_BINARY)

        #PARA LA ZONA 2

    mascara3 = deteccion3.apply(zona3)
    _,mascara3=cv2.threshold(mascara3,254,255,cv2.THRESH_BINARY)
    #EVALUANDO EL FRAME
    #video_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    video_gris = cv2.cvtColor(zona1, cv2.COLOR_BGR2GRAY)
    #Se detectan los autos de diferentes medidas en cualquier parte del video
    autos = car_cascade.detectMultiScale(video_gris, 1.1, 1)
    for (x,y,w,h) in autos:
        #Se  dibujan los rectangulos alrededor de los autos en formato rgb sobre FRAME
         #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         cv2.rectangle(zona1,(x,y),(x+w,y+h),(0,255,0),2)
         area_nueva=w*h
         #52000 es el rango minimo que podria detectarse
         # en el movimiento vehicular
         if area_nueva>52000 :
            area1=area_nueva
            print('zona 1:',area1)
            for i in range (1,550):
                if(i%5==1):
                    hora_ran=random.randint(9,14)
                    min_ran=random.randint(0,30)
                    seg_ran=random.randint(0,60)
                    retiros.append(['Peter Castle','M4T-642','Santa Clara','A1','{}:00:00'.format(hora_ran),'{}:{}:42'.format(hora_ran,min_ran),'{}:{}:{}'.format(hora_ran+1,min_ran,seg_ran)])
                if(i%5==2):
                    hora_ran=random.randint(8,10)
                    min_ran=random.randint(0,30)
                    seg_ran=random.randint(0,60)
                    retiros.append(
                        ['Bala Garcia','R5F-445','Santa Clara','A2',
                        '{}:00:00'.format(hora_ran),
                        '{}:{}:42'.format(hora_ran,min_ran),
                        '{}:{}:{}'.format(hora_ran+1,min_ran,seg_ran)])
                if(i%5==3):
                    hora_ran=random.randint(8,10)
                    min_ran=random.randint(0,30)
                    seg_ran=random.randint(0,60)
                    retiros.append(
                    ['Botijas River','Y8U-456','Santa Clara','A3',
                    '{}:00:00'.format(hora_ran),
                    '{}:{}:42'.format(hora_ran,min_ran),
                    '{}:{}:{}'.format(hora_ran+1,min_ran,seg_ran)])
                if(i%5==4):
                    hora_ran=random.randint(7,9)
                    min_ran=random.randint(0,30)
                    seg_ran=random.randint(0,60)
                    retiros.append(
                    ['Alejandra Guinelli','W4T-345','Santa Clara','A1',
                    '{}:00:00'.format(hora_ran),
                    '{}:{}:42'.format(hora_ran,min_ran),
                    '{}:{}:{}'.format(hora_ran+1,min_ran,seg_ran)])
                if(i%5==0):
                    hora_ran=random.randint(14,20)
                    min_ran=random.randint(0,30)
                    seg_ran=random.randint(0,60)        
                    retiros.append(
                    ['Ronaldo Junior','M1G-642','Santa Clara','A1',
                    '{}:00:00'.format(hora_ran),
                    '{}:{}:42'.format(hora_ran,min_ran),
                    '{}:{}:{}'.format(hora_ran+1,min_ran,seg_ran)])
            archivo=open("entrenar.csv","w")
            print("El archivo se ha creado")

            with open('entrenar.csv','w',newline='') as file:
                writer=csv.writer(file,delimiter=',')
                #Con el punto y come(;) se puede visualizar correctamente en el Excel
                #writer=csv.writer(file,delimiter=';')
                writer.writerows(retiros)

            archivo.close()
            datos = pd.read_csv("entrenar.csv")

        #EL MAXIMO AREA ENCONTRADO EN EL AREA1 AL INGRESO DE UN VEHICULO ES 62500
         cv2.imshow("Main",frame)
         """ cv2.imshow("blancos y negros",mascara) """
         cv2.imshow("Primer tramo",zona1)
         """  cv2.imshow("Mascara del primer tramo ",mascara1) """
         """ cv2.imshow("Segundo tramo",zona2) """
         """ cv2.imshow("Mascara del segundo tramo ",mascara2) """
         """ cv2.imshow("Tercer tramo",zona3) """
         """ cv2.imshow("Mascara del tercer tramo ",mascara3) """
        
         #cv2.imshow("video gris",video_gris)
    video_gris2 = cv2.cvtColor(zona2, cv2.COLOR_BGR2GRAY)
    autos2 = car_cascade.detectMultiScale(video_gris2, 1.1, 1)
    for (x2,y2,w2,h2) in autos2:
         cv2.rectangle(zona2,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)
         area_nueva2=w2*h2
         if area_nueva2>area2 :
            area2=area_nueva2
            print('zona 2:',area2)
        #EL MAXIMO AREA ENCONTRADO EN EL AREA2 AL INGRESO DE UN VEHICULO ES 75625 (70000-78000)
        #AQUI SE ESTACIONA POR EJEMPLO

         cv2.imshow("Segundo tramo",zona2)

    video_gris3 = cv2.cvtColor(zona3, cv2.COLOR_BGR2GRAY)
    autos3 = car_cascade.detectMultiScale(video_gris3, 1.1, 1)
    for (x3,y3,w3,h3) in autos2:
         cv2.rectangle(zona3,(x3,y3),(x3+w3,y3+h3),(0,255,0),2)
         area_nueva3=w2*h2
         if area_nueva3>area3 :
            area3=area_nueva3
            print('zona 3:',area3)
         cv2.imshow("Tercer tramo",zona3)
        #EL MAXIMO AREA ENCONTRADO EN EL AREA2 AL INGRESO DE UN VEHICULO ES 75625 (70000-78000)

    key = cv2.waitKey(5)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
