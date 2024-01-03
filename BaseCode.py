import math
class Element:
    def __init__(self, ElementName, mass):
        self.name = ElementName
        self.mass = mass
        self.AtomicMass = AtomicMass[ElementName]

    def numMoles(self):
        return self.mass / self.AtomicMass
AtomicMass = {
    "H": 1.00784,
    "He": 4.0026,
    "Li": 6.941,
    "Be": 9.0122,
    "B": 10.811,
    "C": 12.0107,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.9984,
    "Ne": 20.1797,
    "Na": 22.9897,
    "Mg": 24.305,
    "Al": 26.9815,
    "Si": 28.0855,
    "P": 30.9738,
    "S": 32.065,
    "Cl": 35.453,
    "Ar": 39.9428,
    "K": 39.0983,
    "I": 126.904,
    "Ni": 58.6934,
    "Cu": 63.546,
    "Mn": 54.938044,
    "Br": 79.904,
    "Ca": 40.078,
    "Xe": 131.294,
    "Ce": 140.116,
    "Cs": 132.90545,
    "Tl": 204.3833,
    "Co": 58.933195,
    "As": 74.9216,
    "Cd": 112.411,
    "Ba":137.327,
    "Ti":47.867,
  "Fe":55.845
}

def calcRelativeAbundance(ListOfMass, ListOfPercents):
    SumOfValues = 0
    for i in range(len(ListOfMass)):
        SumOfValues += ListOfMass[i] * ListOfPercents[i]
    return SumOfValues


def MoleParticleCountCalc(numMoles, sigFig):
    AvNum = 6.022
    tmpan = AvNum * numMoles
    b = math.floor(math.log10(tmpan))
    a = (tmpan / (10 ** b))
    tmpan = round(a, (sigFig - 1))
    return tmpan, 23 + b


def CalcMolarMass(chemical):
    mass = 0
    i = 0

    while i < (len(chemical)):
        if not chemical[i].isdigit():

            if chemical[i] == "(":
                MolStr = ""
                j = 1
                while chemical[i + j] != ")":
                    MolStr += chemical[i + j]

                    j += 1

                if (chemical[i + j + 1]).isdigit():
                    mass += CalcMolarMass(MolStr) * int(chemical[i + j + 1])

                    i += j + 2

                else:
                    i += j + 1
                if i >= len(chemical):

                    return mass

            if i < len(chemical) - 1:
                if chemical[i + 1].isdigit():
                    j = 1
                    TempStr = ''
                    while (i + j) < (len(chemical)) and chemical[i + j].isdigit():
                        TempStr += chemical[i + j]
                        j += 1
                    mass = mass + AtomicMass[chemical[i]] * int(TempStr)

                else:
                    tmpStr = chemical[i]
                    tmpStr += chemical[i + 1]
                    if tmpStr in AtomicMass:
                        if i < len(chemical):
                            j = 2
                            TempStr = ''
                            while i + j <= len(chemical) - 1 and chemical[i + j].isdigit():
                                TempStr += chemical[i + j]
                                j += 1
                            if TempStr != '':
                                mass = mass + AtomicMass[tmpStr] * int(TempStr)
                            else:
                                mass = mass + AtomicMass[tmpStr]
                            i += 1
                    else:
                        mass += AtomicMass[chemical[i]]
            else:
                mass += AtomicMass[chemical[i]]

        i += 1
    return mass





def ElementalAnalysis(mass,CompoundsInMixture,KnownElements):
  for i in KnownElements:
    v=i.numMoles()

    for j in CompoundsInMixture:
      if i.name in j:
        m= CalcMolarMass(j)
        print(m*v/mass*100)
  return 1