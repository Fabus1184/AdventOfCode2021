#include <bits/stdc++.h>

#include "19.h"

using namespace std;

int main()
{
		vector<Scanner> scanners = {};
		vector<Point> map = {};

		for (const vector<Point> &vs: mydata) {
				Scanner s = Scanner(vs);
				scanners.push_back(s);
		}

		for (Point p: scanners.at(0).signals) {
				map.emplace_back(p);
		}

		scanners = vector(scanners.begin() + 1, scanners.end());

		vector<Point> diff = {};

		diff.reserve(map.size());

		for (Point p: map) {
				diff.emplace_back(p);
		}

		for (int ss = 0; ss < scanners.size(); ss++) {
				cout << ss << "/" << scanners.size() << endl;
				for (const Scanner &s: scanners) {
						//DIRECTION
						for (int r = 0; r < 24; r++) {
								//REFERENCE POINT IN MAP
								for (Point ref: map) {
										//REFERENCE POINT IN SIGNALS
										for (Point zero: s.signals) {
												Point v = ref - zero.rotate(r);
												//cout << zero.rotate2d(r) << endl;
												//cout << v << endl;

												int match = 0;
												for (Point p: s.signals) {
														Point tmp = p.rotate(r) + v;
														//cout << "VORHER: " << p << " NACHER: " << tmp << endl;
														if (find(map.begin(), map.end(), tmp) != map.end()) {
																match++;
														}
												}

												//cout << match << endl << r << endl;
												//cout << match << endl;
												if (match >= 12) {
														//cout << match << " " << r << endl;
														for (Point p: s.signals) {
																Point tmp = p.rotate(r) + v;
																//cout << tmp << endl;
																if (find(map.begin(), map.end(), tmp) == map.end()) {
																		map.emplace_back(tmp);
																}
														}
												}
										}
								}
						}
				}
		}
		cout << map.size() << endl;
		cout << "ENDE LOOL" << endl;
		return 0;
}