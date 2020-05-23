Feature: Calculator
	Scenario: Add two numbers
		Given I have entered 2 into the calculator
		And I have also entered 7 into the calculator
		When I press soma
		Then the sum should be 9
	Scenario: Subtracting two numbers
		Given I have entered 3 into the calculator
		And I have also entered 5 into the calculator
		When I press subtrai
		Then the sum should be -2
	Scenario: Multiplying three numbers
		Given I have entered 9 into the calculator
		And I have also entered 3 into the calculator
		When I press multiplica
		Then the sum should be 27
	Scenario: Dividing three numbers
		Given I have entered 4 into the calculator
		And I have also entered 2 into the calculator
		When I press divide
		Then the sum should be 2