#include <iostream>
using namespace std;

int w;

int main()
{
	std::cin >> w;
	if (w >= 1 && w <= 100 && w % 2 == 0 && w != 2)
	{
		std::cout << "YES\n";
	}
	else
	{
		std::cout << "NO\n";
	}
}