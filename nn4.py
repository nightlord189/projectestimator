from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import os
from tensorflow.python.client import device_lib

def create_model():
    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=7, kernel_initializer='normal', activation='selu'))
    model.add(Dense(10, kernel_initializer='normal', activation='linear'))
    #model.add(Dense(10, kernel_initializer='normal', activation='selu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

print(device_lib.list_local_devices())
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
dataframe = read_csv("files/f3.csv", header=0)
dataset = dataframe.values
X = dataset[:,2:9]
Y = dataset[:,9]

estimator = KerasRegressor(build_fn=create_model, epochs=500, batch_size=5, verbose=0)
kfold = KFold(n_splits=10)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))