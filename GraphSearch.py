##############
# Original code from:
# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
# Original Author: Valerio Velardo
# License: none given
##############
# Change log:
# new main, new graph 
# Modified shortest path to return empty list if no pth found
# Modified shortest path to retturn list with start if goal == start
##############

def bfs_connected_component(graph, start):
    explored = []

    queue = [start]



    while queue:

        node = queue.pop(0)
        if node not in explored:

            explored.append(node)
            neighbors = graph[node]


            for neighbor in neighbors:
                queue.append(neighbor)
    return explored
# end bfs_connected_component(graph,start)

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return [start]
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return []
# end bfs_shortest_path(graph, start, goal) 



def main():
    graph = {'1': ['2', '5'],
             '2': ['1', '2', '5'],
             '3': ['2', '4'],
             '4': ['3', '5', '6'],
             '5': ['1', '2', '4'],
             '6': ['4']
             }
    #print(bfs_connected_component(graph, '6'))
    print(bfs_shortest_path(graph, '1', '2'))  
    print(bfs_shortest_path(graph, '2', '6'))  
    print(bfs_shortest_path(graph, '1', '6'))  
# End Main

if __name__ == "__main__":
    main()