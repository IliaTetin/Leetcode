class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in lists:
            cur = i
            while cur:
                heapq.heappush(heap, cur.val)
                cur = cur.next
        if not heap:
            return None
        
        head = ListNode(heapq.heappop(heap))
        cur = head

        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return head
        