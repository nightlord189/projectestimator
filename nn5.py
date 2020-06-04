from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from tensorflow.python.client import device_lib
import os
import tools
import numpy

def create_model():
    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=6, kernel_initializer='normal', activation='selu'))
    model.add(Dense(10, kernel_initializer='normal', activation='linear'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#print(device_lib.list_local_devices())
dataframe = read_csv("files/f4.csv", header=0)
dataset = dataframe.values
X = dataset[:,2:8]
Y = dataset[:,8]

estimator = KerasRegressor(build_fn=create_model)
estimator.fit(X, Y, epochs=500, batch_size=5, verbose=False, shuffle=False)
prediction = estimator.predict(X)
prediction=tools.round_arr(prediction)

print (Y)
print (numpy.array(prediction))
print("Baseline: %.2f, std %.2f " % (tools.mean(Y, prediction), tools.std(Y, prediction)))