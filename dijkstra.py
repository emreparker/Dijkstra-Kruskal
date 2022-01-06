from collections import defaultdict
from heapq import *
from tkinter import *
import math

def dijkstra(edges, s, d):
	dictionary = defaultdict(list)
	total_lines_read = 20 #number of lines, because there are 20 lines except counter.

	for l, r, w in edges:
		dictionary[l].append((w, r))
		total_lines_read += 1

	q, visited, min_dst = [(0, s, ())], set(), {s: 0}

	while q:
		(current_cost, v1, followed_path) = heappop(q)
		if v1 in visited:
			continue

		visited.add(v1) #adds point to visited list
		followed_path += (v1,) #logs the path followed
		if v1 == d:
			return current_cost, followed_path, total_lines_read

		for w, v2 in dictionary.get(v1, ()):
			if v2 in visited:
				continue

			if v2 not in min_dst or current_cost + w < min_dst[v2]:
				min_dst[v2] = current_cost + w
				heappush(q, (current_cost + w, v2, followed_path))
				total_lines_read += 1

		total_lines_read += 1

	return float("inf")

edges = []

flag = False


#gets input from user and raise error if given inputs are not compatible with rules.
nodePoint = input("Node Entry:")
startPoint = input("Start Entry:")
endPoint = input("End Entry:")

if nodePoint == '' or startPoint == '' or endPoint == '':
	print("Error: You must fill all the inputs.")
elif 20 < int(nodePoint) or int(nodePoint) < 1:
	print("Error: N must be between 1-20.")
elif int(startPoint) > int(nodePoint):
	print("Error: Start Point must be between 1-N.")
elif int(endPoint) > int(nodePoint):
	print("Error: End Point must be between 1-N.")
else:
	flag= True




if flag:
	N = int(nodePoint)
	S = int(startPoint)
	D = int(endPoint)

	r = 20
	x = 45
	y = 200

	for i in range(1, N+1):
		for j in range(i+1, i + 4):
			if j > N:
				break
			edges.append((i, j, (i + j)))
			edges.append((j, i, (i + j)))
		if i % 2 == 1:
			y = 200
		else:
			y = 400
			x += 4 * r

	print(str(S), " -> ", str(D))
	distance, road, total_cost = dijkstra(edges, S, D)
	print("Distance: ", distance)
	print("Road: ", road)
	print("|E|: ", str(len(edges)))
	print("|V|: ", str(N))
	theory = (len(edges)+N)*math.log(N, 10)
	print("(|E|+|V|)*log|V| :", str(theory))
	print("Total Cost: ", total_cost)

	x = 45
	y1 = 200
	y2 = 200
	for i in range(len(road)-1):
		if road[i] % 2 == 1:
			y1 = 200
		else:
			y1 = 400
		if road[i+1] % 2 == 1:
			y2 = 200
		else:
			y2 = 400

		x1 = x + int((road[i]-1)/2) *4*r
		x2 = x + int((road[i+1]-1)/2)*4*r


