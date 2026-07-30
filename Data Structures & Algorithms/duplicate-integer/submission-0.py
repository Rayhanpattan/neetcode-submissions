class Solution:
  def hasDuplicate(self,nums):
      seen=set()
      for num in nums:
          if num in seen:
              return True
          seen.add(num)

      return False

nums=[1,2,3,3]
obj1=Solution()

if obj1.hasDuplicate(nums):
    print("Duplciate")
else:
    print("no duplicate")

