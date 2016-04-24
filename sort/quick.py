
def quick_sort(data):
    quick_sort_helper(data, 0, len(data) - 1)


def quick_sort_helper(data, first, last):
    if first < last:
        split_point = partition(data, first, last)

        # recursive
        quick_sort_helper(data, first, split_point-1)
        quick_sort_helper(data, split_point+1, last)


def partition(data, first, last):
    pivot = data[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        # move left mark to right
        while left_mark <= right_mark and data[left_mark] <= pivot:
            left_mark += 1

        # move right mark to left
        while left_mark <= right_mark and data[right_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            # exchange value items of left mark and right mark
            tmp = data[right_mark]
            data[right_mark] = data[left_mark]
            data[left_mark] = tmp

    # exchange pivot and right mark item value
    tmp = data[right_mark]
    data[right_mark] = pivot
    data[first] = tmp

    return right_mark

if __name__ == '__main__':
    data = [1,10,20,10,201,32,12,3]
    quick_sort(data)
    print data