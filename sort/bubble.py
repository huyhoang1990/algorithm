def bubble_sort(data):
    for last in range(len(data)-1, 0, -1):
        for i in range(last):
            if data[i] > data[i+1]:
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp


data = [10,4,1,15]
bubble_sort(data)
print data