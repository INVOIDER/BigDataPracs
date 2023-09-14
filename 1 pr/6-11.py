import numpy as np
# 6 задача
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing(as_frame=True)
print('data = ', data, '\n------------------\n')

# 7 задача
print(data['data'].info(verbose=True), '\n------------------\n')

# 8 задача
print('Пропущенные значения: \n', data['data'].isna().sum(), '\n------------------\n')

# 9 задача
print('Записи по фильтрам: \n', data['data'].loc[(data['data']['HouseAge'] > 50) & (data['data']['Population'] > 2500)],
      '\n------------------\n')

# 11 задача
print('Max значения медианной стоимости дома: ', data['target'].max())
print('Min значения медианной стоимости дома: ', data['target'].min())

# 12 задача
print('Max, min значения медианной стоимости дома: \n',data['data'].apply(np.mean), '\n------------------\n')


