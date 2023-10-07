class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = [set() for _ in range(n)] 
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        bobpath = dict() 
        self.stop = False 
        visited = [False]*n 
        def backtrackbob(node,time): 
            bobpath[node] = time 
            visited[node] = True 
            if node==0: 
                self.stop = True
                return None
            count = 0 
            for nei in graph[node]: 
                if not visited[nei]:
                    count += 1
                    break
            if count==0: 
                del bobpath[node] 
                return None
            for nei in graph[node]: 
                if self.stop: return None 
                if not visited[nei]:
                    backtrackbob(nei,time+1)
            if not self.stop: 
                del bobpath[node]
            return None

        backtrackbob(bob,0) 

        self.ans = float(-inf) 
        self.income = 0 
        visited = [False]*n 
        def backtrackalice(node,time): 
            visited[node] = True
            if node in bobpath: 
                if time == bobpath[node]: 
                    reward = amount[node]//2
                elif time<bobpath[node]: 
                    reward = amount[node]
                else: 
                    reward = 0
            else: 
                reward = amount[node]
            self.income += reward
            count = 0 
            for nei in graph[node]:
                if not visited[nei]:
                    count += 1
                    break
            if count==0: 
                self.ans = max(self.ans,self.income) 
                self.income -= reward 
                return None
            for nei in graph[node]: 
                if not visited[nei]:
                    backtrackalice(nei,time+1)
            self.income -= reward 
            return None

        backtrackalice(0,0)

        return self.ans
