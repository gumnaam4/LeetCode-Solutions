nums = [3,6,9,12,15,18]
k = 3
l=0
b=True
for i in range(len(nums)):
    if nums[i] % k == 0:
        if l < nums[i]:
            l = nums[i]
#print(l//k)
for j in range(1,l//k):
    if j * k not in nums:
        print(j * k)
        b= False
        break
if b == True:
    print(k * ((l//k)+1))          