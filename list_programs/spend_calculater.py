# a program to add the money you spend
# in a week , so that we can calcute the sum

money=[]
for i in range(1,8):
    amt = int(input(f'enter spend for day {i}:'))
    money.append(amt)

total_spend = sum(money) # sum() func adds all numbers
avg_spend = total_spend/len(money) # calc avg spend of week

print('so you have spent')
print('total weekly spend:',total_spend)
print('day-wise average spend:',avg_spend)