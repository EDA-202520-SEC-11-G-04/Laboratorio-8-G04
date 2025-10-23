from DataStructures.Tree import rbt_node as node
RED=0
BLACK=1
def new_map():
    return {"root":None,"tipo":"RBT"}

def put(my_rbt, key, value):
    return 0

def insert_node(root, key, value):
    return 0

def rotate_left(node_rbt):
    new_root = node["right"]  
    node["right"] = new_root["left"]     
    new_root["left"] = node           
    return new_root
    
def rotate_right(node_rbt):
    new_root = node["left"]  
    node["left"] = new_root["right"]     
    new_root["right"] = node           
    return new_root

def flip_node_color(node_rbt):
    if node_rbt is not None :
        if node.is_red(node_rbt):
            node_rbt["color"]=BLACK
        else:
            node_rbt["color"]=RED
    return node_rbt

def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    if node_rbt is not None :
        left=node_rbt["left"]
        right=node_rbt["right"]
        flip_node_color(left)
        flip_node_color(right)
    return node_rbt
    
    
    return node_rbt

def is_red(node_rbt):
    return node.is_red(node_rbt)

def size (my_rbt):
    return size_tree(my_rbt["root"])

def size_tree(root):
    if root is None:
        return 0
    return root["size"]    