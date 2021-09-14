print("Bienvenido@")
a=int(float(input("ingresa el primer numero    "))) # se utiliza esta sintaxis para convertir un decimal a entero
b=int(input("ingresa el segundo numero    "))
c=int(input("ingresa el tercer numero    "))
# lo que se captura con input son caracteres y no se puede hacer operaciones con ellos
if a >= b and a >=c:
    maximo=a
if b>=a and b>=c:
    maximo=b
if c >=a and c>=b:
    maximo=c

print("El maximo es :  ", maximo)
