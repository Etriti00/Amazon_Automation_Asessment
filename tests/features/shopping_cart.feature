Feature: Shopping Cart

  Scenario: Add a product to the cart and update the quantity
    Given I open the Amazon homepage
    When I enter "watch" in the search field
    And I select the first search result
    And I add the product to the cart
    And I navigate to the cart
    And I update the quantity of the product to "2"
    Then the cart should reflect the updated quantity "2"
