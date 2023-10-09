'''
Question : you are given a lottry ticket and you win the lottery if the sum 
           of first three and the sum of the last three numbers are equal 
'''

ticket_number = int(input())
ticket_number = list(str(ticket_number))

a = []
for i in ticket_number:
    a.append(int(i))

if sum(a[:3]) == sum(a[len(ticket_number)-3:]):
    print('Yes')
else:
    print('No')