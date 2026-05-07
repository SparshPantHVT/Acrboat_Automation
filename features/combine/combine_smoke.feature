Feature: Adobe Acrobat Combine Files Workflow

  Scenario: User can open the Combine Files tool and close it
    Given Acrobat is running and maximized
    When the user clicks the "Menu" button
    And the user selects "Combine Files"
    Then the user closes the Combine Files page
