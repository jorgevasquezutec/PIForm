import requests
import random
import json
import time
import sys


#URL COPIA
url="https://docs.google.com/forms/u/0/d/e/1FAIpQLSdYu5D8FWnu5q_wGKLXGDiaYjCzDrFBEfZ1bcfV5Zk8wb9Txg/formResponse"
#URL ORIGINAL
# url="https://docs.google.com/forms/u/0/d/e/1FAIpQLSfeb7as_jzQOD4EsDAe5nJa3iUBe9yrPbs-zPywf73aIAG_PA/formResponse"

options=[
    {"data":["Superior Técnico Completa","Superior Universitaria Incompleta","Superior Universitaria Completa","Postgrado Universitario"],"multi":False,"id":"entry.434501224"},
    {"data":["Computadora, laptop, tablet en funcionamiento","Lavadora en funcionamiento","Horno microondas en funcionamiento","Refrigeradora/Congeladora en funcionamiento"],"multi":True,"id":"entry.600359236"},
    {"data":["Auto o camioneta solo para uso particular (NO TAXI NI AUTO DE LA EMPRESA)","Servicio doméstico en el hogar pagado (MÍNIMO QUE VAYA AL HOGAR UNA VEZ POR SEMANA)","Ninguno de los anteriores"],"multi":False,"id":"entry.1951667386"},
    {"data":["Losetas /terrazos, mayólicas, cerámicos, vinílicos, mosaico o similares","Parquet o madera pulida y similares; porcelanato, alfombra, mármol"],"multi":False,"id":"entry.867290208"},
    {"data":["Entidad prestadora de salud (EPS)/Seguro privado de salud","ESSALUD"],"multi":False,"id":"entry.1219269864"},
    {"data":["Ladrillo o bloque de cemento"],"multi":False,"id":"entry.1054334888"},
    {"data":["Baño dentro de la vivienda"],"multi":True,"id":"entry.2068064588"},
    {"data":["18 a 24 años","Menor a 18","25 a 34 años"],"multi":False,"id":"entry.829362305"},
    {"data":["Masculino","Femenino"],"multi":False,"id":"entry.1335896991"},
    {"data":["Estudiante","Trabajador"],"multi":False,"id":"entry.82645235"},
    {"data":["1","2","3","3 o más","No hay bicicletas"],"multi":False,"id":"entry.511586506"},
    {"data":["Bicicleta","Carro","Moto","Transporte Público"],"multi":False,"id":"entry.332006789"},
    {"data":["No hay suficientes ciclovías","Es inseguro","Por la distancia a recorrer","Por el clima"],"multi":True,"id":"entry.729705553"},
    {"data":["Diario","Fin de semana","De vez en cuando","No la uso","No tengo bicicleta"],"multi":False,"id":"entry.1864285519"},
    {"data":["Eléctricas","De paseo","De carrera","Montañeras","No tengo bicicleta"],"multi":False,"id":"entry.789230503"},
    {"data":["Distancia larga","Distancia corta"],"multi":False,"id":"entry.520306883"},
    {"data":["15 a 30 min","30 a 60 min","Más de una hora","No manejo bicicleta"],"multi":False,"id":"entry.1070535978"},
    {"data":["Sí","No"],"multi":False,"id":"entry.892471230"},
    {"data":["Realizo actividad física","Evitar el tráfico de los carros","Es eco amigable","Me divierte"],"multi":True,"id":"entry.993089940"},
    {"data":["Sí"],"multi":False,"id":"entry.1153549636"},
    {"data":["Sí, me gustaría"],"multi":False,"id":"entry.1504398395"},
    {"data":["Solar","Uso de la energía del pedaleo"],"multi":True,"id":"entry.690311723"},
    {"data":["Sí, me gustaría","No lo sé","No, me parece innecesario"],"multi":False,"id":"entry.2141766592"},
    {"data":["Precio","Calidad","Rapidez","Cuidado el medio ambiente"],"multi":True,"id":"entry.376303385"},
    {"data":["Sí, me parece genial","Podría mejorar","No, no me gusta"],"multi":False,"id":"entry.1211722380"},
    {"data":["S/.300- S/.500","S/.500- S/.700","S/.700- S/.900","S/.900 a más"],"multi":False,"id":"entry.1442261410"}
]



def main(arg1):

    for iteration in range(int(arg1)):
        #de 1 a 10 miutos.
        values={}
        timeSleepRamdom=random.randint(1,10);
        for option in options:
            dat=option['data']
            if(option['multi']):
                n=random.randint(1,len(dat))
                values[option['id']]=random.sample(dat,n)
            else:
                n=random.randint(0,len(dat)-1)
                values[option['id']]=dat[n];

        r =requests.post(url, data=values)
        requestOuput={"numberOfIteration":iteration,"status":r.status_code,"data":values,"timeSleep":timeSleepRamdom}
        print(json.dumps(requestOuput))
        time.sleep(timeSleepRamdom*60)


#ejecutar el comando pasandole la cantidad de request que quieres hacer:
if __name__ == "__main__":
    main(sys.argv[1])

# print(json.dumps(values)) 
# print(r);




