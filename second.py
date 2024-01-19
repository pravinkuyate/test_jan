
sentence=input("enter the sentaence")
u=0
l=0
for i in sentence:
    if (i.isupper()):
        u=u+1
    else:
        l=l+1

print("the upper case are",u)
print("the lower case are ",l)



    
