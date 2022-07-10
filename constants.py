BODY = '''
#include <iostream>

char memory[1024];
int cursor = 0;

#define ADD_CURSOR() { if(!addcursor()){std::cout<<"Cannot add cursor"<<std::endl;return -1;} }
#define SUBTRACT_CURSOR() { if(!subtractcursor()){std::cout<<"Cannot subtract cursor"<<std::endl;return -1;} }

bool addcursor(){if(cursor+1<1024){cursor++;return true;}else{return false;}}
bool subtractcursor(){if(cursor-1>=0){cursor--;return true;}else{return false;}}

int main()
{
'''
