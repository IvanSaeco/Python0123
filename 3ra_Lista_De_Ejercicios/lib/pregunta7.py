class Producto:

    #Metodos
    def __init__(self, nombreProducto, codigo): # Constructor de clase Producto
        self.nombreProducto = nombreProducto
        self.codigo = codigo
        print('Se ha creado el producto2:', self.nombreProducto)

    def getPais(self):
        return self.codigo.split('-')[0]
    
    def getNroLote(self):
        return self.codigo.split('-')[1]
    
    def __str__(self): 
        return f'{self.nombreProducto} ({self.codigo}) es de {self.codigo.split("-")[0]} del lote {self.codigo.split("-")[1]}'