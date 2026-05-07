import sys
import os
import pyautogui
from datetime import datetime
from behave.model_core import Status
import allure

# Ensure we can import the adobe_acrobat_automation package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.app_manager import AcrobatAppManager
from pages.cv_engine import VisionEngine

def before_scenario(context, scenario):
    """Start Acrobat and initialize the Vision Engine before each scenario."""
    print(f"\n--- Starting Scenario: {scenario.name} ---")
    
    # Get OS type from CLI args (default to win)
    context.os_type = context.config.userdata.get('os', 'win').lower()
    
    # Start App Manager
    context.manager = AcrobatAppManager(os_type=context.os_type)
    context.manager.start_acrobat()
    context.window = context.manager.get_main_window()
    
    # Start Vision Engine
    context.vision = VisionEngine()

def after_scenario(context, scenario):
    """Clean up Acrobat after each scenario and capture failures."""
    print(f"\n--- Ending Scenario: {scenario.name} ---")
    
    # 1. Failure Handling: Take a screenshot if the test fails
    if scenario.status == Status.failed:
        print(f"  [ERROR] Scenario Failed! Capturing error screenshot...")
        failures_dir = os.path.join(os.path.dirname(__file__), '..', 'reports', 'failures')
        os.makedirs(failures_dir, exist_ok=True)
        
        # Create a unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = scenario.name.replace(' ', '_').replace('"', '')
        screenshot_path = os.path.join(failures_dir, f"FAIL_{safe_name}_{timestamp}.png")
        
        try:
            pyautogui.screenshot(screenshot_path)
            print(f"  [SAVED] Debug screenshot saved to: {screenshot_path}")
            allure.attach.file(screenshot_path, name="Failure_Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"  [FAIL] Could not capture screenshot: {e}")
            
    # 2. Lifecycle Management: Always close Acrobat when the scenario ends
    if hasattr(context, 'manager'):
        context.manager.stop_acrobat()
