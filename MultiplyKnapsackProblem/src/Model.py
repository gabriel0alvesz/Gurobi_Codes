from ReadDocs import ReadDocs
import gurobipy as gp
from gurobipy import GRB
import sys

class Model:
    """Cria o modelo de otimização linear inteira para o problema das multiplas mochilas
    """    

    def __init__(self):
        self.model = gp.Model()
    
    def create_decision_variables(self, n: int, m: int):
        self.x = self.model.addVars(n, m, vtype=GRB.BINARY, name='x')
        
    def define_objective(self, n: int, m: int, benefits: list):
        sum = gp.quicksum(self.x[i,j] * benefits[i] for i in range(0,n) for j in range(m))
        self.model.setObjective(sum, GRB.MAXIMIZE)

    def constraints(self, n: int, m: int, capacity:list,  weights: list):
        # Unicidade dos itens nas mochilas.
        for i in range(n):
            expr = gp.LinExpr()
            for j in range(m):
                expr = expr + self.x[i, j]
            self.model.addConstr(expr <= 1, name=f"item{i}")
            
        # Capacidade de cada mochila
        for j in range(m):
            expr = gp.LinExpr()
            for i in range(n):
                expr = expr + (self.x[i, j] * weights[i])
            self.model.addConstr(expr <= capacity[j], name=f"backpack{j}")
    
    def optimize_model(self):
        self.model.optimize()
    
    def print_result(self, n: int, m: int):
        if(self.model.Status == GRB.OPTIMAL):
            print("---------------------------------------------------")
            print("Solução Ótima")
            print("---------------------------------------------------")

        print(f"Valor da Função Objetivo: {self.model.objVal}")  
        self.print_items(n, m)


    def print_items(self, n: int, m: int):
        for j in range(m):
            items_bp = list()
            
            for i in range(n):    
                if self.x[i,j].X == 1: items_bp.append(i+1)
            print(f"Itens na Mochila {j}: {items_bp}")
        

if __name__ == "__main__":
    
    rd = ReadDocs()

    try:
        rd.read_Doc(sys.argv[1])
    except:
        print("---Erro ao abrir o arquivo!---")
        exit()
    
    rd.tokenizer()
    lines = rd.define_Variables()

    model = Model()
    model.create_decision_variables(n=lines[0], m=lines[1])
    model.define_objective(n=lines[0], m=lines[1], benefits=lines[3])
    model.constraints(n=lines[0], m=lines[1], capacity=lines[2], weights=lines[4])
    model.optimize_model()

    model.print_result(n=lines[0], m=lines[1])