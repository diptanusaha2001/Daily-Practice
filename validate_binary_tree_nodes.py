from queue import Queue
class Solution:
    def isBinaryTreeValid(self, root: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [False] * len(leftChild)
        nodeQueue = Queue()  
        nodeQueue.put(root)
        visited[root] = True

        while not nodeQueue.empty():
            current = nodeQueue.get()
            if leftChild[current] != -1:
                if visited[leftChild[current]]:
                    return False

                nodeQueue.put(leftChild[current])
                visited[leftChild[current]] = True  
            if rightChild[current] != -1:
                if visited[rightChild[current]]: 
                    return False

                nodeQueue.put(rightChild[current])
                visited[rightChild[current]] = True
        for visit in visited:
            if not visit:
                return False

        return True  

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        childCount = [False] * n  
        for child in leftChild:
            if child != -1:
                childCount[child] = True  
        for child in rightChild:
            
            if child != -1:
                if childCount[child]:  
                    return False

                childCount[child] = True
        root = -1  
        for i in range(n):
            if not childCount[i]:
                if root == -1:
                    root = i  
                else:
                    return False 
        if root == -1:
            return False 

        return self.isBinaryTreeValid(root, leftChild, rightChild)  
