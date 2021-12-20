#ifndef INC_19_POINT_H
#define INC_19_POINT_H

#include <bits/stdc++.h>

using namespace std;

class Point
{
public:
	int x, y, z;

	Point(int x, int y, int z)
	{
			this->x = x;
			this->y = y;
			this->z = z;
	}

	Point rotate(int r)
	{
			switch (r) {
					//-----------------------------------------------------------------------
					// x y z
					case 0:
							return *this;
					case 1:
							return Point{x, -y, -z};
					case 2:
							return Point{-y, -x, -z};
					case 3:
							return Point{-x, y, -z};
					case 4:
							return Point{y, x, -z};
					case 5:
							return Point{-y, x, z};
					case 6:
							return Point{-x, -y, z};
					case 7:
							return Point{y, -x, z};
							//----
					case 8:
							return Point{y, z, x};
					case 9:
							return Point{-z, y, x};
					case 10:
							return Point{-y, -z, x};
					case 11:
							return Point{z, -y, x};
					case 12:
							return Point{z, y, -x};
					case 13:
							return Point{-y, z, -x};
					case 14:
							return Point{-z, -y, -x};
					case 15:
							return Point{y, -z, -x};
							//----
					case 16:
							return Point{-x, z, y};
					case 17:
							return Point{-z, -x, y};
					case 18:
							return Point{x, -z, y};
					case 19:
							return Point{z, x, y};
					case 20:
							return Point{z, -x, -y};
					case 21:
							return Point{x, z, -y};
					case 22:
							return Point{-z, x, -y};
					case 23:
							return Point{-x, -z, -y};
			}
			return {0, 0, 0};
	}

	bool operator==(Point a) const
	{
			return (a.x == this->x && a.y == this->y && a.z == this->z);
	}

	bool operator!=(Point a) const
	{
			return !(a.x == this->x && a.y == this->y && a.z == this->z);
	}

	Point operator+(Point a) const
	{
			return Point{a.x + this->x, a.y + this->y, a.z + this->z};
	}

	Point operator-(Point a) const
	{
			return Point{this->x - a.x, this->y - a.y, this->z - a.z};
	}

};

double distance(Point a, Point b)
{
		return sqrt(pow((a.x - b.x), 2) + pow((a.y - b.y), 2) + pow((a.z - b.z), 2));
}

ostream &operator<<(ostream &os, const Point &p)
{
		os << "(x: " << p.x << ", y: " << p.y << ", z: " << p.z << ")";
		return os;
}

#endif //INC_19_POINT_H
