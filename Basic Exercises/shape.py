shape = input("Shape: ")
if(shape == "Quadrangle"):
    side_1,side_2,side_3,side_4 = input("Enter side lengths: ").split()
    side_1 = float(side_1)
    side_2 = float(side_2)
    side_3 = float(side_3)
    side_4 = float(side_4)
    if side_1 == side_2 and side_2 == side_3 and side_3 == side_4:
        print("Shape is square.")
    elif side_1 == side_2 and side_3 == side_4:
        print("Shape is rectangle.")
    else:
        print("Shape is quadrangle.")
elif shape == "Triangle":
    side_1,side_2,side_3 = input("Enter sides of triangle: ").split()
    side_1 = float(side_1)
    side_2 = float(side_2)
    side_3 = float(side_3)
    if (abs(side_1 - side_2) < side_3 and side_1 + side_2 > side_3) and (abs(side_1 - side_3) < side_2 and side_1 + side_3 > side_2) and (abs(side_3 - side_2) < side_1 and side_3 + side_2 > side_1):
        if side_1 == side_2 and side_2 == side_3:
            print("Equilateral triangle.")
        elif(side_1 == side_2 or side_1 == side_3 or side_2 == side_3):
            print("Isosceles triangle")
        else:
            print("Scalene triangle.") 
    else:
        print("Entered shape is not a triangle.") 
else:
    print("Uncorrect Shape")