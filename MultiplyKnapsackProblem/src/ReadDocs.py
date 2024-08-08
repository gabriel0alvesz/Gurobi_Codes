
class ReadDocs:
    """Realiza a leitura do arquivo e retorna:\n
        n = Quantidade de itens\n
        m = Quantidade de mochilas.\n
        b = Lista com a capacidade de cada mochila respectivamente.\n
        p = Lista com os valores de benefício de cada item respectivamente.\n
        w = Lista com os pesos de cada item respectivamente\n
    """    

    def __init__(self):
        self.lines: list
    
    def read_Doc(self, name_doc: str):
        with open(name_doc,'r') as f:
            self.lines = f.readlines()
    
    def tokenizer(self):
        self.lines = [line.strip().split() for line in self.lines]

    def define_Variables(self) -> list:
        n, m = map(int, self.lines[0][0:2]) # n = Quantidade de itens & m = Numero de mochilhas
        b = list(map(float, self.lines[1])) # Capacidades de cada mochila
        
        p = list() # Beneficios
        w = list() # Pesos
        
        for e in range(0, n):
            p.append(float(self.lines[2+e][0]))
            w.append(float(self.lines[2+e][1]))

        return [n, m, b, p, w]

# Para teste de leitura       
if __name__ == "__main__":
    rd = ReadDocs()

    rd.read_Doc("input.txt")
    rd.tokenizer()

    print(rd.define_Variables())