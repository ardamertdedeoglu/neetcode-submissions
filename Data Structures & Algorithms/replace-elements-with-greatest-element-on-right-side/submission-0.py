class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        j = i + 1
        while i < len(arr) - 1:
            j = i + 1
            arr[i] = arr[j]
            while j < len(arr):
                arr[i] = max(arr[i], arr[j])
                j+=1
            i+=1
        arr[-1] = -1
        return arr