import heapq

def k_largests_ele(n,nums,k):
  if n < k:
    return None
  
  min_heap = nums[:k]
  heapq.heapify(min_heap)
  
  for num in nums[k:]:
    if num > min_heap[0]:
      heapq.heapreplace(min_heap,num)
      
  return min_heap[0]

def main():
  try:
    n = int(input("Enter length : "))
    k = int(input("Enter target : "))
    nums = list(map(int,input("Enter num : ").split()))
    res = k_largests_ele(n,nums,k)
    print(res)
  except Exception as e:
    print(e)
    

if __name__ == "__main__":
  main()