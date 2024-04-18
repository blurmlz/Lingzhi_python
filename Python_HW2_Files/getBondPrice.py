import numpy as np
def get_bond_price(y, face, couponRate, m):

    dfs = (1 +y)** -np.arange(1, m+1)
    print(dfs)
    discounted_coupons =sum(face*couponRate*dfs)
    discounted_face = face*dfs[-1]

    return(discounted_coupons+discounted_face)

get_bond_price(0.03, 2000000, 0.04, 10)

