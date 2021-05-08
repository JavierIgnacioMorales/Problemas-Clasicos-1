import threading
import random
import time
import logging
from rwlock import RWLock

logging.basicConfig(format='%(asctime)s.%(msecs)04d %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

equipos = ["Boca", "River", "Racing", "Independiente", "San Lorenzo", "Huracán", "Gimnasia",
           "Estudiantes", "Velez", "Ferro", "Lanus", "Quilmes"]

def escritor(partido, name):

    llave_Escritor = RWLock()

    while True:
        llave_Escritor.w_acquire()
        try:
            equipo_1 = random.choice(equipos)
            equipo_2 = random.choice(equipos)
            while equipo_1 == equipo_2:
                equipo_2 = random.choice(equipos)
            partido.append((equipo_1, random.randint(0,3),equipo_2, random.randint(0,3)))
            logging.info("Partido actualizado por: %s",name)
        finally:
            llave_Escritor.w_release()
            time.sleep(random.randint(1,2))



def lector(partido,name):

    llave_Lector = RWLock()

    while True:
        llave_Lector.r_acquire()
        try:
            logging.info( '%s',name+':  El resultado fue: {0[0]} {0[1]} - {0[2]} {0[3]} '.format(random.choice(partido)))
        finally:
            #time.sleep(random.randint(1,2))
            llave_Lector.r_release()
            time.sleep(random.randint(1,2))



def main():

    partido = []
    hilos = []

    escritor1 = threading.Thread(target=escritor,args=(partido,"Escritor 1"))
    hilos.append(escritor1)
    escritor1.start()

    for i in range(4):
        lector1= threading.Thread(target=lector,args=(partido,"Lector "+str(i + 1)))
        hilos.append(i)
        lector1.start()

    for i in hilos:
        i.join()


if __name__ == '__main__':
    main()
