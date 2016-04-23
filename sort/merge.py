

def merge_sort(data):
    if len(data) > 1:
        mid = len(data)//2
        list_part_1 = data[:mid]
        list_part_2 = data[mid:]

        merge_sort(list_part_1)
        merge_sort(list_part_2)

        i, j, k = 0, 0, 0
        while i < len(list_part_1) and j < len(list_part_2):
            if list_part_1[i] > list_part_2[j]:
                data[k] = list_part_2[j]
                j += 1
            else:
                data[k] = list_part_1[i]
                i += 1
            k += 1

        while i < len(list_part_1):
            data[k] = list_part_1[i]
            i += 1
            k += 1
        while j < len(list_part_2):
            data[k] = list_part_2[j]
            j += 1
            k += 1

        return data

if __name__ == '__main__':
    print merge_sort([10, 5, 6, 8, 9, 11, 3, 1, 12, 34, 35])
