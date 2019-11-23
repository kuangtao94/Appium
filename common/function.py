
#截图功能

import os
import time

def insert_image(driver,picturetype):
    image_path =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'Image')
    timer = time.strftime('%Y_%m_%d_%H_%M_%S')
    new_path = image_path + '\\' + timer + picturetype
    # return new_path
    driver.get_screenshot_as_file(new_path)



