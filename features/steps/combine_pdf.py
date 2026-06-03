from behave import given, when, then, step
import time
import pyautogui
import pyperclip

@when('user clicks on combine pdf button')
def step_impl(context):
    success = context.vision.click_element("home\combine_pdf", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Combine PDF menu"

@then('user selects add file button to select first file')    
def step_impl(context):
    success = context.vision.click_element("helper/add_files",
            timeout=10                                                                
            )
    time.sleep(10)
    assert success is True, "Failed to click on Add Files"

@then('user add another file for combining the PDFs') 
def step_impl(context):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('i')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

@then('user clicks on Combine Button to button')    
def step_impl(context):
    success = context.vision.click_element("home\pdf_combine",
            timeout=10                                                                
            )
    time.sleep(10)
    assert success is True, "Failed to click on combine button"  

@then('user clicks on Combine as pdf option to combine the pdfs')    
def step_impl(context):
    success = context.vision.click_element("helper\combine_as_pdf",
            timeout=10                                                                
            )
    time.sleep(10)
    assert success is True, "Failed to click on combine as PDF option"       

@then('the user verifies that the pdfs are combined into one')
def step_impl(context):
    print("  -> Verifying the combined document....")
    # Wait for the file saved visual indicator
    success = context.vision.wait_for_element("home\ybinder_text", 
              timeout=10
              )
    assert success is True, "Failed to visually verify the format"      