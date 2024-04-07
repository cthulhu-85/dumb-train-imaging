#!python
# import the opencv library 
import cv2 
  
  
# define a video capture object 
vid = cv2.VideoCapture(1) 
  
while(True): 
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 

    print("shape=", frame.shape)

    #bright_pixels = frame.item(255,255,2)
    #print("bright_pixels=", bright_pixels)
    #frame.itemset((255, 255, 2), 1)

    frame_width = frame.shape[0]
    frame_height= frame.shape[1]

    bright_pixels = frame.item(int(frame_width/2), int(frame_height/2), 2)

    train_came = False
    print("bright_pixels=", bright_pixels);
    if bright_pixels >= 255:
        print("the train came!!")
        train_came = True

    #how_intense = 0
    #for i in range(0, frame_width):
    #    for j in range(0, frame_height):
    #        px = frame[i,j]
    #        intensity = (px[0] + px[1] + px[2])/3
    #        #print("intensity=", intensity)
    #        if intensity > 90:
    #            how_intense += 1

  
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

