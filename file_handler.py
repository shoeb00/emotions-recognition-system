from logic import videoAnalyzer, Image_handler, text_handler

file_type = int(input('Select Input type :\n1.Image\t2.Video\t3.Text\n>>'))
if file_type == 1:
    Image_handler.imageHandler()
elif file_type == 2:
    videoAnalyzer.videoHandler()
elif file_type == 3:
    text_handler.texHandler()
else:
    print('Invalid input')
    exit()
