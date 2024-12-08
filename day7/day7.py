import treelib
# from binarytree import Node

from treelib import *

# data = open('example7.txt').readlines()
data = open('input7.txt').readlines()

part1 = part2 = 0


def create_tree(nums):
    tree = Node(nums[0])
    for i, n in enumerate(nums[1:]):
        for node in tree.levels[i]:
            node.left = Node(node.value + n)
            node.right = Node(node.value * n)
    return tree


def create_another_tree(nums):
    tree = treelib.Tree()
    tree.add_node(Node(nums[0]))
    for i, n in enumerate(nums[1:]):
        for leaf in tree.leaves():
            tree.add_node(treelib.Node(leaf.tag + n), leaf)
            tree.add_node(treelib.Node(leaf.tag * n), leaf)
            tree.add_node(treelib.Node(int(str(leaf.tag) + str(n))), leaf)
    return tree


length = len(data)
for i, line in enumerate(data):
    print('solving equation', i, length)
    result, nums = line.split(':')
    result = int(result)
    nums = [int(x) for x in nums.strip().split()]

    # tree = create_tree(nums)
    # if result in [leaf.value for leaf in tree.leaves]:
    #     part1 += result
    #

    tree = create_another_tree(nums)
    if result in [leaf.tag for leaf in tree.leaves()]:
        part2 += result

print('part1: ', part1)  # TOO SLOOOOW
print('part2: ', part2)  # WAY SLOOOOOOWER
