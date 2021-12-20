#include <iostream>
#include <vector>
#include <cmath>

#include "fuenfzehn.h"

using namespace std;

int ssmain()
{
		int n, k;
		vector<Edge> vec;

		//AUFGABE 2
		n = pow(500, 2);
		vec = a2(sqrt(n), input1);
		Graph g(vec, n);
		k = findShortestPath(g, 0, n - 1, n);

		cout << "Minimum path weight: " << k << endl;

		return 0;
}
