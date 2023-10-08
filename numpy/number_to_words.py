n = int(input())
numbers = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'nine', '9':'nine'}
n = str(n)
n = list(n)
for i in n:
    print(numbers[i],end=' ')