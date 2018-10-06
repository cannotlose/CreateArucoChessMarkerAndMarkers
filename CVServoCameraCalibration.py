import serial
import time
import tkinter as tk
import cv2
from tkinter import HORIZONTAL
import numpy as np
from serial.tools import list_ports

class Application(tk.Frame):
    def __init__(self):
        super().__init__()

        #show list of ports
        listOfPorts = list_ports.comports()
        print(listOfPorts)

        for n in listOfPorts:
            print (n.device)






        self.create_widgets()
        self.ser = serial.Serial('COM8', 115200, timeout=1000)
        time.sleep(3)

        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        self.board = cv2.aruco.CharucoBoard_create(8, 8, .025, .0125, self.dictionary)

    def createMicroStep(self,formPos, toPos, numbrtOfSteps):
        # calcolaetion
        formPos = formPos.astype('float64')
        moveDelta = toPos - formPos
        print("delta calcla moveDelta: %s" % moveDelta)
        moveDelta = moveDelta / numbrtOfSteps
        stepVector = formPos

        for value in range(0, numbrtOfSteps):
            formPos += moveDelta
            stepVector = np.row_stack((stepVector, formPos))

        return stepVector

    def sendCommand(self,value):
        print(value)

        self.servoSlide1.get()
        test = "servo1,%d\n"%self.servoSlide1.get();
        self.ser.write(test.encode())
        print(self.ser.readline())

        self.servoSlide2.get()
        test = "servo2,%d\n"%self.servoSlide2.get();
        self.ser.write(test.encode())
        print(self.ser.readline())

        self.servoSlide3.get()
        test = "servo3,%d\n"%self.servoSlide3.get();
        self.ser.write(test.encode())
        print(self.ser.readline())


    def basicInfoWindow:
        self.basicWindow = tk.Tk()

        self.basicWindow.option_add("*Button.Background", "black")
        self.basicWindow.option_add("*Button.Foreground", "red")

        self.basicWindow.title('SERVO Controller')
        self.basicWindow.geometry("500x500")

        self.back = tk.Frame(master=self.basicWindow, bg='black')
        self.back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

        self.pack()





    def create_widgets(self):

        self.root = tk.Tk()

        self.root.option_add("*Button.Background", "black")
        self.root.option_add("*Button.Foreground", "red")

        self.root.title('SERVO Controller')
        self.root.geometry("500x500")

        self.back = tk.Frame(master=self.root, bg='black')
        self.back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

        self.pack()

        self.hi_there = tk.Button(self, width=500)
        self.hi_there["text"] = "speed test\n(click me)"
        self.hi_there["command"] = self.runspeedtest
        self.hi_there.pack(side="top")

        self.servoSlide1 = tk.Scale(self, from_=0, to=3000, label="Servo 1", orient=HORIZONTAL, sliderlength=30, width=30 ,length=800)
        self.servoSlide1.bind("<ButtonRelease-1>", self.sendCommand)
        self.servoSlide1.set(1500)
        self.servoSlide1.pack()
        self.servoSlide2 = tk.Scale(self, from_=0, to=3000, label="Servo 2", orient=HORIZONTAL, sliderlength=30, width=30 ,length=800)
        self.servoSlide2.bind("<ButtonRelease-1>", self.sendCommand)

        self.servoSlide2.set(1500)
        self.servoSlide2.pack()
        self.servoSlide3 = tk.Scale(self, from_=0, to=3000, label="Servo 3", orient=HORIZONTAL, sliderlength=30, width=30,length=800)
        self.servoSlide3.bind("<ButtonRelease-1>", self.sendCommand)
        self.servoSlide3.set(1500)
        self.servoSlide3.pack()
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.exit)
        self.quit.pack(side="bottom")

        self.calibration = tk.Button(self, text="Calibration", fg="red",
                              command=self.calibration)
        self.calibration.pack(side="bottom")


    def calibration(self):

        # Start capturing images for calibration
        cap = cv2.VideoCapture(1)
        cap2 = cv2.VideoCapture(1)

        calServo1 = np.random.randint(550, 2400, size=20)
        calServo2 = np.random.randint(870, 1818, size=20)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 5000)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 5000)

        cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 5000)
        cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 5000)




        calServo = np.column_stack((calServo1, calServo2))
        print(calServo)

        lastpos = np.array([1500, 1500])

        # init camera array's
        allCorners = []
        allIds = []
        decimator = 0

        # init camera array's
        allCorners2 = []
        allIds2 = []
        decimator2 = 0

        for step in calServo:
            for MicroStep in self.createMicroStep(lastpos,step,100):

                print(MicroStep)
                test = "servo1,%d\n" % MicroStep[0];
                self.ser.write(test.encode())
                print(self.ser.readline())

                test = "servo2,%d\n" % MicroStep[1];
                self.ser.write(test.encode())
                print(self.ser.readline())

                time.sleep(0.1)

            time.sleep(10)

            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            res = cv2.aruco.detectMarkers(gray, self.dictionary)

            if len(res[0]) > 0:
                res2 = cv2.aruco.interpolateCornersCharuco(res[0], res[1], gray, board)
                if res2[1] is not None and res2[2] is not None and len(res2[1]) > 3 and decimator % 3 == 0:
                    allCorners.append(res2[1])
                    allIds.append(res2[2])

                cv2.aruco.drawDetectedMarkers(gray, res[0], res[1])

            cv2.imshow('frame1', gray)



            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            decimator += 1

            print("End One Step")
            lastpos = step


        print("End Detla Calculation")


    def runspeedtest(self):
        loop = range(0,100)

        stringResult = "ddd\n"
        for d in loop:
            test = "Echo,%d\n" % d;
            self.ser.write(test.encode())
            stringResult+=self.ser.read_until(size=None).decode('utf-8')

        print(stringResult)
        print("done")

    def exit(selfself):
        print("sababa egozim")
        self.ser.close()
        self.print(self.ser.is_open)
        root.destroy


app = Application()
app.mainloop()





