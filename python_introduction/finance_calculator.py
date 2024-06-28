Monthly_income = int(input('enter your monthly income:'))
Monthly_expenses = int(input('enter your monthly expenses:'))
Monthly_savings = Monthly_income - Monthly_expenses
Projected_savings = Monthly_savings*12 + (Monthly_savings*12*0.05)
print ('your monthly savings are ', '$' + str(Monthly_savings))
print('Projected savings after on year, with interest, is:', '$'+str(Projected_savings))
