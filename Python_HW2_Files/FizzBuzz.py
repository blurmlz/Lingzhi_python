

import numpy as np
import pandas as pd

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    df = pd.DataFrame(nums, columns=['Number'])

    df_new = np.where(df['Number'] % 15 == 0, 'fizzbuzz',
                              np.where(df['Number'] % 3 == 0, 'fizz',
                                       np.where(df['Number'] % 5 == 0, 'buzz',
                                                df['Number'].astype(str))))

    return df_new.tolist()

output = FizzBuzz(3, 22)
print(output)