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
    model.add(Dense(20, input_dim=10, kernel_initializer='normal', activation='selu'))
    model.add(Dense(10, kernel_initializer='normal', activation='linear'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#print(device_lib.list_local_devices())
dataframe = read_csv("files/f2.csv", header=0)
dataset = dataframe.values
numpy.random.seed(2)
numpy.random.shuffle(dataset)

X_train = dataset[0:10,2:12]
Y_train = dataset[0:10,12]

X_test = dataset[10:,2:12]
Y_test = dataset[10:,12]

estimator = KerasRegressor(build_fn=create_model)
estimator.fit(X_test, Y_test, epochs=1500, batch_size=5, verbose=False, shuffle=False)
prediction = estimator.predict(X_test)
prediction=tools.round_arr(prediction)

print (Y_test)
print (numpy.array(prediction))
print("Baseline: %.2f, std %.2f " % (tools.mean(Y_test, prediction), tools.std(Y_test, prediction)))