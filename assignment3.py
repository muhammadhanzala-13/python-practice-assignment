""" Q1) Check Discount Eligibility
Write a program to check if a customer is eligible for a discount. If the total purchase is
more than $100, apply a 10% discount and display the final price. Otherwise, display the
total price as it is."""
# print("-----------------------------------------------------------")
# print("\t welcome in our store")
# costumer_amount =int(input("enter the total amount of you purchase : "))
# if costumer_amount > 100:
#     discount = costumer_amount* 0.1
#     discounted_price = costumer_amount-discount
#     print(f"the final price after discount is {discounted_price}")
# else:
#     print(f"you are not eligible of discount,The final price is to pay : {costumer_amount}")
"""
Q2)Calculate Bulk Discount
If a customer buys more than 5 items, apply a 15% discount on the total price. Otherwise,
no discount is applied. Display the total price.
"""
# print("-----------------------------------------------------------")
# print("\t welcome in our store")
# costumer_amount = int(input("Enter the total amount of you purchase : "))
# listItem = []
# numbersOfItems =int(input("Enter the number of item you purchased :"))
# for i in range (numbersOfItems):
#     itemNamed = input(f"Enter the name of product you purchased {i+1}: ")
#     listItem.append(itemNamed)

# if len(listItem) > 5 :
#         discount = costumer_amount *0.15
#         discounted_price = costumer_amount - discount
#         print(f"you have purchased items :{listItem}")
#         print(f"Congratulation !! you are entitled of 15% discount ")
#         print(f"amount payable after discount is {discounted_price}")
# else:
#         print(f"you have purchased items :{listItem} and no discount is applicable")
#         print(f"amount payable is : {costumer_amount}")
"""
Q3)Membership Discount
Check if the customer is a member (is_member = True). Members get a 20% discount;
non-members get a 5% discount. Calculate and print the discounted price. 
"""
# print("-----------------------------------------------------------")
# costumerData =input("kindly tell us are you member or not (yes/no) :")
# costumerAmount =int(input("Enter the total amount of you purchase : "))
# if costumerData.lower() == "yes":
#     print(f"Yes! your are a member and Avail a discount of 20% ")
#     discount = costumerAmount * 0.2
#     discounted_price = costumerAmount - discount
#     print(f"amount payable after discount is: {discounted_price:.2f}")
# elif costumerData.lower() == "no":
#     print(f"you are not a member but can avail 5% of discount ")
#     discount = costumerAmount * 0.05
#     discounted_price =costumerAmount - discount 
#     print(f"amount payable after discount is :{discounted_price:.2f}")
# else:
#     print("Invalid input")
"""
Q4)Buy-One-Get-One-Free
If a customer buys an even number of items, they get half of them for free. Otherwise,
they pay for all. Calculate the number of items the customer has to pay for.
"""
# print("-----------------------------------------------------------")
# costumerItems = int(input(
#     "Enter how many items you have purchased :"))
# costumerItemCost = float(input("please enter the total ammount of bill :"))
# if costumerItems % 2 == 0:
#     print(f"\nyou got (buy one get one free) scheme")
#     # discount = costumerItemCost * 0.5
#     # discounted_price = costumerItemCost - discount
#     # print(f"amount payable after discount is : {discounted_price:.2f}")
#     print(f"amount payable after discount is : {costumerItems / 2} ")
# else:
#     print(f"\n sorry! you did not avail our [B O G O F] scheme,have to pay for all items")
#     print(f"amount payable for your purchased : {costumerItemCost:.2f}")
"""
"""
"""Q5)Sales Tax
If the price of an item is greater than $500, apply a luxury tax of 15%. Otherwise, apply a
standard tax of 8%. Display the total price after tax.

"""
# print("-----------------------------------------------------------")
# price = float(input("enter the amount of purchase :"))
# if price > 500 :
#     print(f"your purchased is more than 500$,according to govt you have to pay 15% tax ")
#     charge = price * 0.15
#     tax = price+charge
#     print(f"the amount payable after tax : {tax:.2f}")
# else:
#     print(f"your purchased is less than 500$,according to govt you have to pay 8% tax ")
#     charge = price * 0.08
#     tax = price+charge  
#     print(f"the amount payable after tax : {tax:.2f}

"""Q6)Income Tax
If a person's annual income is above $50,000, they pay 20% tax. Otherwise, they pay
10%. Calculate and display the tax amount.
"""
# print("-----------------------------------------------------------")  
# annualIncome = float(input("enter the annual income please :"))
# if annualIncome > 50000 :
#     print(f"your annual income is more than 50000$,according to govt you have to pay 20% tax. ")
#     charge = annualIncome  * 0.2
#     tax = annualIncome + charge
#     print(f"the tax is charged : {charge :.2f}")
#     print(f"the amount payable after tax : {tax:.2f}")
# else:
#     print(f"your annual income is less than 50000$,according to govt you have to pay 10% tax. ")
#     charge = annualIncome  * 0.1
#     tax = annualIncome +charge  
#     print(f"the tax is charged : {charge :.2f}")
#     print(f"the amount payable after tax : {tax:.2f}")
# print("-----------------------------------------------------------")  
"""

Q8. Tax Bracket
Write a program to categorize a person into tax brackets:
 Income < $30,000:Low Tax;
 $30,000 ≤ Income < $100,000:Medium Tax;
 Income ≥ $100,000: High Tax
"""
print("---------------------------------------------------------------")
income = int(input("enter the correct ammount of your income :"))
if income < 30000:
    print("your tax charge is low")
elif income >= 30000 and income <1000000:
    print("your tax charge is medium")
else:
    print("your income is more than 1000000 tax applied high")
print("---------------------------------------------------------------")

"""Q9. VAT Calculation
If the item is marked as essential (is_essential = True), apply a VAT of 5%. Otherwise,
apply a VAT of 12%. Display the final price.
"""

"""Q10. Tax-Free Day
If today is a tax-free day (tax_free = True), display the original price. Otherwise, add a
7% tax.")


C- Shopping and Billing
"""

"""Q11. Free Shipping
If the total purchase amount is more than $50, offer free shipping; otherwise, charge $5
for shipping. Display the total amount including shipping.
"""

"""Q12. Discount Code
If a customer enters the correct discount code (DISCOUNT10), apply a 10% discount.
Otherwise, charge the full amount.
"""

"""Q13. Tiered Discounts
Apply discounts based on the total price:
 $0–$50: No discount.
 $50–$100: 10% discount.
 Over $100: 20% discount.
"""

"""Q14. Minimum Purchase Requirement
If the total amount is less than $20, display a message: &quot;Minimum purchase of $20 is
required.&quot; Otherwise, display the total amount.
"""

"""Q15. Loyalty Points
If a customer is a loyal member (is_loyal = True), they earn double loyalty points for
their purchase. Otherwise, they earn standard points.

D- Travel and Tickets
"""

"""Q16. Travel Discount
If a person is traveling more than 500 miles, offer a 20% discount on ticket price.
Otherwise, charge the full amount.
"""

"""Q17. Child or Senior Discount
If a passenger is under 12 or over 60 years old, apply a 15% discount on the ticket price.
Otherwise, charge the full price.
"""

"""Q18. Ticket Type Pricing
If the ticket is for a weekend (is_weekend = True), add a 10% surcharge. Otherwise,
charge the standard price.
"""

"""Q19. Baggage Fee
If the total baggage weight is over 20kg, charge $10 per extra kilogram. Otherwise, no
extra fee.

"""

"""Q20. Early Bird Discount
If a ticket is booked more than 30 days in advance, apply a 10% discount. Otherwise,
charge the full price.

E- Grades and Performance
"""

"""Q21. Pass or Fail
If a student scores 40 or more, print &quot;Pass&quot;. Otherwise, print &quot;Fail&quot;.
"""

"""Q22. Grade Assignment
Based on a student&#39;s score, assign grades:
 90 and above: &quot;A&quot;
 75–89: &quot;B&quot;
 50–74: &quot;C&quot;
 Below 50: &quot;F&quot;
"""

"""Q23. Bonus Marks
If a student completes all assignments, add 5 bonus marks to their score. Otherwise, no
bonus marks."""
""""

Q24. Attendance Eligibility
If a student&#39;s attendance is 75% or more, they are eligible to take the exam. Otherwise,
they are not."""


""" Q25. Scholarship Eligibility
If a student&#39;s grade is &quot;A&quot; and their annual family income is below $30,000, they are
eligible for a scholarship. Otherwise, theyare not """

