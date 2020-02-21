#include <iostream>
#include <vector>
#include <string_view>
#include "utils.h"

using namespace std;

class purchase_t {
private:
    double _price;
    string _description;

public:
    purchase_t(string_view description, double price)
        : _description(description)
        , _price(price) {}

    inline const string&
    get_description() const {
        return _description;
    }

    inline double
    get_price() const {
        return _price;
    }

    friend ostream&
    operator<<(ostream& os, const purchase_t& p) {
        os << "<" << p.get_description() << " - R$" << p.get_price() << ">";
        return os;
    }
};

void
prioritize_urgent(vector<purchase_t>& purchases, double price_cap) {
    int last = 0;

    for (size_t i = 0; i < purchases.size(); ++i) {
        if (purchases[i].get_price() >= price_cap) {
            swap(purchases[i], purchases[last]);
            last++;
        }
    }
}

int main(int argc, char* argv[]) {
    vector<purchase_t> purchases = {
        purchase_t("Mug", 10), purchase_t("Car", 20000),
        purchase_t("Pen", 3), purchase_t("Notebook", 5000),
        purchase_t("PS4", 1200),
    };

    cout<< "original\n\t" << utils::join(purchases, "\n\t") << endl;
    prioritize_urgent(purchases, 1000);
    cout << "with priorioty\n\t" << utils::join(purchases, "\n\t") << endl;

    return EXIT_SUCCESS;
}