headTilt=Runtime.createAndStart("headTilt","Servo")
# OpenCV
#opencv = i01.startOpenCV()
#opencv.setCameraIndex(2)
#opencv.capture()
#opencvR = Runtime.createAndStart("opencvR","OpenCV")
#opencvR.setCameraIndex(0)
#opencvR.capture()

def startAll():
  startLeftArm()
  startRightArm()
  startLeftHand()
  startRightHand()
  startTorso()
  headTilt.attach(i01.arduinos.get(rightPort).getName(),12, 105)
  headTilt.setMinMax(30,150)
  headTilt.setRest(105)
  headTilt.rest()
  i01.rest()
  startNeopixel()
  #i01.arduinos.get(leftPort).enabledHeartbeat()
  #i01.arduinos.get(rightPort).enabledHeartbeat()
