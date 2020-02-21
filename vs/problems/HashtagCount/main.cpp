#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <queue>
#include <list>
#include "utils.h"

using namespace std;

struct hashtag_t {
    string hashtag;
    int count;

    friend ostream&
    operator<<(ostream& os, const hashtag_t& h) {
        os << "<" << h.hashtag << " " << h.count << ">";
        return os;
    }
};

struct cpm_hashtag_t {
    bool
    operator() (hashtag_t* lhs, hashtag_t* rhs) {
        return lhs->count > rhs->count;
    }
};

vector<hashtag_t*>
read_file(const string& path) {
    vector<hashtag_t*> ans;
    ifstream           infile(path);
    string             hashtag;
    int                count;

    while (infile >> hashtag >> count) {
        ans.push_back(new hashtag_t({ hashtag, count }));
    }
    return move(ans);
}

vector<hashtag_t>
top_k_hashtags_v1(vector<hashtag_t*> const& hashtags_count, size_t k) {
    vector<hashtag_t>  ans;
    vector<hashtag_t*> tmp = hashtags_count;

    sort(tmp.begin(), tmp.end(), cpm_hashtag_t());
    for (size_t i = 0; i < k; i++)
        ans.push_back(*tmp[i]);
    return move(ans);
}

vector<hashtag_t>
top_k_hashtags_v2(vector<hashtag_t*> const& hashtags_count, size_t k) {        
    priority_queue<hashtag_t*, vector<hashtag_t*>, cpm_hashtag_t> pq;
    vector<hashtag_t> ans;

    for (hashtag_t* item : hashtags_count) {
        pq.push(item);
        if (pq.size() > k)
            pq.pop();
    }

    while (!pq.empty()) {
        ans.push_back(*pq.top()); pq.pop();
    }
    reverse(ans.begin(), ans.end());

    return move(ans);
}

vector<hashtag_t>
top_k_hashtags_v3(vector<hashtag_t*> const& hashtags_count, size_t k) {
    vector<vector<hashtag_t*>> buckets(10000 + 1);
    vector<hashtag_t>          ans;

    for (hashtag_t* h : hashtags_count) {
        buckets[h->count].push_back(h);
    }

    for (int i = buckets.size() - 1; i >= 0 && k; i--) {
        for (int j = 0; j < (int) buckets[i].size() && k; j++, k--) {
            ans.push_back(*buckets[i][j]);
        }
    }

    return move(ans);
}

int main(int argc, char* argv[]) {
    vector<hashtag_t*> hashtags_count = read_file(R"(..\hashtags.txt)");
    double             elapsed        = 0;
    vector<hashtag_t>  top(6);

    {
        utils::timestamp_t ts;

        top = top_k_hashtags_v1(hashtags_count, 6);
        elapsed = ts.elapsed_msec();

        cout << "v1 [" << elapsed << " ms]" << endl;
        cout << "\t" << utils::join(top, "\n\t") << endl << endl;
    }

    {
        utils::timestamp_t ts;

        top = top_k_hashtags_v2(hashtags_count, 6);
        elapsed = ts.elapsed_msec();

        cout << "v2 [" << elapsed << " ms]" << endl;
        cout << "\t" << utils::join(top, "\n\t") << endl << endl;
    }

    {
        utils::timestamp_t ts;

        top = top_k_hashtags_v3(hashtags_count, 6);
        elapsed = ts.elapsed_msec();

        cout << "v3 [" << elapsed << " ms]" << endl;
        cout << "\t" << utils::join(top, "\n\t") << endl << endl;
    }

    for (auto item : hashtags_count) {
        delete item;
    }

    return 0;
}