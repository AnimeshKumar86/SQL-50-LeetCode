class Solution(object):
    def runningSum(self, nums):
        running_sum=[]
        total=0
        for i in range (len(nums)):
            total+=nums[i]
            running_sum.append(total)
        return running_sum
        