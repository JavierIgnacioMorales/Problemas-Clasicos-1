import threading
import random
import time
import logging
from rwlock import RWLock

logging.basicConfig(format='%(asctime)s.%(msecs)04d %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

equipos = ["Boca", "River", "Racing", "Independiente", "San Lorenzo", "Huracán", "Gimnasia",
           "Estudiantes", "Velez", "Ferro", "Lanus", "Quilmes"]

class Escritor(threading.Thread):

    def __init__(self, partido, lock):
        super().__init__()
        self.partido = partido
        self.llave_Escritor = lock


    def run(self):

        while True:
            self.llave_Escritor.w_acquire()
            try:
                equipo_1 = random.choice(equipos)
                equipo_2 = random.choice(equipos)
                while equipo_1 == equipo_2:
                    equipo_2 = random.choice(equipos)
                self.partido.append((equipo_1, random.randint(0,3),equipo_2, random.randint(0,3)))
                logging.info("Partido actualizado por Escritor: %s",self.name[7:])
            finally:
                self.llave_Escritor.w_release()
                time.sleep(random.randint(1,2))



class Lector(threading.Thread):

    def __init__(self, partido, lock):
        super().__init__()
        self.partido = partido
        self.llave_Lector = lock


    def run(self):
        while True:
            self.llave_Lector.r_acquire()
            try:
                logging.info( 'Lector %s',self.name[7:]+':  El resultado fue: {0[0]} {0[1]} - {0[2]} {0[3]} '.format(random.choice(self.partido)))
            finally:
                #time.sleep(random.randint(1,2))
                self.llave_Lector.r_release()
                time.sleep(random.randint(1,2))



def main():

    partido = []
    hilos = []
    lock = RWLock()

    escritor= Escritor(partido, lock)
    hilos.append(escritor)
    escritor.start()

    for i in range(4):
        lector= Lector(partido,lock)
        hilos.append(i)
        lector.start()

    for i in hilos:
        i.join()


if __name__ == '__main__':
    main()
