def helper(i, count):
    if i > count:
        print("Harvest time!")
        return
    print("Day ", i)
    helper(i + 1, count)


def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))
    helper(1, count)
