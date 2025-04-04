# Sistema para arrastrar y Soltar usando el seguimiento de manos en Phyton

## Descripción
En este proyecto se implementa un sistema interactivo que permite abrir un visor en la computadora para poder arrastrar y soltar un objeto virtual, en este caso un "Circulo Rojo", se puede mover usando los gestos de la mano. Para este sistema  se usa la biblioteca de MediaPipe para poder identificar las manos en tiempo real a traves de la Webcam.

## Características principales
- Detección en tiempo real de las manos usando MediaPipe
- Interacción por medio de los gestos, usando el indice y pulgar de la mano
- El objeto virtual sigue los movimientos de la mano
- Se visualizan los puntos de referencia de la mano
- Se configura la resolución para adaptar la cámara

## Requisitos del sistema
 - Phyton 3.x (compatible con MediaPipe) - 3.7 o superior
 - OpenCV (pip install opencv-python)
 - MediaPipe (pip install mediapipe)
 - NumPy (pip install numpy)

## Instrucciones para su uso
1. Se ejecuta el script: python visorphyton.py
2. Se mueve la mano al frente de la cámara
3. Se arrastra el objeto de la siguiente forma:
    - Acercar el dedo indice al objeto
    - Realizar el gesto de pinza (Juntar el índice y pulgar)
4. Soltar el objeto:
    - Separar los dedos índice y pulgar
5. Presionar la tecla "q" para salir del sistema

## Configuración del sistema

    - min_detection_confidence: Permite ajustar la sensibilidad de la detección de manos (0-1)
    - min_tracking_confidence: Permite ajustar la sensibilidad del seguimiento de manos (0-1)
    - obj_radius: Ajusta el tamaño del objeto
    - Ajuste de la resolución de cámara: Se hace el ajuste en la linea cap.set(3, 1280) y en cap.set (4,720)

## Estructura del codigo usado

- Se importan los modulos de cv2, numpy, mediapipe

- Configuraciones
    - Se inicia MediaPipe
    - Se añaden parametros del objeto virtual
    - se Configura la cámara

- Se usa un bucle principal para lo siguiente:
    - Capturar los fotogramas
    - Procesar con MediaPipe
    - Detectar los gestos
    - Actualizar la posicion del objeto
    - Visualizar en pantalla

## Notas del sistema
    - Este sistema tiene una mejro función cuando hay una buena iluminación en el fondo
    - Es recomendable usar el programa donde no existan fondos muy complejos o con diseños que afecten la funcionalidad
    - Se puede ajustar la sensibilidad de identificar la pinza, modificando el valor de la distancia entre ambos dedos. En este momento tiene 50px
    



