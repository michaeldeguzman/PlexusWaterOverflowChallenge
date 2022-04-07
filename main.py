class Glass:
    def __init__(self):
        self.capacity = 250
        self.content = 0

class GlassInPile(Glass):
    def __init__(self, rowNumber, glassNumber):
        super().__init__()
        self.rowNumber = rowNumber
        self.glassNumber = glassNumber
        self.rateToFill = 0

class Water:
    def __init__(self, volume):
        self.volume = volume 

### input variables ##########
print("Please enter water volume (ml):")
waterVolume = input()
waterVolume = int(waterVolume)

print("Please enter Glass Number: ")
gNumber = input()
gNumber = int(gNumber)

print("Please enter Row #:")
rNumber = input()
rNumber = int(rNumber)
##############################

# Initialize water
water = Water(waterVolume)

# LIMITATION (for now):  If rows > 4, the rate for the inner glass to become full is inaccurate
rows = 4
fullRate = 100

### Form the Glass Pyramid ###
pile = []
leafRate = 0

print('*** Glass Pile Content ***')
for rowNumber in range(rows):

    arr = []

    # Compute for the rate the glass becomes full for the outer glasses
    if(rowNumber == 0):
        leafRate = fullRate
    else:
        leafRate = (leafRate) / 2

    # Compute for the rate the glass becomes full for the inner glasses
    insideRate = leafRate * rowNumber
        
    for glassNumber in range(rowNumber + 1):
        g = GlassInPile(rowNumber, glassNumber)

        #compute the rateToFill for leaf glasses
        if(glassNumber == 0 or glassNumber == rowNumber):
            g.rateToFill = leafRate
        else:
            g.rateToFill = insideRate
        #print('Rate to fill:',g.rateToFill)

        if(g.capacity * (rowNumber + 1)) <= water.volume:
            g.content = g.capacity
        else:
            availableCapacity = g.capacity * (g.rateToFill/100)

            if(availableCapacity <= water.volume):
                g.content = availableCapacity
            else:
                g.content = water.volume

        water.volume = water.volume - g.content

        print("Row #=", g.rowNumber, 'Glass #=', g.glassNumber, ' Rate=', g.rateToFill, "%", 'Content=', g.content)

        arr.append(g)
        #print("Row #=", g.rowNumber, 'Glass #=', g.glassNumber, ' Rate=', g.rateToFill, "%")
        #print('----')

    pile.append(arr)

print('*** End of Content ***')
print()
print("ANSWER:  Glass Number", gNumber, " at row ", rNumber," has ", pile[rNumber][gNumber].content," ml")

