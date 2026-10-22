lst=list(map(int,input("Enter numbers in space").split()))
for num in range(len(lst)):
    if lst[num]%2==0:
        lst[num]=lst[num]//2
    else:
        lst[num]=lst[num]*2

print("Modified list is:",lst)        
