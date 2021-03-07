#Reference: https://www.geeksforgeeks.org/python-program-for-topological-sorting/
#Python program to print topological sorting of a DAG
import sys
from collections import defaultdict

#Class to represent a graph
class Graph:
    def __init__(self):
        self.parents = defaultdict(list)
        self.children = defaultdict(list) #dictionary containing adjacency List
        self.start = sys.maxsize
        self.end = -sys.maxsize

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.start = min(self.start, u, v)
        self.end = max(self.end, u, v)
        self.children[u].append(v)
        self.parents[v].append(u)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v-self.start] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.children[v]:
            if visited[i-self.start] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        num = self.end - self.start + 1
        # Mark all the vertices as not visited
        visited = [False]*num
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(num):
            if visited[i] == False:
                self.topologicalSortUtil(i+self.start,visited,stack)

        # Print contents of stack
        # print(stack)
        return stack

if __name__ == '__main__':
    g = Graph()
    g.addEdge(6, 3)
    g.addEdge(6, 1)
    g.addEdge(5, 1)
    g.addEdge(5, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 2)
    ans = g.topologicalSort()
    print(ans)
#This code is contributed by Neelam Yadav