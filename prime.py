def prime(bilangan):
    count=0
    for i in range (1,bilangan+1):
        if (bilangan % i == 0):
            count+=1
    if(count==2):
        return "prime"
    else:
        return "false"
p = prime(2)
print (p)
#tambah komentar 
