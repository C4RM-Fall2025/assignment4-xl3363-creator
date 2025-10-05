def getBondDuration(y,face,couponRate,m,ppy=1):
    y1 = y/ppy
    m1 = m * ppy
    cf = couponRate * face / ppy
    pvcfsum = 0
    weightedsum = 0
    for i in range(m1):
        pvm = (1+y1)**-(i+1)
        pvcf = pvm * cf
        pvcfsum = pvcf + pvcfsum
        weightedsum = pvcf * (i+1) + weightedsum
    totalbondprice = pvcfsum + face*(1+y1)**-m1
    totalweighted = weightedsum + m1*face*(1+y1)**-m1
    bondduration = totalweighted/totalbondprice
    return bondduration

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 2
getBondDuration(y,face,couponRate,m,ppy=1)
