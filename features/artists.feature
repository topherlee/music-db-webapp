Feature: Artists
""" 
Confirm that the artists page is working 
"""

Scenario: success for visiting the artists page
    Given I navigate to the artists page
    When I click on the Adam Lambert hyperlink
    Then I should see Adam Lambert's details page


