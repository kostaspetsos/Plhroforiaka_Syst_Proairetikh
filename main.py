
# Press the green button in the gutter to run the script.
def RemoveDuplicates():
    n = int(input("Enter number of elements in List : "))
    list = []

    for i in range(0, n):
        ele = int(input())

        list.append(ele)  # adding the element

    print(list)

    arr = []
    for i in list:
        if i not in arr:
            arr.append(i)

    print("The list without the Duplicates : " + str(arr))
    SortList(arr)


def SortList(arr):
    arr.sort()

    print("The list after Sorting in Ascenting order : " + str(arr))



if __name__ == '__main__':
    RemoveDuplicates()




