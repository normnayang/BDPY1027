import lab27_useModule
import lab27_useModule as l27
from lab27_useModule import foo,bar
from lab27_useModule import foo as f , bar as b

print(lab27_useModule.foo(5, 6))
print(lab27_useModule.bar(7, 8))
print(l27.foo(9, 10))
print(l27.bar(11, 12))
print(foo(13, 14),bar(15,16))
print(f(17,18),b(19,20))