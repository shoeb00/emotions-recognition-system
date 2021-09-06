# Emotion Recognition System
A Python application which detects a Human face using the [Haar Cascade Algorithm](https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08) and categorized the emotion into one of the following emotion `Happy`, `Neutral`, `Sad`, `Angry` and `Surprise`. For Image analysis [DeepFace](https://research.fb.com/publications/deepface-closing-the-gap-to-human-level-performance-in-face-verification/) provides additional attributes such as `Age`, `Gender`, `Emotion` and `Race`. 

## Getting Started
### Dependencies
* Inorder to move forward with the Installation we must have [Python 3.8.5](https://www.python.org/downloads/) or `above` installed on our system.
* After installation of Python, install pip using the following this [link](https://pip.pypa.io/en/stable/installation/)
* If you have more than one python versions installed type `python3` in place of `python` and `pip3` in place of `pip`. Check python version using the following command:
```bash
$ python --version 
```
* This command will give you the list of installed python versions

### Installation
* `requirements.txt` file contains all the packages required
* To install run the following command in your terminal:
```bash
$ pip install -r requirements.txt
```
* This may take a few minutes to complete the installation process.

### Executing the program
* This application does not have a GUI available yet, so it uses the standard Command line interface. `file_handler.py` is responsible for taking care of the user input.
* To run the program run the following command in your terminal:
```bash
$ python file_handler.py
```
* It will take some time to start, then it will give the options to select a input format. for selecting an image or video a finder window will pop-up and for live video feed the program will launch the webcam

### Training the model
* `take2_train.py` file contains the logic to train the model. To create the model follow the command below:
```bash
$ python logic/take2_train.py
```
* To train the model it can take few minutes to an hour depending on your system. `epochs` defines  training the neural network with all the training data for one cycle I have tried with different values and `25` seems to worked the best with my project.
* you can set the epochs in `take2_train.py` and also rename your model name
* [Face detection Cascade](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) for face detection and the used [Dataset](https://www.kaggle.com/msambare/fer2013)
* More information on the [model](https://github.com/pypower-codes/Emotion-Detection)

### Demo video 
* [demo](https://drive.google.com/file/d/1vkVMU0QmLYqciR4rflpi8JMJf5Cju_cd/view?usp=sharing)
