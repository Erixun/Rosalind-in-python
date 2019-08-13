
def firstLaw(k, m, n):
    t = k+m+n
    PrA = (k*(k-1 + 2*(m+n)) + m*((m-1)*.75+n) )/( t*(t-1) )
    print(PrA)

firstLaw(2,2,2)
