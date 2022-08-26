from typing import List


series=[1,1]
[series.append(series[k-1]+series[k-2]) for k in range(2,20)]
Lista=[20,33]
[Lista.append(Lista[n-1]+Lista[n-2]) for n in range(2,20)]
print(series)
print(Lista)