def getBondPrice_Z(face, couponRate, times, yc):
    cf=couponRate*face   
    pvcfsum =  0
    for t,r in zip(times, yc):
        pvcf=cf/(1+r)**t
        pvcfsum = pvcfsum + pvcf
    bondPrice=pvcfsum + face/(1+yc[-1])**times[-1]
    return(bondPrice)

# Test values
yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04
getBondPrice_Z(face, couponRate, times, yc)
