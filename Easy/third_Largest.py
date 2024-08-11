def third_largest_ele(nums):
  fst = nums[0]
  scnd = nums[0]
  thrd = nums[0]
  
  for i in nums:
    if i > fst:
      thrd = scnd
      scnd = fst
      fst = i
    elif i > scnd:
      thrd = scnd
      scnd = i
    elif i > thrd:
      thrd = i
  
  return thrd

def main():
  try:
    nums = list(map(int,input().split()))
    res = third_largest_ele(nums)
    print(res)
  except Exception as e:
    print(str(e))
    

if __name__ == "__main__":
  main()