class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()

        solution = list()
        seen_triplets = set()


        for i, num in enumerate(nums):

            # find j, k for this i, such that sum(nums[i], nums[j], nums[k]) = 0

            # Given we know that at i there is nums, we need to find sum(nums[j], nums[k]) == -nums


            low, high = 0, len(nums) - 1

            target = num * -1

            while low != i and high != i:
                if (nums[low] + nums[high]) == target:
                    if (nums[low], num, nums[high]) not in seen_triplets:
                        solution.append([nums[low], num, nums[high]])
                        seen_triplets.add((nums[low], num, nums[high]))
                    low += 1
                    high -= 1
            
                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    low += 1

        
        return solution 



        