Feature: Tracks
""" 
Confirm that we filter the tracks list on the tracks page
"""

Scenario: success for visiting tracks page and getting the results for year 2000
    Given I navigate to the tracks page
    When I filter by year 2000 and track title Y
    Then I should see the track Yellow by Coldplay 


