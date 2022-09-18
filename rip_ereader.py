import pygetwindow
import time
import pyautogui
import PIL
import math

width, height = pyautogui.size()

my = pygetwindow.getWindowsWithTitle("misael's Kindle for PC 5 - The World's Worst Assistant")[0]

new_width = width // 2
new_height = height // 2

my.resizeTo(new_width, new_height)
my.moveTo(0,0)
time.sleep(3)
my.activate()


# crop image to only kindle window

width_offset = new_width * .058229
height_offset = new_height * .134399

click_right_pos_x = math.floor(new_width * .85)
click_right_pos_y = new_height // 2

for i in range(10):
    time.sleep(1)
    p = pyautogui.screenshot()
    p.save(f'{i}.png')

    im = PIL.Image.open(f'{i}.png')
    im_crop = im.crop((width_offset, height_offset, new_width, new_height))
    im_crop.save(f'{i}.png', quality=100)

    # image saved, go to next page
    pyautogui.click(click_right_pos_x, click_right_pos_y)
