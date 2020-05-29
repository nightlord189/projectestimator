from scipy.io import arff
import pandas as pd
from model.final import FinalModel

def processKemerer ():
    print ("kemerer")
    data = arff.loadarff('original/kemerer.arff')
    df = pd.DataFrame(data[0])
    df.head()
    result=[]
    for i in range (0, len(df.ID)):
        item=FinalModel()
        item.Size=df.KSLOC.array[i]
        item.Year=1987
        result.append(item)
    return result


print ("start")
kemererResult=processKemerer()
print ("finish")