#Find First and Last Position of Element in Sorted Array
class Solution(object):
    def searchRange(self, nums, target):
        def binary_search(find_left):
            low, high = 0, len(nums) - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    idx = mid
                    if find_left:
                        high = mid - 1  # Keep looking left
                    else:
                        low = mid + 1   # Keep looking right
            return idx

        return [binary_search(True), binary_search(False)]
