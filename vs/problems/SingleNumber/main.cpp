#include <iostream>
#include <vector>
#include <unordered_map>
#include "utils.h"

using namespace std;

int
find_single_number_v1(vector<int>& nums) {
    for (size_t i = 0; i < nums.size(); ++i) {
        bool is_unique = true;

        for (size_t j = 0; j < nums.size(); ++j) {
            if (i != j && nums[i] == nums[j]) {
                is_unique = false;
                break;
            }
        }

        if (is_unique) {
            return nums[i];
        }
    }
    return 0;
}

int
find_single_number_v2(vector<int>& nums) {
    unordered_map<int, int> count;

    for (auto n : nums) {
        count[n]++;
    }
    for (const auto& item : count) {
        if (item.second == 1) {
            return item.first;
        }
    }
    return 0;
}

int
find_single_number_v3(vector<int>& nums) {
    int x = 0;

    for (auto n : nums) {
        x ^= n;
    }
    return x;
}

// 0 0 - 0
// 0 1 - 1
// 1 0 - 1
// 1 1 - 0

int main(int argc, char* argv[]) {
    constexpr int   large_size = 10000;
    int             ret = 0;
    double          elapsed = 0;
    vector<int>     small_input = { 2,2,1,1,3,5,3 };
    vector<int>     large_input;

    cout << "v1 = " << find_single_number_v1(small_input) << endl;
    cout << "v2 = " << find_single_number_v2(small_input) << endl;
    cout << "v3 = " << find_single_number_v3(small_input) << endl;

    large_input.resize(large_size + 1);
    for (size_t i = 0; i < large_size/2; i++) {
        large_input[i] = i;
        large_input[large_size - i - 1] = i;
    }
    large_input[large_size] = large_size + 1;

    {
        utils::timestamp_t ts;

        ret = find_single_number_v1(large_input);
        elapsed = ts.elapsed_msec();
    }
    cout << "v1 = " << ret << " [" << elapsed << " ms]" << endl;

    {
        utils::timestamp_t ts;

        ret = find_single_number_v2(large_input);
        elapsed = ts.elapsed_msec();
    }
    cout << "v2 = " << ret << " [" << elapsed << " ms]" << endl;

    {
        utils::timestamp_t ts;

        ret = find_single_number_v3(large_input);
        elapsed = ts.elapsed_msec();
    }
    cout << "v3 = " << ret << " [" << elapsed << " ms]" << endl;

    return EXIT_SUCCESS;
}