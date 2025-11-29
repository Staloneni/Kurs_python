import csv

class FileHandler:
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.transformations = transformations
        self.data = self.load_data()
    
    def load_data(self):
        with open(self.input_file) as file:
            reader = csv.reader(file, delimiter=",")
            temp_matrix = []
            print("Wczytana zawartość pliku:")
            for row in reader:
                temp_matrix.append(row)
                print(row)
                
        return temp_matrix
    
    def save_data(self):
        with open(self.output_file, mode="w+") as file:
            writer = csv.writer(file)
            print("Zapisana zawartość pliku:")  
            for row in self.data:
                writer.writerow(row)
                print(row)
                
    def do_transformations(self):
        for transformation in self.transformations:
            x, y, value = transformation.split(",")
            x, y = int(x), int(y)
            self.data[y][x] = value

