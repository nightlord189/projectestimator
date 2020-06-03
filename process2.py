from model.final import FinalModel
import csv
import xlrd

def processExperience():
    print ("read experience")
    result=[]
    workbook = xlrd.open_workbook("dataset/Experience.xlsx")
    sheet = workbook.sheet_by_index(0)
    for rowx in range(sheet.nrows):
        row = sheet.row_values(rowx)
        if row[0]=='':
            break
        if row[0].lower()=='name':
            continue
        item=FinalModel()
        item.Name=row[0]
        item.Year=int(row[1])
        platformStr=row[2].lower()
        if platformStr=='generic':
            item.Platform=0
        elif platformStr=='web':
            item.Platform=1
        elif platformStr=='mobile':
            item.Platform=2
        elif platformStr=='desktop':
            item.Platform=3
        item.Language=int(row[3])
        item.Team=int(row[4])
        item.SizeMetric=int(row[5])
        item.Size=int(row[6])
        item.DevelopmentMode=int(row[7])
        item.CodeReuse=float(row[8])/100.0
        item.Architecture=int(row[9])
        item.CustomerQuality=int(row[10])
        item.ProjectManagementQuality=int(row[11])
        item.Duration=int(row[12])
        result.append(item)
    return result

def exportResult (arr):
    print ("export to csv")
    with open(r'files\f2.csv', 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        wr.writerow(arr[0].getColumns())
        for item in arr:
            wr.writerow(list(item))
    with open(r'files\f3.csv', 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        wr.writerow(arr[0].getColumns3())
        for item in arr:
            wr.writerow(item.toArr3())
    with open(r'files\f4.csv', 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        wr.writerow(arr[0].getColumns4())
        for item in arr:
            wr.writerow(item.toArr4())

print ("start")
d4=processExperience()
exportResult(d4)