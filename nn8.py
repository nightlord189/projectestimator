from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
import keras.utils
import os
import tools
import numpy
from ann_visualizer.visualize import ann_viz
import matplotlib.pyplot as plt

def create_model():
    model = Sequential()
    model.add(Dense(20, input_dim=10, kernel_initializer='normal', activation='selu'))
    model.add(Dense(10, kernel_initializer='normal', activation='linear'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def exportAndVisualize(model):
    model.save('output/model1.h5')
    keras.utils.plot_model(model, to_file='output/model1.png', show_shapes=True)
    model_json = model.to_json()
    with open("output/model.json", "w") as json_file:
        json_file.write(model_json)
    ann_viz(model, filename='output/network.gv', title="Project estimation")

def createPlot (history):
    plt.plot(history.history['loss'], label='MAE (testing data)')
    plt.title('Project Estimator MAE')
    plt.ylabel('MAE value')
    plt.xlabel('No. epoch')
    plt.legend(loc="upper left")
    plt.show()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#print(device_lib.list_local_devices())
dataframe = read_csv("files/f2.csv", header=0)
dataset = dataframe.values
numpy.random.seed(1)
numpy.random.shuffle(dataset)

X= dataset[:,2:12]
Y = dataset[:,12]

X_train = dataset[0:10,2:12]
Y_train = dataset[0:10,12]

X_test = dataset[10:,2:12]
Y_test = dataset[10:,12]

model=create_model()
history=model.fit(X_train, Y_train, epochs=1500, batch_size=5, verbose=False, shuffle=False)
#createPlot(history)
exportAndVisualize(model)

prediction = model.predict(X_test)
prediction=tools.convertPredictArray(prediction)
prediction=tools.round_arr(prediction)

print (Y_test)
print (numpy.array(prediction))
print("Result: %.2f, std %.2f " % (tools.mean(Y_test, prediction), tools.std(Y_test, prediction)))

print ('')
prediction = model.predict(X)
prediction=tools.convertPredictArray(prediction)
prediction=tools.round_arr(prediction)
print (Y)
print (numpy.array(prediction))
print("Result: %.2f, std %.2f " % (tools.mean(Y, prediction), tools.std(Y, prediction)))