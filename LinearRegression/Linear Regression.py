import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class LinearRegressionGD():

    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros((X.shape[1], 1))
        self.b = 0
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[:] += self.eta * X.T.dot(errors)
            self.b += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_) + self.b

    def predict(self, X):
        return self.net_input(X)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
                 header=None, sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
              'NOX', 'RM', 'AGE', 'DIS', 'RAD',
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head())

x = df[['RM']].values
y = df[['MEDV']].values

sc_x = StandardScaler()
sc_y = StandardScaler()
X_std = sc_x.fit_transform(x)
y_std = sc_y.fit_transform(y)

lr = LinearRegressionGD()
lr.fit(X_std, y_std)

print('Slope: %.3f' % lr.w_)
print('Intercept: %.3f' % lr.b)
arr = np.array([5.0])
num_rooms_std = sc_x.transform(arr.reshape(-1, 1))
price_std = lr.predict(num_rooms_std)
print("Price in $1000's: %.3f" % sc_y.inverse_transform(price_std))

slr = LinearRegression()
slr.fit(x, y)
y_pred = slr.predict(x)
print('Slope: %.3f' % slr.coef_[0])
print('Intercept: %.3f' % slr.intercept_)

#---------------------NOX--------------------------

x = df[['RAD']].values
y = df[['NOX']].values

sc_x = StandardScaler()
sc_y = StandardScaler()
X_std = sc_x.fit_transform(x)
y_std = sc_y.fit_transform(y)

lr = LinearRegressionGD()
lr.fit(X_std, y_std)

print('Slope: %.3f' % lr.w_)
print('Intercept: %.3f' % lr.b)
arr = np.array([5.0])
num_rooms_std = sc_x.transform(arr.reshape(-1, 1))
price_std = lr.predict(num_rooms_std)
print("NOX: %.3f" % sc_y.inverse_transform(price_std))

slr = LinearRegression()
slr.fit(x, y)
y_pred = slr.predict(x)
print('Slope: %.3f' % slr.coef_[0])
print('Intercept: %.3f' % slr.intercept_)