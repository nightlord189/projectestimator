import numpy

def round_arr(arr):
    i=0
    result=[None]*len(arr)
    while i < len(arr):
        r=round(arr[i], 0)
        result[i]=int(r)
        i += 1
    return result

def mean (data, prediction):
    diff=[None]*len(data)
    if len(data)!=len(prediction):
        raise Exception('array lengths are not the same!')
    i=0
    while i<len(data):
        diff[i]=prediction[i]-data[i]
        i += 1
    arr = numpy.array(diff)
    return numpy.mean(arr, axis=0)

def std (data, prediction):
    diff=[None]*len(data)
    if len(data)!=len(prediction):
        raise Exception('array lengths are not the same!')
    i=0
    while i<len(data):
        diff[i]=prediction[i]-data[i]
        i += 1
    arr = numpy.array(diff)
    return numpy.std(arr, axis=0)