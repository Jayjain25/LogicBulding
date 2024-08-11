def missing_ele(nums):
  n = len(nums)+1
  return (n * (n + 1)//2) - sum(nums)

print(missing_ele([1,2,3,4,5]))