from functions import *
from bintree_prettyprint import *

# s = "i do not really know what i am doing rn"
# f = build_frequency_list(s)
# b = build_Huffman_tree(f)


def printTree(B):
    if B == None:
        return "()"
    else:
        return f"({(B.key,'.')[B.key == None]},{printTree(B.left)},{printTree(B.right)})"

# print(f)
# prettyprint(b)
# v = encode_data(b,s)
# res = decode_data(b,v)
# print(v,res)
# prettyprint(b)
# eb = encode_tree(b)
# print(eb)
# prettyprint(decode_tree(eb))

# prettyprint(decode_tree("0010111010010110001001011000010101100011101100101"))
# (data,dataAlign),(tree,treeAlign) = compress("um ah human huffman is fun ha")
# print(data,dataAlign,tree,treeAlign)
# print(decompress(data,dataAlign,tree,treeAlign))


(data,dataAlign),(tree,treeAlign) = compress("""""")

print(decompress(data,dataAlign,tree,treeAlign)
