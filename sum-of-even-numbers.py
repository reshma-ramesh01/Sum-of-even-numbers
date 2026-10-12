limit=int(input("Enter a number : "))
total=0
count=0
for i in range(2,limit+1):  #iterates number
    if i%2==0:              #checks whether the number is even or not
        total+=i            #sum of even numbers stored in total
        count+=1            #count if even numbers occur
print("Sum of even numbers : ",total)
print("Number of even numbers : ",count)
