class ZPT:
    # TODO TODO Refactorizacion and put it beautiful
    def __init__(self):
        self.dicta = {}
        self.values = {}

    def get_data(self):
        # TODO Get the data from a csv file
        self.a = [1, 2, 3]
        self.b = [4, 5, 9, 10]
        self.c = [6, 7, 8]

        #TODO autogenerate pairs
        #Creamos la coma para hacer el split
        self.dicta["A,B"], self.values["A,B"] = self.combinatoria(self.a, self.b)
        self.dicta["A,C"], self.values["A,C"] = self.combinatoria(self.a, self.c)
        self.dicta["B,C"], self.values["B,C"] = self.combinatoria(self.b, self.c)
        # TODO output into a file
        # TODO add in the output if the data should give an error or not


        fin = []
        while not self.check_all_combinations_finish():
            self.dict_resultado = {}
            for nombres_combinaciones in self.dicta:
                name1 = nombres_combinaciones.split(",")[0]
                name2 = nombres_combinaciones.split(",")[1]
                #Ahora hay dos opciones, que si este o que no.
                # Si no esta añadimos del tiro
                if name1 in self.dict_resultado:
                    index = nombres_combinaciones.split(",").index(name1)
                    self.check_pairs(nombres_combinaciones, index)
                elif name2 in self.dict_resultado:
                    index = nombres_combinaciones.split(",").index(name2)
                    self.check_pairs(nombres_combinaciones, index)
                elif not (name1 in self.dict_resultado and name2 in self.dict_resultado ):
                    self.first_pair(nombres_combinaciones)
            fin.append(self.dict_resultado)

        print(fin)
        # Log que nos cuenta lo que nos ahorramos de lineas respecto a las finales
        print("Nº Final Test Data: " + str(len(fin)) + " | All the combinatory are: " + str(len(self.a)*len(self.b)*len(self.c)))



    def check_all_combinations_finish(self):
        for values in self.values.values():
            if 0 in values.values():
                return False
        return True

    def first_pair(self, nombres_combinaciones):
        pareja_sin_valorar_str = None
        name1 = nombres_combinaciones.split(",")[0]
        name2 = nombres_combinaciones.split(",")[1]
        for pair in self.dicta[nombres_combinaciones]:
            if self.values[nombres_combinaciones][str(pair)] == 0:
                self.values[nombres_combinaciones][str(pair)] = self.values[nombres_combinaciones][str(pair)] + 1
                self.dict_resultado[name1] = pair[0]
                self.dict_resultado[name2] = pair[1]
                return
        # No hay ninguna pareja sin valor, por lo que las combinaciones primeras se han qeudado sin oportunidades
        pareja_sin_valorar_str = min(self.values[nombres_combinaciones], key=lambda k: self.values[nombres_combinaciones][k])
        pareja_sin_valorar_str = pareja_sin_valorar_str.replace("[", "").replace("]", "").split(",")
        pareja_sin_valorar = list(map(int, pareja_sin_valorar_str))

        self.values[nombres_combinaciones][str(pareja_sin_valorar)] = self.values[nombres_combinaciones][str(pareja_sin_valorar)] + 1
        self.dict_resultado[name1] = pareja_sin_valorar[0]
        self.dict_resultado[name2] = pareja_sin_valorar[1]

    def check_pairs(self, nombres_combinaciones, nombre_repetido_indice):
        pareja_sin_valorar = None
        name1 = nombres_combinaciones.split(",")[0]
        name2 = nombres_combinaciones.split(",")[1]
        for pair in self.dicta[nombres_combinaciones]:
            if pair[nombre_repetido_indice] == self.dict_resultado[nombres_combinaciones[nombre_repetido_indice]]:
                if (pareja_sin_valorar and self.values[nombres_combinaciones][str(pareja_sin_valorar)] > self.values[nombres_combinaciones][str(pair)]) or pareja_sin_valorar == None:
                    pareja_sin_valorar = pair
                    if self.values[nombres_combinaciones][str(pair)] == 0:
                        break

        self.values[nombres_combinaciones][str(pareja_sin_valorar)] = self.values[nombres_combinaciones][str(pareja_sin_valorar)] + 1
        self.dict_resultado[name1] = pareja_sin_valorar[0]
        self.dict_resultado[name2] = pareja_sin_valorar[1]

    def combinatoria(self, array1, array2):
        new_array = []
        values = {}
        for a in array1:
            for b in array2:
                new_array.append([a, b])
                values[str([a, b])] = 0
        return new_array, values

if __name__ == '__main__':
    d = ZPT()
    d.get_data()

