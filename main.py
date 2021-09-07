import ctypes  
math1 = ctypes.CDLL("./math1.so")  
print(math1.f1())
print("***finish***") 
