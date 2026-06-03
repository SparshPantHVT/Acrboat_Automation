from behave import given, when, then, step
import time
import pyautogui
import pyperclip

@when('user clicks on E-sign option to open the tab')
def step_impl(context):
    success = context.vision.click_element("helper\e_sign", 
         timeout=10                                  
         )
    time.sleep(20)
    assert success is True, "Failed to click on E-Sign option"

@then('user clicks on add signature option')
def step_impl(context):
    success = context.vision.click_element("helper/add_sign", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click Add Signature option"    

@then('user choose a style for the signature')
def step_impl(context):
    success = context.vision.click_element("helper\change_style",
                timeout = 10
                )    
    time.sleep(10)
    assert success is True, "Failed to change the signature style"   

@then('user choose a style for the signature to be applied')
def step_impl(context):
    success = context.vision.click_element("helper\style_1",
                timeout = 10
                )    
    time.sleep(10)
    assert success is True, "Failed to choose the signature style"     


@then('user applied the style for')
def step_impl(context):
    success = context.vision.click_element("helper/apply_style",
                timeout = 10
                )    
    time.sleep(10)
    assert success is True, "Failed to apply the changes"      

@then('user choose a location for applying the sign')
def step_impl(context):
    success = context.vision.click_element("helper/sign_space",
                timeout = 10
                )    
    time.sleep(10)
    assert success is True, "Failed to choose the location"  

@then('user verifies the signature is applied in the document')
def step_impl(context):
    success = context.vision.wait_for_element("helper/sign_visible",
                timeout = 10
                )    
    time.sleep(10)
    assert success is True, "Failed to choose the location"            