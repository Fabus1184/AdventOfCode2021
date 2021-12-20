#include <bits/stdc++.h>

using namespace std;

int main()
{
		int distinct = 0;

		auto start = std::chrono::high_resolution_clock::now();

		for (int x = 1; x < 222; x++) {
				for (int y = -122; y < 122; y++) {
						int pos[] = {0, 0};
						int vel[] = {x, y};

						for (int i = 0; i < 1000; i++) {
								//TEST: target area: x=20..30, y=-10..-5
								/*if (pos[0] <= 30 && pos[0] >= 20 && pos[1] >= -10 && pos[1] <= -5) {
										distinct++;
										break;
								}*/

								//target area: x=185..221, y=-122..-74
								if (pos[0] <= 221 && pos[0] >= 185 && pos[1] >= -122 && pos[1] <= -74) {
										distinct++;
										break;
								}

								if (pos[0] > 221 || pos[1] < -122) break;

								pos[0] += vel[0];
								pos[1] += vel[1];

								if (vel[0] > 0) {
										vel[0] -= 1;
								} else if (vel[0] < 0) {
										vel[0] += 1;
								}
								vel[1] -= 1;
						}
				}
		}

		auto stop = std::chrono::high_resolution_clock::now();
		auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

		cout << setprecision(2);
		cout << distinct << endl;
		cout << (float) duration.count() / 1000 << " ms" << endl;
}
