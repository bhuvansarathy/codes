array = [int(x) for x in input().split()]
k = int(input())
target = int(input())
k = k % len(array)
rotated = array[k:] + array[:k]
print(rotated)
print(rotated.index(target))
