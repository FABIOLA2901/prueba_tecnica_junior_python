class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total (self):
        return self.precio * self.cantidad

    def __str__(self):
        return self.nombre
    #return f"({self.x}, {self.y})"
    

producto = Producto("Laptop",1500,2)
print(producto.calcular_total())
print(producto)

            
