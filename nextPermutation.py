# 31. Next Permutation

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        ind = None
        
        for r in range(n - 1, 0, -1):
            if nums[r] > nums[r - 1]:
                ind = r - 1
                break
        else:
            nums.reverse()
            return nums


        swap = n - 1

        while(nums[swap] <= nums[ind]):
            swap -= 1
        nums[ind], nums[swap] = nums[swap], nums[ind]
        nums[ind + 1:] = reversed(nums[ind + 1:])

        return nums



if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1]
    print("Output is : ", sol.nextPermutation(nums))
    
    nums2 = [1, 5, 4, 3, 2]
    print("Output is : ", sol.nextPermutation(nums2))
