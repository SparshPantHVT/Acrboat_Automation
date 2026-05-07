import os
import time
import pyautogui
from PIL import ImageGrab

class VisionEngine:
    def __init__(self, image_dir=r"C:\Users\sparsh.pant\desktop_automation\templates"):
        self.image_dir = image_dir
        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)
            
    def click_element(self, element_path, text_fallback=None, region=None, timeout=10):
        """
        Attempts to find an element by its auto-captured image first.
        element_path can include subdirectories (e.g., 'home/menu').
        Uses FluentWait to continuously poll the screen until the UI element renders.
        """
        # Ensure the file has a .png extension
        if not element_path.endswith('.png'):
            element_path += '.png'
            
        image_path = os.path.join(self.image_dir, element_path)
        
        # Ensure the specific subdirectories exist for this image
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        
        print(f"\n[Vision] Attempting to click '{element_path}'...")
        
        if not os.path.exists(image_path):
            print(f"  -> [FAIL] Reference image not found at: {image_path}")
            print(f"     Please take a Snipping Tool screenshot and save it there.")
            return False

        print(f"  -> Found existing reference image. Polling with FluentWait up to {timeout}s...")
        from utils.fluent_wait import FluentWait
        wait = FluentWait(timeout=timeout)
        
        def find_image():
            return pyautogui.locateCenterOnScreen(image_path, confidence=0.8, region=region)
            
        try:
            location = wait.until(find_image, error_message=f"Image match failed for '{element_path}'")
            print(f"  -> [SUCCESS] Image matched at {location}!")
            pyautogui.moveTo(location)
            time.sleep(0.5) # Pause to let UI register hover state
            pyautogui.click(location)
            return True
        except TimeoutError as e:
            print(f"  -> [FAIL] {e}")
            return False

    def wait_for_element(self, element_path, timeout=10):
        """
        Uses FluentWait to continuously poll the screen until the UI element renders,
        but does NOT click it. Useful for final visual assertions.
        """
        if not element_path.endswith('.png'):
            element_path += '.png'
            
        image_path = os.path.join(self.image_dir, element_path)
        print(f"\n[Vision] Waiting for '{element_path}' to appear on screen...")
        
        if not os.path.exists(image_path):
            print(f"  -> [FAIL] Reference image not found at: {image_path}")
            return False

        from utils.fluent_wait import FluentWait
        wait = FluentWait(timeout=timeout)
        
        def find_image():
            return pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            
        try:
            location = wait.until(find_image, error_message=f"Image match failed for '{element_path}'")
            print(f"  -> [SUCCESS] Element verified at {location}!")
            return True
        except TimeoutError as e:
            print(f"  -> [FAIL] {e}")
            return False

    def scroll_and_click(self, target_element_path, focus_element_path, scroll_amount=-300, timeout=15):
        """
        Dynamically hovers over a 'focus' element (e.g., a panel header) to lock the mouse into 
        a specific scrollable view, then scrolls the mouse wheel until it finds the target element.
        """
        if not focus_element_path.endswith('.png'): focus_element_path += '.png'
        if not target_element_path.endswith('.png'): target_element_path += '.png'
        
        focus_path = os.path.join(self.image_dir, focus_element_path)
        target_path = os.path.join(self.image_dir, target_element_path)
        
        print(f"\n[Vision] Attempting to scroll and click '{target_element_path}' inside '{focus_element_path}'...")
        
        if not os.path.exists(focus_path) or not os.path.exists(target_path):
            print(f"  -> [FAIL] Missing reference images. Ensure both '{focus_element_path}' and '{target_element_path}' exist.")
            return False
            
        print(f"  -> Focusing the view panel...")
        # We don't use FluentWait for focus_path because it should already be on screen
        try:
            focus_location = pyautogui.locateCenterOnScreen(focus_path, confidence=0.8)
            if focus_location:
                pyautogui.moveTo(focus_location)
                print(f"  -> View focused. Beginning scroll-and-poll sequence...")
            else:
                raise Exception("Not found")
        except Exception:
            print(f"  -> [FAIL] Could not find the focus element '{focus_element_path}' on screen.")
            return False

        from utils.fluent_wait import FluentWait
        wait = FluentWait(timeout=timeout, poll_frequency=0.2)
        
        def find_target():
            return pyautogui.locateCenterOnScreen(target_path, confidence=0.8)
            
        def scroll_action():
            pyautogui.scroll(scroll_amount)
            time.sleep(0.5) # Wait for UI to render the scroll
            
        try:
            location = wait.until(find_target, on_poll_fail=scroll_action, error_message=f"Could not find '{target_element_path}' after scrolling")
            print(f"  -> [SUCCESS] Target matched at {location}!")
            pyautogui.click(location)
            return True
        except TimeoutError as e:
            print(f"  -> [FAIL] {e}")
            return False

    def click_within_anchor(self, target_element_path, anchor_element_path, timeout=15):
        """
        Dynamically finds the bounding box of 'anchor_element_path' and restricts the 
        search for 'target_element_path' strictly to that region.
        """
        if not anchor_element_path.endswith('.png'): anchor_element_path += '.png'
        if not target_element_path.endswith('.png'): target_element_path += '.png'
        
        anchor_path = os.path.join(self.image_dir, anchor_element_path)
        target_path = os.path.join(self.image_dir, target_element_path)
        
        print(f"\n[Vision] Attempting to click '{target_element_path}' inside the bounding box of '{anchor_element_path}'...")
        
        if not os.path.exists(anchor_path) or not os.path.exists(target_path):
            print(f"  -> [FAIL] Missing reference images.")
            return False
            
        print(f"  -> Finding anchor bounding box...")
        from utils.fluent_wait import FluentWait
        wait = FluentWait(timeout=timeout, poll_frequency=0.2)
        
        def find_anchor():
            return pyautogui.locateOnScreen(anchor_path, confidence=0.8)
            
        try:
            anchor_box = wait.until(find_anchor, error_message=f"Could not find the anchor element '{anchor_element_path}'")
            print(f"  -> Anchor found at {anchor_box}. Restricting search to this region.")
        except TimeoutError as e:
            print(f"  -> [FAIL] {e}")
            return False

        def find_target_in_region():
            # Add a 10px padding to the bounding box to prevent OpenCV from cutting off edge pixels
            padded_region = (
                max(0, int(anchor_box.left) - 10),
                max(0, int(anchor_box.top) - 10),
                int(anchor_box.width) + 20,
                int(anchor_box.height) + 20
            )
            return pyautogui.locateCenterOnScreen(target_path, confidence=0.8, region=padded_region)
            
        try:
            location = wait.until(find_target_in_region, error_message=f"Could not find '{target_element_path}' inside the anchor's bounding box")
            print(f"  -> [SUCCESS] Target matched at {location}!")
            pyautogui.click(location)
            return True
        except TimeoutError as e:
            print(f"  -> [FAIL] {e}")
            return False

    def type_relative_to_label(self, label_element_path, text_to_type, height_multiplier=1.5, timeout=15, delay_before_typing=0.5):
        """
        Finds a static text label, calculates a dynamic scale-proof offset based on the label's height,
        clicks into the corresponding input box, clears any auto-filled text, and types the new text.
        """
        if not label_element_path.endswith('.png'): label_element_path += '.png'
        label_path = os.path.join(self.image_dir, label_element_path)
        
        print(f"\n[Vision] Attempting to type '{text_to_type}' relative to label '{label_element_path}'...")
        
        if not os.path.exists(label_path):
            print(f"  -> [FAIL] Missing reference image for label '{label_element_path}'.")
            return False
            
        from utils.fluent_wait import FluentWait
        wait = FluentWait(timeout=timeout, poll_frequency=0.2)
        
        def find_label():
            return pyautogui.locateOnScreen(label_path, confidence=0.8)
            
        try:
            label_box = wait.until(find_label, error_message=f"Could not find label '{label_element_path}'")
            print(f"  -> Label found at {label_box}.")
        except TimeoutError as e:
            print(f"  -> [FAIL] {e}")
            return False
            
        # Optional delay to allow web page javascript/animations to settle
        if delay_before_typing > 0:
            time.sleep(delay_before_typing)
            
        # Calculate dynamic scale-proof coordinates
        # click_y = bottom of label + (height * multiplier)
        click_x = int(label_box.left + (label_box.width / 2))
        click_y = int(label_box.top + label_box.height + (label_box.height * height_multiplier))
        
        print(f"  -> Clicking computed offset at ({click_x}, {click_y}) to focus input field...")
        pyautogui.click(click_x, click_y)
        
        # Clear auto-filled text using standard OS hotkeys
        print(f"  -> Clearing cached text and typing...")
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(0.1) # brief pause to let UI react
        
        # Use Clipboard Pasting to inject text (bypasses physical Caps Lock states)
        import pyperclip
        pyperclip.copy(text_to_type)
        pyautogui.hotkey('ctrl', 'v')
        
        print(f"  -> [SUCCESS] Text injected securely via clipboard.")
        return True
