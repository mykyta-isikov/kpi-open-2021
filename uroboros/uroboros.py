import time
start_time = time.time()

# Fetching data from input file
inp_file = open("input2.txt", "r")
inp_contents = inp_file.readlines()
inp_file.close()

# Functions
def checkSlice(inp):
  mutQty = 0
  for i in range(0, len(inp)):
    if inp[i] == oriC[i]:
      pass
    else:
      mutQty += 1
  return False if mutQty > L else True

# Input formatting
firstRow = inp_contents[0].split(" ")
L = int(firstRow[0])
oriC = firstRow[1]
dna = inp_contents[1]

# Seeking for similars
simPointer = []

for pointer in range(0, len(dna)-len(oriC)+2):
  dnaSlice = dna[pointer:pointer+len(oriC)-1]

  status = pointer if checkSlice(dnaSlice) else -1

  if status != -1:
    simPointer.append(pointer)


# Output
outputString = ""
for item in simPointer:
  outputString += str(item) + " "

outp_file = open("output.txt", "w")
outp_file.write(outputString)
outp_file.close()

print("--- {} seconds ---".format(time.time() - start_time))