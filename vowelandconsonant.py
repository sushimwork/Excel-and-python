n=input("Enter a string")
vowels=0
consonant=0
space=0
digits=0

for char in n:
    if char in 'aeiouAEIOU':
        vowels+=1
    elif char.isalpha():
        consonant+=1
    elif char.isdigit():
        digits+=1
    elif char ==' ':
        space+=1

print(f"vowel is:{vowels}")
print(f"consonant is:{consonant}")
print(f"digits is:{digits}")
print(f"space is:{space}")
