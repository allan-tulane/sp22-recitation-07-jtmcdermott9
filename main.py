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
      x = p.get(0)
      y = p.get(1)
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

  if(node.left):
    prefix = prefix + '0'
    get_code(node.left, prefix, code)

  if(node.right):
    prefix = prefix + '1'
    get_code(node.right, prefix, code)

  if(not node.left and not node.right):
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

  f_values = list(f.values())
  C_values = list(C.values())
  for i in range(len(f_values)):
    cost += f_values[i] * len(C_values[i])
 
      
  return cost
      

f = get_frequencies('f1.txt')
f2 = get_frequencies('alice29.txt')
f3 = get_frequencies('asyoulik.txt')
f4 = get_frequencies('fields.c')


print("Fixed-length cost:  %d" % fixed_length_cost(f))
print("Fixed-length cost:  %d" % fixed_length_cost(f2))
print("Fixed-length cost:  %d" % fixed_length_cost(f3))
print("Fixed-length cost:  %d" % fixed_length_cost(f4))

print( '\n'*2)
T = make_huffman_tree(f)

T2 = make_huffman_tree(f2)
T3 = make_huffman_tree(f3)
T4 = make_huffman_tree(f4)

C = get_code(T)
C2 = get_code(T2)
C3 = get_code(T3)
C4 = get_code(T4)


print("Huffman cost:  %d" % huffman_cost(C, f))
print("Huffman cost:  %d" % huffman_cost(C2, f2))
print("Huffman cost:  %d" % huffman_cost(C3, f3))
print("Huffman cost:  %d" % huffman_cost(C4, f4))