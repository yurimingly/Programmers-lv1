#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    string week[7] = { "THU","FRI","SAT","SUN","MON","TUE","WED" };
    int m[12] = { 31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31 };
    int temp;

    for (int i = 0; i < a - 1; i++) {
        temp += m[i];
    }

    temp += b;

    answer = week[temp % 7];


    return answer;
}

int main() {

    solution(2,1);

    return 0;
}