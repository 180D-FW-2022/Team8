import cv2
import mediapipe as mp
import time
import math

def hyp(n1, n2):
  return math.sqrt((n1.x-n2.y)**2 + (n1.y-n2.y)**2)

def count_fingers(node):
  count = 0
  threshY = abs(node.landmark[0].y*100 - node.landmark[9].y*100)/2
  if abs(node.landmark[5].y*100 - node.landmark[8].y*100) > threshY: #pointer finger
    count += 1
  if abs(node.landmark[9].y*100 - node.landmark[12].y*100) > threshY: #middle finger
    count += 1
  if abs(node.landmark[13].y*100 - node.landmark[16].y*100) > threshY: #ring finger
    count += 1
  if abs(node.landmark[17].y*100 - node.landmark[20].y*100) > threshY: #pinker finger
    count += 1
  # if  abs(node.landmark[5].x*100 - node.landmark[4].x*100) > 6: #thumb buggy
  #   count += 1
  return count

def gestures(node): #Uses node position logic to interpert hand gestures and returns a string of said gesture
  num_fingers = count_fingers(node)
  output = ""

  if ((abs(node.landmark[10].x*100 - node.landmark[0].x*100)) > (abs(node.landmark[12].x*100 - node.landmark[0].x*100))) and abs(node.landmark[4].y) > abs(node.landmark[12].y):
    output = 1 #Thumbs Down
  if ((abs(node.landmark[10].x*100 - node.landmark[0].x*100)) > (abs(node.landmark[12].x*100 - node.landmark[0].x*100))) and abs(node.landmark[4].y) < abs(node.landmark[12].y):
    output = 2 #Thumbs Up
  if num_fingers == 0 and (hyp(node.landmark[4], node.landmark[0]) < hyp(node.landmark[10], node.landmark[0])):
    output = 3 #Fist
  if (num_fingers == 3) and ((abs(node.landmark[4].y*100 - node.landmark[8].y*100)) < 5):
    output = 4 #OK Sign
  if (num_fingers == 2) and ((abs(node.landmark[4].y*100 - node.landmark[14].y*100)) < 3):
    output = 5 #Peace Sign
  return output

def runMediaPipe():
  print("Gesture Recognizer Intializing...")
  cap = cv2.VideoCapture(0) # reads frames from video source
  drawing = mp.solutions.drawing_utils
  hands = mp.solutions.hands
  hand_obj = hands.Hands(max_num_hands=1)
  start_init = False 
  pastGesture = 0
  currentGesture = 0
  while True:
    begin_delay = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm,1) # flips video output horizontally 
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
      hand_nodes = res.multi_hand_landmarks[0]
      # frm = cv2.putText(frm, gestures(hand_nodes), (00, 185), 1, 10,(0, 0, 255), 8, cv2.LINE_AA, False)
      if not(start_init):
        end_delay = time.time()
        start_init = True
      elif abs(end_delay-begin_delay) > .5: #<-------- Adjust recognition delay
        #print(gestures(hand_nodes)) #Console output to test what gestures are recognized
        currentGesture = gestures(hand_nodes)
        if (currentGesture == pastGesture and currentGesture != 0):
          # if (currentGesture == "Fist"):
          #   print("GESTURE RECOGNIZED: ", currentGesture)
          #   print("Gesture Recognizer Shutting Down...")
          #   print('fist')
          #   cv2.destroyAllWindows()
          #   break
          print(currentGesture) #<-------- THIS IF WHERE YOU'D PUT A FUNCTION TO INTERPRET THE RECOGNIZED GESTURES!!!!!!
          currentGesture = 0
          time.sleep(2.5) # Delay for 2.5 seconds to prevent double recognitions
          # temp = "GESTURE RECOGNIZED: " + currentGesture
          # frm = cv2.putText(frm, temp, (00, 300), 1, 4,(0, 0, 0), 8, cv2.LINE_AA, False)
        else:
          pastGesture = currentGesture
        start_init = False
      # drawing.draw_landmarks(frm, hand_nodes, hands.HAND_CONNECTIONS) #connects the nodes in video output

    #cv2.imshow("window", frm) # Video output window (ONLY FOR TESTING PURPOSE WE WONT HAVE VIDEO OUT FOR THE MIRROR)
    if cv2.waitKey(1) == 27: # 'Escape' key to cancel program
      cv2.destroyAllWindows()
      break

runMediaPipe()