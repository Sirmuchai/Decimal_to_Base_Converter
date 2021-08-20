def baseCon(n,base):
    vals = "0123456789ABCDEF"
    if n < base:
        return vals[n]
    else:
        return baseCon((n//base),base)+vals[n%base]
    
    
print(baseCon(31,10))