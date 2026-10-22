#Write a function to find if a number is present in the function , if it is return the postion of it and if not send an apppropiate essage
def number(num,list2):
    for i in range(0,len(list2)):
        if list2[i]==num:
            return i
    return None
## end of function 1


list2=[]
maximum=int(input("Enter number of numbers you want to enter"))
for m in range(0,maximum):
    n=int(input())
    list2.append(n)

num=int(input("Enter element to search"))
result=number(num,list2)
if result is None:
    print("Number/element not found")
else:
    print("Number",num,"is present at",result+1)


