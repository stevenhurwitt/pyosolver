from pyosolver import PYOSolver
from analytics import simplify_solve
import os

base = os.getcwd()
print(base)
PATH = "pyosolver"
EXECUTABLE = "PYOSOLVER2-edge"


def main():
	directory = "pyosolver/saves/discover"
	convert(directory)

	pyosolver = PYOSolver(PATH, EXECUTABLE)
	print(pyosolver)
	return


def convert(directory_path):
	for name in os.listdir(directory_path):
		if not name.endswith(".cfr"):
			continue
		full_path = directory_path + "\\" + name
		print(full_path)
		simplify_solve(full_path, "IP", directory_path + "\\" + "simplified_" + name)

main()