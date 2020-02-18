#!/usr/bin/python
import sys
from xml.etree import ElementTree

e = ElementTree.parse(sys.argv[1])

SCALE_FACTOR = 1.0/2.54

def printtree(parent, tree, height):
    print " "*height + str(tree) + str(tree.attrib)
    for i in tree:
        printtree(tree, i, height + 1)

def replacetransform(parent, tree):
    if parent is not None and parent.tag == tree.tag and tree.tag == "Transform":
        parent.extend(tree.getchildren())
        parent.remove(tree)
        parent.attrib['translation'] = '0.000000 0.000000 0.000000'
        parent.attrib['scale'] = '%s %s %s' % (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
        parent.attrib['rotation'] = '1.000000 0.000000 0.000000 0.000000'
    else:
        for i in tree:
            replacetransform(tree, i)

a = e.getroot()
#printtree(None, a, 0)
replacetransform(None, a)
#printtree(None, a, 0)
e.write(sys.argv[1])
