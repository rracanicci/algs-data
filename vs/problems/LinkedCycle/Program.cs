using System;

namespace LinkedCycle {
    public class ListNode {
        public int Value { get; set; }
        public ListNode Next { get; set; }

        public ListNode(int v, ListNode n) {
            Value = v;
            Next = n;
        }

        public ListNode(int v) : this(v, null) { }

        public bool HasCycle() {
            ListNode slow = this, fast = this;

            while (fast != null && fast.Next != null) {
                slow = slow.Next;
                fast = fast.Next.Next;
                if (slow == fast) return true;
            }
            return false;
        }
    }

    class Program {
        static void Main(string[] args) {
            ListNode node, head = new ListNode(
                1,
                new ListNode(
                    2,
                    new ListNode(
                        3,
                        (node = new ListNode(
                            4,
                            new ListNode(5)
                        ))
                    )
                )
            );

            // 1 - 2 - 3 - 4 - 5

            Console.WriteLine(head.HasCycle());
            node.Next = head;
            Console.WriteLine(head.HasCycle());
        }
    }
}
