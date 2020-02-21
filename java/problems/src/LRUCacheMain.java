import java.util.LinkedHashMap;
import java.util.Map;

public class LRUCacheMain {
    public static class LRUCache extends LinkedHashMap<Integer, Integer> {
        private int capacity;

        public LRUCache(int capacity) {
            super(capacity, 0.75f, true);
            this.capacity = capacity;
        }

        public int get(int key) {
            Integer v = super.get(key);
            return v == null ? -1 : v;
        }

        public void put(int key, int value) {
            super.put(key, value);
        }

        @Override
        protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
            return this.size() > capacity;
        }
    }

    public static void main(String[] args) {
        LRUCache cache = new LRUCache( 2 /* capacity */ );

        cache.put(1, 1);
        cache.put(2, 2);
        assert(cache.get(1) == 1);     // returns 1

        cache.put(3, 3);               // evicts key 2
        assert(cache.get(2) == -1);    // returns -1 (not found)

        cache.put(4, 4);               // evicts key 1
        assert(cache.get(1) == -1);    // returns -1 (not found)

        assert(cache.get(3) == 3);     // returns 3
        assert(cache.get(4) == 4);     // returns 4
    }
}
