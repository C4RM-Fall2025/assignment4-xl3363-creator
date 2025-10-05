
def getBondPrice(y,face,couponRate,m,ppy=1):
    cf = couponRate * face/ppy
    pvcfsum = 0
    y1 = y/ppy
    m1 = m*ppy
    for i in range(m1):
        pvm = (1+y1)**-(i+1)
        pvcf = pvm * cf
        pvcfsum = pvcf + pvcfsum
    bondprice = pvcfsum + face * (1+y1)**-m1
    return bondprice

