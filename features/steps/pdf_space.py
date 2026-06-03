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
     
@then('the user click on Create PDF space Card in Home Page')
def step_impl(context):
    success = context.vision.click_element("gen_pdf_space/create_btn", 
              timeout=10
              )
    time.sleep(5)
    assert success is True, "Failed to click on Create PDF space Card in Home Page"

@then('the user click on Web Link Button')
def step_impl(context):
    success = context.vision.click_element("gen_pdf_space/web_link", 
              timeout=10
              )
    time.sleep(5)
    assert success is True, "Failed to click on Web Link Button"

@then('the user click on Text Box inside the Web Link pop up')
def step_impl(context):
    success = context.vision.click_element("gen_pdf_space/text_box", 
              timeout=10
              )
    time.sleep(5)
    assert success is True, "Failed to click on Text Box inside the Web Link pop up"   
    
@then('the user click add files later button to close')
def step_impl(context):
    success = context.vision.click_element("gen_pdf_space/add_files_later", 
              timeout=10
              )
    time.sleep(10)
    assert success is True, "Failed to click on add files later button to close"   

@then('the user click on Web Link Card in Home Page')
def step_impl(context):
    success = context.vision.click_element("gen_pdf_space/web_pages_url", 
              timeout=10
              )
    time.sleep(5)
    assert success is True, "Failed to click on Web Link Card in Home Page"    

@then('the user gives the URL for PDF Space "{file_path}"')
def step_impl(context, file_path):
    print(f"  -> Triggering Open File Dialog for {file_path}...")
        
    time.sleep(2) # Wait for the native Windows dialog to render
    
    # 2. Paste the exact file path into the dialog to avoid typo/Caps Lock issues
    pyperclip.copy(file_path)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    
    # 3. Hit Enter to open the file
    pyautogui.press('enter')
    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 4 seconds for PDF to load...")
    time.sleep(4)

@then('the user click on Add Button to Continue the Process')
def step_impl(context):
    success = context.vision.click_element("gen_pdf_space/add_btn", 
              timeout=10
              )
    time.sleep(5)
    assert success is True, "Failed to click on Add Button to Continue the Process" 

@then('the user click on Add to PDF Space Button to Continue the Process')
def step_impl(context):
    success = context.vision.click_element("gen_pdf_space/add_to_pdf_space", 
              timeout=10
              )
    time.sleep(5)
    assert success is True, "Failed to click on Add to PDF Space Button to Continue the Process"     

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
