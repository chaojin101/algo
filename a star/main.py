'''
Leetcode 1091. Shortest Path in Binary Matrix
https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/
'''

import heapq


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def print_grid():
            for row in grid:
                print(row)
            print()

        def heuristic(point1, point2):
            return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))
        
        n = len(grid)
        directions = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1]
        ]
        def get_neighbors(point):
            x, y = point
            neighbors = []
            for dx, dy in directions:
                u = x + dx
                v = y + dy
                if 0 <= u < n and 0 <= v < n and grid[u][v] == 0:
                    neighbors.append((u, v))
            return neighbors

        print_grid()
        
        cost_so_far = {}
        q = []

        start = (0, 0)
        goal = (n - 1, n - 1)
        heapq.heappush(q, (0, start))
        cost_so_far[start] = 1
        came_from = { start: None }

        while q:
            _, current_point = heapq.heappop(q)

            if current_point == goal:

                p = goal
                while p:
                    x, y = p
                    grid[x][y] = 2
                    p = came_from[p]
                print_grid()

                return cost_so_far[current_point]

            for next_point in get_neighbors(current_point):
                new_cost = cost_so_far[current_point] + 1
                if new_cost < cost_so_far.get(next_point, float('inf')):
                    cost_so_far[next_point] = new_cost
                    next_point_priority = new_cost + heuristic(next_point, goal)
                    heapq.heappush(q, (next_point_priority, next_point))

                    came_from[next_point] = current_point
            
        return -1
