import random
from functools import reduce
from utils import data_to_dictionary

class PageRankDiGraph:
    def __init__(self, data):
        self.data = data
        self.link_dict = data_to_dictionary(data)
    
    def __add__(self, other):
        return PageRankDiGraph(self.data + other.data)

    def __len__(self):
        return len(self.data)
    
    def get_nodes(self):
        #return list(self.link_dict.keys())
        sung_to = reduce(lambda x, y: x+y, self.link_dict.values())
        singer = list(self.link_dict.keys())
        return list(set(sung_to + singer)) 

    def __contains__(self, item):
        #return item in self.link_dict
        return item in self.get_nodes()
    
    def __str__(self):
        return "PageRankDiGraph with " + str(len(self.get_nodes())) + " nodes and " + str(len(self)) + " edges."
            
    def linked_by(self, x):
        return self.link_dict[x]

class PageRankIterator(object):   
    def __init__(self, graph, iteration_limit=20, jump_prob=0.85):
        self.graph = graph
        if not isinstance(self.graph, PageRankDiGraph):
            raise TypeError("Graph should be an instance of PageRankDiGraph.")
        
        self.iter_limit = iteration_limit
        self.p = jump_prob

        self.iter = 0
        self.current_state = "hamilton" # pick a different initialization for airports

    def follow_link(self):
        # main block: attempt to follow a link
        try: 
            possibilities = self.graph.linked_by(self.current_state)
            next_state = random.choice(possibilities)
            # if trying to follow a self-link, teleport instead
            if self.current_state == next_state:
                self.teleport()
            else:
                self.current_state = next_state
        # if no links to follow, teleport
        except KeyError:
            self.teleport()
    
    def teleport(self):
        self.current_state = random.choice(self.graph.get_nodes())
    
    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        # self.iter gives the number of times that __next__() has been called. 
        self.iter += 1
        
        # check if we have reached the limit, stop if so
        if self.iter > self.iter_limit:
            raise StopIteration
        
        # follow link w/probability jump_prob, otherwise teleport
        if random.random() < self.p:
            self.follow_link()
        else:
            self.teleport()
        
        # return the current state
        return self.current_state


class IterablePageRankDiGraph(PageRankDiGraph):
    def __init__(self, data, iteration_limit=20, jump_prob=0.75):
        super().__init__(data)
        self.iter_limit = iteration_limit
        self.p = jump_prob
    
    def __str__(self):
        return "IterablePageRankDiGraph with " + str(len(self.get_nodes())) + " nodes and " + str(len(self)) + " edges."
       
    def __iter__(self):
        return PageRankIterator(self, self.iter_limit, self.p)
