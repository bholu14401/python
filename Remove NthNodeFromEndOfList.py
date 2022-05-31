class Solution:
    
    def removeNthFromEnd(self, head, n):

        p=q=head
        for _ in range(n):
            q=q.next
            
        if not q:
            return head.next
        
        while q.next:
            p=p.next
            q=q.next
        p.next=p.next.next
        return head
