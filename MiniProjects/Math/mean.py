i = int(input("how many numbers do you wish to enter"))
nums = []

for x in range(i):
    nums.append(int(input("Enter a number")))

mean = sum(nums) / i
print(mean)

