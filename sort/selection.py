

def selection_sort(data):
    for last in range(len(data)-1, 0, -1):
        position_max = 0
        for position in range(0, last+1):
            if data[position] > data[position_max]:
                position_max = position

        tmp = data[last]
        data[last] = data[position_max]
        data[position_max] = tmp

    return data


if __name__ == '__main__':
    print selection_sort([10, 30, 5, 1, 4, 2])


