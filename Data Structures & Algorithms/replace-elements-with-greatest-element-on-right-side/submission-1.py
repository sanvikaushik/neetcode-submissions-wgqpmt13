class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 2, 4, 5, 3, 1, 2           #            ,2,-1         

        # 5, 4, 5, 3, 1, 2 
        # 5, 5, 5, 3, 1, 2  
        # 5, 5, 3, 3, 1, 2
        # 5, 5, 3, 2, 1, 2
        # 5, 5, 3, 2, 2, 1 

        # backwards
        curr_max = -1
        max_arr = [0] * len(arr)

        for i in range(len(arr) - 1, -1, -1):

            if i + 1 < len(arr):
                curr_max = max(curr_max, arr[i + 1])
            
            max_arr[i] = curr_max

        return max_arr

