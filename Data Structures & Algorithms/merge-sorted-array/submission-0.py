class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j += 1
        
        def merge_sort(nums1):

            if len(nums1) <= 1:
                return nums1
            
            # split
            left_a = nums1[:len(nums1)//2]
            right_a = nums1[len(nums1)//2:]

            left_a = merge_sort(left_a)
            right_a = merge_sort(right_a)

            i = 0
            j = 0
            k = 0
            while i < len(left_a) and j < len(right_a):

                if left_a[i] < right_a[j]:
                    nums1[k] = left_a[i]
                    i += 1
                    k += 1
                
                else:
                    nums1[k] = right_a[j]
                    j += 1
                    k += 1
                
            
            while i < len(left_a):
                nums1[k] = left_a[i]
                i += 1
                k += 1
            
            while j < len(right_a):
                nums1[k] = right_a[j]
                j += 1
                k += 1

            return nums1
        
        return merge_sort(nums1)

