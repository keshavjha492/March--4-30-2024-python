# [(3, 2, 0), (5, 4, 1), (1, 7), (2, 9), (0, 10)]
"""
Given a list a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)], sort the list based on the last item of each tuple inside the list.
Output : [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]

"""

a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]


def sort_by_last_element(item):  # item => (5, 4)
    return item[-1]
    # return item[len(item)-1]  # item[3-1] = item[2], item[2-1] item[1]


a.sort(key=sort_by_last_element)
print(a)  # [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]


a = ["a", "e", "i", "o", "u"]
print(len(a))  # 5