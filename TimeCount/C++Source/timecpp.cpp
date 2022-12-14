#include <bits/stdc++.h>

using namespace std;

int main(int argc, char **argv){
	if(argc > 2){
		printf("Too many arguments.");
		return -1;
	}else if(argc < 2){
		printf("Please enter file.exe");
		return -1;
	}
	auto startTime = chrono::system_clock::now();
	try{
		system(argv[1]);
	}catch(exception &e){
		printf("%s", e.what());
		return 0;
	}
	auto endTime = chrono::system_clock::now();
	chrono::duration<double> timeRunning = endTime - startTime;
	printf("Finished running at %lfs", timeRunning.count());

	return 0;
}