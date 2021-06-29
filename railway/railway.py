import time
import tracemalloc
start_time = time.time()
tracemalloc.start()

# Classes
class Kasa():
  def __init__(self):
    self.prevOrder = -1
    self.totalCash = 0
  
  def order(self, destination):
    if self.prevOrder == destination:
      self.totalCash += prices[destination] * 0.8
    else:
      self.totalCash += prices[destination]
    self.prevOrder = destination

# Fetching data from file
inp_file = open("input1.txt", "r")
inp_contents = inp_file.readlines()
inp_file.close()

nums = inp_contents[0].split(" ")
n = int(nums[0])
m = int(nums[1])
k = int(nums[2])

destinations = []
prices = []
for i in range(1, k+1):
  destItem = str(inp_contents[i].split(" ")[0]).strip("\n")
  priceItem = int(inp_contents[i].split(" ")[1])
  destinations.append(destItem)
  prices.append(priceItem)

ticketOrder = []
for i in range(k+1, k+1+n):
  ticketOrder.append(str(inp_contents[i]).strip("\n"))

# Functions
def calculateSum(sequence):
  result = 0
  kasa = []
  for i in range(0, m):
    kasa.append([])
  for i in range(0, n):
    kasa[int(sequence[i])].append(i)

  for item in kasa:
    temp = Kasa()
  
    for i in range(0, len(item)):
      currentDest = -1
      for x in range(0, k):
        if ticketOrder[item[i]] == destinations[x]:
          currentDest = x
          continue
      temp.order(currentDest)
    result += temp.totalCash
  return result

# Body
## Declaring minimum values
minString = ""
for i in range(0, n):
  minString += "0"
minSum = calculateSum(minString)

## Seeking all combinations
for i in range(0, pow(m, n)):
  variantString = ""
  variant = i
  for y in range(0, n):
    variantString += str(variant % m)
    variant = variant // m
  
  currentSum = calculateSum(variantString)
  if currentSum < minSum:
    minSum = currentSum
    minString = variantString
  
# Output
sequence = ""
for char in minString:
  sequence += str(int(char)+1) + "\n"
result = str(round(minSum, 1)) + "\n" + sequence

outp_file = open("output.txt", "w")
outp_file.write(result)
outp_file.close()

print("--- {} seconds ---".format(time.time() - start_time))
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
