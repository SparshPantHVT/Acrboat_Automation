from behave import given, when, then
import time
import pyautogui
import pyperclip

@when('the user clicks on menu button to open the menu')
def step_impl(context):
    success = context.vision.click_element("home/menu", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on menu button"

@then('the user clicks on open file button')
def step_impl(context):
    success = context.vision.click_element("home/open_btn", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on open file"    

@when('the user opens the local file from the system "{file_path}"')
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

@then('the user clicks on AI Assistant CTA')
def step_impl(context):
    success = context.vision.click_element("helper/ai_assistant_btn", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on open file"   

@when('the user enters a prompt for the action which has to be performed using the AI "{enter_prompt}"')
def step_impl(context, enter_prompt):
    print(f"  -> Triggering Open File Dialog for {enter_prompt}...")
    
    time.sleep(2) # Wait for the native Windows dialog to render
    
    # 2. Paste the exact file path into the dialog to avoid typo/Caps Lock issues
    pyperclip.copy(enter_prompt)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    
    # 3. Hit Enter to open the file
    pyautogui.press('enter')
    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 10 enter the prompt...")
    time.sleep(10)

@then('the user verifies that the page is scrolled to the respective page')
def step_impl(context):
    print("  -> Verifying the page is visible...")
    # Wait for the file saved visual indicator
    success = context.vision.wait_for_element("helper/page_index", 
              timeout=10
              )
    assert success is True, "Failed to visually verify the page index."  

@then('the user verifies that the page is rotated as expected')
def step_impl(context):
    print("  -> Verifying the page is visible...")
    # Wait for the file saved visual indicator
    success = context.vision.wait_for_element("helper/180_degree", 
              timeout=10
              )
    assert success is True, "Failed to visually verify rotated page."              