
import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):

    dfs = (1 +y)** -np.arange(1, m+1)
    t = np.array(range(1,m+1))
    print(t)
    discounted_coupons =sum(face*couponRate*dfs)
    discounted_face = face*dfs[-1]
    discounted_coupons_D =sum(face*couponRate*dfs*t)
    discounted_face_D = face*dfs[-1]*t[-1]
    ans = (discounted_coupons_D+discounted_face_D)/(discounted_coupons+discounted_face)
    return(ans)

getBondDuration(0.03, 2000000, 0.04, 10)

