def second_largest_ele(nums):
  fst = nums[0]
  scnd = nums[0]
  
  for i in nums:
    if i > fst:
      scnd = fst
      fst = i
    elif i > scnd:
      scnd = i
  
  return scnd

def main():
  try:
    nums = list(map(int,input().split()))
    res = second_largest_ele(nums)
    print(res)
  except Exception as e:
    print(str(e))
    

if __name__ == "__main__":
  main()