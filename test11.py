from typing import List, Optional
#from pythonds import PriorityQueue
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        dummy = ListNode(0)
        curr_node = dummy
        for listnode in lists:
            if listnode:
                heapq.heappush(pq , (listnode.val, id(listnode), listnode))
        while pq:
            _, _ , min_node = heapq.heappop(pq)
            curr_node.next = min_node
            curr_node = curr_node.next
            if min_node.next:
                heapq.heappush(pq, (min_node.next.val, id(min_node.next), min_node.next))
        return dummy.next

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         # 初始化一个优先队列
#         heap = []
#         for l in lists:
#             if l:
#                 # 将每个链表的头节点加入到堆中
#                 # 由于ListNode没有实现比较操作，我们用元组(val, index, ListNode)来存储
#                 heapq.heappush(heap, (l.val, id(l), l))
#
#         # 初始化一个哑节点作为合并后链表的头部
#         dummy = ListNode(0)
#         current = dummy
#
#         # 当堆不为空时循环
#         while heap:
#             # 弹出最小的节点
#             val, node_id, node = heapq.heappop(heap)
#             # 将该节点加入到结果链表
#             current.next = node
#             current = current.next
#             # 如果该节点的下一个节点存在，则加入到堆中
#             if node.next:
#                 heapq.heappush(heap, (node.next.val, id(node.next), node.next))
#
#         return dummy.next
