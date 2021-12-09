import mss
import mss.tools
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os

import time
def save_screenshot(path=r"../screenshots", num=0):
    if not os.path.exists(path):
        os.makedirs(path)

    with mss.mss() as sct:
        # Get information of monitor 2
        monitor_number = 2
        mon = sct.monitors[monitor_number]

        # The screen part to capture
        monitor = {
            "top": mon["top"],
            "left": mon["left"],
            "width": mon["width"],
            "height": mon["height"],
            "mon": monitor_number,
        }
        output = "{}/{}.png".format(path, num)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)

def convert_to_rgb(path=r"../screenshots", num=0):
    image = Image.open("{}/{}.png".format(path, num))
    return image.convert('RGB')


def run(last_slide=205):
    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # counter = 0
    # driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
    # driver.get("https://turgibot.github.io/RoboticsAlgorithmsPart2/")
    # element = WebDriverWait(driver, 100).until(
    #         EC.element_to_be_clickable((By.CLASS_NAME, "navigate-right")))
    # element.click()
    # driver.fullscreen_window()
    # time.sleep(5)
    # save_screenshot(num=0)
    # time.sleep(0.5)
    
    
    # for i in range(1,last_slide):
    #     element = WebDriverWait(driver, 100).until(
    #         EC.element_to_be_clickable((By.CLASS_NAME, "navigate-right")))
    #     element.click()
    #     time.sleep(5)
    #     save_screenshot(num=i)
    #     time.sleep(0.5)
    
    images = []
    im1 = convert_to_rgb()
    images.append(im1)

    for i in range(1, last_slide):
        images.append(convert_to_rgb(num=i))
    
    im1.save('slides.pdf', save_all=True, append_images=images)

    # driver.quit()


run(45)