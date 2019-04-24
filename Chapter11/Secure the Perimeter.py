def trianglePerimeter(xA, yA, xB, yB, xC, yC):
   a = distance2D(xA, yA, xB, yB)
   b = distance2D(xA, yA, xC, yC)
   c = distance2D(xB, yB, xC, yC)
   perimeter = a+b+c
   return(perimeter)
