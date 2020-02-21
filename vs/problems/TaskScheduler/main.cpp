#include <iostream>
#include <queue>
#include <unordered_map>
#include "utils.h"

using namespace std;

struct task_t {
    int frequency;
    string name;
};

vector<string>
schedule_tasks(vector<string> const& tasks, int cooldown) {
    // max heap
    auto cmp_task = [] (const task_t& lhs, const task_t& rhs) {
        return lhs.frequency < rhs.frequency;
    };
    priority_queue<task_t, vector<task_t>, decltype(cmp_task)> pq(cmp_task);
    // count the number of each task
    unordered_map<string, int> count;
    // answer with scheduled tasks
    vector<string> ans;

    // count all tasks by name
    for (auto t : tasks) count[t]++;
    // insert the tasks in the priority queue
    for (auto t : count) pq.push({ t.second, t.first });

    while (!pq.empty()) {
        vector<task_t> cache;

        for (int i = 0; i <= cooldown; i++) {
            if (!pq.empty()) {
                auto task = pq.top(); pq.pop();

                if (task.frequency > 1) {
                    task.frequency--;
                    cache.push_back(task);
                }
                ans.push_back(task.name);
            }
            else {
                ans.push_back("idle");
            }
            if (pq.empty() && cache.empty()) break;
        }
        for (auto f : cache) pq.push(f);
    }
    return move(ans);
}

int main(int argc, char* argv[]) {
    auto ans = schedule_tasks({
        "A","A","A","B","B","B","C"
    }, 3);

    cout << utils::join(ans, ", ") << endl;
    return EXIT_SUCCESS;
}