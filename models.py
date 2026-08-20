import numpy as np
from sklearn.linear_model import LinearRegression

class LinearEffectModel:
    def __init__(self):
        self.model=LinearRegression()

    def fit(self,X,y):
        self.model.fit(X,y)
        return self

    def predict(self,X):
        return self.model.predict(X)
