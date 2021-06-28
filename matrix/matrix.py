# Matrix class
class Matrix:
  def __init__(self, m, n):
    self.rows = m
    self.cols = n
    self.purifString = ""

    self.grid = []
    for i in range(self.rows):
      self.grid.append([])
      for j in range(self.cols):
        self.grid[i].append(1)

  def addZero(self, m, n):
    self.grid[m-1][n-1] = 0

  def show(self):
    print("Displaying {}x{} matrix:".format(self.rows, self.cols))
    for i in range(0, self.rows):
      print(self.grid[i])

  def purify(self):
    maxQty = 0
    _type = 0
    pos = 0
    # Check rows
    for i in range(self.rows):
      rowQty = 0
      for j in range(self.cols):
        if self.grid[i][j] == 0:
          rowQty += 1
      if rowQty > maxQty:
        maxQty = rowQty
        _type = 1
        pos = i+1
    
    # Check cols
    for i in range(self.cols):
      colQty = 0
      for j in range(self.rows):
        if self.grid[j][i] == 0:
          colQty += 1
      if colQty > maxQty:
        maxQty = colQty
        _type = 2
        pos = i+1
    
    # Execute chop()
    if maxQty > 0:
      self.chop(_type, pos)
      self.purifString += "{} {}\n".format(_type, pos)
      self.purify()
    else:
      return self.purifString

  def chop(self, _type, pos):
    if _type == 1:
      for j in range(0, self.cols):
        self.grid[pos-1][j] = 1
    else:
      for i in range(0, self.rows):
        self.grid[i][pos-1] = 1
        

# Fetching data from file
inp_file = open("input1.txt", "r")
inp_data = inp_file.readlines()
inp_file.close()

dims = inp_data[0].split(" ")
M = int(dims[0])
N = int(dims[1])

K = int(inp_data[1])

# Creating matrix
matrix = Matrix(M, N)
for i in range(2, K+2):
  coords = inp_data[i].split(" ")
  matrix.addZero(int(coords[0]), int(coords[1]))

# Executing purify()
matrix.purify()
changelog = matrix.purifString
result = str(changelog.count("\n")) + "\n" + changelog

# Output
outp_file = open("output.txt", "w")
outp_file.write(result)
outp_file.close()
