# i=0
# while(i<101):
    
#     if i%2 == 0 :
#         if i%5 == 0:
#             continue
#         print(i,end=" ")
# #     i = i+10
# a=list(range(0,100,2))
# print(a)
# st ="Sting"
# st1 = st[::-1]
# print(st1)

# st = "aAbD"
# st1 = []
# for i in st:
#     if i == i.upper():
#         st1.append(i.lower())
#     else:
#         st1.append(i.upper())
# print("".join(st1))
st = "aAbDfmvndsfglkregjQTfsfhosfewT"
countcapital = 0
countsmall = 0

for i in st:
    if i == i.upper():
        countcapital = countcapital+1
    else:
        countsmall = countsmall+1
print(f"Capitals:{countcapital}  Small: {countsmall}")
        

# s = "Bablu"
# print(s.reverse())
# str1 = "Reverse"
# sr=""
# srx= ""
# i=0
# for i in str1:  
#    sr = i + sr
#    srx = srx+i
# print("The original string is: ",str1)  
# print("The reverse string is",sr)
# print("The 00 string is",srx)
# a="reverse"
# for i in range(len(a)-1,-1,-1):
#    print(a[i],end="")
# s = "bablu"
x  = [1,2,3,4,2,3,4]
def uniquelist(x):
    return set(x)
print(uniquelist(x))


# print(s.reverse())
li = ['bablu','anil', 'rohit']
print(li,sep="\n")