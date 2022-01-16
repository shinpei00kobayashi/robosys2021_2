#!/usr/bin/env python3

import rospy
from decimal import Decimal
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
import time



rospy.init_node('answer')
pub = rospy.Publisher('answer_up',Float32,queue_size=1)
rate=rospy.Rate(10)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(22,GPIO.OUT) 
GPIO.setup(21,GPIO.OUT) 



which = int(input("1 or 2を入力してください"))

if which == 1:
  x = 0
  n = 1
 
  for x in range(1,10):

   time.sleep(1)

   if x % 3 == 0 and x != 0:
    print(x,"!!!!!")
    pub.publish(x)

    i = 25
    for n in range(4):
     i -= 1
     GPIO.output(i,1)
     time.sleep(0.3)
     GPIO.output(i,0)
    
   
   else:
    print(x)
    pub.publish(x)
    GPIO.output(24,0)
    GPIO.output(23,0)
    GPIO.output(22,0)
    GPIO.output(21,0)



if which == 2:
  h = 0
  n = 0
  v = 0
  a = 0
  num1 = Decimal(input('最初の数字を入力してください:'))
  num2 = Decimal(input('次の数字を入力:')) 

  o = str(input('いずれかのkeyを入力してください\n+...加算\n-...引算\n*...掛算\n/...割算\n '))



  if o =='+':
   print('{}+{}='.format(num1,num2))

   for h in range(4):
    i = 25
    for n in range(4): 
     i -= 1
     GPIO.output(i,1)
     time.sleep(0.2)
     GPIO.output(i,0)
   for v in range(4):
    GPIO.output(24,1)
    GPIO.output(23,1)
    GPIO.output(22,1)
    GPIO.output(21,1)
    time.sleep(0.2)
    GPIO.output(24,0)
    GPIO.output(23,0)
    GPIO.output(22,0)
    GPIO.output(21,0)
    time.sleep(0.2)
   print(num1 + num2)
   a = (num1 + num2)
   pub.publish(a)
   rate.sleep()


  elif o =='-':
   print('{} - {} = '.format(num1, num2))

   for h in range(4):                                                
    i = 25
    for n in range(4):                                              
     i -= 1                                                          
     GPIO.output(i,1)
     time.sleep(0.2)
     GPIO.output(i,0)
   for v in range(4):
    GPIO.output(24,1)
    GPIO.output(23,1)
    GPIO.output(22,1)
    GPIO.output(21,1)
    time.sleep(0.2)
    GPIO.output(24,0)
    GPIO.output(23,0)
    GPIO.output(22,0)
    GPIO.output(21,0)
    time.sleep(0.2)
   print(num1 - num2)
   a = num1 - num2
   pub.publish(a)
   rate.sleep()



 
  elif o =='*':
   print('{} * {} = '.format(num1, num2))

   for h in range(4):
    i = 25
    for n in range(4):
     i-=1
     GPIO.output(i,1)
     time.sleep(0.2)
     GPIO.output(i,0)
   for v in range(4):
    GPIO.output(24,1)
    GPIO.output(23,1)
    GPIO.output(22,1)
    GPIO.output(21,1)
    time.sleep(0.2)
    GPIO.output(24,0)
    GPIO.output(23,0)
    GPIO.output(22,0)
    GPIO.output(21,0)
    time.sleep(0.2)
   print(num1 * num2)
   a = num1 * num2
   pub.publish(a)
   rate.sleep()



  elif o =='/':
   print('{} / {} = '.format(num1, num2))

   for h in range(4):
    i = 25
    for n in range(4):
     i-=1
     GPIO.output(i,1)
     time.sleep(0.2)
     GPIO.output(i,0)
   for v in range(4):
    GPIO.output(24,1)
    GPIO.output(23,1)
    GPIO.output(22,1)
    GPIO.output(21,1)
    time.sleep(0.2)
    GPIO.output(24,0)
    GPIO.output(23,0)
    GPIO.output(22,0)
    GPIO.output(21,0)
    time.sleep(0.2)
   print(num1 / num2)
   a = num1 / num2
   pub.publish(a)
   rate.sleep()


  else:
    print('そのkeyは対応していません')

elif which != 1 and which != 2:
 print('入力された値が間違っています')



GPIO.cleanup()

