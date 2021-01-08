
# SKlearn包
from sklearn.linear_model import LogisticRegression
from utils.data_utils import get_chinese_data
# 模型持久化的包
import joblib
# 实例化算法
lr = LogisticRegression()

# fit
x, y = get_chinese_data(path='../../data/chinese_char/train')
print(x)
print(y)
lr.fit(x, y)
# 保存lr模型，模型持久化
joblib.dump(lr, '../../model/ml/logistic_regression.model')
print('lr模型保存成功')
print('coef')
print(lr.coef_)
print('intercept')
print(lr.intercept_)