import cv2

#Loading The Cascade File
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Reading the Input Image
# image= cv2.imread('1.jpg')
image= cv2.imread('1.png')

#Resizing the Image
img = cv2.resize(image,None,fx=0.3,fy=0.3)

#Converting the image into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

#Pointing The Faces
for (x,y,w,h) in faces:
  cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
cv2.imshow('img', img)
cv2.waitKey()


# Angelena Yu Lecture
print("Hello"[4])
# In python for large integer valu we can use _ instead of , for 
# For human understanding as python will ignore it
print(12_34_56)

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print(type(new_num_char))

num = input("Type a two digit number: ")
print(int(num[0]) + int(num[1]))

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2  
bmi_as_int = int(bmi)
print(bmi_as_int)

print(round(8/3, 2))