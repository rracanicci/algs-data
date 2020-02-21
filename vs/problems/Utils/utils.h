#include <windows.h>
#include <iostream>
#include <vector>
#include <sstream>

namespace utils {
    class timestamp_t {
    private:
        LARGE_INTEGER _begin, _end, _freq;

    public:
        timestamp_t(void)
            : _begin({ 0, 0 })
            , _end({ 0, 0 }) { QueryPerformanceFrequency(&_freq); now(); }

        virtual
        ~timestamp_t(void) {}

        __forceinline void
        now(void) { QueryPerformanceCounter(&_begin); }

        __forceinline double
        elapsed_msec(void) {
            QueryPerformanceCounter(&_end);
            return ((double) ((_end.QuadPart - _begin.QuadPart) * 1000)) /
                        _freq.QuadPart;
        }
    };

    template<typename container_t>
    __forceinline std::string
    join(container_t const& c, std::string const& sep = " ") {
        std::ostringstream oss;

        if (c.empty()) return "";
        for (size_t i = 0; i < c.size() - 1; i++) {
            oss << c[i] << sep;
        }
        oss << c.back();
        return oss.str();
    }
}