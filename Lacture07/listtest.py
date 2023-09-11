def find_peak_indices(nums):
    peak_indices = []
    
    if len(nums) == 1:
        return [0]
    
    if nums[0] >= nums[1]:
        peak_indices.append(0)
    
    for i in range(1, len(nums) - 1):
        if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
            peak_indices.append(i)
    
    if nums[-1] >= nums[-2]:
        peak_indices.append(len(nums) - 1)
    
    return peak_indices

# Test cases
nums1 = [3]
nums2 = [1, 2, 1, 3, 5, 6, 4]
nums3 = [1, 2, 1, 4, 5, 6, 4, 7]

print("Peak element index of :", nums1,'->',find_peak_indices(nums1))  
print("Peak element index of :", nums2,'->',find_peak_indices(nums2))  
print("Peak element index of :", nums3,'->',find_peak_indices(nums3)) 
