

#1. Personal Information
print('Keith Rogers')
print('32 Golden Glow, Corner Brook, NL. A2H 6M6')
print('709-640-4811')
print('Software Development')

#2. Sales Prediction
ProjectedSales = float(input('Please enter your projected number of total sales:'))
Profit = ProjectedSales*(0.23)
print(round(Profit, 2))

#3. Land Calculation
LandSize = float(input('Please enter total land size in square feet:'))
Acres = LandSize/(43560)
print('Your land is ', round(Acres, 2), 'acres.')


#4. Total Purchase

Purchase1 = float(input('Price of first item?'))
Purchase2 = float(input('Price of second item?'))
Purchase3 = float(input('Price of third item?'))
Purchase4 = float(input('Price of fourth item?'))
Purchase5 = float(input('Price of fifth item?'))

Subtotal = Purchase1 + Purchase2 + Purchase3 + Purchase4 + Purchase5
SalesTax = Subtotal*(0.07)
SalesTotal = Subtotal + SalesTax

print('Your subtotal is', Subtotal)
print('The sales tax on this purchase is', round(SalesTax, 2))
print('This brings your total to', SalesTotal)

#5. Distance Traveled
print('In six hours, the car will travel',6*70,'miles.')
print('In ten hours, the car will travel',10*70,'miles.')
print('In fifteen hours, the car will travel',15*70,'miles.')

#6. Sales Tax
purchase = float(input('Please enter your purchase total:'))
StateTax = round(purchase*(0.05), 2)
CountryTax = round(purchase*(0.025), 2)
print('The total before tax is', purchase)
print('State sales tax:', StateTax)
print('Country sales tax:', CountryTax)
print('Total sales tax:', StateTax+CountryTax)
print('Which brings your total to:', float(StateTax+CountryTax+purchase))

#7. Miles-per-Gallon
miles = float(input('How many miles have you driven today?'))
gas = float(input('How much gas have you consumed in gallons?'))
print('Your miles per gallon is', round(miles/gas, 2))

#8. Tip, Tax, Total
MealTotal = float(input('Please enter your meal total:'))
SalesTax = float(round(MealTotal*0.07, 2))  #rounding to 2 decimal places
TipAmount =float(round(MealTotal*0.18, 2))
print('Your meal total before tax is', MealTotal)
print('The sales tax on your bill is', SalesTax)
print('Your tip amount is', TipAmount)
print('This brings your total to', MealTotal+SalesTax+TipAmount)


#10. Ingredient Adjuster
cookies = float(input('How many cookies would you like to make?'))
IngredientRatio = round(cookies/48, 2)
SugarAmount = IngredientRatio*1.5
ButterAmount = IngredientRatio
FlourAmount = round(IngredientRatio*2.75, 2)

print('You will need:')
print(SugarAmount, 'cups of sugar')
print(ButterAmount, 'cups of butter')
print(FlourAmount, 'cups of flour')

#9. Celcius to Farenheit
##I think there's a typo in the text as F=95*C + 32 isn't the forumla for farenheit. Will use the given
#equation despite it not being accurate.
celcius = float(input('Please enter the temperature in Celcius:'))

farenheit = 95*celcius + 32

print('The temperature in farenheit is', farenheit)

#11. Male and Female Percentages
males = float(input('How many males in the class?'))               #setting as float, ratio will be float.
females = float(input('How many females in the class?'))
ClassSize = males+females
MalePercent = round(males/ClassSize, 3)
FemalePercent = round(females/ClassSize, 3)

print(MalePercent*100, '% of the class is male.')
print(FemalePercent*100,'% of the class is female')                #100 multiply for percent value

#12. Stock Transaction Program
PurchasedStock = 2000*40
PurchaseCommission = round(PurchasedStock*0.03, 2)
SoldStock = 2000*42.75
SoldCommission = SoldStock*0.03

print('Joe paid', PurchasedStock, 'for his stock originally.')
print('He also paid a commission of', PurchaseCommission, 'to his broker.')
print('He then sold the stock for', SoldStock)
print('with another commision fee of', SoldCommission)
print("In total, Joe's net sales left him with", SoldStock - (PurchasedStock+PurchaseCommission+SoldCommission))

#13. Planting Grapevines
length = float(input('What is the length of your row?'))
EndPostSpace = float(input('How much space is used by the end-post assembly?'))
VineSpace = float(input('How much space is between the vines?'))
NumberGrapevines = length - 2*(EndPostSpace*VineSpace)

print('The number of grapevines that will fit in the row is', round(NumberGrapevines))

#14. Compound Interest
OriginalAmount = float(input('What was the principal originally deposited?'))
AnnualRate = float(input('What is the interest rate paid by this account?'))
CompoundTime = float(input('Number of times the interest is compounded a year?'))
YearsSaved = int(input('How many years will be left to earn interest?'))
BalanceAmount = round(OriginalAmount*(1.0+(AnnualRate*CompoundTime))*(CompoundTime*YearsSaved), 2)

print('The total amount after', YearsSaved, 'years of saving will be: $', BalanceAmount)
