import pyautogui
import cv2 as cv
import time
import PySimpleGUI as sg
from threading import Thread
import threading
import subprocess

#step 0: manual download
#step 1: additional download
#step 2: slow download
#step 3: back button
step = 0
timer = 0
conf = 0.8
retry = False
back = False
running = False
status = "Automatic Wabbajack v0.1"
tag = "@ge1c4t"
autoproc = None

sg.theme('DarkPurple4')
col = [
    [sg.Multiline(size=(40,15), background_color='black', text_color='white', key='-TEXT-')]
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
    add = 0
    while True and running:
        global step, timer
        time.sleep(3)
        manualbuttonloc = pyautogui.locateOnScreen('manual.png', confidence = conf)
        additionalbuttonloc = pyautogui.locateOnScreen('additional download.png', confidence = 0.9)
        slowbuttonloc = pyautogui.locateOnScreen('slow download.png', confidence = conf)
        backbuttonloc = pyautogui.locateOnScreen('back.png', confidence = conf)
        printWindow("[" + str(timer) + "] Attempted Actions")
        timer += 1
        if step == 0:
            printWindow('Locating manual download button...')
            if manualbuttonloc != None:
                printWindow('Clicking manual download button!')
                manualbuttonloc = pyautogui.center(manualbuttonloc)
                pyautogui.click(manualbuttonloc.x, manualbuttonloc.y)
                step += 1
                continue
            if manualbuttonloc == None:
                printWindow('Could not locate manual download button.')
            step += 1
        if step == 1:
            printWindow('Locating additional download button...')
            if additionalbuttonloc != None:
                printWindow('Clicking additional download button!')
                additionalbuttonloc = pyautogui.center(additionalbuttonloc)
                pyautogui.click(additionalbuttonloc.x, additionalbuttonloc.y)
                step += 1
                continue
            if additionalbuttonloc == None:
                printWindow('Could not locate additional download button.')
            step += 1
        if step == 2:
            printWindow('Locating slow download button...')
            if slowbuttonloc != None:
                printWindow('Clicking slow download button!')
                slowbuttonloc = pyautogui.center(slowbuttonloc)
                pyautogui.click(slowbuttonloc.x, slowbuttonloc.y)
                step += 1
                time.sleep(6)
                continue
            if slowbuttonloc == None:
                printWindow('Could not locate slow button.')
            time.sleep(6)
            step += 1
        if step == 3:
            if back:
                if retry == False:
                    retry = True
                    continue
                printWindow('Locating back button...')
                if backbuttonloc != None and manualbuttonloc == None and additionalbuttonloc == None and slowbuttonloc == None and retry:
                    printWindow('Clicking back button!')
                    backbuttonloc = pyautogui.center(backbuttonloc)
                    pyautogui.click(backbuttonloc.x, backbuttonloc.y)
                    retry = False
                if backbuttonloc == None:
                    printWindow('Could not locate back button.')
            step = 0
            timer += 1


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