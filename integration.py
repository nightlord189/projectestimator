from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
import csv

def create_model():
    model = Sequential()
    model.add(Dense(20, input_dim=10, kernel_initializer='normal', activation='selu'))
    model.add(Dense(10, kernel_initializer='normal', activation='linear'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

def export_result(filename, prediction):
    pass
    lines = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        i=0
        for line in reader:
            if i==1:
                line[12]=prediction
            lines.append(line)
            i+=1
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(lines)

dataframe = read_csv("files/current.csv", header=0)
dataset = dataframe.values
X = dataset[:,2:12]

model=create_model()
model.load_weights('output/model1.h5')
prediction = model.predict(X)
prediction=int(round(prediction[0][0]))
print (prediction)
export_result("files/current.csv", prediction)
