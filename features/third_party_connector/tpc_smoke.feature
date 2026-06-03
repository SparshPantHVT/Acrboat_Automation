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
  Scenario: User can create a pdf space
    Given Acrobat is running and maximized
    When user clicks on select files button to open the pdf space
    Then user select a file from the recents option
    Then user selects create pdf space button
    Then user clicks on insights button
    Then the user verifies that the insights are visible

  @gen_presentation
   Scenario: User can create a ppt
    Given Acrobat is running and maximized  
    When user clicks on generate ppt button to create ppt
    Then the user adds a demo prompt in prompt area
    Then the user clicks on Add File option to add a file
    Then user select a file from the recents option
    Then the user clicks on add button
    Then the user clicks on use for PPT button
    Then the user clicks on Customize menu
    Then the user clicks on Customize menu to click on Length
    Then the user clicks on Length to choose ppt slide
    Then the user clicks on continue to select the template  
    Then the user selects a presentation template
    Then the user clicks on continue to select the template 
    Then the user clicks on Generate

  @pdf_actions  
    Scenario: User can do various pdf actions using AI 
      Given Acrobat is running and maximized 
      When the user clicks on menu button to open the menu
      Then the user clicks on open file button
      When the user opens the local file from the system "C:\Users\sparsh.pant\Desktop\cars.pdf"
      Then the user clicks on AI Assistant CTA
      When the user enters a prompt for the action which has to be performed using the AI "rotate page 1 by 180 degree"
      Then the user verifies that the page is rotated as expected

 @edit_pdf  
  Scenario: User can Edit PDF 
      Given Acrobat is running and maximized 
      When user clicks on Edit PDF option to open Edit Section
      When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\Tyco tidy-up button in Adobe Express.pdf" 
      Then user clicks on pen icon to perform the PDF Edit Action
      Then user clicks on highlight action to highlight the text
      Then the user opens the search panel to search for the text which needs to be highlighted
      When the user enters the text which needs to highlighted "typographic"
      Then user clicks on the text which was found
      Then user clicks on pen icon to perform the PDF Edit Action
      Then the user clicks on the text area
      When the user clicks on cross icon to close the search bar to enter "express"
      Then the user clicks on selected text for strike through
      Then the user clicks on selected text to perform the strike through
      Then the user clicks on the text box
      When the user clicks on cross icon to close the search box to enter "experiment"
      Then the user clicks on the text to be underlined
      Then the user clicks on the underline option to underline the text
      Then the user verifies that the highlighted text is visible

@convert_pdf  
  Scenario: User can Convert a PDF 
      Given Acrobat is running and maximized 
      When user clicks on Edit PDF option to open Edit Section
      When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\Tyco tidy-up button in Adobe Express.pdf"       
      Then user clicks on convert tab present in the top bar
      Then user clicks on convert to PPT Option
      Then user clicks on convert Button to start the conversion to PPT
      Then user choose the location to save the coverted file
      Then the user verifies that the file is converted to correct format
      Then user clicks on Enter to confirm the location

@combine_pdf
  Scenario: User can Combine Mutliple PDF into One
      Given Acrobat is running and maximized  
      When user clicks on combine pdf button
      Then user selects add file button to select first file
      When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\Tyco tidy-up button in Adobe Express.pdf"
      Then user add another file for combining the PDFs 
      When the user opens the local file from the system "C:\Users\sparsh.pant\Desktop\cars.pdf"
      Then user clicks on Combine Button to button
      Then user clicks on Combine as pdf option to combine the pdfs
      Then the user verifies that the pdfs are combined into one    

 @e_sign  
  Scenario: User can perform e-signature at a document
      Given Acrobat is running and maximized 
      When user clicks on Edit PDF option to open Edit Section
      When the user opens the local file from the system "C:\Users\sparsh.pant\Desktop\cars.pdf"
      When user clicks on E-sign option to open the tab
      Then user clicks on add signature option
      Then user choose a style for the signature
      Then user choose a style for the signature to be applied
      Then user applied the style for
      Then user choose a location for applying the sign
      Then user verifies the signature is applied in the document

  
 @print_pdf
  Scenario: User can perform printing of PDF
      Given Acrobat is running and maximized 
      When user clicks on Edit PDF option to open Edit Section
      When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\Tyco tidy-up button in Adobe Express.pdf"
      Then user tries to print the PDF
      Then user clicks on print button to print the pdf
      Then user choose the location where the PDF is to be saved
      Then user should see the pop-up regarding confirmation

 @gen_podcast
  Scenario: User can Generate Podcast 
      Given Acrobat is running and maximized  
      Then user clicks on all tools button in home page
      Then user clicks on Generate Podcast button
      Then user select a file from the recents option
      Then user clicks on Next Button to create podcast
      Then user clicks on Podcast Generate Option
      Then user should see the PlayBack Panel
      Then user clicks on playback speed option
      Then user chooses a new playback speed for the podcast

 @pdf_protect  
  Scenario: User can Protect a PDF with password
      Given Acrobat is running and maximized 
      When user clicks on Edit PDF option to open Edit Section
      When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\Hemant Sharma.pdf"  
      Then the user opens the search panel to search for the text which needs to be highlighted
      When the user search for Password menu in the Edit Panel "Encrypt"
      Then user clicks on portect PDF button to protect the PDF
      Then user clicks on Protect a PDF menu in LHP view
      Then user clicks on Type Passowrd text Box
      When the user search for Password menu in the Edit Panel "Adobe@1234"
      Then user clicks on Type Passowrd text Box
      When the user search for Password menu in the Edit Panel "Adobe@1234"
      Then user clicks on Apply button to Confirm the Password
      Then user should see the confirmation Toast


 @book_mark
   Scenario: User can Go to Specific Text in the PDF using BookMark in RHP
    Given Acrobat is running and maximized  
    When user clicks on Edit PDF option to open Edit Section
    When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\Tyco tidy-up button in Adobe Express.pdf"
    Then user clicks on Book Mark option in the RHP
    Then user clicks on KPI Option Present in the Book Mark Panel
    Then user clicks on verfies the text present in the PDF for the selected heading


 @create_form
  Scenario: User can create a form in Acrobat
    Given Acrobat is running and maximized  
    Then user clicks on all tools button in home page   

  @gen_podcast_2
  Scenario: User can Generate Podcast 
      Given Acrobat is running and maximized  
      Then user clicks on all tools button in home page
      Then user clicks on Generate Podcast button
      Then user select a file from the recents option
      Then user clicks on Next Button to create podcast
      Then user clicks on Podcast Generate Option 
      Then user clicks on Expand button to view in Expanded form
      Then user should see the Expanded Panel
      Then user clicks on Forwarding the video by 15 seconds
      Then user should see that the Panel is at 15 Seconds

 @organize_pdf
  Scenario: User can Oragnize a PDF
      Given Acrobat is running and maximized  
      Then user clicks on all tools button in home page    
      Then user clicks on organize page menu  
      Then user clicks on select button to select a pdf to be organized  
      When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\Tyco tidy-up button in Adobe Express.pdf"
      Then user should see that PDF is opened in multi-page view
      Then user clicks to change the page style
      Then user clicks to change the page style to odd pages
      Then user should see that only odd pages are selected
      Then the user clicks on Insert Page button
      Then the user clicks on Insert Page button to insert a blank page
      Then the user clicks on OK button to insert a page

 @edit_image
  Scenario: User can Edit an Image
      Given Acrobat is running and maximized  
      Then user clicks on edit Image Card 
      When the user opens the local file from the system "C:\Users\sparsh.pant\Downloads\image (7).jpg"
      Then user clicks on Effects Tab
      Then user clicks on Gray Scale Tone
      Then user should see that the tone is changed to Gray Scale
      Then user clicks on Edit Tab
      Then user clicks on Flip Button to Flip the Image
      Then user clicks on Vertical Flip
      Then user should see that the Image is grayed out an as well Flipped

 @remove_bg     
  Scenario: User can Remove a Background
      Given Acrobat is running and maximized  
      Then user clicks on Start New Design Card
      Then user clicks Quick Action Menu
      Then user clicks on remove background option
      When the user opens the local file from the system "C:\Users\sparsh.pant\Desktop\car.jpg"
      Then user should see the Background Removed Image

 @pdf_space_weblink     
 Scenario: User can Create a PDF Space using the Web Link
      Given Acrobat is running and maximized
      Then the user click on Create PDF space Card in Home Page
      Then the user click add files later button to close
      Then the user click on Web Link Card in Home Page
      Then the user click on Web Link Button
      Then the user click on Text Box inside the Web Link pop up
      Then the user gives the URL for PDF Space "https://en.wikipedia.org/wiki/Virat_Kohli"
      Then the user click on Add Button to Continue the Process
      Then the user click on Add to PDF Space Button to Continue the Process
