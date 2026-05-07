import time

class FluentWait:
    """
    A utility class designed to repeatedly poll a condition until it evaluates to True,
    or until a timeout is reached. This eliminates the need for hardcoded time.sleep()
    commands and makes the automation framework perfectly sync with the application's
    rendering speed.
    """
    def __init__(self, timeout=10, poll_frequency=0.2):
        """
        :param timeout: Maximum time in seconds to wait before failing.
        :param poll_frequency: Time in seconds to sleep between polls.
        """
        self.timeout = timeout
        self.poll_frequency = poll_frequency

    def until(self, condition_func, on_poll_fail=None, error_message="Condition not met within timeout"):
        """
        Repeatedly executes condition_func() until it returns a truthy value.
        
        :param condition_func: A callable that returns truthy on success, falsey/None on failure.
        :param on_poll_fail: Optional callable to execute every time the condition fails (e.g., to scroll).
        :param error_message: The message to include if a TimeoutError is raised.
        :return: The truthy value returned by condition_func.
        """
        end_time = time.time() + self.timeout
        
        while time.time() < end_time:
            try:
                result = condition_func()
                if result:
                    return result
            except Exception:
                # If the condition function crashes (e.g., pyautogui throws ImageNotFoundException)
                # we swallow it and keep polling until timeout.
                pass
                
            if on_poll_fail:
                on_poll_fail()
                
            time.sleep(self.poll_frequency)
            
        raise TimeoutError(f"{error_message} after {self.timeout} seconds")
