import sys
from   collections import Counter
from   queue       import PriorityQueue

class MaxPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)

    def put(self, priority, data):
        PriorityQueue.put(self, (-priority, data), block=False)

    def get(self):
        priority, data = PriorityQueue.get(self, block=False)
        return -priority, data

def schedule_tasks(tasks: list, cooldown: int) -> int:
    ans = []
    pq = MaxPriorityQueue()
    for task, count in Counter(tasks).items():
        pq.put(count, task)

    while not pq.empty():
        cache = []
        for _ in range(cooldown + 1):
            if not pq.empty():
                freq, task = pq.get()
                if freq > 1:
                    cache.append((freq - 1, task))
                ans.append(task)
            else:
                ans.append('idle')
            if (pq.empty() and not cache):
                break
        for freq, task in cache:
            pq.put(freq, task)
    return ans

def main():
    print(schedule_tasks(["A","A","A","B","B","B","C"], 3))
    return 0

if __name__ == '__main__': sys.exit(main())


