def reverse_vowels(str):
  left = 0
  right = len(str) - 1
  vowels = "aeiouAEIOU"
  str = list(str)
  
  while left < right:
    if str[left] in vowels and str[right] in vowels:
      str[left],str[right] = str[right],str[left]
      right -= 1
      left += 1
    elif str[left] in vowels:
      right -= 1
    
    elif str[right] in vowels:
      left += 1
    
    else:
      left += 1
      right -= 1
  
  return "".join(str)

print(reverse_vowels("practice"))
