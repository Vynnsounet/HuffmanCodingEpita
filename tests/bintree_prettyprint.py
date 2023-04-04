# -*- coding: utf-8 -*-
"""
pretty print for binary trees (BinTree)
"""

from algo_py import bintree

def __height(ref):
    """Compute height of Tree.

    Args:
        ref (BinTree).

    Returns:
        int: The maximum depth of any leaf.

    """

    if ref == None:
        return -1
    else:
        return 1 + max(__height(ref.left), __height(ref.right))


def prettyprint(root, digits=1):
    """
    display in ASCII the tree root
    digits: maximum nb digits of keys (when int)
    """
    nodes = [root]
    level = 1
    maxLevel = __height(root) + 1 + digits // 2
    while level <= (maxLevel-digits//2):
        floor = maxLevel - level
        edgeLines = 2 ** (max(floor - 1, 0))
        firstSpaces = 2 ** floor - 1
        betweenSpaces = 2 ** (floor + 1) - 1
        print(' ' * (firstSpaces - digits // 2), end='')
        newNodes = []
        for node in nodes:
            if node != None:
                if node.key != None:
                    print(node.key, end='')
                else:
                    print('.', end='')
                newNodes.append(node.left)
                newNodes.append(node.right)
            else:
                newNodes.append(None)
                newNodes.append(None)
                print(' ' * digits, end='')
            print(' ' * (betweenSpaces-digits+1), end='')
        print()
        if level < (maxLevel-digits//2):
            for i in range(1, edgeLines + 1):
                for node in nodes:
                    print(' ' * (firstSpaces - i), end='')
                    if node == None:
                        print(' ' * (2 * edgeLines + i + 1), end='')
                    else:
                        if node.left != None:
                            print('/', end='')
                        else:
                            print(' ', end='')
                        print(' ' * (2 * i - 1), end='')
                        if node.right != None:
                            print('\\', end='')
                        else:
                            print(' ', end='')
                        if node != nodes[-1]:
                            print(' ' * (2 * edgeLines - i), end='')
                print()
        nodes = newNodes
        level += 1
