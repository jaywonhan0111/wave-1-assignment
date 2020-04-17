# define a function to calculate interest
def compound_interest(principle, rate, time):
    #apply the formula of Compount interest
    CI = principle * (pow((1 + rate / 100), time))
    #return the compound interest
    return CI

money = float(input("Enter the value of money initially deposited \n"))
# add the calculated interest to the princile to get the balance of savings account
# for 1st year
money += compound_interest(money, 4, 1)
print("After 1 year " + str(money))
# add the calculated interest to the princile to get the balance of savings account
# for 2nd year
money += compound_interest(money, 4, 1)
print("After 2 years" + str(money))
# add the calculated interest to the princile to get the balance of savings account
# for 3rd year
money += compound_interest(money 4, 1)
print("After 3 years " + str(money))
