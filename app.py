import cv2
 
def capturar_e_salvar():
 
    webcam = cv2.VideoCapture(0)
 
    if not webcam.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return

    fonte = cv2.FONT_HERSHEY_COMPLEX
    escala = 0.6
    cor_texto =(255, 255, 255)
    espessura = 1
 
    print("[ESPAÇO] Capturar e salvar foto")
    print("[ESC] Sair")
 
    while True:
        status, frame = webcam.read()
 
        if not status:
            print("Falha ao receber o frame da webcam.")
            break

        frame_limpo = frame.copy()

        cv2.rectangle(frame, (10,10), (320, 75), (0, 0, 0), -1)
        cv2.putText(frame, "[ESPAÇO] salvar foto", (20, 35), fonte, escala, cor_texto, espessura)
        cv2.putText(frame, "[ESCAPE] sair", (20, 60), fonte, escala, cor_texto, espessura)
 
        cv2.imshow("Captura da Webcam local", frame)
 
        tecla = cv2.waitKey(1) & 0xFF
 
        if tecla == 32:
            cv2.imwrite("foto.jpg", frame_limpo)
            print("Foto salva: foto.jpg")
 
            foto_cinza = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("foto_cinza.jpg", foto_cinza)
 
            foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_BAYER_BG2BGR)
            cv2.imwrite("foto_invertida.jpg", foto_invertida)
 
        elif tecla == 27:
            print ("Encerramento câmera...")
            break
 
    webcam.release()
    cv2.destroyAllWindows()
 
if __name__== "__main__":
    print()
    capturar_e_salvar()
 