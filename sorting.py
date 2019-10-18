def quick_sort(list):

    def get_pivot_number(list):
        listsize = len(list)
        pivotindex = int(listsize / 2)
        return list[pivotindex]

    if len(list) == 1:
        return list

    left = []
    right = []
    middle = []

    pivotnumber = get_pivot_number(list)

    for i in list:
        if i > pivotnumber:
            right.append(i)
        elif i < pivotnumber:
            left.append(i)
        else:
            middle.append(i)

    if len(left) > 1:
        sortedleft = quick_sort(left)
    else:
        sortedleft = left

    if len(right) > 1:
        sortedright = quick_sort(right)
    else:
        sortedright = right

    return sortedleft + middle + sortedright


def bubble_sort(list):

    for index, value in enumerate(list):
        ran = False
        numsorted = 0

        if index <= len(list) - 1:
            nextindex = index + 1
        else:
            return list

        while value > list[nextindex]:
            list[index], list[nextindex] = list[nextindex], list[index]
            index += 1
            numsorted += 1
            ran = True

            if nextindex == len(list) - 1:
                break

        return list

    def bubble_up(list):

        for i, v in enumerate(list):
            nextv = list[v]
            if v > nextv:
                list[index], list[nextindex] = list[nextindex], list[index]



# def quick_sort_within_list(list, lindex=0, rindex=int(len(list) - 1), pivot):
#
#     def swap_items(list, index1, index2):
#         list[index1], list[index2] = list[index2], list[index1]
#
#     def get_pivot_number(list):
#         listsize = len(list)
#         pivotindex = int(listsize / 2)
#         return list[pivotindex]
#
#
#
#     left = []
#     right = []
#     middle = []
#
#     pivot = get_pivot_number(list)
#
#     for i in list:
#         if i > pivotnumber:
#             ...
#         elif i < pivotnumber:
#             ...
#         else:
#             ...
#
#     return list
#

    #
    #
    # i = 0
    #
    # while i < len(self.list):
    #     if i < len(lefthalf):
    #         if list[i] > self.pivotnumber:
    #             swapstack.push(i)
    #             i += 1
    #         i += 1
    #
    #     elif i > len(righthalf):
    #         if list[i] < self.pivotnumber:
    #             if swapstack.pop() is None:
    #                 swap_list_items(self.pivotindex, i)
    #             else:
    #                 item_to_swap = swapstack.pop()
    #                 swap_list_items(i, item_to_swap)
    #             i += 1
    #         i += 1


# for i in range(len(list)):
#     if i < pivotindex:
#         if list[i] > pivotnumber:
#             list.insert(pivotindex + 1, list[i])
#             list.remove(list[i])
#             i += 1
#
#     if i > pivotindex:
#         if list[i] < pivotnumber:
#             list.insert(pivotindex - 1, i)
#             pivotindex += 1
#             list.remove(list[i + 1])
#             i += 1
#     else:
#         continue
