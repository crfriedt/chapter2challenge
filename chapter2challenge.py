#Simple tax/fee calculator in python

#Establish fees
tax_fee = 0.055
license_fee = 0.030
tire_check_fee = 20
mechanic_smokes_fee = 10


#Ask user for the base price of vehicle
base_price = input("\nEnter the base price of the vehicle to calculate total cost with tax (Example: 5234.54): ")

#Calculate fees
fees = float(base_price) * float(tax_fee) * float(license_fee) + int(tire_check_fee) + int(mechanic_smokes_fee)

#Round the fees
rounded_fees = round(fees,2)

#Add fees to the total
total_price = float(base_price) + rounded_fees

#Round total price
total_price_rounded = round(total_price,2)

#Display message to user with final price
print("The total price for the vehicle with tax is is $" + str(total_price_rounded))