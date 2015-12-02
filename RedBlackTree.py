# -*- coding: utf-8 -*-
__author__ = 'jaundice'

class Tree(object):
    def __init__(self):
        self.nil=TreeNode()
        self.root=self.nil

class TreeNode(object):
    # 默认的就是红黑树的nil节点
    def __init__(self,data=0,left=None,right=None,color="b"):
        self.data=data
        self.left=left
        self.right=right
        self.color=color
        self.parent=None

def RB_insert(T,z):
    y=T.nil
    x=T.root
    while x!=T.nil:
        y=x
        if z.data<y.data:
            x=x.left
        else:
            x=x.right
    z.parent=y
    if y.data>z.data:
        y.left=z
    else:
        y.right=z
    z.color="r"
    z.left=T.nil
    z.right=T.nil
    dict[z]=0
    RB_insert_fixup(T,z)
    # mid_Order(T) # 调用二叉树的中序遍及来打印红黑树
    post_Order(T) # 中序和后序可以确定一棵红黑树

def mid_Order(T):
   ss=[]
   ss.append(T.root)
   while len(ss)!=0:
       dict[ss[-1]]+=1
       if dict[ss[-1]]==2:
           print(str(ss[-1].data)+"===>"+ss[-1].color)
           temp=ss[-1]
           ss.pop(-1)
           if temp.right!=T.nil:
               ss.append(temp.right)
       elif dict[ss[-1]]==1:
            if ss[-1].left!=T.nil:
                ss.append(ss[-1].left)

def post_Order(T):
    ss=[]
    ss.append(T.root)
    while len(ss)!=0:
        temp=ss[-1]
        dict[temp]+=1
        if dict[temp]==3:
            print (str(temp.data)+"=====>"+temp.color)
            ss.pop(-1)
        elif dict[temp]==1:
            if temp.left!=T.nil:
                ss.append(temp.left)
        elif dict[temp]==2:
            if temp.right!=T.nil:
                ss.append(temp.right)

def right_rotate(T,node):
    if node!=T.root:
        temp=node.left
        if node.parent.left==node:
            node.parent.left=temp
        else:
            node.parent.right=temp

        temp.parent=node.parent
        node.parent=temp
        node.left=temp.right
        node.left.parent=node
        temp.right=node
    else:
        T.root=node.left
        node.left=T.root.right
        T.root.right.parent=node
        T.root.right=node

def left_rotate(T,node):
    temp=node.right
    if node.parent.right==node:
        node.parent.right=temp
    else:
        node.parent.left=temp

    temp.parent=node.parent
    node.parent=temp
    node.right=temp.left
    node.right.parent=node
    temp.left=node

def RB_insert_fixup(T,z):
    while z.parent.color=="r":
        if z.parent==z.parent.parent.left:
            y=z.parent.parent.right
            if y.color=="r":
                z.parent.parent.color="r"
                z.parent.color="b"
                y.color="b"
                z=y.parent
            else:
                if z==z.parent.right:
                    z=z.parent
                    left_rotate(T,z)
                z.parent.color="b"
                z.parent.parent.color="r"
                right_rotate(T,z.parent.parent)
        else:
            y=z.parent.parent.left
            if y.color=="r":
                z.parent.parent.color="r"
                z.parent.color="b"
                y.color="b"
                z=y.parent
            else:
                if z==z.parent.left:
                    z=z.parent
                    right_rotate(T,z)
                z.parent.color="b"
                z.parent.parent.color="r"
                left_rotate(T,z.parent.parent)

tree=Tree()
n8=TreeNode(8,tree.nil,tree.nil,"r")
n7=TreeNode(5,tree.nil,tree.nil,"r")
n6=TreeNode(15,tree.nil,tree.nil,"r")
n5=TreeNode(7,n7,n8)
n4=TreeNode(1,tree.nil,tree.nil)
n3=TreeNode(14,tree.nil,n6,"b")
n2=TreeNode(2,n4,n5,"r")
n1=TreeNode(11,n2,n3,"b")

n2.parent=n1
n3.parent=n1
n4.parent=n2
n5.parent=n2
n6.parent=n3
n7.parent=n5
n8.parent=n5

dict={}
for i in range (1,9):
    dict[eval("n"+str(i))]=0

z=TreeNode(4)
tree.root=n1
RB_insert(tree,z)
# left_rotate(tree,n2)
# mid_Order(tree)
# post_Order(tree)
