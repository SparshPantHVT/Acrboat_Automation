from behave import given, when, then
import time
import pyautogui
import pyperclip

@then('user clicks on edit Image Card')
def step_impl(context):
    success = context.vision.click_element("edit_image/edit_image", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Edit Image Card"

@then('user clicks on Effects Tab')
def step_impl(context):
    success = context.vision.click_element("edit_image/effects", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Effects Tab" 

@then('user clicks on Gray Scale Tone')
def step_impl(context):
    success = context.vision.click_element("edit_image/gray_scale", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Gray Scale Tone"  

@then('user should see that the tone is changed to Gray Scale') 
def step_impl(context):
    success = context.vision.wait_for_element("edit_image/gray_image",
            timeout = 10                                                                    
            )       
    time.sleep(5)
    assert success is True, "Failed to view the Image"

@then('user clicks on Edit Tab')
def step_impl(context):
    success = context.vision.click_element("edit_image/edit_tab",
            timeout = 10                               
            )    
    time.sleep(5)
    assert success is True, "Failed to click on Edit Tab"

@then('user clicks on Flip Button to Flip the Image')
def step_impl(context):
    success = context.vision.click_element("edit_image/flip_image",
            timeout = 10                               
            )    
    time.sleep(4)
    assert success is True, "Failed to click on Flip Button"

@then('user clicks on Vertical Flip')
def step_impl(context):
    success = context.vision.click_element("edit_image/vertical_flip",
            timeout = 10                               
            )    
    time.sleep(3)
    assert success is True, "Failed to click on Vertical Flip"

@then('user should see that the Image is grayed out an as well Flipped')
def step_impl(context):
    success = context.vision.wait_for_element("edit_image/vertical_image",
           timeout = 10                                   
           )      
    time.sleep(3)
    assert success is True, "Failed to View the image"


@then('the user opens the local Image file for "{file_path}"')
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
    print("  -> Waiting 15 seconds for Image to load...")
    time.sleep(15)    