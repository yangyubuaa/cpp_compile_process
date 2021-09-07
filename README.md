### C++的编译和链接过程
---
##### 文件内容
main.cpp是程序执行入口
math1.cpp是程序执行调用的函数的实现文件
math1.h是math1的头文件，包含了math1中函数的定义

##### 编译过程
C++中每个文件可以分别进行编译和汇编过程，最终得到二进制文件，然后进行链接才可以执行，比如main.cpp可以单独执行编译过程，但是main.cpp中使用了math1.cpp的函数；math1.cpp也可以单独执行编译过程。编译完后我们通过链接生成可执行文件

##### 涉及命令
1. g++ -c xxx.cpp -o xxx.o	生成二进制文件
2. g++ xxx.o qqq.o sss.o -o a.out	生成可执行文件

##### 动态链接库和静态链接库
1. 动态链接库生成xxx.so文件，在程序运行时动态链接，如果要使用python调用，则生成so文件
2. 静态链接库生成xxx.a文件，在程序运行时静态链接

##### python调用c++动态链接库
1. 使用c++编写函数文件xxx.cpp（注意不要包含main函数）
2. 使用g++ -c xxx.cpp 生成xxx.o二进制文件
3. 使用g++ -fPIC -shared xxx.o -o xxx.so 生成动态链接库文件
4. 在python脚本中import ctypes; xxx = ctypes.CDLL("./xxx.so"); 通过xxx.func()调用即可
5. 注意c++编译完会更改函数名，如果第四步报错出现找不到函数，需要在函数前加上extern "C"再编译为动态链接库即可
