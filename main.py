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
    prefixLeft = prefix + '0'
    Lstring = node.left.data[1]
    code[Lstring] = prefixLeft
    return get_code(node.left, prefixLeft, code)

  if(node.right):
    prefixRight = prefix + '1'
    Rstring = node.right.data[1]
    code[node.right.data[1]] = prefixRight
    return get_code(node.right, prefixRight, code)
 

    
  if(not node.left and not node.right):
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
    pass

f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
print(T.data[0])
C = get_code(T)
print(C)
#print("Huffman cost:  %d" % huffman_cost(C, f))