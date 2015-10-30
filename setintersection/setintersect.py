#!/usr/bin/python

def intersect(arrM, arrN):
    res = []
    for i in arrM:
        for j in arrN:
            if i == j:
                res.append(i)
    return res

def intersectsorted(arrM, arrN):
    res = []
    newArr = arrM + arrN
    newArr.sort()
    skip = False
    for i in range(len(newArr)-1):
        if skip:
            skip = False
            continue
        if newArr[i] == newArr[i+1]:
            res.append(newArr[i])
            skip = True
    return res

def main():
    m = [1, 5, 6, 2, 3, 7, 23, 11, 133, 42, 152, 32, 62, 73]
    n = [7, 3, 42, 123, 14, 1515, 1245, 78, 12, 33, 92, 46, 1]
    print intersect(m, n)
    print intersectsorted(m, n)

if __name__ == "__main__":
    main()
