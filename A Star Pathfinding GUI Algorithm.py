from tkinter import *
import pygame
import sys
import math

###################################################################################PLAN#########################################################################################
#Draw 50 x 50 Grid (Code + GUI)-
#Allow Input from user (start and end coordinate)-
#Wait for user to click start-
#Update surrounding pixel heuristics based on user input, will be determined using Pythagoreans THM (int)
#Create list of possible steps
#Sort list of steps from lowest to highest priority (increasing heuristic)
#Execute step
#Recursion
###################################################################################PLAN#########################################################################################

#Define global variables
global x1_int
global y1_int
global x2_int
global y2_int
global startPixel
global endPixel
global gridList
global gridRowList

class Pixel:
    def __init__(self, x, y, heuristic):
        self.x = x
        self.y = y
        self.heuristic = heuristic

    def __str__(self):
        return str(self.getCoordinate() + "H = " + str(self.getHeuristic()))

    def __repr__(self):
    	return str(self)

    def getCoordinate(self):
        return (str(self.x) + ", " + str(self.y))

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getHeuristic(self):
    	return int(self.heuristic)

    def get(self):
    	return self

    def updateHeuristic(self, new_heuristic):
        self.heuristic = new_heuristic

    def calculatePixelHeuristic(self, x2_int, y2_int):

######################################SOMETHING HERE IS WRONG##################################################
        local_x = int(self.getx())
        local_y = int(self.gety())

        local_x_differential = int(abs(local_x - x2_int))

        print(local_x_differential)

        local_y_differential = int(abs(local_y - y2_int))
        
        print(local_y_differential)



        local_heuristic = int(math.sqrt((local_x_differential ** 2) + (local_y_differential ** 2)))

        return local_heuristic        
######################################SOMETHING HERE IS WRONG##################################################

def calculateSurroundingHeuristic(x1_int, y1_int, x2_int, y2_int):
	#append all valid surrounding pixels
	rowNumber = int(y1_int)
	columnNumber = int(x1_int) 
	listofMoves = []
	
	try:
		#R-1, C-1
		newRow = int(rowNumber) - 1
		newColumn = int(columnNumber) - 1

		#TEST
		global gridRowlist
		print(gridRowlist[0][0])
		print(gridRowList[newRow][newColumn])

		#find a way here to access a pixel based on coordinates in the gridRowlist and modify its heuristic
		#gridRowList[rowNumber]

	except:
		#TEST
		print("calculateSurroundingHeuristic() error")
		pass

#pixel.updateHeuristic(pixel.calculatePixelHeuristic(pixel.getx(), pixel.gety()))


def initialButtonPress():
	global gridRowlist
	#Set values for string coordinates
	x1_string = (x1.get()).strip(" ")
	y1_string = (y1.get()).strip(" ")
	x2_string = (x2.get()).strip(" ")
	y2_string = (y2.get()).strip(" ")
	startPixelRow_string = "r"
	endPixelRow_string = "r"

	#Check to see if input coordinates are valid, if not, error statement, try again
	if((isinstance(int(x1_string), int) == True) and (isinstance(int(y1_string), int) == True) and (isinstance(int(x2_string), int) == True) and (isinstance(int(y2_string), int) == True)):
		x1_int = int(x1_string)
		y1_int = int(y1_string)
		x2_int = int(x2_string)
		y2_int = int(y2_string)

		if((x1_int>0) and (x1_int<51) and (x2_int>0) and (x2_int<51) and (y1_int>0) and (y1_int<51) and (y2_int>0) and (y2_int<51)):
			try:
				x1_string = (x1.get())
				y1_string = (y1.get())
				x2_string = (x2.get())
				y2_string = (y2.get())
				x1_int = int(x1_string)
				y1_int = int(y1_string)
				x2_int = int(x2_string)
				y2_int = int(y2_string)

				#Get startPixel & endPixel, update global
				startPixel = (gridRowList[(y1_int - 1)][(x1_int - 1)])
				endPixel = (gridRowList[(y2_int - 1)][(x2_int - 1)])

				calculateSurroundingHeuristic(x1_int, y1_int, x2_int, y2_int)
			except:
				print("Incorrect Input, Only Numbers Are Accepted As Inputs")
		else:
			print("Incorrect Input, Coordinates Must Be In Between 1-50")
	else:
		print("Incorrect Input, Please Try Again")

########################################################MAIN LOOP####################################################################
#Create all Pixels and append them to gridList
gridList = []
for i in range(1, 51):
    for j in range(1, 51):
        pixels = [Pixel(j,i,0)]
        for pixel in pixels:
            gridList.append(pixel)

#Create gridRowList and each row
gridRowList = []
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []
r10 = []
r11 = []
r12 = []
r13 = []
r14 = []
r15 = []
r16 = []
r17 = []
r18 = []
r19 = []
r20 = []
r21 = []
r22 = []
r23 = []
r24 = []
r25 = []
r26 = []
r27 = []
r28 = []
r29 = []
r30 = []
r31 = []
r32 = []
r33 = []
r34 = []
r35 = []
r36 = []
r37 = []
r38 = []
r39 = []
r40 = []
r41 = []
r42 = []
r43 = []
r44 = []
r45 = []
r46 = []
r47 = []
r48 = []
r49 = []
r50 = []

#Populate Rows
i = 0
for p in gridList:
    i = i + 1
    if i >= 0 and i < 51:
        r1.append(p)
    if i >= 51 and i < 101:
        r2.append(p)
    if i >= 101 and i < 151:
        r3.append(p)
    if i >= 151 and i < 201:
        r4.append(p)
    if i >= 201 and i < 251:
        r5.append(p)
    if i >= 251 and i < 301:
        r6.append(p)
    if i >= 301 and i < 351:
        r7.append(p)
    if i >= 351 and i < 401:
        r8.append(p)
    if i >= 401 and i < 451:
        r9.append(p)
    if i >= 451 and i < 501:
        r10.append(p)
    if i >= 501 and i < 551:
        r11.append(p)
    if i >= 551 and i < 601:
        r12.append(p)
    if i >= 601 and i < 651:
        r13.append(p)
    if i >= 651 and i < 701:
        r14.append(p)
    if i >= 701 and i < 751:
        r15.append(p)
    if i >= 751 and i < 801:
        r16.append(p)
    if i >= 801 and i < 851:
        r17.append(p)
    if i >= 851 and i < 901:
        r18.append(p)
    if i >= 901 and i < 951:
        r19.append(p)
    if i >= 951 and i < 1001:
        r20.append(p)
    if i >= 1001 and i < 1051:
        r21.append(p)
    if i >= 1051 and i < 1101:
        r22.append(p)
    if i >= 1101 and i < 1151:
        r23.append(p)
    if i >= 1151 and i < 1201:
        r24.append(p)
    if i >= 1201 and i < 1251:
        r25.append(p)
    if i >= 1251 and i < 1301:
        r26.append(p)
    if i >= 1301 and i < 1351:
        r27.append(p)
    if i >= 1351 and i < 1401:
        r28.append(p)
    if i >= 1401 and i < 1451:
        r29.append(p)
    if i >= 1451 and i < 1501:
        r30.append(p)
    if i >= 1501 and i < 1551:
        r31.append(p)
    if i >= 1551 and i < 1601:
        r32.append(p)
    if i >= 1601 and i < 1651:
        r33.append(p)
    if i >= 1651 and i < 1701:
        r34.append(p)
    if i >= 1701 and i < 1751:
        r35.append(p)
    if i >= 1751 and i < 1801:
        r36.append(p)
    if i >= 1801 and i < 1851:
        r37.append(p)
    if i >= 1851 and i < 1901:
        r38.append(p)
    if i >= 1901 and i < 1951:
        r39.append(p)
    if i >= 1951 and i < 2001:
        r40.append(p)
    if i >= 2001 and i < 2051:
        r41.append(p)
    if i >= 2051 and i < 2101:
        r42.append(p)
    if i >= 2101 and i < 2151:
        r43.append(p)
    if i >= 2151 and i < 2201:
        r44.append(p)
    if i >= 2201 and i < 2251:
        r45.append(p)
    if i >= 2251 and i < 2301:
        r46.append(p)
    if i >= 2301 and i < 2351:
        r47.append(p)
    if i >= 2351 and i < 2401:
        r48.append(p)
    if i >= 2401 and i < 2451:
        r49.append(p)
    if i >= 2451 and i < 2501:
        r50.append(p)

########################################################MAIN LOOP####################################################################
##############################################################GUI####################################################################
#Instantiating and setting up windows and frames
mainwindow = Tk()
mainwindow.geometry("750x750")
mainwindow.title("A* Path-Finding Algorithm")
mainframe = Frame(mainwindow)
initialFrame = Frame(mainwindow)
mainframe.pack()
initialFrame.pack()

#Setting Up initialFrame Widgets
initialButtonImage = PhotoImage(file="startbutton.png")
Label(initialFrame, text="Enter Start Location Coordinates (Between 1-50)").grid(row=0, sticky=W)
Label(initialFrame, text="x:").grid(row=1, sticky=W)
Label(initialFrame, text="y:").grid(row=2, sticky=W)
Label(initialFrame, text="Enter End Location Coordinates (Between 1-50)").grid(row=5, sticky=W)
Label(initialFrame, text="x:").grid(row=6, sticky=W)
Label(initialFrame, text="y:").grid(row=7, sticky=W)
startButton = Button(initialFrame, command=initialButtonPress)
startButton.grid(row=10)
startButton.config(image=initialButtonImage) #Original Image Dimensions: 512 x 273 pixels

buttonImage = PhotoImage(file="button.png")
cumulativeButtonColumn = 0
cumulativeButtonRow = 0

#Append items to gridRowList & populate GUI grid
tempString = "r"
for i in range(1, 51):
	tempString = tempString + str(i)
	gridRowList.append(eval(tempString))

	for pixel in eval(tempString):
		tempButton = Button(mainframe)
		tempButton.grid(row=i, column=cumulativeButtonColumn, sticky=W)
		tempButton.config(image=buttonImage, height=5, width=5)
		cumulativeButtonColumn = cumulativeButtonColumn + 1

	cumulativeButtonColumn = 0
	cumulativeButtonRow = cumulativeButtonRow + 1
	tempString = "r"

#Setting Up Input Boxes and Values
x1 = Entry(initialFrame)
y1 = Entry(initialFrame)
x2 = Entry(initialFrame)
y2 = Entry(initialFrame)
x1.grid(row=1, column=1)
y1.grid(row=2, column=1)
x2.grid(row=6, column=1)
y2.grid(row=7, column=1)

mainwindow.mainloop() 
##############################################################GUI####################################################################