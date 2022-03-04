Feature: Homepage
""" 
Confirm that the i'm feeling lucky button will redirect to a random artist's details page
"""

Scenario: success for visiting a random artist's details page
    Given I navigate to the home page
    When I click on the "i'm feeling lucky" button
    Then I should see an artist's details page


