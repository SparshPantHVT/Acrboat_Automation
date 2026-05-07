@tpc_smoke
Feature: Third Party Connector - Smoke Suite
  As a user,
  I want to integrate third party tools,
  So that I can leverage external functionality.

  @add_box
  Scenario: User can add Box file storage
    Given Acrobat is running and maximized
    When the user scrolls the Left Hand Panel to click "Add File Storage"
    Then the user clicks the "Add" button for "Box" storage
    And the user authenticates with "Box" using email "dvarshne+test2@adobetest.com" and password "tester123"
    And the user grants access to "Box"
    And the user sees the "Box" storage account successfully added

  @save_box
  Scenario: User can save a file to Box file storage
    Given Acrobat is running and maximized
    And the user opens the local file for "C:\Users\sparsh.pant\Downloads\Tyco tidy-up button in Adobe Express.pdf"
    When the user triggers the "Save As" action
    And the user selects "Box" from the Save As locations
    Then the user saves the file

  @pdf_space
  Scenario: User can save a file to Box file storage
    Given Acrobat is running and maximized
    When user clicks on select files button to open the pdf space
    Then user select a file from the recents option
    Then user selects create pdf space button
    Then user clicks on insights button
    Then the user verifies that the insights are visible