y = int(input())

# Please write your code here.
def year(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return 'false'
        else:
            return 'true'
    elif y % 4 != 0:
        return 'false'
        

print(year(y))