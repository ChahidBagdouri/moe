# Author: Abdullah Mohammad

import cv2
from deepface import DeepFace
import sounddevice as sd
import soundfile as sf

cascPath = 'OpenCV_Cascades/haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0) # Change this num to change camera
imgcount = 0
# Function to play sound
def play_sound(file):
    data, fs = sf.read(file, dtype='float32')
    sd.play(data, fs)
    sd.wait()

print("Press Q to quit")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # save image to path
    cv2.imwrite("img.jpg", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Quit using Q
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(faces) == 0:
        continue

    emotions = DeepFace.analyze("img.jpg", actions=("emotion"), detector_backend='opencv', enforce_detection=False)
    negative_emotions = ["angry", "sad", "fear", "disgust"]
    dominant_emotion = emotions[0]["dominant_emotion"]
    print(dominant_emotion)
    if dominant_emotion in negative_emotions:
        print(f'Negative emotion detected: {dominant_emotion}')
        filename = f"database/{dominant_emotion}_{str(imgcount)}.jpg"
        cv2.imwrite(filename, frame)
        if dominant_emotion in ["angry", "disgust"]:
            play_sound("oof.wav")
        elif dominant_emotion in ["sad", "fear"]:
            play_sound("trombone.wav")
            pass
        imgcount+=1

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
