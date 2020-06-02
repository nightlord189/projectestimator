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

def processExperience():
    print ("read experience")
    result=[]
    with open('dataset/Experience.csv') as f:
        reader = csv.reader(f)
        i=0
        for row in reader:
            i+=1
            if i>1:
                item=FinalModel()
                item.Name=row[0]
                item.Year=row[1]
                platformStr=row[2].lower()
                if platformStr=='generic':
                    item.Platform=0
                elif platformStr=='web':
                    item.Platform=1
                elif platformStr=='mobile':
                    item.Platform=2
                elif platformStr=='desktop':
                    item.Platform=3
                item.Language=row[3]
                item.Team=row[4]
                item.SizeMetric=row[5]
                item.Size=row[6]
                item.DevelopmentMode=row[7]
                item.CodeReuse=float(row[8])/100.0
                item.Architecture=row[9]
                item.CustomerQuality=row[10]
                d=row[11]
                item.ProjectManagementQuality=d
                item.Duration=row[12]
                result.append(item)
    return result

def exportResult (arr, filename):
    print ("export to csv")
    columns= ['Name', 'Year', 'Platform', 'Language', 'Team', 'SizeMetric', 'Size', 'DevelopmentMode', 'CodeReuse', 'Architecture', 'CustomerQuality', 'ProjectManagementQuality', 'Duration']
    #df = pd.DataFrame(arr, columns)
    #df.to_csv (r'files\export_dataframe.csv', index = False, header=True)
    with open('files\\'+filename, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        wr.writerow(columns)
        for item in arr:
            wr.writerow(list(item))  # @Shankar suggestion

print ("start")
#d1=processKemerer()
#d2=processDesharnais()
#d3=processMaxwell()
#result=d1+d3
#exportResult(result, 'f1.csv')
d4=processExperience()
exportResult(d4, 'f2.csv')