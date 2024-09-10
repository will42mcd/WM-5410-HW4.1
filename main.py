from GraphSearch import *


def main():

    graph = {'Omaha': ['Houston', 'Dallas', 'Chicago'],
             'Louisville': ['Houston', 'Dallas', 'Chicago', 'Baltimore'],
             'Baltimore': ['Houston', 'Dallas', 'Chicago', 'Portland', 'Salt Lake City', 'Belize City', 'Omaha','Louisville' ],
             'Portland': ['Baltimore', 'Chicago'],
             'Salt Lake City': ['Chicago', 'Baltimore', 'Dallas', 'Houston'],
             'Belize City': ['Houston', 'Baltimore'],
             'Dallas': ['Louisville', 'Baltimore', 'Chicago', 'Salt Lake City', 'Houston', 'Omaha'],
             'Houston': ['Dallas', 'Chicago', 'Salt Lake City', 'Belize City', 'Omaha','Louisville', 'Baltimore' ],
             'Chicago': ['Houston', 'Dallas', 'Chicago', 'Portland', 'Salt Lake City', 'Omaha','Louisville' ]}
    
    print(bfs_shortest_path(graph, 'Omaha', 'Louisville'))
    print()
    path = ['Baltimore', 'Salt Lake City', 'Portland']
    trip1 = bfs_shortest_path(graph, path[0], path[1])
    trip2 = bfs_shortest_path(graph, path[1], path[2])
    trip2.pop(0)
    trip = trip1 + trip2
    print(trip)
    print()
    print(bfs_shortest_path(graph, 'Belize City', 'Portland'))
if __name__ == "__main__":
    main()