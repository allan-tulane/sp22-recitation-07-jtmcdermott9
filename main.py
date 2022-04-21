import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        # TODO
      x = p.get()
      y = p.get()
      #print(x.data[1])
      #print(y.data[0])
      #x.data[1] = '0'
      #y.data[1] = '1'
      z = TreeNode(x, y, (x.data[0] + y.data[0], ""))
      

      p.put(z)
      

      
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
  # TODO - perform a tree traversal and collect encodings for leaves in code

  if(node.left!= None):
    # prefix = prefix + '0'
    get_code(node.left, prefix+'0', code)

  if(node.right !=None):
    # prefix = prefix + '1'
    get_code(node.right, prefix+'1', code)

  if(node.left==None and node.right ==None):
    code[node.data[1]] = prefix
  return code
  

  

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
  # TODO
  freq = f
  words = len(freq.keys())
  bit_len = math.ceil(math.log(words, 2))
  file_len = 0
  for i in freq.values():
    file_len += i
  cost = bit_len * file_len


  return cost 

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding

def huffman_cost(C, f):
  # TODO
  cost = 0

  f_values = f.keys()#list(f.values())
  # print()
  # print(len(f_values))
  
  # C_values = list(C.values())
  # print(len(C_values))
  for i in f_values:
    cost += f[i] * len(C[i])
 
      
  return cost
      

f = get_frequencies('f1.txt')


#f = {'A': 9, 'B': 1, 'C': 1, 'D': 1}
# f = {'a': 15, 'b':2, 'c':1, 'd':1, 'e':1}


print("Fixed-length cost:  %d" % fixed_length_cost(f))


T = make_huffman_tree(f)
C = get_code(T)

print("Huffman cost:  %d" % huffman_cost(C, f))

print( '\n'*2)
f2 = get_frequencies('alice29.txt')
T2 = make_huffman_tree(f2)
C2 = get_code(T2)

print("Fixed-length cost:  %d" % fixed_length_cost(f2))
print("Huffman cost:  %d" % huffman_cost(C2, f2))

print( '\n'*2)
f3 = get_frequencies('asyoulik.txt')

T3 = make_huffman_tree(f3)
C3 = get_code(T3)

print("Fixed-length cost:  %d" % fixed_length_cost(f3))



print("Huffman cost:  %d" % huffman_cost(C3, f3))

print( '\n'*2)

f4 = get_frequencies('fields.c')

T4 = make_huffman_tree(f4)


print("Fixed-length cost:  %d" % fixed_length_cost(f4))



# print(C)


C4 = get_code(T4)





print("Huffman cost:  %d" % huffman_cost(C4, f4))
print('\n'*2)

f5 = get_frequencies('grammar.lsp')
T5 = make_huffman_tree(f5)
C5 = get_code(T5)
print("Fixed length cost: %d" % fixed_length_cost(f5))
print("Huffman cost: %d" % huffman_cost(C5, f5))

f6 = {'a':20, 'b':20, 'c':20, 'd':20, 'e':20, 'f':20, 'g':20, 'h':20, 'i': 20}
T6 = make_huffman_tree(f6)
C6 = get_code(T6)
print("Fixed length cost: %d" % fixed_length_cost(f6))
print("Huffman cost: %d" % huffman_cost(C6, f6))