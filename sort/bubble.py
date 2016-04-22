def bubble_sort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            print alist


#This is the worst O(n^2)
def bubble_sort_hoang(data):
    for index1, index1_value in enumerate(data):
        for index2, index2_value in enumerate(data):
            if index2_value > index1_value:
                tmp = data[index2]
                data[index2] = data[index1]
                data[index1] = tmp
            print data

alist = [10,4,1,15]
bubble_sort(alist)
print "======================"
bubble_sort_hoang(alist)