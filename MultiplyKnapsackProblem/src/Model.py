from ReadDocs import ReadDocs
import gurobipy as gp
from gurobipy import GRB
import sys as s

class Model:

    def __init__(self, args: str ):
        self.model = gp.Model()
    
    def create_decision_variables(self, n: int, m: int):
        self.x = self.model.addVars(n, m, vtype=GRB.BINARY, name='x')
        
    def define_objective(self, n: int, m: int, benefits: list):
        sum = gp.quicksum(self.x[i,j] * benefits[i] for i in range(0,n) for j in range)
        self.model.setObjective(sum, GRB.MAXIMIZE)

    def constraints(self, n: int, m: int, weights: list):
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
                self.model.addConstr(expr <= 1, name=f"backpack{j}")
    
    def optimize_model(self):
        self.model.optimize()
    
    def print_objetive_function(self, n: int, m: int):
        # -> Como verificar se o modelo foi otimo?
        print("---------------------------------------------------")
        print("Solução Ótima")
        print("---------------------------------------------------")
        print(f"Valor da função objetivo: {self.model.ObjVal}")
        
        self.print_items(n, m)

        
    def print_items(self, n: int, m: int):
        for j in range(m):
            items_bp = list()
            
            for i in range(n):    
                if self.x[i,j].x == 1: items_bp.append(i+1)
            print(f"Itens na Mochila {j}: {items_bp}")
        
