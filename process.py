from scipy.io import arff
import pandas as pd
from model.final import FinalModel
import csv

def processKemerer ():
    print ("kemerer")
    data = arff.loadarff('dataset/kemerer.arff')
    df = pd.DataFrame(data[0])
    df.head()
    result=[]
    for i in range (0, len(df.ID)):
        item=FinalModel()
        item.Year=1987
        item.Name="kemerer"+str(int(df.ID.array[i]))
        item.Size=df.KSLOC.array[i]
        item.DevelopmentMode=0
        item.CodeReuse=0.0
        item.Language=0
        item.Duration=int(df.Duration.array[i]*4)
        item.CustomerQuality=2
        result.append(item)
    return result

def processDesharnais():
    print ("desharnais")
    data = arff.loadarff('dataset/desharnais.arff')
    df = pd.DataFrame(data[0])
    df.head()
    result=[]
    managerExpMax=0
    for i in range (0, len(df.TeamExp)):
        item=FinalModel()
        item.Year='19'+str(int(df.YearEnd.array[i]))
        item.Name="desharnais"+str(int(i+1))
        item.CustomerQuality=2
        if df.ManagerExp.array[i]>managerExpMax:
            managerExpMax=df.ManagerExp.array[i]
        item.DevelopmentMode=0
        item.CodeReuse=0.0
        item.Language=0
        item.Size=df.Effort.array[i]

        result.append(item)
    for i in range (0, len(df.TeamExp)):
        result[i].ProjectManagementQuality=round(3*df.ManagerExp.array[i]/managerExpMax, 2)
    return result

def processMaxwell ():
    print ("maxwell")
    data = arff.loadarff('dataset/maxwell.arff')
    df = pd.DataFrame(data[0])
    df.head()
    result=[]
    for i in range (0, len(df.Syear)):
        item=FinalModel()
        item.Year='19'+str(int(df.Syear.array[i]))
        item.Name="maxwell"+str(int(i+1))

        item.Duration=int(df.Duration.array[i]*4)
        item.SizeMetric=2
        item.Size=df.Size.array[i]
        item.DevelopmentMode=0
        item.CodeReuse=0.0
        item.Language=0

        result.append(item)
    return result

def exportResult (arr):
    print ("export to csv")
    columns= ['Name', 'Year', 'Platform', 'Language', 'Team', 'SizeMetric', 'Size', 'DevelopmentMode', 'CodeReuse', 'Architecture', 'CustomerQuality', 'ProjectManagementQuality', 'Duration']
    #df = pd.DataFrame(arr, columns)
    #df.to_csv (r'files\export_dataframe.csv', index = False, header=True)
    with open(r'files\f1.csv', 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        wr.writerow(columns)
        for item in arr:
            wr.writerow(list(item))  # @Shankar suggestion

print ("start")
d1=processKemerer()
#d2=processDesharnais()
d3=processMaxwell()
result=d1+d3
exportResult(result)
print ("finish")