#This python script is from Krzysztof Pietroszek
from java.lang import String
from org.myrobotlab.service import Sphinx
from org.myrobotlab.net import BareBonesBrowserLaunch 
from datetime import datetime
from subprocess import Popen, PIPE, call
from time import strftime
from time import sleep
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import smtplib
import random
import time
import threading
import urllib, urllib2
import json
import io
import itertools
import textwrap
import codecs
import socket
import os
import shutil
import hashlib
import subprocess
import string
import csv
import re
import datetime
import email
import imaplib
import mailbox
import ast
import math

counter=0
opencvimie=u''
opencvnazwisko=u''
uzytkownik=u''
nowaosoba = "" #name
ostatniaosoba = "" #previous name
start = 0 # time OPENCV
x=0 #for AIML. AIML is a language to program AI 
puste=u''
odkogo=u''
alarmgodzina="22"
alarmminuta="55"

rightport = "COM5"
leftport = "COM3"

# notice hard coded paths. Change it to relative paths or make sure that you follow the setup.
gestyPath = "C:\Myrobotlab\myrobotlab\pythonModules"

#Runtime.createAndStart("webGui", "WebGui") 
#speak test to special characters
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
#mouth=Runtime.createAndStart("mouth", "AcapelaSpeech")
htmlFilter=Runtime.createAndStart("htmlFilter", "HtmlFilter")
sleep(1)
#
ear.addListener("publishText", python.name, "talk") 
#
htmlFilter.addListener("publishText", python.name, "say")
htmlFilter.addListener("publishText", python.name, "speech2")
htmlFilter.addListener("publishText", python.name, "speech")
#mouth.setLanguage("pl-PL")
#mouth.setVoice("Ania")
ear.setLanguage("pl-PL")
#
aimlDir = "C:/MyRobotLab/myrobotlab/ProgramAB"
userName = "bartosz"
botName = "damian"
damian = Runtime.createAndStart("damian", "ProgramAB")
#
def speech(word):
  ear.stopListening()
  call('tts.exe -v 0 "'+word+'"')
  sleep(0.2)
  ear.startListening()
  ear.resumeListening()
  
#
def speech2(word):
  ison = False
  a = word.split()
  for word in a:
    if word[len(word)-2:] == "es" : # removing es at the end of the word
      testword = word[:-2] +'xx' # adding x's to help keep the timing
    elif word[len(word)-1:] == "e" : # removing the silant e at the end of the word
      testword = word[:-1] +'x'
    else:
      testword = word
        
    for x in range(0, len(testword)):
    
      if testword[x] in ('a', 'e', 'i', 'o', 'u', 'y' ) and ison == False :
        #arduino.digitalWrite(13, Arduino.HIGH)
        jaw.moveTo(180) # move the servo to the open spot
        ison = True
        sleep(0.15)
        jaw.moveTo(0) # close the servo 
      elif testword[x] in ('.') :
        #arduino.digitalWrite(13, Arduino.LOW)
        
        ison = False
        sleep(.95)
      else: #sleep(0.5)  sleep half a second
        #arduino.digitalWrite(13, Arduino.LOW)
        
        ison = False
        sleep(0.06) # sleep half a second
  
    #arduino.digitalWrite(13, Arduino.LOW)
    
    sleep(0.08)
# end of talk function

# start the session for the chat bot

damian.startSession(aimlDir, "bartosz", "damian")
ear.addTextListener(damian)
damian.addTextListener(htmlFilter)
#htmlFilter.addTextListener("python", "speech2")
ear.addListener("recognized", "python", "heard")
#
ear.startListening()

def wakeup():
     ear.stopListening()
     sleep(0.2)
     ear.startListening()
     sleep(0.2)
     ear.resumeListening()
#zapytanie='Albert Einstein'
wiki = Runtime.createAndStart("Wikipedia", "WikiDataFetcher")
wiki.setLanguage('pl')
#print "Label from query : " + wiki.getLabel(zapytanie)
wiki.setWebSite("plwiki") 
#print "Description EN : " + wiki.getDescription(zapytanie)
stayingawake = Runtime.createAndStart("czuwanie","Sphinx")
stayingawake.startListening("damian")
stayingawake.addCommand("damian", "python", "pobudka")

#vision=Runtime.createAndStart("wzrok","OpenCV")
#vision.setCameraIndex(2)

larduino = Runtime.start("larduino","Arduino")
larduino.connect(leftport)
parduino = Runtime.start("parduino","Arduino")
parduino.connect(rightport)
delta = 0
larduino = Runtime.start("larduino","Arduino")
larduino.connect(leftport)
parduino = Runtime.start("parduino","Arduino")
parduino.connect(rightport)

neckturn=Runtime.createAndStart("szyja.skret","Servo")
leftneck=Runtime.createAndStart("l.szyja","Servo")
rightneck=Runtime.createAndStart("p.szyja","Servo")
eyeshorizontal=Runtime.createAndStart("x.oczy","Servo")
eyesvertical=Runtime.createAndStart("y.oczy","Servo")

rightthumb=Runtime.createAndStart("p.kciuk","Servo")
rightindexfinger=Runtime.createAndStart("p.wskazujacy","Servo")
rightmiddlefinger=Runtime.createAndStart("p.srodkowy","Servo")
rightringfinger=Runtime.createAndStart("p.serdeczny","Servo")
rightlittlefinger=Runtime.createAndStart("p.maly","Servo")

rightwrist=Runtime.createAndStart("p.nadgarstek","Servo")

rightelbow=Runtime.createAndStart("p.biceps","Servo")
rightarmturn=Runtime.createAndStart("p.ramie.skret","Servo")
rightarmforward=Runtime.createAndStart("p.ramie.przodtyl","Servo")
rightarmsidemove=Runtime.createAndStart("p.ramie.bok","Servo")

leftthumb=Runtime.createAndStart("l.kciuk","Servo")
leftindexfinger=Runtime.createAndStart("l.wskazujacy","Servo")
lefttmiddlefinger=Runtime.createAndStart("l.srodkowy","Servo")
leftringfinger=Runtime.createAndStart("l.serdeczny","Servo")
leftlittlefinger=Runtime.createAndStart("l.maly","Servo")

lefttwrist=Runtime.createAndStart("l.nadgarstek","Servo")

leftelbow=Runtime.createAndStart("l.biceps","Servo")
leftarmturn=Runtime.createAndStart("l.ramie.skret","Servo")
leftarmforward=Runtime.createAndStart("l.ramie.przodtyl","Servo")
leftarmsidemove=Runtime.createAndStart("l.ramie.bok","Servo")

rightwaist=Runtime.createAndStart("p.plecy","Servo")
leftwaist=Runtime.createAndStart("l.plecy","Servo")
jaw=Runtime.createAndStart("jaw","Servo")

jaw.setMinMax(50,70)
jaw.map(0,180,50,70)
jaw.setRest(0)
#rightthumb.setInverted(True)
jaw.setSpeed(1)
jaw.attach(larduino.getName(),26)

rightwaist.setMinMax(0,180)
rightwaist.map(0,180,0,180)
rightwaist.setRest(30)
rightwaist.setInverted(True)
rightwaist.setSpeed(0.99)
rightwaist.attach(parduino.getName(),40)
rightwaist.moveTo(30)

leftwaist.setMinMax(0,180)
leftwaist.map(0,180,0,180)
leftwaist.setRest(30)
leftwaist.setInverted(True)
leftwaist.setSpeed(0.99)
leftwaist.attach(parduino.getName(),42)
leftwaist.moveTo(30)


neckturn.setMinMax(0,150)
neckturn.map(0,180,20,150)
neckturn.setRest(133)
#rightthumb.setInverted(True)
neckturn.setSpeed(0.99)
neckturn.attach(larduino.getName(),13)
neckturn.moveTo(133)

rightneck.setMinMax(0,180)
rightneck.map(0,180,10,105)
rightneck.setRest(120)
#rightthumb.setInverted(True)
rightneck.setSpeed(0.99)
rightneck.attach(larduino.getName(),38)
rightneck.moveTo(142)

def onServoEvent(pos):
     leftneck.moveTo(pos+delta)
     
python = Runtime.getService("python")
rightneck.addServoEventListener(python)
rightneck.eventsEnabled(True)

#INIT: RESET POSITIONS OF ALL SERVOS
leftneck.setMinMax(0,180)
leftneck.map(0,180,0,160)
#leftneck.setRest(120)
#rightthumb.setInverted(True)
leftneck.setSpeed(0.99)
leftneck.attach(larduino.getName(),12)

eyeshorizontal.setMinMax(0,180)
eyeshorizontal.map(0,180,62,130)
eyeshorizontal.setRest(82)
#rightthumb.setInverted(True)
eyeshorizontal.setSpeed(1)
eyeshorizontal.attach(larduino.getName(),22)
eyeshorizontal.moveTo(82)

eyesvertical.setMinMax(0,180)
eyesvertical.map(0,180,52,150)
eyesvertical.setRest(90)
#rightthumb.setInverted(True)
eyesvertical.setSpeed(1)
eyesvertical.attach(larduino.getName(),24)
eyesvertical.moveTo(90)

rightthumb.setMinMax(0,180)
rightthumb.map(0,180,0,180)
rightthumb.setRest(0)
#rightthumb.setInverted(True)
rightthumb.setSpeed(1)
rightthumb.attach(parduino.getName(),2)

rightindexfinger.setMinMax(0,180)
rightindexfinger.map(0,180,0,180)
rightindexfinger.setRest(0)
#rightthumb.setInverted(True)
rightindexfinger.setSpeed(1)
rightindexfinger.attach(parduino.getName(),3)

rightmiddlefinger.setMinMax(0,180)
rightmiddlefinger.map(0,180,0,175)
rightmiddlefinger.setRest(0)
#rightthumb.setInverted(True)
rightmiddlefinger.setSpeed(1)
rightmiddlefinger.attach(parduino.getName(),4)

rightringfinger.setMinMax(0,180)
rightringfinger.map(0,180,0,170)
rightringfinger.setRest(0)
#rightthumb.setInverted(True)
rightringfinger.setSpeed(1)
rightringfinger.attach(parduino.getName(),5)

rightlittlefinger.setMinMax(0,180)
rightlittlefinger.map(0,180,0,180)
rightlittlefinger.setRest(0)
#rightthumb.setInverted(True)
rightlittlefinger.setSpeed(1)
rightlittlefinger.attach(parduino.getName(),6)

rightwrist.setMinMax(0,180)
rightwrist.map(0,180,0,170)
rightwrist.setRest(90)
#rightthumb.setInverted(True)
rightwrist.setSpeed(1)
rightwrist.attach(parduino.getName(),7)

rightelbow.setMinMax(0,180)
rightelbow.map(0,180,4,92)
rightelbow.setRest(4)
#rightthumb.setInverted(True)
rightelbow.setSpeed(1)
rightelbow.attach(parduino.getName(),8)

rightarmturn.setMinMax(0,180)
rightarmturn.map(0,180,30,180)
rightarmturn.setRest(82)
#rightthumb.setInverted(True)
rightarmturn.setSpeed(1)
rightarmturn.attach(parduino.getName(),9)

rightarmforward.setMinMax(0,180)
rightarmforward.map(0,180,0,180)
rightarmforward.setRest(25)
#rightthumb.setInverted(True)
rightarmforward.setSpeed(1)
rightarmforward.attach(parduino.getName(),10)

rightarmsidemove.setMinMax(0,180)
rightarmsidemove.map(0,180,113,177)
rightarmsidemove.setRest(2)
rightarmsidemove.setInverted(True)
rightarmsidemove.setSpeed(0.95)
rightarmsidemove.attach(parduino.getName(),11)

leftthumb.setMinMax(0,180)
leftthumb.map(0,180,0,180)
leftthumb.setRest(0)
#rightthumb.setInverted(True)
leftthumb.setSpeed(1)
leftthumb.attach(larduino.getName(),2)

leftindexfinger.setMinMax(0,180)
leftindexfinger.map(0,180,0,180)
leftindexfinger.setRest(0)
#rightthumb.setInverted(True)
leftindexfinger.setSpeed(1)
leftindexfinger.attach(larduino.getName(),3)

lefttmiddlefinger.setMinMax(0,180)
lefttmiddlefinger.map(0,180,0,175)
lefttmiddlefinger.setRest(0)
#rightthumb.setInverted(True)
lefttmiddlefinger.setSpeed(1)
lefttmiddlefinger.attach(larduino.getName(),4)

leftringfinger.setMinMax(0,180)
leftringfinger.map(0,180,0,170)
leftringfinger.setRest(0)
#rightthumb.setInverted(True)
leftringfinger.setSpeed(1)
leftringfinger.attach(larduino.getName(),5)

leftlittlefinger.setMinMax(0,180)
leftlittlefinger.map(0,180,0,180)
leftlittlefinger.setRest(0)
#rightthumb.setInverted(True)
leftlittlefinger.setSpeed(1)
leftlittlefinger.attach(larduino.getName(),6)

lefttwrist.setMinMax(0,180)
lefttwrist.map(0,180,0,170)
lefttwrist.setRest(90)
#rightthumb.setInverted(True)
lefttwrist.setSpeed(1)
lefttwrist.attach(larduino.getName(),7)

leftelbow.setMinMax(0,180)
leftelbow.map(0,180,4,92)
leftelbow.setRest(0)
#rightthumb.setInverted(True)
leftelbow.setSpeed(1)
leftelbow.attach(larduino.getName(),8)
leftelbow.moveTo(1)

leftarmturn.setMinMax(0,180)
leftarmturn.map(0,180,30,180)
leftarmturn.setRest(78)
#rightthumb.setInverted(True)
leftarmturn.setSpeed(1)
leftarmturn.attach(larduino.getName(),9)
leftarmturn.moveTo(78)

leftarmforward.setMinMax(0,180)
leftarmforward.map(0,180,0,180)
leftarmforward.setRest(24)
#rightthumb.setInverted(True)
leftarmforward.setSpeed(1)
leftarmforward.attach(larduino.getName(),10)
leftarmforward.moveTo(24)

leftarmsidemove.setMinMax(0,180)
leftarmsidemove.map(0,180,113,177)
leftarmsidemove.setRest(2)
leftarmsidemove.setInverted(True)
leftarmsidemove.setSpeed(0.95)
leftarmsidemove.attach(larduino.getName(),11)

def wysunprawareka():
  rightarmforward.moveTo(70)
  rightarmturn.moveTo(80)
  rightelbow.moveTo(70)
  rightwrist.moveTo(0)
  eyeshorizontal.moveTo(0)
  eyesvertical.moveTo(70)
  neckturn.moveTo(180)
  delta=0
  rightneck.moveTo(150)
  leftneck.moveTo(110)
  sleep(3)
  rightthumb.moveTo(160)
  rightindexfinger.moveTo(150)
  rightringfinger.moveTo(160)
  rightmiddlefinger.moveTo(150)
  rightlittlefinger.moveTo(140)
  sleep(0.7)
  neckturn.moveTo(150)
  rightarmturn.moveTo(110)
  rightelbow.moveTo(180)
  sleep(3)
  eyeshorizontal.moveTo(70)
  neckturn.moveTo(138)
  lefttwrist.moveTo(170)
  rightelbow.moveTo(173)
  rightwrist.moveTo(180)
  leftelbow.moveTo(143)
  rightarmturn.moveTo(136)
  leftarmturn.moveTo(127)
  leftarmforward.moveTo(62)
  sleep(1.3)
  rightelbow.setSpeed(0.99)
  rightelbow.moveTo(130)
  rightwrist.moveTo(100)
  rightarmsidemove.moveTo(17)
  rightringfinger.moveTo(20)
  rightmiddlefinger.moveTo(20)
  rightlittlefinger.moveTo(20)
  rightarmforward.moveTo(78)
  sleep(0.1)
  leftthumb.moveTo(160)
  leftlittlefinger.moveTo(140)
  lefttmiddlefinger.moveTo(130)
  leftringfinger.moveTo(160)
  leftindexfinger.moveTo(120)
  sleep(0.7)
  rightthumb.moveTo(20)
  leftarmturn.moveTo(100)
  leftelbow.moveTo(90)
  sleep(0.2)
  rightelbow.moveTo(1)
  sleep(1)
  rightarmsidemove.moveTo(3)
  rightthumb.moveTo(0)
  rightindexfinger.moveTo(0)
  rightringfinger.moveTo(0)
  rightmiddlefinger.moveTo(0)
  rightlittlefinger.moveTo(0)
  neckturn.moveTo(130)
  delta=3
  rightneck.moveTo(170)
  eyesvertical.moveTo(56)
  sleep(1)
  #tu opuszenie lewej reki
  delta=0
  rightneck.moveTo(90)
  leftneck.moveTo(50)
  neckturn.moveTo(133)
  eyesvertical.moveTo(90)
  eyeshorizontal.moveTo(90)
  rightwrist.moveTo(40)
  rightelbow.setSpeed(1)
  rightelbow.moveTo(0)
  rightarmturn.moveTo(82)
  rightarmforward.moveTo(27)
  sleep(1)
  lefttwrist.setSpeed(0.99)
  lefttwrist.moveTo(10)
  sleep(1)
  leftringfinger.moveTo(0)
  lefttmiddlefinger.moveTo(0)
  leftindexfinger.moveTo(1)
  leftlittlefinger.moveTo(0)
  leftthumb.moveTo(0)
  lefttwrist.setSpeed(0.99)
  lefttwrist.moveTo(70)
  sleep(0.7)
  lefttwrist.setSpeed(1)
  lefttwrist.moveTo(10)
  sleep(0.3)
  leftelbow.moveTo(0)
  leftarmturn.moveTo(80)
  leftarmforward.moveTo(24)
  lefttwrist.setSpeed(1)
  lefttwrist.moveTo(90)

#alarm()
#start()
neckturn.moveTo(90)
#os.system(gestyPath,"*.py")
speech(u'Oh, nice to be awake again. All system function, well, I think, except for my neck and finger.') ## We could implement a self test here.


# functions:

def introduce_yourself():
  eyeshorizontal.moveTo(30)
  rightelbow.setSpeed(0.9)
  rightelbow.moveTo(40)
  neckturn.moveTo(125)
  neckturn.setSpeed(0.8)
  sleep(0.8)
  rightwrist.moveTo(20)
  neckturn.moveTo(62)
  speech(u'Hello! game students! I am Damian')
  eyeshorizontal.moveTo(150)
  sleep(0.5)
  rightelbow.moveTo(5)
  rightarmturn.moveTo(100)
  speech(u'I am a humanoid robot from the Institute for Ideas')
  neckturn.moveTo(90)
  leftelbow.moveTo(60)
  leftarmturn.moveTo(45)
  eyeshorizontal.moveTo(90)
  sleep(0.8)
  rightneck.setSpeed(0.7)
  rightneck.moveTo(70)
  neckturn.setSpeed(0.7)
  neckturn.moveTo(100)
  eyeshorizontal.moveTo(150)
  speech(u'Make sure that you do your assignment!')
  neckturn.moveTo(85)
  eyeshorizontal.moveTo(60)
  #rightneck.moveTo(145)
  leftelbow.moveTo(5)
  leftarmturn.moveTo(90)
  rightelbow.moveTo(170)
  rightarmforward.moveTo(71)
  rightarmsidemove.moveTo(62)
  sleep(0.2)
  rightarmturn.moveTo(150)
  #neckturn.moveTo(77)
  rightneck.moveTo(178)
  leftneck.moveTo(151)
  leftarmforward.setSpeed(0.8)
  leftarmforward.moveTo(45)
  leftarmturn.setSpeed(0.7)
  leftarmturn.moveTo(111)
  leftelbow.setSpeed(0.8)
  leftelbow.moveTo(135)
  rightwrist.moveTo(147)
  rightlittlefinger.moveTo(180)
  rightringfinger.moveTo(180)
  rightmiddlefinger.moveTo(180)
  rightthumb.moveTo(180)
  eyeshorizontal.moveTo(90)
  eyesvertical.moveTo(0)
  speech(u'I am being trained to become an administrative assistant at the Institute for Ideas')
  leftarmturn.moveTo(82)
  leftelbow.moveTo(5)
  rightwrist.moveTo(90)
  rightlittlefinger.moveTo(0)
  rightringfinger.moveTo(0)
  rightmiddlefinger.moveTo(0)
  rightthumb.moveTo(0)
  eyeshorizontal.moveTo(90)
  eyesvertical.moveTo(108)
  leftarmforward.moveTo(20)
  rightelbow.setSpeed(0.6)
  rightelbow.moveTo(3)
  speech(u'I can see, smell, recognize people, answer question, and learn varios tasks.')
  rightarmturn.moveTo(82)
  rightarmforward.moveTo(20)
  rightarmsidemove.moveTo(4)
  neckturn.setSpeed(0.5)
  neckturn.moveTo(107)
  speech(u'I am also planning to become an actor. But I have a long way to go. My dream is to play Hamlet')
  lefttwrist.setSpeed(0.5)
  lefttwrist.moveTo(53)
  eyeshorizontal.setSpeed(0.5)
  eyeshorizontal.moveTo(110)
  #rightneck.setSpeed(0.5)
  #rightneck.moveTo(107)
  rightwaist.setSpeed(0.7)
  rightwaist.moveTo(95)
  leftwaist.setSpeed(0.7)
  leftwaist.moveTo(95)
  neckturn.moveTo(90)
  speech(u'I cant wait for the pandemic to be over, since I am sitting in the attic of professor Pietroszek rather than interacting with American University Students')
  rightwaist.setSpeed(0.98)
  leftwaist.setSpeed(0.98)
  rightwaist.moveTo(0)
  leftwaist.moveTo(180)
  speech(u'I also want to be a standup comedian')
  rightwaist.moveTo(180)
  speech(u'but I have no sense of humor yet')
  leftwaist.moveTo(0)
  rightwaist.moveTo(35)
  leftwaist.moveTo(35)
  speech(u'If my creators are smart enough, I might even learn how to walk one day')
  speech(u'That is all about me. How about you? Are you a human or a robot, like me?')
  rightwaist.setSpeed(0.99)
  leftwaist.setSpeed(0.99)
  rightwaist.moveTo(180)
  leftwaist.moveTo(180)
  rightwaist.setSpeed(0.9)
  leftwaist.setSpeed(0.9)
  rightwaist.moveTo(35)
  leftwaist.moveTo(35)

def shake_hand():
 #podniesienie reki (podanie)
 rightarmsidemove.moveTo(11)
 rightelbow.setSpeed(0.95)
 rightelbow.moveTo(20)
 rightarmforward.setSpeed(0.99)
 rightarmforward.moveTo(60)
 sleep(2)
 #jak wyczuje reke i zamyka dlon
 rightarmturn.moveTo(90)
 rightwrist.moveTo(120)
 rightthumb.setSpeed(0.95)
 rightthumb.moveTo(120)
 rightindexfinger.setSpeed(0.95)
 rightindexfinger.moveTo(70)
 rightmiddlefinger.setSpeed(0.95)
 rightmiddlefinger.moveTo(85)
 rightringfinger.setSpeed(0.95)
 rightringfinger.moveTo(90)
 rightlittlefinger.setSpeed(0.95)
 rightlittlefinger.moveTo(85)
 #po zlapaniu delikatnie machanie
 sleep(2)
 rightelbow.moveTo(30)
 sleep(0.3)
 rightelbow.moveTo(10)
 sleep(0.3)
 rightelbow.moveTo(30)
 sleep(0.3)
 rightelbow.moveTo(10)
 sleep(1.5)
 #tutaj otwieramy dlon
 rightarmturn.moveTo(82)
 rightwrist.moveTo(60)
 rightarmsidemove.moveTo(2)
 rightthumb.setSpeed(1)
 rightindexfinger.setSpeed(1)
 rightmiddlefinger.setSpeed(1)
 rightringfinger.setSpeed(1)
 rightlittlefinger.setSpeed(1)
 rightthumb.moveTo(0)
 rightindexfinger.moveTo(0)
 rightmiddlefinger.moveTo(0)
 rightringfinger.moveTo(0)
 rightlittlefinger.moveTo(0)
 sleep(0.5)
 #tu opuszczamy reke
 rightelbow.setSpeed(0.99)
 rightelbow.moveTo(2)
 rightarmforward.moveTo(25)
 rightelbow.setSpeed(1)
 rightarmforward.setSpeed(1)
 
#pobudka()
introduce_yourself()
