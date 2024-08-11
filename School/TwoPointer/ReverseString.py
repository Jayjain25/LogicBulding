def reverse_vowels(s):
  left = 0
  right = len(s) - 1
  ls = list(s)
  
  while left < right:
    ls[left],ls[right] = ls[right],ls[left]
    left += 1
    right -= 1
      
  
  return "".join(ls)

def main():
  try:
    s = input("Enter a string : ")
    res = reverse_vowels(s)
    print(res)
  
  except Exception as e:
    print(e)
    
    
if __name__ == "__main__":
  main()
