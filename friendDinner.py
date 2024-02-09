# Developed by: Manaal Hashmi
# Date: February 7th
# Desc: A program to sort orders at a restaurant and calculate costs
# Determines meal based on dietary restrictions and shows
# totals before tax, after tax, and after tip and tax. Also sums up the amount
# of orders of a certain dish and how many orders of a dish are made.
# Inputs: Dietary restrictions, and amount of tip given
# Outputs: Total costs, and type of meals given


# variables for storing invitees by food type
pizzaInvitee = 0
pastaInvitee = 0
falafelInvitee = 0
steakInvitee = 0
beverageInvitee = 0

# constants for food prices
COST_PIZZA = 44.50
COST_PASTA = 48.99
COST_FALAFEL = 52.99
COST_STEAK = 49.60
COST_BEV = 5.99

# variables for calculating total cost, tax and tip
totalBeforeTax = 0.0
totalAfterTax = 0.0
totalAfterTip = 0.0

# variables for storing choices made by the user, default value is no
selectK = "n"
selectV = "n"
selectG = "n"

# this prompts user to enter number of invitees
invitees = int(input("Please enter the number of invitees: "))

# this for loop allows us to ask choices for all the invitees
for inviteeNo in range(1, invitees + 1):

    print('Please enter the order details for invitee Number', inviteeNo, '/', invitees)

    # this prompts user to enter values for meal choices
    selectK = input("Do you want a keto friendly meal? (type y for yes): ")
    selectV = input("Do you want a vegan meal? (type y for yes): ")
    selectG = input("Do you want a Gluten-free meal? (type y for yes): ")

    # if elif statements to determine what kind of invitee dish will be charged for
    if selectK == "y" and selectV == "y" and selectG == "n":
        pizzaInvitee = pizzaInvitee + 1
    elif selectK == "n" and selectV == "y" and selectG == "n":
        pastaInvitee = pastaInvitee + 1
    elif selectK == "y" and selectV == "y" and selectG == "y":
        falafelInvitee = falafelInvitee + 1
    elif selectK == "y" and selectV == "n" and selectG == "y":
        steakInvitee = steakInvitee + 1
    else:
        beverageInvitee = beverageInvitee + 1
    print('____________________________\n\n')

# this is the prompt for asking the user for tip %
tip = int(input("How much do you want to tip your server (% percent)? : "))
# shows user the amount of invitees that ordered a certain dish and the cost of the dishes sorted by type and number ordered
print('You have', invitees, 'invitees with the following orders:')
print(pizzaInvitee, 'invitees ordered Pizza. The cost is:''$', COST_PIZZA * pizzaInvitee)
print(pastaInvitee, 'invitees ordered Pasta. The cost is:''$', COST_PASTA * pastaInvitee)
print(falafelInvitee, 'invitees ordered Falafel. The cost is:''$', COST_FALAFEL * falafelInvitee)
print(steakInvitee, 'invitees ordered Steak. The cost is:''$', COST_STEAK * steakInvitee)
print(beverageInvitee, 'invitees ordered only Beverage. The cost is:', '$', COST_BEV * beverageInvitee)

print("----")

# total cost before tax is multiplying types of food ordered and prices for each
totalBeforeTax = (COST_PIZZA * pizzaInvitee) + (COST_PASTA * pastaInvitee) + (COST_FALAFEL * falafelInvitee) + (
            COST_STEAK * steakInvitee) + (COST_BEV * beverageInvitee)
print('The total cost before tax is', '$', round(totalBeforeTax, 2))

# totalAfterTax =total before tax + total before tax (multiplied by 13%)
totalAfterTax = totalBeforeTax + (totalBeforeTax * (13 / 100))
print('The total cost after tax is', '$', round(totalAfterTax, 2))

# totalAfterTip =total after tax  multiplied by ((100+tip)/100)

totalAfterTip = totalAfterTax * ((100 + tip) / 100)
print('The total cost after', tip, '% tip is', '$', round(totalAfterTip, 2))

print("----")










