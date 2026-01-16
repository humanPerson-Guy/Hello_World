number=0# asins number
while number <1 or number >20:#checks if numbers are not in 1-20 and repeats the code if not
    number=int(input("input a number 1-20 "))#asks for number 1-20
    if number <1 or number >20:#tells you to put anumber 1-20 if you failed at it
        print("put a number 1-20 its not hard ")


for count in range(1,number+1):#counts to the number skiping evens and brakeing at 13
    if count==13:
        print("eww 13")
        break
    if not(count % 2):
        continue
    print(count)
    
