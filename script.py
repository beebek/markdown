from collections import OrderedDict
from pprint import pprint
import sys

NEW_BLOCK = "* "
BULLETS = "."


def block_separator(content=None):
    blocks = []
    block_items = []
    same_block = False
    for line in content.splitlines():
        if not line:
            continue
        if line.startswith(NEW_BLOCK):
            blocks.append(block_items)
            block_items = []
        block_items.append(line)
    blocks.append(block_items)
    blocks.pop(0)
    return blocks

def bullet_processor(head_no, family):
    parent = family.pop(0)
    print("{} {}".format(head_no, parent.strip(NEW_BLOCK)))
    children = OrderedDict()

    for i, child in enumerate(family):
        print(i+1, child)
        

if __name__ == "__main__":
    # content = sys.stdin.read()

    with open("input.txt", "r") as f:
        content = f.read()

    for i, item in enumerate(block_separator(content)):
        bullet_processor(i+1, item)
        print()
