from behave import given, when, then, step
import time
import pyautogui
import pyperclip

pyautogui.FAILSAFE = False

@step('the user opens the local file "{file_path}"')
@step('the user opens the local file for "{file_path}"')
def step_impl(context, file_path):
    print(f"  -> Triggering Open File Dialog for {file_path}...")
    
    # 0. Click the center of the screen to ensure Acrobat actually has keyboard focus!
    screen_width, screen_height = pyautogui.size()
    pyautogui.click(int(screen_width / 2), int(screen_height / 2))
    time.sleep(0.5)
    
    # 1. Trigger the OS Open File Dialog (Ctrl + O)
    pyautogui.keyDown('ctrl')
    pyautogui.press('o')
    pyautogui.keyUp('ctrl')
    
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

@when('the user triggers the "Save As" action')
def step_impl(context):
    print("  -> Triggering Save As Dialog (Ctrl + Shift + S)...")
    try:
        # 0. Ensure focus
        screen_width, screen_height = pyautogui.size()
        pyautogui.click(int(screen_width / 2), int(screen_height / 2))
        time.sleep(0.5)
        
        # 1. Trigger Save As
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('s')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')
        
        # Wait for the Acrobat specific "Save as PDF" dialog to open
        time.sleep(2)
    except Exception as e:
        print(f"  -> [PYTHON ERROR IN STEP]: {str(e)}")
        raise e

@when('the user selects "{connector}" from the Save As locations')
def step_impl(context, connector):
    prefix = connector.lower().replace(' ', '_') # e.g. "box"
    print(f"  -> Selecting {connector} in the Save Dialog...")
    
    # We use the generic save_dialog folder as requested by the user
    image_path = f"save_dialog/{prefix}_save_location"
    
    success = context.vision.click_element(image_path, timeout=10)
    assert success is True, f"Failed to find and click the {connector} save location in the dialog."
    
    time.sleep(1) # Brief pause to let the location load

@then('the user saves the file')
def step_impl(context):
    print("  -> Clicking the blue Save button...")
    
    # Click the generic blue save button from the new save_dialog directory
    success = context.vision.click_element("save_dialog/blue_save_button", timeout=10)
    assert success is True, "Failed to find and click the Save button."
    
    print("  -> Waiting for file to upload to the cloud...")
    time.sleep(5) # Wait for the upload/save progress bar to finish before tearing down

@then('the user verifies the file is saved successfully')
def step_impl(context):
    print("  -> Verifying the file was saved successfully...")
    # Wait for the file saved visual indicator
    success = context.vision.wait_for_element("save_dialog/file_saved_success", timeout=15)
    assert success is True, "Failed to visually verify the file was saved successfully."
    
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
