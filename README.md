# SEDA
Sistemas Electrónicos Digitales Avanzados

Se trata de un sistema empotrado basado en el Micro ARM Cortex-M3 LPC1769, que hará de cerebro de un robot de tracción diferencial capaz de seguir una secuencia de órdenes.

Se partirá de una plataforma mecánica de metacrilato de un tamaño superior al de la Mini-DK2, a la que se le acoplarán los dos motores de corriente continua que proporcionan la tracción a las dos ruedas, y una tercera rueda de apoyo que da estabilidad al sistema. Cada motor integra un encoder en cuadratura que será utilizado para medir la distancia recorrida por el robot y ajustar el movimiento de cada rueda para proporcionar correctamente los giros deseados. Para el control de los motores, se utiliza un puente en H.

El sistema representa en un display las medidas tomadas mediante un ADC que hacen referencia a la batería y al umbral deseado y dispondrá de un medidor de tensión de alimentación con aviso acústico (pitido de 2KHz) en caso de baja tensión de entrada con un altavoz conectado a un DAC.
También se visualizan estadísticas como la distancia recorrida, los grados o la velocidad de las ruedas, gracias a unos cálculos matemáticos sencillos que se hacen a raíz de las señales de entrada que se toman de los encoders de las ruedas.

Además, se permite aumentar la velocidad de los motores (sólo en modo Debug). Este aumento, que se realiza mediante el display, es directamente llevado a un módulo PWM que habilita los motores y hacen que el robot avance.
El robot también cuenta con una máquina de estados que se encarga de decodificar una secuencia de movimientos (avanzar una distancia determinada en centímetros, girar, reproducir audio...).

Se utiliza la UART para comunicarnos vía serie asíncrona con un terminal (en este caso el PC, gracias al programa termite) y poder tanto recibir como dar órdenes. Desde el terminal podemos solicitar la velocidad o la distancia, o también podemos enviar un cambio de modo, una secuencia de movimientos o poner a una velocidad determinada las ruedas. Para esta parte también se emplea una máquina de estados encargada de esperar que se haya terminado de enviar o de recibir y luego de comparar lo recibido con una serie de órdenes determinadas.

Se introduce un servidor web empotrado, con una página web que muestra la batería, el umbral y el modo de funcionamiento. Además, permite cambiar de modo y enviar una secuencia de movimientos.

Finalmente, contamos con un mando Nunchuck, que será usado en el modo manual. Nos comunicamos con él mediante I2C, y hacemos que el robot haga caso a los valores del joystick para moverse, el botón C para grabar y el botón Z para reproducir audio.

El sistema hace un uso frecuente de diferentes timers y está diseñado para cambiar de modo con el botón de la tarjeta (ISP). Los modos utilizados en el funcionamiento son el modo manual, automático y depuración (debug).

Emplea el TIMER 2 en modo match, que interrumpe cada 100ms, para realizar los cálculos de las estadísticas y las operaciones. Además, este timer está configurado en modo capture para detectar las señales de entrada de los encoders.
El ADC muestrea a 10Hz en modo burst con la interrupción del TIMER 1 y el DAC hace uso del TIMER 3 para sacar las muestras, con una frecuencia de 2KHz para el pitido de la alarma y 8KHz para el audio.
El TIMER 0 en modo match se usa para el I2C interrumpiendo cada segundo, mirando si el modo es manual y leyendo el mando en ese caso.
Durante el modo debug, se hará caso únicamente al display para el movimiento del robot. En el modo automático, las secuencias de movimiento recibidas por el servidor web o la UART serán las que hagan que el robot se mueva, y finalmente para el modo debug, se hará caso al mando Nunchuck.

Se hará uso de prioridades y timers para lograr un buen comportamiento del robot y evitar conflictos. Así como un estudio de la ejecutabilidad del sistema teniendo en cuenta prioridades, regiones críticas, tiempos de ejecución, periodos de activación y plazos de respuesta para cada tarea.


MANUAL DE USUARIO:
El robot es capaz de realizar las siguientes tareas:
- Comunicaciones asíncronas a través del software Termite. Los comandos que podemos introducir son los siguientes: SetVel, GetVel, SetModo, SetComando, GetPosicion, fin. Modo automático.
- Cuenta con una página web que permite cambiar el modo y enviar una secuencia de movimiento y visualizar la batería y el umbral. Modo automático.
- Un nunchuck para controlar el movimiento y reproducir audio. Modo manual.
- Un display táctil para manejar los motores. Modo Debug.
- Un display para visualizar una serie de características (velocidades, tensiones, IP, …).
A continuación, se propone una serie de pasos para comprobar su funcionamiento:
1) Abre el programa termite y sigue las instrucciones, comienza enviando tu nombre.
2) Introduce el comando "SetModo" y cambia a "Manual". Se puede ver la batería y el umbral en el display. Así como la velocidad de las ruedas, la distancia y la posición.
3) Prueba que el robot se mueve con el joystick y que al pulsar Z reproduce el audio.
4) En la página web cambia de modo a "Automático" y envía una cadena de comandos, como por ejemplo "R20DIA". Se muestra el comando en el display, así como la velocidad de las ruedas, la distancia y la posición.
5) Vuelve al programa termite, envía "SetComando" y envía un comando, por ejemplo, "R20DI".
6) Prueba enviar otro comando en la UART, por ejemplo, "GetPosición", "SetVel" o "GetVel".
7) Marca el modo "Debug" en la página web, también puedes cambiar de modo pulsando el botón ISP de la placa.
8) Ahora el movimiento de las ruedas los define el display, para ello pulsa el '+' o el '-' situados en la parte superior. Hay que ponerlo al 45% como mínimo para que las ruedas se muevan, menos porcentaje no es suficiente potencia y se pueden parar.
9) Para terminar, envía el comando "fin" en el programa termite.




