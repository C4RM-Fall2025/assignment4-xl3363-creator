def getBondPrice_E(face, couponRate, m, yc):
    m = len(yc)
    bondprice = 0
    for t,y in enumerate (yc):
        cf = face * couponRate if t+1 < m else face * (1+couponRate)
        pvm = 1/(1+y)**(t+1)
        pvcf = cf*pvm
    bondPrice = bondprice + pvcf
    
    return(bondPrice)

# Test values

yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
getBondPrice_E(face, couponRate, m, yc)
