import tkinter
from tkinter.filedialog import askopenfilename

from logic import imageAnalyzer

attributes = ['', 'Emotion', 'Age', 'Gender', 'Race', ['Emotion', 'Age', 'Gender', 'Race']]
filetypes = (('jpg files', '*.jpg'), ('jpeg files', '*.jpeg'), ('png files', '*.png'))


def selected_attributes(actions):
    print('selected attributes : ')
    for i in actions:
        if i != '':
            print(attributes[int(i)], ', ', end=' ')


def imageHandler():
    model = int(input('Select model\n1.Deepface\t2.Pre Trained\n>>'))
    while not 3 > model > -1:
        print('Provide a valid input')
        model = int(input('Select model\n0.Exit\t1.Deepface\t2.Pre Trained\n>>'))

    if model == 1:
        actions = {''}
        attribute = int(input('Select the attributes:\n1.Emotion\t2.Age\t3.Gender\t4.Race\t5.All\n>>'))
        actions.add(attribute)
        if 0 in actions:
            print('Provide a valid input')
            actions.discard(0)
        elif 0 > attribute > 5:
            print('Provide a valid input')
            actions.discard(attribute)
        while len(actions) < 5:
            if -1 > attribute or attribute > 5:
                print('Provide a valid input')
                actions.remove(attribute)
            elif 5 in actions:
                selected_attributes(actions)
                break
            elif attribute == 0:
                if len(actions) > 2:
                    selected_attributes(actions)
                    break
                else:
                    print('Provide a valid input')
                    actions.remove(attribute)
            selected_attributes(actions)
            attribute = int(input('\n\nSelect the attributes:\n0.Confirm\t1.Emotion\t2.Age\t3.Gender\t4.Race\t5.All\n>>'))
            actions.add(attribute)

        root = tkinter.Tk()
        root.withdraw()

        file_path = askopenfilename(initialdir='/Users/apple', title='image', filetypes=filetypes)
        label = ['emotion', 'age', 'gender', 'race']
        temp = []
        if 5 in actions:
            actions = label
        else:
            for i in actions:
                if i == 0:
                    continue
                if i:
                    # print('--', i)
                    temp.append(label[int(i - 1)])
            # print('-----', temp)
            actions = temp
        print('Selected file : ', file_path)
        print('Analyzing the image...')
        image = imageAnalyzer.deep_face(file_path, list(actions))
        for i, j in image.items():
            if image[i] is None:
                continue
            print(i, ' : ', j)
        if not image:
            print('No face detected!')
    elif model == 2:

        root = tkinter.Tk()
        root.withdraw()

        file_path = askopenfilename(initialdir='/Users/apple', title='image', filetypes=filetypes)
        print('Selected file : ', file_path)
        print('Analyzing the image...')
        imageAnalyzer.pre_train(file_path)
        print('Press q to close the image tab')
    elif model == 0:
        print('Thank you!')
        exit()