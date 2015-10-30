#!/usr/bin/python

def bubblesort(data):
    profile = {'outer': 0, 'compare': 0}
    work = list(data)
    for i in range(1, len(work)):
        profile['outer'] += 1
        for j in range(len(work)-i):
            profile['compare'] += 1
            if work[j] > work[j+1]:
                work[j], work[j+1] = work[j+1], work[j]
    print "Naive implementation stats for ", data
    print "List of length %d sorted in %d outer and %d compares" % (len(data),
            profile['outer'], profile['compare'])
    return work

def bubblesortim(data):
    profile = {'outer': 0, 'compare': 0}
    work = list(data)
    for i in range(1, len(work)):
        sorted = True
        profile['outer'] += 1
        for j in range(len(work)-i):
            profile['compare'] += 1
            if work[j] > work[j+1]:
                work[j], work[j+1] = work[j+1], work[j]
                sorted = False
        if sorted:
            break
    print "Improved implementation stats for ", data
    print "List of length %d sorted in %d outer and %d compares" % (len(data),
            profile['outer'], profile['compare'])
    return work

def cocktailsort(data):
    profile = {'outer': 0, 'compare': 0, 'bubbling': 0}
    work = list(data)
    for i in range(1, len(work)):
        sorted = True
        profile['outer'] += 1
        profile['bubbling'] += 1
        for j in range(len(work)-i):
            profile['compare'] += 1
            if work[j] > work[j+1]:
                work[j], work[j+1] = work[j+1], work[j]
                sorted = False
        if sorted:
            break

        sorted = True
        profile['bubbling'] += 1
        for j in range(len(work)-i, 0, -1):
            profile['compare'] += 1
            if work[j] < work[j-1]:
                work[j], work[j-1] = work[j-1], work[j]
                sorted = False
        if sorted:
            break
    print "Cocktail implementation stats for ", data
    print "List of length %d sorted in %d outer and %d compares" % (len(data),
            profile['outer'], profile['compare'])
    print "Bubbled %d times." % profile['bubbling']
    return work

def main():
    data = [7,1,2,3,4,5,6]
    data2 = [7,2,3,4,5,6,1]
    data3 = [8,1,2,3,4,5,9,10,6,7]

    bubblesort(data)
    bubblesortim(data)
    cocktailsort(data)
    print

    bubblesort(data2)
    bubblesortim(data2)
    cocktailsort(data2)
    print

    bubblesort(data3)
    bubblesortim(data3)
    print cocktailsort(data3)


if __name__ == "__main__":
    main()
