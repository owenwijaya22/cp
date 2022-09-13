#include <chrono>

/* Only needed for the sake of this example. */
#include <iostream>
#include <thread>

using namespace std;

void long_operation()
{
    int i;
    for (i = 0; i < 1000;i++){
        cout << "Count is at " << i <<endl;
    }

}

int main()
{
    using chrono::high_resolution_clock;
    using chrono::duration_cast;
    using chrono::duration;
    using chrono::milliseconds;

    auto t1 = high_resolution_clock::now();
    long_operation();
    auto t2 = high_resolution_clock::now();

    duration<double, std::milli> ms_double = t2 - t1;

    cout << ms_double.count() << "ms\n";
    std::string x;

    return 0;
}