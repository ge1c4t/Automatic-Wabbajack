import pyautogui
import cv2 as cv
import time
import PySimpleGUI as sg
from threading import Thread

#step 0: slow download
#step 1: back button
step = 0
timer = 0
conf = 0.8
retry = False
back = False
running = False
status = "Automatic Wabbajack v0.3"
tag = "@ge1c4t"
autoproc = None

sg.theme('DarkGrey13')
col = [
    [sg.Multiline(size=(40,15), key='-TEXT-')]
]
layout = [
    [sg.Text(status, justification='left'), sg.Text(tag, justification='right')],
    [sg.Column(col)],
    [sg.Button('Start'), sg.Button('Stop'), sg.Checkbox('Auto Back Button', default=False)]
]

window = sg.Window("Automatic Wabbajack by ge1c4t", layout, finalize=True, keep_on_top=True)

def printWindow(string):
    text = window['-TEXT-']
    text.print(string)
    print(string)

def autostuff():
    global autoproc, running
    while True and running:
        global step, timer
        time.sleep(3)
        slowbuttonloc = pyautogui.locateOnScreen('img/slow download.png', confidence = conf)
        backbuttonloc = pyautogui.locateOnScreen('img/back.png', confidence = conf)
        if step == 0:
            printWindow('Locating slow download button...')
            if slowbuttonloc != None:
                printWindow('Clicking slow download button!')
                slowbuttonloc = pyautogui.center(slowbuttonloc)
                pyautogui.click(slowbuttonloc.x, slowbuttonloc.y)
                time.sleep(1)
                #For disabling button hover
                pyautogui.moveTo(10, 10)
                step += 1
                continue
            if slowbuttonloc == None:
                printWindow('Could not locate slow button.')
            step += 1
        if step == 1:
            if back:
                if retry == False:
                    retry = True
                    continue
                printWindow('Locating back button...')
                if backbuttonloc != None and slowbuttonloc == None and retry:
                    printWindow('Clicking back button!')
                    backbuttonloc = pyautogui.center(backbuttonloc)
                    pyautogui.click(backbuttonloc.x, backbuttonloc.y)
                    retry = False
                if backbuttonloc == None:
                    printWindow('Could not locate back button.')
            step = 0


def main():
    global autoproc, running
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            if autoproc != None:
                running = False
            break
        if event == 'Start':
            printWindow('Auto Process Started.')
            running = True
            if autoproc == None:
                autoproc = Thread(target=autostuff)
                autoproc.start()
        elif event == 'Stop':
            if autoproc != None:
                printWindow('Auto Process Stopped.')
                running = False

    print("Goodbye :)")
    window.Close()

if __name__ == "__main__":
    main()