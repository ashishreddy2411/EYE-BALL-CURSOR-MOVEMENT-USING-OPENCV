"""
moving mouse cursor using opencv eyeball tracking logic
to move cursor we are using pyautogui

"""
#python library import statement
import cv2
from gaze_tracking import GazeTracking #python opencv gaze library to track eye ball movement
import pyautogui

gaze = GazeTracking() #eye ball tracking object  creation
webcam = cv2.VideoCapture(0) #starting web cam

while True:
    
    _, frame = webcam.read() #reading frames from webcam

    
    gaze.refresh(frame)#sending frame to opencv gaze library to detect eye ball movement

    frame = gaze.annotated_frame() #returns eye ball movement data
    text = ""

    if gaze.is_blinking(): #displaying result
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords() #getting pupil location as x and y cordinates

    x = str(left_pupil).split(",") #getting left pupil x and y location
    y = str(right_pupil).split(",") #getting right pupil x and y location
    if len(x) > 1:
        data_x = x[0]
        data_x = data_x[1:len(data_x)];
        data_y = x[1]
        data_y = data_y[0:len(data_y)-1]
        pyautogui.moveTo(int(data_x),int(data_y)) #moving mouse cursor to eye pupil x and y left side location 

    if len(y) > 1:
        data_x = y[0]
        data_x = data_x[1:len(data_x)];
        data_y = y[1]
        data_y = data_y[0:len(data_y)-1]
        pyautogui.moveTo(int(data_x),int(data_y)) #moving mouse cursor to eye pupil x and y right sidelocation 
        
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("EyeBall Cursor Movement", frame)

    if cv2.waitKey(1) == 27:
        break
