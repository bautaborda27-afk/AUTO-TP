class Auto:
    def __init__(self, marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.habilitados = []
        self.nohabilitados = []
    def crear_conductor (self, nombre, edad, habilitado):
        conductor = {
        "nombre":nombre,
        "edad":edad,
        "habilitado": habilitado
        }
        if conductor["habilitado"].lower() == "si":
            self.habilitados.append(conductor)
        else:
            self.nohabilitados.append(conductor)
    def get_info_auto(self):
        print(" - Marca: ", self.marca)
        print(" - Modelo: ", self.modelo)
        print(" - Año: ", self.ano)
    def get_conductores (self):
        print("Conductores Habilitados: ", self.habilitados)
        
    


    
        
    