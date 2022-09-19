Feature:OKR-LK Integration

  Scenario: Happy Flow
    Given Admin user logs into LK
    When  user navigates to OKR board
    Then Objective create button should be available

  Scenario Outline: Negative Flow
    Given LK Admin user logs into LK
    When  user navigates to OKR board
    Then Objective create button should be available

    Examples:
    |Hey There|
    |        1|