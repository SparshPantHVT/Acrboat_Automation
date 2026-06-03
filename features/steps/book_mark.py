from behave import given, when, then, step
import time
import pyautogui
import pyperclip

@then('user clicks on Book Mark option in the RHP')
def step_impl(context):
    success = context.vision.click_element("book_mark/book_mark", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Book Mark option"

@then('user clicks on KPI Option Present in the Book Mark Panel')
def step_impl(context):
    success = context.vision.click_element("book_mark/heading", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Book Mark option"  
    
@then('user clicks on verfies the text present in the PDF for the selected heading')
def step_impl(context):
    success = context.vision.wait_for_element("book_mark/content", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to verify the content"        