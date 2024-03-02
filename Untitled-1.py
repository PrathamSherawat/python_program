import re
 
def array_depth(l):
    if len(l) > 100:
        print("Error: The string should not exceed 100 characters.")
        return
    
    if re.search(r'a-z()\s]', l):
        print("Error: The string should only contain uppercase alphabets and properly spaced parentheses.")
        return
    c=0
    for i in range (0,len(l)):
        if l[i]=='(':
            c+=1
        elif  l[i]==')':
            c-=1
        else:
            print(c,end=" ")
    print("#")  
    
l="(a(b(cd)e)f)g"

array_depth(l)
