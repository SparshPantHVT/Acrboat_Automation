from behave import given, when, then, step
import time
import pyautogui
import pyperclip

@when('user clicks on Edit PDF option to open Edit Section')
def step_impl(context):
    success = context.vision.click_element("home\pdf_edit", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Edit PDF Button"

@then('user clicks on pen icon to perform the PDF Edit Action')
def step_impl(context):
    success = context.vision.click_element("helper\highlight_pen", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on highlight pen"    

@then('user clicks on highlight action to highlight the text')
def step_impl(context):
    success = context.vision.click_element("helper\option", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on highlight option"  

@then('user selects the text which need to highlighted')
def step_impl(context):
    success = context.vision.click_element("helper\start_text",
            ) 
    pyautogui.keyDown('shift')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left') 
    pyautogui.keyUp('shift')                               
    time.sleep(10)
    assert success is True, "Failed to click on highlight option"    


@then('the user opens the search panel to search for the text which needs to be highlighted')
def step_impl(context):
    
    

    # 1. Trigger the OS Open File Dialog (Ctrl + O)
    pyautogui.keyDown('ctrl')
    pyautogui.press('f')
    pyautogui.keyUp('ctrl')
    
    time.sleep(2) # Wait for the native Windows dialog to render
    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 4 seconds for text to load..")
    time.sleep(4)    

@when('the user enters the text which needs to highlighted "{enter_text}"')
def step_impl(context, enter_text):
    print(f"  -> Triggering Open File Dialog for {enter_text}...")
    
    time.sleep(2) # Wait for the native Windows dialog to render
    
    # 2. Paste the exact file path into the dialog to avoid typo/Caps Lock issues
    pyperclip.copy(enter_text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    
    # 3. Hit Enter to open the file
    pyautogui.press('enter')
    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 10 enter the prompt...")
    time.sleep(10)

    
@then('user clicks on selected highlight action to highlight the text')
def step_impl(context):
    success = context.vision.click_element("helper\highlight_pen_selected", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on highlight option"  

@then('user clicks on the text which was found')  
def step_impl(context):
    success = context.vision.click_element("home\ytext_found", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on highlight option"  


@then('the user verifies that the highlighted text is visible')
def step_impl(context):
    print("  -> Verifying the highlighted texts are visible...")
    # Wait for the file saved visual indicator
    success = context.vision.wait_for_element("helper\yfinal_img", 
              timeout=10
              )
    assert success is True, "Failed to visually verify the highlighted text."    

@then('the user clicks on selected text for strike through')
def step_impl(context):
    success = context.vision.click_element("helpers\ltext_string", 
              timeout=10
              )
    assert success is True, "Failed to click on the text"     

@then('the user clicks on selected text to perform the strike through')
def step_impl(context):
    success = context.vision.click_element("helpers\strike_through", 
              timeout=10
              )
    assert success is True, "Failed to click on the strike through option"  

@then('the user clicks on the text area')
def step_impl(context):
    success = context.vision.click_element("helpers\ytext_area", 
              timeout=10
              )
    assert success is True, "Failed to click on the text area"     

@when('the user clicks on cross icon to close the search bar to enter "{new_text}"')
def step_impl(context,new_text):
    print(f"  -> Triggering Open File Dialog for {new_text}...")
    
    time.sleep(2) # Wait for the native Windows dialog to render
    
    pyautogui.hotkey('ctrl', 'a')

    # 2. Paste the exact file path into the dialog to avoid typo/Caps Lock issues
    pyperclip.copy(new_text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    
    # 3. Hit Enter to open the file
    pyautogui.press('enter')
    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 10 enter the prompt...")
    time.sleep(10)    

@when('the user clicks on cross icon to close the search box to enter "{new_string}"')
def step_impl(context,new_string):
    print(f"  -> Triggering Open File Dialog for {new_string}...")
    
    time.sleep(2) # Wait for the native Windows dialog to render
    
    pyautogui.hotkey('ctrl', 'a')

    # 2. Paste the exact file path into the dialog to avoid typo/Caps Lock issues
    pyperclip.copy(new_string)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    
    # 3. Hit Enter to open the file
    pyautogui.press('enter')
    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 10 enter the prompt...")
    time.sleep(10)    

@then('the user clicks on the text box')
def step_impl(context):
    success = context.vision.click_element("helpers\ybox_text", 
              timeout=10
              )
    assert success is True, "Failed to click on the text box"    

@then('the user clicks on the text to be underlined')
def step_impl(context):
    success = context.vision.click_element("helper\experiment_text", 
              timeout=10
              )
    assert success is True, "Failed to click on the text"     

@then('the user clicks on the underline option to underline the text')
def step_impl(context):
    success = context.vision.click_element("helpers\ybelow_line", 
              timeout=10
              )
    assert success is True, "Failed to underline the text"          