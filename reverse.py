nums = [2,3,4,5]
fruits = ["apple", "banana", "orange"]
print(nums)
nums.reverse()
print(nums)

print(fruits)
fruits.reverse()
print(fruits)

a_string = "This is a string"
a= len(a_string) - 1
b_string = ""
while  a >= 0:    
    b_string = b_string + a_string[a]    
    a -= 1
print(b_string)


