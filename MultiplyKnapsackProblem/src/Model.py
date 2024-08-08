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
        sum = gp.quicksum(benefits[i] * self.x[i,j] for i in range(0,n) for j in range)
        self.model.setObjective(sum, GRB.MAXIMIZE)

    def constraints(self, n: int, m: int):
        # Unanidade dos intens na mochila. -> teste
        for i in range(n):
            expr = gp.LinExpr()
            for j in range(m):
                expr = expr + self.x[i, j]
                self.model.addConstr(expr <= 1, name=f"item_{i}")

