from behave import given, when, then
import time
import pyautogui
import pyperclip

@when('user clicks on select files button to open the pdf space')
def step_impl(context):
    success = context.vision.click_element("home/select_files_for_pdf_space", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Select File"

@then('user clicks on your device')
def step_impl(context):
    success = context.vision.click_element("helpers/your_devices", 
         timeout=50                                  
         )
    assert success is True, "Failed to click on Your Devices" 

@then('user click on Select Files to select file')
def step_impl(context):
    success = context.vision.click_element("helpers/select_files_your_device", 
         timeout=10                                  
         )
    assert success is True, "Failed to click on Your Devices" 

@then('user click on the checkbox to select the recent files')
def step_impl(context):
    success = context.vision.click_element("helpers/select_files_your_device", 
         timeout=10                                  
         )
    assert success is True, "Failed to click on Your Devices" 

@then('user select a file from the recents option')
def step_impl(context):
    success = context.vision.click_element("helpers/recent_files_checkbox", 
         timeout=10                                  
         )
    assert success is True, "Failed to select a file" 

@then('user selects create pdf space button')
def step_impl(context):
    success = context.vision.click_element("helpers/create_pdf_space", 
         timeout=10                                  
         )
    assert success is True, "Failed to click on create pdf space button"

@then('user clicks on skip tour button')
def step_impl(context):
    success = context.vision.click_element("helpers/skip_tour", 
         timeout=10                                  
         )
    assert success is True, "Failed to click on skip tour button"

@then('user clicks on insights button')
def step_impl(context):
    success = context.vision.click_element("helpers/insights_button", 
         timeout=10                                  
         )
    time.sleep(15)
    assert success is True, "Failed to click insights button"             

@then('the user verifies that the insights are visible')
def step_impl(context):
    print("  -> Verifying the insights are visible...")
    # Wait for the file saved visual indicator
    success = context.vision.wait_for_element("helpers\insights_options", 
              timeout=10
              )
    assert success is True, "Failed to visually verify the insights."
     

    import allure
    import tempfile
    import os
    import pyautogui
    
    # Capture success screenshot as evidence for the Allure report
    temp_dir = tempfile.gettempdir()
    screenshot_path = os.path.join(temp_dir, f"SUCCESS_file_saved.png")
    pyautogui.screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name="File Successfully Saved Verification", attachment_type=allure.attachment_type.PNG)
    
    time.sleep(3)
