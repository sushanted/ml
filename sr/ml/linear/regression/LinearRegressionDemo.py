import numpy as np

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

regr.fit(np.array([121012,107204,101977,19306,18835,17580,15665,13452,10868,7921,7906,7467,5234,4126,3594,3134,2886]).reshape(-1,1),
         np.array([20124,41444,24484,4005,6391,6017,4806,3707,4351,4795,3549,5023,1967,2437,1202,1581,433]).reshape(-1,1))

print(np.array([2307,2139,2011]).reshape(-1,1))

print("Coef")
print(regr.coef_)

print("Intercept")
print(regr.intercept_)

print(regr.predict(np.array([125224]).reshape(-1,1)))