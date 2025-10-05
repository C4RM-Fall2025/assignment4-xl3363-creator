def getBondPrice_E(face, couponRate, m, yc):
    m = len(yc)
    bondprice = 0
    for t,y in enumerate (yc,start=1):
        cf = face * couponRate if t < m else face * (1+couponRate)
        pvm = 1/(1+y)**(t)
        pvcf = cf*pvm
    bondPrice = bondprice + pvcf
    
    return(bondPrice)
