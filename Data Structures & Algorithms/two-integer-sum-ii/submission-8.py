class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        s = -1
        for i in range(n): 
            s += 1
            for j in range(s, n):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        