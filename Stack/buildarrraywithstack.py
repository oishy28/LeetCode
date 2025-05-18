class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        result = []
        index = 0
        
        for i in range(1,n+1):
            if index >= len(target):
                break
            elif i in target:
                result.append("Push")
                index += 1
            else:
                result.append("Push")
                result.append("Pop")
                
        return result