#include <iostream>


int main(int argc, char* argv[]) {

    int i = 0;
    int arg = atoi(argv[1]);
    //std::cout << argc << std::endl;
    for (i = 1 ; i <= arg; i++ ) {
        std::cout << argv[2] << std::endl;
    }
    return 0;

}