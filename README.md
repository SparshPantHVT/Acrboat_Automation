# Adobe Acrobat Computer Vision Framework

This is a **Pure Computer Vision** automation framework built for desktop applications (like Adobe Acrobat) that heavily restrict or block standard Accessibility Trees and WebViews. 

It leverages `behave` for BDD reporting and `OpenCV` / `pyautogui` for high-speed template matching.

## Architecture
- **`features/`**: Contains pure English BDD scenarios (`.feature` files) and Python Step Definitions (`steps/`).
- **`features/environment.py`**: The central lifecycle hook. It automatically launches Acrobat before every scenario, takes full-screen error screenshots if a step fails, and safely closes Acrobat after every scenario.
- **`templates/`**: The template database. The framework matches the user's screen against these Snipping Tool images.
- **`pages/cv_engine.py`**: The core OpenCV wrapper that executes the fast template matching and clicking.

## How to Automate a New Workflow

Because this is a pure CV framework, you do not need Developer Tools or XPaths. You only need your Snipping Tool!

1. **Write the Scenario:** Open a `.feature` file and write your steps in English:
   ```gherkin
   When the user clicks the "Save As" button
   ```
2. **Take a Screenshot:** Open Acrobat, use your Snipping Tool to take a small screenshot of the "Save As" button.
3. **Save the Image:** Save it as `save_as.png` inside the `templates/` folder (you can use subdirectories to stay organized).
4. **Map the Step:** Update `steps/` to link the English string `"Save As"` to your image path.

## Execution and Reporting
Run the tests and generate an Allure report:
```cmd
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results features/
allure serve reports/allure-results
```

If a test fails, the Allure report will contain a full-screen debug screenshot showing exactly why the image could not be matched.
