#!/usr/bin/python


def atleastk(data, k):
    m = {}
    res = []
    for i in data:
        if i in m.keys():
            m[i] += 1
        else:
            m[i] = 1
        if m[i] == k:
            res.append(i)
    return res


def counting(data):
    bucket = [0]*1001
    maximum = 0
    maxnum = -1
    for i in data:
        bucket[i] += 1
        if maximum < bucket[i]:
            maximum = bucket[i]
            maxnum = i
    print "Maximum occurences belongs to %d" % maxnum
    sorts = []
    for i in range(len(bucket)):
        sorts += [i] * bucket[i]
    return sorts


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3]
    twice = atleastk(data, 2)
    print twice
    count = counting(data)
    print count

if __name__ == "__main__":
    main()
