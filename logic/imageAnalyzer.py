from deepface import DeepFace
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np


def deep_face(image, actions):
    # os.chdir('..')
    try:
        res = DeepFace.analyze(image, actions)
    except Exception as e:
        print('Exception reading the image', e)
        exit()
    # print('deep_face->', res)
    output = {}
    if 'emotion' in actions:
        output['Emotion'] = res['dominant_emotion']
    if 'age' in actions:
        output['Age'] = res['age']
    if 'gender' in actions:
        output['Gender'] = res['gender']
    if 'race' in actions:
        output['Race'] = res['dominant_race']

    return output


def pre_train(raw_image):
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

    image = cv2.imread(raw_image, 1)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray_image[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            prediction = classifier.predict(roi)[0]
            # print("prediction = ", prediction)
            label = class_labels[prediction.argmax()]
            # print("prediction max = ", prediction.argmax())
            cv2.rectangle(image, (x, y), (x + w, y + h), emotion_color_map[label], 2)
            print("Emotion = ", label, "\n")
            label_position = (x, y)
            cv2.rectangle(image, (x, y), (x + int(w / 2.5), y - int(h / 12)), emotion_color_map[label], -1)
            cv2.putText(image, label, label_position,
                        cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

        else:
            print('No face found')
            cv2.putText(image, 'No Face Found', (20, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 3)
            return None
        cv2.imshow("Emotion Detector - Press 'q' to quit", image)
        while cv2.waitKey(0) != ord('q'):
            pass
        cv2.destroyAllWindows()


# print(pre_train('/Users/apple/PycharmProjects/major1/static/uploads/Scarlett_Johanssen_Meme_Banner.jpg'))
