import sys
from   collections       import OrderedDict
from   utils.ui.lrucache import run

class LRUCache(OrderedDict):
    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
        self.__getitem__(key)

def main():
    return run (LRUCache(int(sys.argv[1])))

if __name__ == '__main__': sys.exit(main())