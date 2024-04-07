#!python
# import the opencv library 
import cv2 
import os
 
# define a video capture object 
vid = cv2.VideoCapture(1) 

how_many_times_train_came = 0

how_many_times_the_train_aint_came = 0

has_played = False


  
while(True): 
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 

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
     
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 

