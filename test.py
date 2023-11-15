# class test
# create a list to store those monthly expenses and using that find out.
month_expense = [
    2200,
    2350,
    2600,
    2130,
    2190
]
# in feb, how many dollars you spent extra compare to january
extra_dollar_feb = month_expense[1] % 28
extra_dollar_jan = month_expense[0] % 31
# print(extra_dollar_feb, extra_dollar_jan)
if extra_dollar_jan > extra_dollar_feb:
    print(f'extra dollars in january {extra_dollar_jan}')
elif extra_dollar_jan == extra_dollar_feb:
    print(f'same month spent')
else:
    print(f'extra dollars in feb {extra_dollar_feb}')
    
# question 2
# find out your total expense in first quater(first three months) of the year
quater_month = (month_expense[0] +month_expense[1] + month_expense[2]) / 3
print(f'total cost of the first three month {quater_month}')

# question 3
# find out if you spent exactly 2000 dollars in any month
monthly_spend = 2000
for i in range(len(month_expense)):
    if month_expense[i] == monthly_spend:
        print(f'spent {monthly_spend} in {month_expense[i]}')
    else:
        print(f'didnt meet up to {monthly_spend}')

#question 4
# june month finished and your expense is 1980 dollar. Add this item to our monthly expense list
june = 1980
month_expense.append(june)
print(month_expense)

# question 5
# you returned an item that you bought in the month of april and got a refund of 200. make a correction to your monthly expense list based on this
month_expense[3] += 200
print(month_expense)