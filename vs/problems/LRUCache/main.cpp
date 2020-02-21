#include <iostream>
#include <list>
#include <unordered_map>
#include <assert.h>

using namespace std;

class lru_cache_t {
private:
    struct cache_data_t {
        int key;
        int value;
    };

    size_t _capacity;
    list<cache_data_t> _accesses;
    unordered_map<int, list<cache_data_t>::iterator> _cache;

public:
    lru_cache_t(size_t capacity) : _capacity(capacity) {}

    int get(int key) {
        auto found = _cache.find(key);

        if (found != _cache.end()) {
            int val = found->second->value;
            put(key, val);
            return val;
        }
        return -1;
    }

    void put(int key, int value) {
        auto found = _cache.find(key);

        if (found != _cache.end()) {
            _accesses.erase(found->second);
        }
        else if (_accesses.size() >= _capacity) {
            _cache.erase(_accesses.back().key);
            _accesses.pop_back();
        }
        _accesses.push_front({ key, value });
        _cache[key] = _accesses.begin();
    }
};

int main(int argc, char* argv[]) {
    lru_cache_t cache(2);

    cache.put(1, 1);
    cache.put(2, 2);
    assert(cache.get(1) == 1);     // returns 1

    cache.put(3, 3);               // evicts key 2
    assert(cache.get(2) == -1);    // returns -1 (not found)

    cache.put(4, 4);               // evicts key 1
    assert(cache.get(1) == -1);    // returns -1 (not found)

    assert(cache.get(3) == 3);     // returns 3
    assert(cache.get(4) == 4);     // returns 4

    return EXIT_SUCCESS;
}