from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os

with open(os.path.abspath('drag_and_drop_helper.js'), 'r') as js_file:
    line = js_file.readline()
    script = ''
    while line:
        script += line
        line = js_file.readline()


driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
AC = ActionChains(driver)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "panel-body")))

drop_here = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div")
drag_items = driver.find_elements_by_xpath("//*[@id='todrag']/span")
drag_target = driver.find_element_by_xpath("//*[@id='todrag']/span[1]")
to_drag_default = []
to_drag_list = []
to_drag_default.extend(drag_items)
to_drag_list.extend(drag_items)

for n in range(1, len(to_drag_default)):
    driver.execute_script(script + "$('#todrag > span:nth-child(2)').simulateDragDrop({ dropTarget: '#mydropzone'});")
    driver.implicitly_wait(1)

driver.execute_script(script + "$('#todrag > span').simulateDragDrop({ dropTarget: '#mydropzone'});")

# even with JQuery support, couldn't figure out "undefined" here is validation code if dnd worked:
dragged_items_list = []
dragged_items = driver.find_elements_by_xpath("//*[@id='droppedlist']")
dragged_items_list.extend(dragged_items)

if len(dragged_items_list) == len(to_drag_default):
    print("Test Pass")
else:
    print("Test failed - Please check the log")