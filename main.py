class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# class lianbiao:
#     def __init__(self):
#         self.head=Node(None)
#     def chuanzao(self):
#         cNode=self.head
#         ele=input("请输入数据")
#         while ele!='#':
#             nNode=Node(int(ele))
#             cNode.next=nNode
#             cNode=nNode
#             ele=input("请输入数据")
#
#     def bianli(self):
#         cNode=self.head
#         while cNode.next!=None:
#             cNode=cNode.next
#             print(cNode.data,end='->')
#         print(None)
#     def changdu(self):
#         cNode=self.head
#         p=0
#         while cNode.next!=None:
#             p+=1
#             cNode=cNode.next
#         return p
#
#     def kong(self):
#         if self.changdu()==0:
#             print("链表为空")
#         else:
#             print(f"链表的长度为{self.changdu()}")
#     def weiduan(self):
#         z=int(input("请输入要在尾端插入元素的次数"))
#         cNode=self.head
#         for i in range(z):
#             k=input("请输入数据")
#             nNode=Node(int(k))
#             while cNode.next!=None:
#                 cNode=cNode.next
#             cNode.next=nNode
#             cNode=nNode
#         self.bianli()
#         self.kong()
#
#     def shouduan(self):
#         x=int(input("请输入首段插入的次数"))
#         for i in range(x):
#             cNode=self.head
#             ele=input("请输入数据")
#             nNode=Node(int(ele))
#             nNode.next=cNode.next
#             cNode.next=nNode
#         self.bianli()
#         self.kong()
#     def weizhi(self):
#         cNode=self.head
#         p=0
#         ele=int(input("请输入要查找的元素"))
#         while cNode.next!=None and cNode.data!=ele:
#             p+=1
#             cNode=cNode.next
#         if cNode.data==ele:
#             print(f"数据在{p}位置")
#     def shanchu(self):
#         ele = int(input("请输入要删除的值"))
#         prev = self.head  # prev始终指向当前节点的前一个节点
#         cNode = self.head.next  # 从头节点的下一个节点开始遍历
#
#         # 查找要删除的节点的前一个节点
#         while cNode.data != ele:
#             prev = prev.next
#             cNode = cNode.next
#
#             # 如果找到了要删除的节点
#         if cNode:
#             prev.next = cNode.next  # 跳过要删除的节点
#
#         self.bianli()  # 遍历链表以查看删除效果
#     def charu(self):
#         x=int(input("请输入要插入的次数"))
#         for i in range(x):
#             wei=int(input("请输入要插入的位置"))
#             ele=int(input("请输入数据"))
#             cNode=self.head
#             nNode=Node(ele)
#             u=0
#             while u!=wei-1:
#                 cNode=cNode.next
#                 u+=1
#             nNode.next=cNode.next
#             cNode.next=nNode
#
#         self.bianli()

class xunhuandan:
    def __init__(self):
        self.head=Node(None)
    def chuanjian(self):
        ele=input("请输入数据")
        cNode=self.head
        while ele!="#":

            nNode=Node(int(ele))
            cNode.next=nNode
            cNode=nNode
            cNode.next=self.head
            ele=input("请输入数据")
    def bianli(self):
        cNode=self.head
        while cNode.next!=self.head:
            cNode=cNode.next
            print(cNode.data,end="->")
        print("None")
    def weiduan(self):
        x=int(input("请输入要插入的次数"))
        for i in range(x):
            ele=input("请输入数据")
            nNode=Node(int(ele))
            cNode=self.head
            while cNode.next!=self.head:
                cNode=cNode.next
            cNode.next=nNode
            nNode.next=self.head
        self.bianli()

    def shouduan(self):
        x=int(input("请输入要插入的次数"))
        for i in range(x):
            ele=int(input("请输入数据"))
            cNode=self.head
            nNode=Node(ele)
            nNode.next=cNode.next
            cNode.next=nNode
        self.bianli()

    def shanchu(self):
        x=int(input("请输入删除次数"))
        for i in range(x):
            cNode=self.head
            ele=int(input("请输入数据"))

        self.bianli()

# lian=lianbiao()
# lian.chuanzao()
# lian.bianli()
#
# lian.kong()
# lian.weiduan()
# lian.shouduan()
# lian.weizhi()
# lian.shanchu()
# lian.charu()


xun=xunhuandan()
xun.chuanjian()

xun.bianli()
xun.weiduan()
xun.shouduan()
xun.shanchu()