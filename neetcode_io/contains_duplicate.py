from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker =  set()

        for num in nums:
            if num in tracker:
                return True
            
            tracker.add(num)

        return False
    

if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums))

    nums = [1, 2, 3, 4]
    print(solution.hasDuplicate(nums))
