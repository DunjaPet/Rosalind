with open('rosalind_cat.txt')as f:
    s = f.readlines()

#s='AUAU'
s= (s[1]) # RNA string
n=int(len(s)/2)
print (n)
# A recursive function to find nth catalan number
def catalan(n):
    # Base Case
    if n <= 1:
        return 1

        # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
    res = []
    for i in range(n):
        #res += catalan(i) * catalan(n - i - 1)
        res.append(catalan(i) * catalan(n - i - 1))
    return sum(res) % 1000000
'''
for i in range (30):
    print (catalan(i))
'''

print(catalan(n))