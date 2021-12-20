#ifndef INC_19_SCANNER_H
#define INC_19_SCANNER_H

#include <bits/stdc++.h>
#include "19.h"
#include "Point.h"

using namespace std;

class Scanner
{
public:
	vector<Point> signals;
	vector<double> distances;

	explicit Scanner(vector<Point> in)
	{
			this->signals = in;
			for (Point p: in) distances.push_back(distance(p, {0, 0, 0}));
	}

	bool operator==(Scanner a) const
	{
		return a.signals == this->signals;
	}
};

#endif //INC_19_SCANNER_H
