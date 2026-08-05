class Solution(object):

  def subsets(self, nums):
    res = []
    cur = []

    def backtrack(index):
      if index == len(nums):
        res.append(list(cur)) 
        return
      cur.append(nums[index])
      backtrack(index + 1)
      cur.pop()
      backtrack(index + 1)
    backtrack(0)
    return res