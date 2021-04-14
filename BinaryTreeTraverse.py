'''
二叉树的遍历(非递归，迭代方式)：前序、中序、后序, 最开始都压入根节点
前序每次循环均弹出
中序、后序关键在于什么时候可以把一个点弹出：栈顶部的点满足条件，则弹出，不满足条件，先拿出来，再按相应顺序压栈
1.剪枝：将左右孩子压入栈时，将该点的左右分支剪掉，判断弹出的条件是：左右孩子为空；
2.维护状态变量：第一次压入某节点，置false，第二次压该节点，置true，弹出的条件是状态变量为true。
'''
#递归遍历需注意：1.为空，返回值 2.定义遍历函数 3.在主函数中调用
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def InOrderTraverse(root):
    if not root:  # 处理空情况
        return []
    '''
    #剪枝
    ans = []
    stack = []
    stack.append(root)
    while (stack):
        tmp = stack[-1]
        stack.pop()
        if not tmp.left and not tmp.right:
            ans.append(tmp.val)
        else:
            if tmp.right:
                stack.append(tmp.right)
            stack.append(tmp)
            if tmp.left:
                stack.append(tmp.left)
            tmp.left = None
            tmp.right = None
    '''
    #状态变量
    ans = []
    stack = []
    stack.append((root, False))
    while (stack):
        tmp = stack[-1]
        stack.pop()
        if tmp[1]:
            ans.append(tmp[0].val)
        else:
            if tmp[0].right:
                stack.append((tmp[0].right, False))
            stack.append((tmp[0], True))
            if tmp[0].left:
                stack.append((tmp[0].left, False))

    return ans

def PreOrderTraverse(root):
    if not root: #处理空情况
        return []

    ans = []
    stack = []
    stack.append(root)
    while (stack):
        tmp = stack[-1]
        ans.append(tmp.val)
        stack.pop()
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)
    return ans

def PostOrderTraverse(root):
    if not root: #处理空情况
        return []
    '''
    #剪枝
    ans = []
    stack = []
    stack.append(root)
    while(stack):
        tmp = stack[-1]
        stack.pop()
        if not tmp.right and not tmp.left:
            ans.append(tmp.val)
        else:
            stack.append(tmp)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
            tmp.left = None
            tmp.right = None
    '''
    #状态变量
    ans = []
    stack = []
    stack.append((root, False))
    while (stack):
        tmp = stack.pop()
        if tmp[1]:
            ans.append(tmp[0].val)
        else:
            stack.append((tmp[0], True))
            if tmp[0].right:
                stack.append((tmp[0].right, False))
            if tmp[0].left:
                stack.append((tmp[0].left, False))
    return ans

if __name__ == '__main__':
    print('BinaryTreeTraverse')