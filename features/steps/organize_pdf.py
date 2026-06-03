from behave import given, when, then
import time
import pyautogui
import pyperclip

@then('user clicks on organize page menu')
def step_impl(context):
    success = context.vision.click_element("organise_pdf/organise_pdf", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Organize PDF"

@then('user clicks on select button to select a pdf to be organized')
def step_impl(context):
    success = context.vision.click_element("organise_pdf/select_pdf", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Select a PDF"

@then('user should see that PDF is opened in multi-page view')
def step_impl(context):
    success = context.vision.wait_for_element("organise_pdf/home_view",
         timeout = 10                                     
         )
    time.sleep(5)
    assert success is True, "Failed to view the PDF"

@then('user clicks to change the page style')
def step_impl(context):
    success = context.vision.click_element("organise_pdf/selected_pages",
         timeout = 10                                 
         )   
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace') 
    time.sleep(5)
    assert success is True, "Failed to click"

@then('user clicks to change the page style to odd pages')
def step_impl(context):
    success = context.vision.click_element("organise_pdf/odd_pages",
         timeout = 10                                 
         )  
    time.sleep(5)
    assert success is True, "Failed to click on odd pages"

@then('user should see that only odd pages are selected')
def step_impl(context):
    success = context.vision.wait_for_element("organise_pdf/selected_pages_odd",
         timeout = 10                                     
         )
    time.sleep(5)
    assert success is True, "Failed to view the Selected Odd pages"

@then('the user clicks on Insert Page button')
def step_impl(context):
    success = context.vision.click_element("organise_pdf/insert",
            timeout = 10                               
            )
    time.sleep(5)
    assert success is True, "Failed to click on the insert button"    

@then('the user clicks on Insert Page button to insert a blank page') 
def step_impl(context):
    success = context.vision.click_element("organise_pdf/blank_page", 
            timeout = 10   
            )
    time.sleep(5)
    assert success is True, "Failed to choose blank page"

@then('the user clicks on OK button to insert a page') 
def step_impl(context):
    success = context.vision.click_element("organise_pdf/ok_btn", 
            timeout = 10   
            )
    time.sleep(5)
    assert success is True, "Failed to click on Ok"    