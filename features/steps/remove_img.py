from behave import given, when, then
import time
import pyautogui
import pyperclip

@then('user clicks on Start New Design Card')
def step_impl(context):
    success = context.vision.click_element("remove_bg/start_new_design", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Start New Design card"

@then('user clicks Quick Action Menu')
def step_impl(context):
    success = context.vision.click_element("remove_bg/quick_actions", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Quick Actions Menu"    

@then('user clicks on remove background option')
def step_impl(context):
    success = context.vision.click_element("remove_bg/remove_bg",
          timeout = 10                                 
          )    
    time.sleep(15)
    assert success is True, "Failed to click on remove backrgound"

@then('user should see the Background Removed Image')
def step_impl(context):
    success = context.vision.wait_for_element("remove_bg/bg_removed",
            timeout = 10                               
            )    
    time.sleep(5)
    assert success is True, "Failed to view the removed image"