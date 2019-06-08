import time
import os
import sys
import signal

fileToWrite = None
CPURAMFile = None
messageSize = None
numberOfMessages = None
timeElapsed = 0
pid = None


def readFile():
    file = open("toSend.txt", "r")
    return file.read()


def savetofile(message):
    fileToWrite.write(message)

def startServerTestSetup(message_size, number_of_messages):
    global messageSize
    global numberOfMessages
    global pid
    global CPURAMFile
    pid = os.getpid()
    messageSize = message_size
    numberOfMessages = number_of_messages
    CPURAMFile = open("-".join([str(messageSize),str(number_of_messages),".csv"]),"w+")
    scheduleCPU_RAM_ETC()

def startTestSetup(message_size, number_of_messages):
    global fileToWrite
    global messageSize
    global numberOfMessages
    global timeElapsed
    global pid
    global CPURAMFile
    messageSize = message_size
    numberOfMessages = number_of_messages
    pid = os.getpid()

    fileToWrite = open("received.txt", "w+")
    CPURAMFile = open("-".join([str(messageSize),str(number_of_messages),".csv"]),"w+")
    timeElapsed -= time.time()
    scheduleCPU_RAM_ETC()


def endTestSetup(filename):
    global timeElapsed
    timeElapsed += time.time()
    file = open(filename, "w+")
    file.write(",".join([str(messageSize), str(numberOfMessages),
                         str(timeElapsed)]))
    sys.exit(0)


def scheduleCPU_RAM_ETC():
    signal.signal(signal.SIGALRM, saveCPU_RAM_ETC)
    signal.setitimer(signal.ITIMER_REAL, 1)


def saveCPU_RAM_ETC(signum, frame):
    myCmd = os.popen(" ".join(["ps -p", str(pid), "-o %cpu,%mem"])).read()
    CPURAMFile.write(myCmd)
    scheduleCPU_RAM_ETC()
