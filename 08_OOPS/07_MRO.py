class A:
    label ="A: Base Class";
class B(A):
    label ="B: B Class"
    marco = True

class C(A):
    lable = "C :Class C";

class D(B,C):
    pass;

cup = D()

print(D.marco)