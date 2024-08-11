import heapq

def k_smallests_ele(n,nums,k):
  if n < k:
    return None
  
  max_heap = [-x for x in nums[:k]]
  heapq.heapify(max_heap)
  
  for num in nums[k:]:
    if num < max_heap[0]:
      heapq.heapreplace(max_heap,-num)
      
  return -max_heap[0]

def main():
  try:
    n = int(input("Enter length : "))
    k = int(input("Enter target : "))
    nums = list(map(int,input("Enter num : ").split()))
    res = k_smallests_ele(n,nums,k)
    print(res)
  except Exception as e:
    print(e)
    

if __name__ == "__main__":
  main()