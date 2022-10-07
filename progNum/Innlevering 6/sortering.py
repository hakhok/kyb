def bubble_sort(l):
    li = l
    unsorted = 1
    while unsorted != 0:
        unsorted = 0
        for i in range(len(li)-1):
            if li[i]>li[i+1]:
                value_1=li[i]
                li[i] = li[i+1]
                li[i+1] = value_1
                unsorted += 1
    return li

def selection_sort(l):
    li = l
    sorted = []
    for i in range(len(li)):
        max_number = max(li)
        sorted.append(max_number)
        li.remove(max_number)
    sorted.reverse()
    return sorted

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]

print(bubble_sort(liste))
print(selection_sort(liste))
