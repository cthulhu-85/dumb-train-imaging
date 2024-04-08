#!python
# import the opencv library 
import cv2 
import os
import time

# From chatgpt
class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def is_done(self):
        if self.start_time is None:
            return False
        elapsed_time = time.time() - self.start_time
        return elapsed_time >= self.duration

    def is_started(self):
        return not (self.start_time == None)

    def reset(self):
        self.start_time = None
camera = input("wich camera?!") 
# define a video capture object 
vid = cv2.VideoCapture(1) 

how_many_times_train_came = 0

how_many_times_the_train_aint_came = 0

has_played = False


MAX_FRAMES = 121
current_frame = 1


train_came_timer = Timer(5)
  
while(True): 
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 

    current_frame = 1+(current_frame+30)%MAX_FRAMES
    print("current_frame=", current_frame)

    tmp_image = cv2.imread("./rail_crossing/"+str(current_frame)+".png")


    print("shape=", frame.shape)

    frame_width = frame.shape[0]
    frame_height= frame.shape[1]

    bright_pixels = frame.item(int(frame_width/2), int(frame_height/2), 2)

    train_came = False
    print("bright_pixels=", bright_pixels);
    if bright_pixels >= 255:
        print("the train came!!")
        train_came = True
        how_many_times_train_came += 1

    if how_many_times_train_came > 20 and train_came:
        if how_many_times_the_train_aint_came > 2:
            os.system("paplay mixkit-toy-train-whistle-1631.wav &")
        how_many_times_train_came = 0
        how_many_times_the_train_aint_came = 0

    if not train_came:
        how_many_times_train_came = 0
        how_many_times_the_train_aint_came += 1

    # Display the resulting frame 
    cv2.imshow('frame', frame) 

    if train_came or not train_came_timer.is_done():
        cv2.imshow('frame', tmp_image)
        if not train_came_timer.is_started():
            train_came_timer = Timer(5)
            train_came_timer.start()
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 

