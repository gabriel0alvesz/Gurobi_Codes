
class ReadDocs:

    def __init__(self):
        self.lines: list
    
    def read_Doc(self, name_doc: str):
        with open(name_doc,'r') as f:
            self.lines = f.readlines()
    
    def tokenizer(self):
        self.lines = [line.strip().split() for line in self.lines]

    def define_Variables(self) -> list:
        n, m = map(int, self.lines[0][0:2])
        b = list(map(float, self.lines[1])) # capacidades de cada mochila
        
        p = list() # beneficios
        w = list() # pesos
        
        for e in range(0, n):
            
            p.append(self.lines[2+e][0])
            w.append(self.lines[2+e][1])

        return [n, m, p, w]
       
if __name__ == "__main__":
    rd = ReadDocs()

    rd.read_Doc("input.txt")

    rd.tokenizer()

    print(rd.define_Variables())