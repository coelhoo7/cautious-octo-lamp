# This project will help the users to calculate how much can they earn back on their investment or how much they need to pay in case of a loan.

import math


# Function to calculate "Simple Investment"
def investment_simple(deposit, interest, years):
      total_amount = deposit * (1 + interest * years)
      return total_amount


# Function to calculate "Compound Investment"
def investment_compound(deposit, interest, years):
      total_amount = deposit * math.pow((1 + interest), years)
      return total_amount


# Function to calculate "Bond Payment"
def bond(house_value, monthly_int_rate, months):
      repayment = (monthly_int_rate * house_value) / (1 - (1 + monthly_int_rate)**(-months))
      return repayment


# Start to give info to the user and ask them for inputs
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan. \n")

user_input = str(input("Enter either 'Investment' or 'Bond' to proceed: "))

# Ask user inputs when "investment" is selected
if user_input.lower() == "investment":
      investment_type = input("Enter 'Simple' or 'Compound': ").lower()
      deposit = float(input("Enter the deposit amount: "))
      interest = float(input("Enter the annual interest rate (as a decimal): "))
      years = float(input("Enter the number of years: "))
      
      if deposit < 0 or interest < 0 or years < 0:
             print("Invalid input. Deposit, interest rate and years must be positive numbers.")

      else:
                    
        # When "Simple Investment" is selected  
        if investment_type == "simple":
                result = investment_simple(deposit, interest, years)
                print(f"After {years} years your return on a simple investment is: £{round(result, 2)}.")
            
        # When "Compound Investment" is selected
        elif investment_type == "compound":
                result = investment_compound(deposit, interest, years)
                print(f"After {years} years your return on a compound investment is: £{round(result, 2)}.")
        else:
                print("Invalid investment type.")


# Ask user inputs when "bond" is selected
elif user_input.lower() == "bond":
      house_value = float(input("Enter the house value: "))
      annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
      years = int(input("Enter the number of years: "))

      if house_value < 0 or annual_interest_rate < 0 or years < 0:
             print("Invalid input. House value, interest rate and years must be positive numbers.")

      else:
        monthly_interest_rate = annual_interest_rate / 12 / 100
        total_repayment = bond(house_value, monthly_interest_rate, years * 12)

        print(f"Monthly repayment for {years} years: £{round(total_repayment, 2)}.")

else:
            print("Invalid investment type.")