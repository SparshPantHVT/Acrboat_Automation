from behave import given, when, then
import time

@when('user clicks on generate ppt button to create ppt')
def step_impl(context):
    success = context.vision.click_element("generate\gen_ppt_home", 
         timeout=10                                  
         )
    time.sleep(10)
    assert success is True, "Failed to click on Genarate PPT button"


@then('the user adds a demo prompt in prompt area')
def step_impl(context):
    success = context.vision.click_element("generate\demo_prompt", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to add a demo prompt"

@then('the user clicks on continue to select the template')
def step_impl(context):
    success = context.vision.click_element("generate\continue_button", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on continue"  

@then('the user selects a presentation template')
def step_impl(context):
    success = context.vision.click_element("generate\ppt_template", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to choose a template"    

@then('the user clicks on Generate')
def step_impl(context):
    success = context.vision.click_element("generate\generate_button", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Generate button"     


@then('the user clicks on Add File option to add a file')
def step_impl(context):
    success = context.vision.click_element("ppt/add_file", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Add File option"         

@then('the user clicks on Customize menu')
def step_impl(context):
    success = context.vision.click_element("ppt/customize_options", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Customize Options" 

@then('the user clicks on add button')
def step_impl(context):
    success = context.vision.click_element("ppt/add_btn", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Add Button"                  

@then('the user clicks on Customize menu to click on Length')
def step_impl(context):
    success = context.vision.click_element("ppt/length_slides", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Length Slides"     

@then('the user clicks on Length to choose ppt slide')
def step_impl(context):
    success = context.vision.click_element("ppt/short_slides", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Length Slides"    

@then('the user clicks on use for PPT button')
def step_impl(context):
    success = context.vision.click_element("ppt/use_ppt", 
         timeout=10                                  
         )
    time.sleep(5)
    assert success is True, "Failed to click on Use as Presentation"      