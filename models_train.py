from sklearn import linear_model
import pickle
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import MaxAbsScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from tpot.builtins import StackingEstimator
from sklearn import linear_model
from sklearn.kernel_approximation import Nystroem
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
df = pd.read_csv("BTC_5MINUTE.csv")
warnings.filterwarnings("ignore", category=UserWarning)
# take a look at the dataset
#df.head()
#use required features
cdf = df[['open','high','low','volume','close']]
#Training Data and Predictor Variable
# Use all data for training (tarin-test-split not used)
x=cdf.iloc[:,:4]
print(x)
y = cdf.iloc[:, -1]
print(y)
reg=KNeighborsRegressor()

#Fitting model with trainig data
reg.fit(x, y)

# Saving model to disk
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.
pickle.dump(reg, open('model_5m.pkl', 'wb'))
#model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[2.6, 8, 10.1]]))