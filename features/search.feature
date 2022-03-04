Feature: Search
""" 
Confirm that we can search the database on our site and going into the artist's details page
"""

Scenario: success for visiting search and artist details pages
    Given I navigate to the search page
    When I click and type on the search box
    When I click on this specific hyperlink
    Then I should see the artist details page


