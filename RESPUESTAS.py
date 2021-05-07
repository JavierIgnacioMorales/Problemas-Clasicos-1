'''

Ejercicio 1
Respuesta punto 1.2:

** Los errores e inconsistencias se deben al mensaje que emite el assert cuando en la lista se quiere cargar otro dato
y esta esta llena, o cuando se quiere quitar algún dato y esta se encuentra vacía.

----------------------------------------------------------------------------------------------------------------------
Ejercicio 3

Respuesta punto 1.a:

Hay definidos dos Locks ( w_lock y num_r_lock) y el que genera la exclusión mutua es el que habilita la escritura,
es decir w_lock.

Respuesta punto 1.b:

b.1   La variable numérica num_r cuenta los hilos de lectura que adquieren el lock num_r_lock.acquire().
b.2     Obtendrá el w_lock el que tenga la variable num_r con valor 1. Los demás procesos continúan con la ejecución y
 liberan el num_r_lock.
b.3    Para poder liberar el w_lock el hilo debe tenerlo en su poder, una vez que haya leído el dato llamara al método
 r_release().
b.4     No creo que se le dé prioridad a ningún tipo de hilo, lo que ocurre es que al tener acceso de forma recurrente
 por parte de los hilos lectores, y donde seguramente hay otros como ellos esperando para poder leer, el hilo escritor
 tiene que esperar cuando le toque.




'''