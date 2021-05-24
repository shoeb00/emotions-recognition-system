from future.moves import tkinter
from tkinter.filedialog import askopenfilename
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np

filetypes = (('mp4 files', '*.mp4'), ('mkv files', '*.mkv'), ('mov files', '*.mov'))


face_classifier = cv2.CascadeClassifier('./docs/haarcascade_frontalface_default.xml')
classifier = load_model('./models/take2_model_E25.h5')
# BGR
RED = (0, 0, 255)
GREEN = (30, 238, 30)
BLUE = (242, 184, 48)
PURPLE = (211, 0, 148)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
emotion_color_map = {'Angry': RED, 'Happy': GREEN, 'Surprise': BLUE, 'Neutral': PURPLE, 'Sad': GRAY}


def videoHandler():
    path = input('Select Input\n1.Webcam\t2.Video file:\n>>')
    if path == '1':
        cap = cv2.VideoCapture(0)
        print('launching camera...')
        print('Initiating the model...')
    elif path == '2':
        root = tkinter.Tk()
        root.withdraw()

        file_path = askopenfilename(initialdir='/Users/apple', title='image', filetypes=filetypes)
        cap = cv2.VideoCapture(file_path)
        print('Analyzing the video...')
    else:
        print('Invalid input')
        exit()
    while True:
        # Grab a single frame of video
        ret, frame = cap.read()
        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 2)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                # make a prediction on the ROI, then lookup the class

                preds = classifier.predict(roi)[0]
                # print("prediction = ", preds)
                label = class_labels[preds.argmax()]
                # print("prediction max = ", preds.argmax())
                cv2.rectangle(frame, (x, y), (x + w, y + h), emotion_color_map[label], 2)
                # print("Emotion = ", label, "\n")
                label_position = (x, y)
                cv2.rectangle(frame, (x, y), (x + int(w / 2.5), y - int(h / 12)), emotion_color_map[label], -1)
                cv2.putText(frame, label, label_position,
                            cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
            else:
                cv2.putText(frame, 'No Face Found', (20, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 3)
            # print("\n\n")
        small_frame = cv2.resize(frame, (960, 540))
        cv2.imshow("Emotion Detector - Press 'q' to quit", small_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# videoHandler()
