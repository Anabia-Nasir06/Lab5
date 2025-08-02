from Triangle import Triangle
print("-------------------------------------")
#Default Triangle
t1 = Triangle()
print("Default Triangle:", t1,"\n")

#One-parameter: Equilateral Triangle
t2 = Triangle(5.0, 5.0, 5.0)
print("Equilateral Triangle:", t2)
print("Perimeter:", t2.perimeter())
print("Is Right-Angled?", t2.isRightAngled(), "\n")


#Two-parameter: Isosceles Triangle
t3 = Triangle(4.0, 4.0, 6.0)
print("Isosceles Triangle:", t3)
print("Perimeter:", t3.perimeter())
print("Is Right-Angled?", t3.isRightAngled(), "\n")


#Three-parameter: Scalene Triangle
t4 = Triangle(3.0, 4.0, 5.0)
print("Scalene Triangle:", t4,)
print("Perimeter:", t4.perimeter())
print("Is Right-Angled?", t4.isRightAngled(),"\n")

#Clone Triangle
t5 = Triangle(clone_from=t4)
print("Cloned Triangle:", t5,"\n")

#Object Count
print("Total Triangle Objects Created:", Triangle.objectCount())
print("-------------------------------------")


