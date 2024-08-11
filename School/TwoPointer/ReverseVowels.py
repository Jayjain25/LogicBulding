def reverse_vowels(s):
  left = 0
  right = len(s) - 1
  vowels = "aeiouAEIOU"
  ls = list(s)
  
  while left < right:
    if ls[left] in vowels and ls[right] in vowels:
      ls[left],ls[right] = ls[right],ls[left]
      right -= 1
      left += 1
    elif ls[left] in vowels:
      right -= 1
    
    elif ls[right] in vowels:
      left += 1
    
    else:
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
