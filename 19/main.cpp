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

		vector<Point> tempmap = {};
		tempmap.reserve(map.size());
		for (Point p: map) {
				tempmap.push_back(p);
		}

		vector<Point> scanner_pos = {};

		for (int ss = 0; ss < scanners.size(); ss++) {
				cout << "\r" << ss << "/" << scanners.size() - 1;
				flush(cout);

				diff = {};
				for (Point p: tempmap) {
						diff.emplace_back(p);
				}
				tempmap = {};

				for (const Scanner &s: scanners) {
						//DIRECTION
						for (int r = 0; r < 24; r++) {
								//REFERENCE POINT IN diff
								for (Point ref: diff) {
										//REFERENCE POINT IN SIGNALS
										for (Point zero: s.signals) {
												Point v = ref - zero.rotate(r);

												int match = 0;
												for (Point p: s.signals) {
														Point tmp = p.rotate(r) + v;
														if (find(map.begin(), map.end(), tmp) != map.end()) {
																match++;
														}
												}

												if (match >= 12) {
														scanner_pos.emplace_back(v);
														for (Point p: s.signals) {
																Point tmp = p.rotate(r) + v;
																if (find(map.begin(), map.end(), tmp) == map.end()) {
																		map.emplace_back(tmp);
																		tempmap.emplace_back(tmp);
																}
														}
												}
										}
								}
						}
				}
		}
		cout << endl << "Number of Scanners: " << map.size() << endl;

		int distance = 0;
		for (pair<Point, Point> pair: combinations(scanner_pos, scanner_pos)) {
				int d = abs(pair.first.x - pair.second.x) + abs(pair.first.y - pair.second.y) +
						abs(pair.first.z - pair.second.z);

				if (d > distance) {
						distance = d;
				}

		}
		cout << "Max Manhattan distance: " << distance << endl;

		return 0;
}
