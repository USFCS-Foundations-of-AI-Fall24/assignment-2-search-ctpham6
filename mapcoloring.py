from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# Instantiate model and solver
antenna_model = cp_model.CpModel()
antenna_solver = cp_model.CpSolver()

## colors: 0: Red, 1: Blue 2: Green
colors = {0 : 'Red',1:'Blue',2:'Green'}

frequencies = {0 : 'f1',1:'f2',2:'f3'}

SF = model.NewIntVar(0,2,'SF')
Alameda = model.NewIntVar(0,2,'Alameda')
Marin = model.NewIntVar(0,2,'Marin')
SanMateo = model.NewIntVar(0,2,'San Mateo')
SantaClara = model.NewIntVar(0,2,'Santa Clara')
ContraCosta = model.NewIntVar(0,2,'Contra Costa')
Solano = model.NewIntVar(0,2,'Solano')
Napa = model.NewIntVar(0,2,'Napa')
Sonoma = model.NewIntVar(0,2,'Sonoma')

# Antenna 1 is adjacent to 2,3 and 4.
# Antenna 2 is adjacent to 1, 3, 5, and 6
# Antenna 3 is adjacent to 1, 2, 6, and 9
# Antenna 4 is adjacent to 1, 2, and 5.
# Antenna 5 is adjacent to 2 and 4
# Antenna 6 is adjacent to 2, 7 and 8
# Antenna 7 is adjacent to 6 and 8
# Antenna 8 is adjacent to 7 and 9
# Antenna 9 is adjacent to 3 and 8

Antenna1 = model.NewIntVar(0,2, "A1")
Antenna2 = model.NewIntVar(0,2, "A2")
Antenna3 = model.NewIntVar(0,2, "A3")
Antenna4 = model.NewIntVar(0,2, "A4")
Antenna5 = model.NewIntVar(0,2, "A5")
Antenna6 = model.NewIntVar(0,2, "A6")
Antenna7 = model.NewIntVar(0,2, "A7")
Antenna8 = model.NewIntVar(0,2, "A8")
Antenna9 = model.NewIntVar(0,2, "A9")

## add edges
model.Add(SF != Alameda)
model.Add(SF != Marin)
model.Add(SF != SanMateo)
model.Add(ContraCosta != Alameda)
model.Add(Alameda != SanMateo)
model.Add(Alameda != SantaClara)
model.Add(SantaClara != SanMateo)
model.Add(Marin != Sonoma)
model.Add(Sonoma != Napa)
model.Add(Napa != Solano)
model.Add(Solano != ContraCosta)
model.Add(ContraCosta != Marin)



status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("SF: %s" % colors[solver.Value(SF)])
    print("Alameda: %s" % colors[solver.Value(Alameda)])
    print("Marin: %s" % colors[solver.Value(Marin)])
    print("Contra Costa: %s" % colors[solver.Value(ContraCosta)])
    print("Solano: %s" % colors[solver.Value(Solano)])
    print("Sonoma: %s" % colors[solver.Value(Sonoma)])
    print("Santa Clara: %s" % colors[solver.Value(SantaClara)])
    print("San Mateo: %s" % colors[solver.Value(SanMateo)])
    print("Napa: %s" % colors[solver.Value(Napa)])


