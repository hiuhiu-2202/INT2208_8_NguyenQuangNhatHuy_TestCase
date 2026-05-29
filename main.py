# Check
def loan_decision(age, income, credit_score, employment):

    # Validate input
    if not isinstance(age, int) or not isinstance(income, (int, float)) or not isinstance(credit_score, int) or not isinstance(employment, str):
        return "Invalid Input"
    
    if not (18 <= age <= 65):
        return "Invalid Input"

    if not (5.0 <= income <= 500.0):
        return "Invalid Input"

    if not (300 <= credit_score <= 850):
        return "Invalid Input"

    if employment not in ['C', 'F']:
        return "Invalid Input"

    # Risk classification
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # Business logic
    if risk == "High":
        return "REJECT"

    if income < 15.0:

        if employment == 'F':
            return "REJECT"

        if risk == "Medium":
            return "REJECT"

        return "MANUAL REVIEW"

    else:

        if employment == 'C':
            return "APPROVE"

        return "MANUAL REVIEW"
    

# Test cases:
test_cases = [

    # Invalid input
    (17, 20, 700, 'C', "Invalid Input"),
    (66, 20, 700, 'C', "Invalid Input"),
    (30, 4.9, 700, 'C', "Invalid Input"),
    (30, 500.1, 700, 'C', "Invalid Input"),
    (30, 20, 299, 'C', "Invalid Input"),
    (30, 20, 851, 'C', "Invalid Input"),
    (30, 20, 700, 'X', "Invalid Input"),

    # Boundary
    (18, 5.0, 300, 'C', "REJECT"),
    (65, 500.0, 850, 'C', "APPROVE"),

    # Decision table
    (30, 20, 450, 'C', "REJECT"),
    (30, 10, 600, 'C', "REJECT"),
    (30, 10, 750, 'C', "MANUAL REVIEW"),
    (30, 10, 750, 'F', "REJECT"),
    (30, 20, 650, 'C', "APPROVE"),
    (30, 20, 650, 'F', "MANUAL REVIEW"),
    (30, 20, 800, 'C', "APPROVE"),
    (30, 20, 800, 'F', "MANUAL REVIEW"),
]



# Run tests
passed = 0

for i, tc in enumerate(test_cases, start=1):

    age, income, credit, emp, expected = tc

    result = loan_decision(age, income, credit, emp)

    if result == expected:
        print(f"TC{i}: PASS")
        passed += 1
    else:
        print(f"TC{i}: FAIL")

print(f"\nPassed: {passed}/{len(test_cases)}")