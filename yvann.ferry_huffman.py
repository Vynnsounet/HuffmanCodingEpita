__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2023-03-24'

"""
Huffman homework
2023-03
@author: yvann.ferry
"""

from algo_py import bintree
from algo_py import heap


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################AttributeError: module 'random' has no attribute 'randint'
## COMPRESSION

def build_frequency_list(dataIN):
    """
    Builds a tuple list of the character frequencies in the input.
    """
    counts = []
    for char in dataIN:

        char_exists = False
        i = 0

        while i < len(counts):
            if counts[i][1] == char:

                counts[i] = (counts[i][0] + 1, char)
                char_exists = True
            i+=1
        
        if not char_exists:
            counts.append((1, char))
    
    return counts



def __convert_to_char(string):
    curr_pow = 1
    number = 0

    for i in range(len(string)):

        number += int(string[len(string) - 1 - i]) * curr_pow
        curr_pow *= 2

    return chr(number)

def build_Huffman_tree(inputList):
    """
    Processes the frequency list into a Huffman tree according to the algorithm.
    """
    h = heap.Heap()

    for occ,value in inputList:
        h.push((occ,bintree.BinTree(value,None,None)))

    while len(h.elts) != 2:

        (o1,v1),(o2,v2) = h.pop(),h.pop()
        newtree = bintree.BinTree(None,v1,v2)
        h.push((o1+o2,newtree))
    
    return h.elts[1][1]


def __get_hierachical_order(B,key,repr):
    if B == None:
        return "",False

    if B.key == key:
        return repr,True

    rep,found = __get_hierachical_order(B.left,key,repr+"0")

    if not found:

        rep,found = __get_hierachical_order(B.right,key,repr+"1")
        return rep,False or found

    return rep,found



def encode_data(huffmanTree, dataIN):
    """
    Encodes the input string to its binary string representation.
    """
    res = ""
    for char in dataIN:
         repr,_ = __get_hierachical_order(huffmanTree,char,"")
         res += repr
    return res

    


def encode_tree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    if huffmanTree.key == None:
        return "0"+encode_tree(huffmanTree.left)+encode_tree(huffmanTree.right)
    
    return "1" + __to_bin(ord(huffmanTree.key),"")


def __to_bin(integer,repr):
    if len(repr) == 8:
        return repr
    return __to_bin(integer//2,str(integer%2)+repr)


def to_binary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """

    res = ""
    currvalue = dataIN[0]
    index = 1

    while index < len(dataIN):

        if index % 8 == 0:
            res += __convert_to_char(currvalue)
            currvalue = dataIN[index]
            index += 1

        else:
            currvalue += dataIN[index]
            index += 1

    res += __convert_to_char(currvalue)
    return res,8 - len(currvalue)
            


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
    tree = build_Huffman_tree(build_frequency_list(dataIn))
    encoded_data = encode_data(tree,dataIn)
    encoded_tree = encode_tree(tree)
    return (to_binary(encoded_data),to_binary(encoded_tree))
    

    
################################################################################
## DECOMPRESSION

def decode_data(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    index = 0
    res = ""
    while index < len(dataIN):
        val,index = __search_with_hierar(huffmanTree,dataIN,index)
        res += val
    return res



def __search_with_hierar(B,string,i):
    if B.key != None:
        return B.key,i
    if string[i] == "0":
        return __search_with_hierar(B.left,string,i+1)
    return __search_with_hierar(B.right,string,i+1)


    
def decode_tree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    bintree,_= __build_tree(dataIN,0)
    return bintree

def __build_tree(string,index):
    if string[index] == "0":

        left,index = __build_tree(string,index + 1)
        right,index = __build_tree(string,index +1)
        return bintree.BinTree(None,left,right),index

    else:
        key = ""
        for i in range(index+1,index+9):
            key += string[i]
        return bintree.BinTree(__convert_to_char(key),None,None),index + 8
        

def from_binary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    # FIXME
    string = ""

    for i in range(len(dataIN)):

        if i == len(dataIN) - 1:
            string += __trim_zero(__to_bin(ord(dataIN[i]),""),align)
        else:
            string += __to_bin(ord(dataIN[i]),"")

    return string
        
        
def __trim_zero(string,n):
    res = ""
    for i in range(n, len(string)):
        res += string[i]

    return res



def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    encoded_text = from_binary(data,dataAlign)
    encoded_tree = from_binary(tree,treeAlign)
    tree = decode_tree(encoded_tree)
    return decode_data(tree,encoded_text)
