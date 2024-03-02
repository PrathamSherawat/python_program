def removing_copying(s1,s2):
    
    l1=s1.split()
    l2=s2.split()
    result=[]
    for i in s2:
        if i not in s1:
            result.append(i)
    return ''.join(result)


s1="programming"
s2="computer"

print (removing_copying(s1,s2))