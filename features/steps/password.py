from behave import given, when, then, step
import time
import pyautogui
import pyperclip

@then('user clicks on convert search button in the top bar')
def step_impl(context):
    success = context.vision.click_element("helper\search_tool", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click Search ToolBar"

@then('user clicks on portect PDF button to protect the PDF')
def step_iml(context):
    success = context.vision.click_element("password\pass_option",
         timeout = 10                                  
         )    
    time.sleep(2)
    assert success is True, "Failed to click on Encrypt PDF option"

@then('user clicks on Protect a PDF menu in LHP view')  
def step_impl(context):
    success = context.vision.click_element("password\password_option",
        timeout = 10
        )  
    time.sleep(5)
    assert success is True, "Failed to click on Passowrd Menu"

@when('the user search for Password menu in the Edit Panel "{text_search}"')
def step_impl(context, text_search):
    print(f"  -> Triggering Open File Dialog for {text_search}...")
    
    time.sleep(2) # Wait for the native Windows dialog to render
    
    # 2. Paste the exact file path into the dialog to avoid typo/Caps Lock issues
    pyperclip.copy(text_search)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    
    # 4. Wait for Adobe Acrobat to fully render the PDF
    print("  -> Waiting 4 seconds for option to be load...")
    time.sleep(4)       

@then('user clicks on Type Passowrd text Box')    
def step_impl(context):
    success = context.vision.click_element("password/type_pass",
            timeout = 10
            )
    time.sleep(3)
    assert success is True, "Failed to click on Text Box"

@then('user clicks on Apply button to Confirm the Password')    
def step_impl(context):
    success = context.vision.click_element("password/apply_btn",
            timeout = 10
            )
    time.sleep(3)
    assert success is True, "Failed to click on Apply Button"  

@then('user should see the confirmation Toast')    
def step_impl(context):
    success = context.vision.wait_for_element("password/confirmation_toast",
            timeout = 10
            )
    time.sleep(3)
    assert success is True, "Failed to view to toast"   
