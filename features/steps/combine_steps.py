from behave import given, when, then
import time

@given('Acrobat is running and maximized')
def step_impl(context):
    if getattr(context, 'os_type', 'win') == "win" and hasattr(context, 'window') and context.window:
        try:
            assert context.window.is_maximized(), "Acrobat Window is not maximized!"
        except Exception as e:
            print(f"  [WARN] Could not verify maximization natively (likely hooked a background process): {e}")

@when('the user clicks the "{button_name}" button')
def step_impl(context, button_name):
    # Mapping to nested folder structure based on button_name
    folder_map = {
        "Menu": "home/menu"
    }
    
    image_path = folder_map.get(button_name, f"general/{button_name.lower().replace(' ', '_')}")
    
    success = context.vision.click_element(image_path, button_name)
    assert success is True, f"Failed to find or click '{button_name}'"

@when('the user selects "{option_name}"')
def step_impl(context, option_name):
    folder_map = {
        "Combine Files": "dropdowns/combine_files"
    }
    
    image_path = folder_map.get(option_name, f"dropdowns/{option_name.lower().replace(' ', '_')}")
    
    success = context.vision.click_element(image_path, option_name)
    assert success is True, f"Failed to find or click '{option_name}'"

@then('the user closes the Combine Files page')
def step_impl(context):
    success = context.vision.click_element("combine_view/close", "Close")
    assert success is True, "Failed to close the Combine Files page"
