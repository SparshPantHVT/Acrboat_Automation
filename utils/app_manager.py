import os
import time
import subprocess

class AcrobatAppManager:
    """Manages the lifecycle of the Adobe Acrobat application natively."""
    
    def __init__(self, os_type="win", exe_path=r"C:\Program Files\Adobe\Acrobat Beta\Acrobat\Acrobat.exe"):
        self.os_type = os_type.lower()
        self.exe_path = exe_path
        self.app = None
        
    def start_acrobat(self):
        """Kills existing instances and starts a clean Acrobat session."""
        self.stop_acrobat()
        print("Launching Adobe Acrobat...")
        
        if self.os_type == "win":
            from pywinauto.application import Application
            # Start application via pywinauto on Windows
            self.app = Application(backend="uia").start(f'"{self.exe_path}"', timeout=15)
            time.sleep(5)
            return self.app
        else:
            # Start application natively on macOS
            subprocess.Popen(['open', '-a', 'Adobe Acrobat'])
            time.sleep(5)
            return None
        
    def stop_acrobat(self):
        """Force kills all Acrobat processes to ensure a clean state."""
        print("Cleaning up Acrobat processes...")
        if self.os_type == "win":
            os.system("taskkill /f /im Acrobat.exe >nul 2>&1")
        else:
            os.system("killall 'Adobe Acrobat' >/dev/null 2>&1")
        time.sleep(2)
        
    def get_main_window(self):
        """Hooks into the main Acrobat window and maximizes it."""
        print("Hooking into Acrobat Main Window...")
        if self.os_type == "win":
            from pywinauto import Desktop
            desktop = Desktop(backend="uia")
            main_window = desktop.window(title_re=".*Adobe Acrobat.*", found_index=0)
            
            main_window.wait('ready', timeout=30)
            
            try:
                if main_window.is_minimized():
                    main_window.restore()
                # Maximizing is CRITICAL for Computer Vision to have a stable starting point
                main_window.maximize()
                main_window.set_focus()
            except Exception as e:
                print(f"  [WARN] Could not manipulate window natively (likely a background process): {e}")
            time.sleep(3)
            return main_window
        else:
            # macOS handles window focus natively via the 'open -a' command
            # We just return None and rely on the OS
            time.sleep(3)
            return None
