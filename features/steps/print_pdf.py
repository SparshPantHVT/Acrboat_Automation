from behave import given, when, then
import time
import pyautogui
import pyperclip

@then('user tries to print the PDF')
def step_impl(context):
    pyautogui.hotkey('ctrl','p')
    time.sleep(10)

@then('user selects option to only print current page')
def step_impl(context):
    pyautogui.hotkey('alt','u') 
    assert success is True, "failed to select current page"

@then('user selects new printer')    
def step_impl(context):
    success = context.vison.click_element("print/new_printer",
            timeout = 10                              
            )
    assert success is True, "failed to select new printer"

@then('user clicks on landscape orientation')    
def step_impl(context):
    success = context.vison.click_element("print\landscape",
            timeout = 10                              
            )
    assert success is True, "failed to choose the orientation"

@then('user clicks on print button to print the pdf')  
def step_impl(context):
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    assert success is True, "failed to click on Print Button"

@then('user choose the location where the PDF is to be saved')
def step_impl(context):
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(10)

@then('user should see the pop-up regarding confirmation')
def step_impl(context):
    success = context.vision.wait_for_element("print\pop-up",
            timeout = 10                                                                
            )    
    assert success is True, "Failed to View the pop-up"
