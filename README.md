# Dijkstra-Kruskal
A program which finds the shortest path between given source (S) and destination (D) nodes of a Graph by using Dijkstra’s shortest path algorithm and Kruskal’s MST algorithm in Python3. The program reads N (&lt; 20) and returns the edges of the MST and its total weight.


# Dijkstra's Shortest Path Algorithm
Dijktra's algorithm is an iterative algorithm that finds the shortest path between two nodes. This technique is critical since it is one of the fastest methods for determining the shortest path. Finding the shortest path is something that lots of people do in their daily lives such as people use navigations in their daily lives. Because the navigation systems we use are essentially huge networks with nodes and weights, Dijkstra algorithm is commonly utilized in navigation apps because of its shorter duration and easier explanation, this method is a suitable choice. The steps of Dijkstra’s shortest path algorithm are as below.
1.	Set up the distances in accordance with the algorithm.
2.	Choose the first node and compute the distances between it and the others.
3.	Choose the next node with the shortest distance; repeat the distance computations for adjacent nodes.
4.	The shortest-path tree's final outcome

```
INITIALIZE-SINGLE-SOURCE(V, s)
	S ← ∅
	Q ← V[G]
	while Q ≠ ∅
		do u ← EXTRACT-MIN(Q)
		S ← S ∪ {u}
		for each vertex v ∈ Adj[u]
			do RELAX(u, v, w)
			Update Q (DECREASE_KEY)
```

•	1st line has O(V) time complexity.
•	2ND line has O (1) time complexity.
•	3RD line has O(V) time complexity. Adding all V vertices to Q takes O(V) time.
•	4th line has O(V) time complexity because while loop has executed O(V) times and 5th line has O(lgV) time complexity. Thus, from line 4TH to 5TH, these lines have O(VlgV) running time complexities.
•	7th line has O(E) time complexity and 9th line has O(lgV) time complexity. From line 7th to 9th, these lines have O(E lgV) running time complexities.
•	The overall complexity is O(VlgV + E lgV) = O(E lgV)
•	The original algorithm had a runtime of O((V+E)log(V)), on the other hand using Fibonacci heap min priority queue to optimize the runtime complexity becomes O(E +V log(V)). 

# Kruskal's Minimum Spanning Tree Algorithm

Kruskal’s MST algorithm is the graph whose sum of weights of edges is minimum. For a linked weighted graph, the Kruskal Algorithm is used to obtain the minimum spanning tree. The algorithm's main goal is to find the minimum subset of edges through which each vertex of the graph can be traversed. The number of edges in a minimum spanning tree is V-1, where V is the number of vertices in the graph. The steps of Kruskal’s MST algorithm are as below.
1.	Sort the edges by weight in an increasing order.
2.	Choose the smallest edge. Check to see if it forms a cycle with the spanning tree you've already created. Include this edge when a cycle isn't formed. Otherwise, throw it out.
3.	Repeat the previous step till the spanning tree has V-1 edges.

```
MST_KRUSKAL(V,E,w)
	A←∅
	for each vertex v ∈ V
	    do MAKE-SET(v)
	sort the edges of E into non-decreasing order by weight w
	for each (u, v) taken from the sorted list
	     do if FIND-SET(u) ≠ FIND-SET(v)
	 	then A ← A ∪ {(u, v)}
	 	UNION(u, v)
	return A
```



