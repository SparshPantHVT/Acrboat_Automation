from behave import given, when, then, step
import time
import pyautogui
import pyperclip

@then('user clicks on convert tab present in the top bar')
def step_impl(context):
    success = context.vision.click_element("helper\convert_pdf", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Convert Menu"

@then('user clicks on convert to PPT Option')
def step_impl(context):
    success = context.vision.click_element("helper\convert_ppt", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Convert to PPT" 

@then('user clicks on convert Button to start the conversion to PPT')
def step_impl(context):
    success = context.vision.click_element("helper\convert_btn", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Convert Button"

@then('user choose the location to save the coverted file')
def step_impl(context):
    success = context.vision.click_element("helper\desktop_loc",
        timeout=10
        )    
    time.sleep(5)
    assert success is True, "Failed to save the file"      

@then('user clicks on Enter to confirm the location')
def step_impl(context):
    pyautogui.press('enter')
    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 10 enter the prompt...")
    time.sleep(10)    

@then('the user verifies that the file is converted to correct format')
def step_impl(context):
    print("  -> Verifying the converted document....")
    # Wait for the file saved visual indicator
    success = context.vision.wait_for_element("helper\ppt_format", 
              timeout=10
              )
    assert success is True, "Failed to visually verify the format"        