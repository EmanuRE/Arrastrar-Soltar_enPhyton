#Uso de los Modulos cv2, numpy y mediapipe
import cv2
import numpy as np
import mediapipe as mp

# Módulos de MediaPipe para la detección de manos a traves de la camara
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Variables que permiten seguir el objeto
obj_pos = [300, 300]  # Posición inicial del objeto
obj_radius = 35  # Radio del objeto
obj_selected = False  # Estado de selección del objeto | sin seleccionar

# Ajuste de la resolución de la camara
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Ancho
cap.set(4, 720)   # Alto

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()

# Configurar MediaPipe para poder detectar las manos
with mp_hands.Hands(
    min_detection_confidence=0.8,  # Margen de confianza minima para detectar la mano
    min_tracking_confidence=0.5) as hands:  # Margen de confianza minima para seguir la mano

    while cap.isOpened():
        ret, frame = cap.read()  # Captura de los fotogramas de la camara

        if not ret:
            print("No se puede capturar el video")
            break
        
        frame = cv2.flip(frame, 1)  # Permitir una imagen intuitiva
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Se convierte a RGB para MediaPipe

        result = hands.process(rgb_frame)  # Se procesa el fotograma con el modelo de manos

        # Cuando se lleguen a detectar manos en la imagen
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Se obtiene el espacio o dimension del frame
                h, w, _ = frame.shape
                
                # Permite obtener las coordenas donde esta el indice y el pulgar
                index_finger_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]

                index_pos = (int(index_finger_tip.x * w), int(index_finger_tip.y * h))
                thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))

                # Calculo de espacio entre el indice y el pulgar
                distance = np.linalg.norm(np.array(index_pos) - np.array(thumb_pos))

                # Detectar si el indice y el pulgar estan juntos (gesto de agarre del objeto)
                if distance < 50:
                    if not obj_selected:
                        # Se detecta si el indice esta sobre el objeto
                        if np.linalg.norm(np.array(index_pos) - np.array(obj_pos)) < obj_radius + 10:
                            obj_selected = True
                else:
                    obj_selected = False  # Dejar el objeto por falta de agarre

                # Cuando se agarre el objeto, se mueve a la posicion del dedo índice
                if obj_selected:
                    obj_pos = index_pos

                # Se establecen los puntos y conexiones de la mano derecha
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Se dibuja el circulo rojo en la imagen (se puede ajustar el color)
        cv2.circle(frame, tuple(obj_pos), obj_radius, (0, 0, 255), -1)

        # Mostrar imagen de camara en una ventana
        cv2.imshow('Arrastrar & Soltar - IA', frame)

        # Se presiona la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Se cierra la camara y las ventanas
cap.release()
cv2.destroyAllWindows()