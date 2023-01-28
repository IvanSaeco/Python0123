class Catalogo:

    #Atributos
    productos = []  # Lista que contiene a los objetos de tipo Catalogo

    #Metodos
    def __init__(self, productos=[]): # Constructor de clase Catalogo
        self.productos = productos

    def agregar(self, p):  # p será un objeto Producto
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)  # Print toma por defecto str(p)

class Producto:
    
    #Atributos
        #No se especifico

    #Metodos
    def __init__(self, nombreProducto, precio, nombreProovedor): # Constructor de clase Producto
        self.nombreProducto = nombreProducto
        self.precio = precio
        self.nombreProovedor = nombreProovedor
        print('Se ha creado el producto:', self.nombreProducto)

    def __str__(self): 
        return '{} (S/{}) by {}'.format(self.nombreProducto, self.precio, self.nombreProovedor) 