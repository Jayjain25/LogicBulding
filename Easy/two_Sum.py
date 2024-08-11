def two_sum(nums,trg):
  dp = {}
  
  for i in range(len(nums)):
    if trg-nums[i] in dp:
      return [dp[trg-nums[i]], i+1]
    else:
      dp[nums[i]] = i+1
  return None

print(two_sum([2,5,8,9,4,5,6],11))