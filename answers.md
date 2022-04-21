# CMPS 2200 Recitation 7
## Answers

**Name:**____JT McDermott_____________________


Place all written answers from `recitation-07.md` here for easier grading.



- **d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |        1340             |        826        | 1.6
alice29.txt    |         1039367    |         676374    | 1.5
asyoulik.txt    |         876253    |      606448       | 1.44
grammar.lsp    |        26047       |          17356    | 1.53
fields.c    |      78050            |    56206          | 1.39


As the size of the file increases, the ratio decreases, meaning the relative improvement of Huffman coding decreases.

- **e.**
The expected cost is proportional to the depth of the constructed binary heap, so as the length of the document increases the cost increases by n log n. 

