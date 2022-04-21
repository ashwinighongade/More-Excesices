
 
# a=1
# while a<=1000:
#     i=a
#     sum=0
#     while i>0:
#         sum=sum+(i%10)
#         i=i//10
#     if a%sum==0:
#         print(a)
#     a=a+1


# x= int(input("Enter the number :"))
# sum=0
# list1=list(str(x))
# print(list1)
# i=0
# while i<len(list1):
#     sum=sum+int(list1[i])
#     i+=1

# if x%sum==0:
#     print("Harshad Number ")
# else:
#     print("not")

def harshad(num):
    sum=0
    while num>0:
        sum=sum+(num%10)
        num=num//10
    if num%sum==0:
        print("True")
    else:
        print("False")

harshad(18)
