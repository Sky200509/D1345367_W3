a = int(input("輸入系數 a :"))
b = int(input("輸入系數 b :"))
c = int(input("輸入系數 c :"))
x1 = (-1*b + (b**2 - 4*a*c)**0.5)/2*a
x2 = (-1*b - (b**2 - 4*a*c)**0.5)/2*a
print("方程式的根為:x1 = ",round(x1,1),", x2 = ",round(x2,1))