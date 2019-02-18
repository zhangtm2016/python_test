#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from data import DataSeq
data = list(range(100))
data = random.sample(data,k=100)
print(data)

def shell(arr):
    n=len(arr)
    h=1
    while h<n/3:
        h=3*h+1
    while h>=1:
        for i in range(h,n):
            j=i
            while j>=h and arr[j]<arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j-=h
        h=h//3
    print(arr)

def ShellSort(ds):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    D = Length//2
    while D>0:
        i=0
        while i<Length:
            tmp = ds.data[i]

            j=i
            while j>=1 and ds.data[j-D]>tmp:
                ds.SetVal(j, ds.data[j-D])
                j-=D
            ds.SetVal(j, tmp)

            i+=D
        D//=2

if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    ShellSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()
# shell(data)

