# import the opencv library
import cv2
import time
  
# define a video capture object
vid = cv2.VideoCapture(0)

width= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
file_size = (width,height)

writer= cv2.VideoWriter('recorded_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, file_size)

pframe_time = time.time()

coordinates = (100,100)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (0,0,255)
thickness = 2
  
while(True):
    
    nframe_time = time.time()
    current_time = str(round(nframe_time - pframe_time, 2))

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # displays current time
    cv2.putText(frame, current_time, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)

    frame = cv2.resize(frame, file_size, interpolation=cv2.INTER_NEAREST)

    writer.write(frame)
    
    # Display the resulting frame
    cv2.imshow('Record Video', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()

writer.release()
# Destroy all the windows
cv2.destroyAllWindows()