def largest_and_smallest(l):
    l = sorted(l, key=len)
    if len(l[0])==len(l[1]) or len(l[len(l)-1])==len(l[len(l)-2]):
        return -1
    return [l[0] , l[len(l)-1]]

s = "it is a  string with largest and smallest word."
l = s.split()
a = largest_and_smallest(l)
print(a)