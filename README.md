# 🔺Triangle Scenario – Week 05 Lab 05 (Python)

This project implements a `Triangle` class in Python to demonstrate core object-oriented programming (OOP) concepts including:

- Constructor flexibility (handling multiple input types)
- Object cloning
- Static methods
- Encapsulation using `@property`
- Geometric logic like perimeter calculation and right-angle detection

---

## 🛠 Features

- Single flexible constructor to handle:
  - Default triangle (all sides = 1.0)
  - Equilateral triangle
  - Isosceles triangle
  - Scalene triangle
  - Cloning from an existing triangle instance
- Static method `object_count()` to return number of Triangle objects created
- Instance methods:
  - `perimeter()` – returns the sum of all three sides
  - `is_right_angled()` – checks if the triangle is right-angled
  - `__str__()` – returns a human-readable string representation
- Encapsulation of side values using `@property` and setters with validation

---

## 📁 Files Structure

```bash
TriangleScenario/
├── main.py              
├── triangle.py         
├── UML_Diagram.png     
└── README.md            
