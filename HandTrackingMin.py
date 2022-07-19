# minimal code to run de program:

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils  # draw the hands points on the images

pTime = 0
cTime = 0

while True:
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)#print how many hands have been detected(2 is the maximum)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm) print landmark values
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h) # landmark value center pixel. landmark = hand points
                print(id, cx,cy)
                if id == 0: # imprimimos el lm con id = 0
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

            # draw the conections between the hand points
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # print the fps
    cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255, 3))

    cv2.imshow("Image", img)
    cv2.waitKey(1)
