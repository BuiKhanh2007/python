import pyautogui as pag
import time

image = 'face.png'
loc = pag.locateOnScreen(image)
pag.click(loc)