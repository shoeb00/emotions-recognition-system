import csv
from logic import textAnalyzer
import tkinter
from tkinter.filedialog import askopenfilename


def texHandler():
    sentiment = ' '
    file_type = int(input('Select the input type\n1.String\t2.txt file\t3.csv file\n>>'))

    if file_type == 1:
        input_string = input('Provide the input\n>>')
        sentiment = textAnalyzer.sentiment_analyze(input_string)
    elif file_type == 2:
        root = tkinter.Tk()
        root.withdraw()

        file_path = askopenfilename(initialdir='/Users/apple', title='text', filetypes=[('txt files', '*.txt')])
        input_string = ' '
        with open(file_path, 'r') as file:
            input_string = file.read().replace('\n', '')
        # print(input_string)
        sentiment = textAnalyzer.sentiment_analyze(input_string)
    elif file_type == 3:
        root = tkinter.Tk()
        root.withdraw()

        file_path = askopenfilename(initialdir='/Users/apple', title='csv', filetypes=[('csv files', '*.csv')])
        input_string = ''
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            temp = []
            for line in csv_reader:
                temp.append(line)
                break
            index = temp[0].index('reviews')
            for line in csv_reader:
                input_string += line[index] + ' '
        sentiment = textAnalyzer.sentiment_analyze(input_string)
    else:
        print('Invalid Input')
        exit()
    print(sentiment)


# texHandler()