
"""
Financial Health Calculator
FNB App Academy - Unit 1: Functions
Author: Copilot (Microsoft AI)

This script provides three calculators:
1. Compound Interest Calculator
2. eBucks Level Estimator
3. Debt Paydown Simulator

It demonstrates reusable functions, logical branching, loops, and error handling.
"""

# -------------------------------
# Function 1: Compound Interest
# -------------------------------
def calculate_compound_interest(principal, monthly_deposit, annual_rate, years):
    """
    Calculates future value of savings with monthly contributions.
    Formula: FV = P*(1+r/n)^(n*t) + PMT * [((1+r/n)^(n*t) - 1) / (r/n)]
    where:
        P = principal1
        PMT = monthly deposit
        r = annual interest rate (decimal)
        n = compounding periods per year (12 for monthly)
        t = years
    """
    n = 12
    r = annual_rate / 100
    try:
        future_value = principal * (1 + r/n)**(n*years)
        future_value += monthly_deposit * (((1 + r/n)**(n*years) - 1) / (r/n))
        return round(future_value, 2)
    except ZeroDivisionError:
        return principal + monthly_deposit * years * 12


# -------------------------------
# Function 2: eBucks Level Estimator
# -------------------------------
def estimate_ebucks_level(app_logins, virtual_card_spend, savings_goal_met):
    """
    Estimates eBucks reward level based on user habits.
    Rules (simplified for demonstration):
        - Level 1: Rare app use, low spend, no savings
        - Level 2: Moderate app use OR some spend
        - Level 3: Frequent app use AND moderate spend
        - Level 4: High app use, high spend, savings goal met
        - Level 5: Exceptional usage and savings discipline
    """
    if app_logins < 5 and virtual_card_spend < 500 and not savings_goal_met:
        return 1
    elif app_logins >= 5 and virtual_card_spend >= 500 and not savings_goal_met:
        return 2
    elif app_logins >= 10 and virtual_card_spend >= 1000 and savings_goal_met:
        return 4
    elif app_logins >= 15 and virtual_card_spend >= 2000 and savings_goal_met:
        return 5
    else:
        return 3


# -------------------------------
# Function 3: Debt Paydown Simulator
# -------------------------------
def calculate_debt_paydown(loan_amount, annual_interest_rate, monthly_payment, extra_payment):
    """
    Simulates loan repayment with optional extra payments.
    Returns total interest paid and months saved compared to no extra payments.
    """
    r = annual_interest_rate / 100 / 12
    balance = loan_amount
    months = 0
    total_interest = 0

    # With extra payments
    while balance > 0:
        interest = balance * r
        total_interest += interest
        balance += interest
        payment = monthly_payment + extra_payment
        if payment > balance:
            payment = balance
        balance -= payment
        months += 1

    # Without extra payments
    balance_no_extra = loan_amount
    months_no_extra = 0
    while balance_no_extra > 0:
        interest = balance_no_extra * r
        balance_no_extra += interest
        payment = monthly_payment
        if payment > balance_no_extra:
            payment = balance_no_extra
        balance_no_extra -= payment
        months_no_extra += 1

    months_saved = months_no_extra - months
    return round(total_interest, 2), months_saved


# -------------------------------
# Main CLI Menu
# -------------------------------
def main():
    print("Welcome to the Financial Health Calculator (FNB App Academy)")
    while True:
        print("\nMenu:")
        print("1. Compound Interest Calculator")
        print("2. eBucks Level Estimator")
        print("3. Debt Paydown Simulator")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                principal = float(input("Enter initial principal amount: "))
                monthly_deposit = float(input("Enter monthly deposit: "))
                annual_rate = float(input("Enter annual interest rate (%): "))
                years = int(input("Enter number of years: "))
                result = calculate_compound_interest(principal, monthly_deposit, annual_rate, years)
                print(f"\nFuture Value after {years} years: R{result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "2":
            try:
                app_logins = int(input("Enter number of app logins per month: "))
                virtual_card_spend = float(input("Enter monthly virtual card spend (R): "))
                savings_goal_met = input("Savings goal met? (yes/no): ").strip().lower() == "yes"
                level = estimate_ebucks_level(app_logins, virtual_card_spend, savings_goal_met)
                print(f"\nProjected eBucks Reward Level: {level}")
            except ValueError:
                print("Invalid input. Please enter numeric values where required.")

        elif choice == "3":
            try:
                loan_amount = float(input("Enter loan amount (R): "))
                annual_interest_rate = float(input("Enter annual interest rate (%): "))
                monthly_payment = float(input("Enter monthly payment (R): "))
                extra_payment = float(input("Enter extra monthly payment (R): "))
                total_interest, months_saved = calculate_debt_paydown(
                    loan_amount, annual_interest_rate, monthly_payment, extra_payment
                )
                print(f"\nTotal Interest Paid: R{total_interest}")
                print(f"Months Saved with Extra Payments: {months_saved}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "4":
            print("Thank you for using the Financial Health Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()
