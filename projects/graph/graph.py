"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create queue
        q = Queue()
        #enqueue with starting vertex
        q.enqueue(starting_vertex)
        #create set to keep track of visited vertices
        visited = set()

        # while size of queue greater than 0
        while q.size() > 0:
            # dequeue next vertex in line
            v=q.dequeue()
            
            #if vertex hasn't been visited
            if v not in visited:
                print(v)
                #mark current as visited
                visited.add(v)
                #add neighbors to queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create stack
        s=Stack()
        #initialize stack with starting vertices
        s.push(starting_vertex)
        # create set to keep track of visited
        visited = set()

        # while stack size greater than 0
        while s.size() > 0:
            #get next vertex
            v = s.pop()
            #if vertex hasn't been visited
            if v not in visited:
                print(v)
                #mark current as visited
                visited.add(v)
                #add neighbors to queue
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def dft_helper(starting_vertex):

            #  if vertex hasn't been visited yet
            if starting_vertex not in visited:
                print(starting_vertex)

                # mark vertex as visited
                visited.add(starting_vertex)

                # go through all neighbors recursively
                for neighbor in self.get_neighbors(starting_vertex):
                    dft_helper(neighbor)
       
        # create a set to keep track of visited vertices
        visited = set()

        dft_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue and enqueue a path to the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
		# create a set to store visited vertices
        visited = set()
        
		# while the queue is not empty...
        while q.size() > 0:
			# dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            v = path[-1]
			

			# if that vertex has not been visited
            if v not in visited:
				# check if it is target
                if v == destination_vertex:
				  # if so, return path
                    return path
                # mark it as visited   
                visited.add(v)
				
				# then add a path to its neighbors to the back of the queue
                for neighbors in self.get_neighbors(v):
                    #copy path
                    path_copy = list(path)
                    #append neighbor to back
                    path_copy.append(neighbors)
                    q.enqueue(path_copy)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack and push a path to the starting vertex
        s = Stack()
        s.push([starting_vertex])
		# create a set to store visited vertices
        visited = set()
        
		# while the stack is not empty
        while s.size() > 0:
			# dequeue the first path
            path = s.pop()
            # grab the last vertex from the path
            v = path[-1]
			
			# if that vertex has not been visited
            if v not in visited:
				# check if target
                if v == destination_vertex:
				  # if so, return path
                    return path
                # mark it as visited
                visited.add(v)
				# then add a path to its neighbors to the back of the queue
                for neighbors in self.get_neighbors(v):
                    # copy path
                    path_copy = list(path)
                    # append neighbor to end
                    path_copy.append(neighbors)
                    #push onto stack
                    s.push(path_copy)
        return None


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dfs_helper(starting_vertex, destination_vertex, path_so_far):

            # check if vertex hasn't been visited yet
            if starting_vertex not in visited:   

                visited.add(starting_vertex)

                # if the vertex has been found elsewhere, stop recursion
                if vertex_found:
                    return
                #
                elif starting_vertex == destination_vertex:
                    final_path = path_so_far[:]
                    final_path.append(starting_vertex)

                    # add answer to dictionary to be returned
                    answer[destination_vertex] = final_path
                    
                else:
                    for neighbor in self.get_neighbors(starting_vertex):
                        new_path = path_so_far[:]
                        new_path.append(starting_vertex)
                        dfs_helper(neighbor, destination_vertex, new_path)

        # create a set to keep track of visited vertices
        visited = set()

        # create a flag to deteremine whether to continue recursion
        vertex_found = False

        # create a variable to hold the answer
        answer = dict()
        
        dfs_helper(starting_vertex, destination_vertex, [])

        return answer[destination_vertex]

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
