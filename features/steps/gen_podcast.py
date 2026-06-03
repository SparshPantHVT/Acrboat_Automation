from behave import given, when, then
import time
import pyautogui
import pyperclip

@then('user clicks on all tools button in home page')
def step_impl(context):
    success = context.vision.click_element("home/all_tools", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on All Tools"

@then('user clicks on Generate Podcast button')
def step_impl(context):
    success = context.vision.click_element("helper/gen_podcast", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Generate Podcast"    

@then('user clicks on Next Button to create podcast')
def step_impl(context):
    success = context.vision.click_element("print/next_btn", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Generate Podcast"   

@then('user clicks on Podcast Generate Option')
def step_impl(context):
    success = context.vision.click_element("helpers/generate_btn", 
         timeout=10                                  
         )
    time.sleep(100)
    assert success is True, "Failed to click on Generate Podcast to Select"   

@then('user should see the PlayBack Panel')   
def step_impl(context):       
    success = context.vision.wait_for_element("print/playback_panel", 
         timeout=10                                  
         )
    time.sleep(30)
    assert success is True, "Failed to view playback panel" 

@then('user clicks on playback speed option')    
def step_impl(context):
    success = context.vision.click_element("helper/play_back",
         timeout = 10
         )
    time.sleep(3)
    assert success is True, "Failed to click on PlayBack"

@then('user chooses a new playback speed for the podcast')    
def step_impl(context):
    success = context.vision.click_element("helpers/play_back_new",
         timeout = 10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to change the playback speed"

@then('user clicks on Expand button to view in Expanded form')   
def step_impl(context):
    success = context.vision.click_element("gen_podcast/expand",
          timeout = 10                                 
          ) 
    time.sleep(5)
    assert success is True, "Failed to click on expand button"

@then('user should see the Expanded Panel')
def step_impl(context):
    success = context.vision.wait_for_element("gen_podcast/expanded_panel",
          timeout = 10                                                                        
          )   
    time.sleep(5)
    assert success is True, "Failed to view the Expanded Panel"

@then('user clicks on Forwarding the video by 15 seconds')
def step_impl(context):
    success = context.vision.click_element("gen_podcast/forward",
          timeout = 10
          ) 
    time.sleep(5)
    assert success is True, "Failed to click on Forward Button"

@then('user should see that the Panel is at 15 Seconds') 
def step_impl(context):
    success = context.vision.click_element("gen_podcast/confirmation",
          timeout = 10                                 
          )   
    time.sleep(5)
    assert success is True, "Failed to View the Confirmation"
