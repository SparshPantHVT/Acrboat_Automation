from behave import given, when, then
import time

@when('the user scrolls the Left Hand Panel to click "Add File Storage"')
def step_impl(context):
    success = context.vision.click_element("home/add_file_storage_button_from_LHP",
         timeout=10  
    )
    assert success is True, "Failed to scroll and find 'Add File Storage'"

@then('the user clicks the "Add" button for "{connector}" storage')
def step_impl(context, connector):
    # Dynamically build the anchor path (e.g., 'Box' -> 'box_add_button')
    anchor_name = f"{connector.lower().replace(' ', '_')}_add_button"
    
    success = context.vision.click_within_anchor(
        target_element_path="third_party_connector_view/add_button", 
        anchor_element_path=f"third_party_connector_view/{anchor_name}"
    )
    assert success is True, f"Failed to find the 'Add' button inside the {connector} card"

@then('the user authenticates with "{connector}" using email "{email}" and password "{password}"')
def step_impl(context, connector, email, password):
    prefix = connector.lower().replace(' ', '_') # e.g. "box"
    
    # 1. Type Email relative to the Email Label
    # Height multiplier 1.5 hits right below the text regardless of resolution
    email_success = context.vision.type_relative_to_label(
        label_element_path=f"third_party_connector_view/email_label_{prefix}",
        text_to_type=email,
        height_multiplier=1.5,
        timeout=30, # Give the browser up to 30s to launch and load
        delay_before_typing=1.5 # Wait 1.5s after the label appears before clicking to type
    )
    assert email_success is True, f"Failed to type into {connector} Email field"
    
    print("  -> Waiting 3 seconds before typing password to allow web UI validation...")
    time.sleep(3)
    
    # 2. Type Password relative to the Password Label
    pass_success = context.vision.type_relative_to_label(
        label_element_path=f"third_party_connector_view/password_label_{prefix}",
        text_to_type=password,
        height_multiplier=1.5
    )
    assert pass_success is True, f"Failed to type into {connector} Password field"
    
    # 3. Click Authorize Button
    auth_success = context.vision.click_element(f"third_party_connector_view/authorize_button_{prefix}")
    assert auth_success is True, f"Failed to click Authorize for {connector}"

@then('the user grants access to "{connector}"')
def step_impl(context, connector):
    prefix = connector.lower().replace(' ', '_') # e.g. "box"
    success = context.vision.click_element(
        f"third_party_connector_view/grant_access_to_{prefix}",
        timeout=30 # Give the second page up to 30s to load
    )
    assert success is True, f"Failed to click the Grant Access button for {connector}"

@then('the user allows the browser to return to Adobe Acrobat')
def step_impl(context):
    # This is a generic browser popup, so we use a generic helper image
    success = context.vision.click_element(
        "helpers/browser_open_button",
        timeout=10
    )
    assert success is True, "Failed to click 'Open' on the browser redirect popup"
    print("  -> Waiting for Adobe Acrobat to relaunch and regain focus...")

@then('the user sees the "{connector}" storage account successfully added')
def step_impl(context, connector):
    prefix = connector.lower().replace(' ', '_') # e.g. "box"
    
    # Wait up to 15 seconds for the "Box (Personal)" or similar text to appear in LHP
    # This replaces the hardcoded time.sleep(5) and serves as a strict visual assertion
    success = context.vision.wait_for_element(
        f"third_party_connector_view/{prefix}_personal_added",
        timeout=15
    )
    assert success is True, f"Failed to visually verify {connector} storage was added to the Left Hand Panel."
    
    import allure
    import tempfile
    import os
    import pyautogui
    
    # Capture success screenshot as evidence for the Allure report
    temp_dir = tempfile.gettempdir()
    screenshot_path = os.path.join(temp_dir, f"SUCCESS_{prefix}_added.png")
    pyautogui.screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name=f"{connector} Successfully Added Verification", attachment_type=allure.attachment_type.PNG)
    
    # Pause for 3 seconds so you can actually see the success before teardown!
    time.sleep(3)
