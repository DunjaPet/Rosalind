import itertools
import math
n=1795
m=1124
C=[]

#--------------------- 1st approach: creating all possible combinations- memory error!
#def generator_sol(n,k):       # fast
#    for x in itertools.combinations(range(n), k):
#        yield x



#for k in range(m, n+1):        #fast
#    C.append(generator_sol(n,k))


#print (sum(len(list(x))% 1000000 for x in C))    # problem!!


#---------------------- 2nd approach: counting of comb not creating them
C1=[]

def gen_comb(n,k):
    C1.append(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))  #  to get an integer back from the division of the two integers use //
    return C1


for k in range(m, n+1):
    C=gen_comb(n,k)


#print(C)
print (int(sum(C)%1000000))

