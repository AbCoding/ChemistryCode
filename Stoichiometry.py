import BaseCode
import math


class Compound:
    def __init__(self, name, numInReaction):
        self.name = name
        self.num = numInReaction

    def molarmass(self):
        return BaseCode.CalcMolarMass(self.name)


def getMoleMoleRat(MainCompound, DesiredCompound):
    return MainCompound.num / DesiredCompound.num


def Stoichiometry(MainCompound, DesiredOut, TypeOfRatio, InputQuantity):
    # BalancedForm is an array of the balanced eq of the reaction describin
    # MainCompound is a Compound Object describing the main element which we are working with
    # Type of ratio is the Stoichiometric ratio in question

    # Steps:

    # Input Value Given
    if TypeOfRatio == "MassToMass":
        # input mass is the InputQuantity
        molmass = BaseCode.CalcMolarMass(MainCompound.name)
        MolInp = InputQuantity / molmass
        MolOut = MolInp / (getMoleMoleRat(MainCompound, DesiredOut))
        MassOut = MolOut * BaseCode.CalcMolarMass(DesiredOut.name)
        return MassOut
    if TypeOfRatio == "MoleToMole":
        MolOut = InputQuantity / (getMoleMoleRat(MainCompound, DesiredOut))
        return MolOut
    if TypeOfRatio == "MoleToMass":
        MolOut = InputQuantity / (getMoleMoleRat(MainCompound, DesiredOut))
        MassOut = MolOut * BaseCode.CalcMolarMass(DesiredOut.name)
        return MassOut
    if TypeOfRatio == "MassToMole":
        molmass = BaseCode.CalcMolarMass(MainCompound.name)
        MolInp = InputQuantity / molmass
        MolOut = MolInp / (getMoleMoleRat(MainCompound, DesiredOut))
        return MolOut
    if TypeOfRatio == "MoleToParticle":
        MolOut = InputQuantity / (getMoleMoleRat(MainCompound, DesiredOut))
        return BaseCode.MoleParticleCountCalc(MolOut, 3)
    if TypeOfRatio == "MassToParticle":
        molmass = BaseCode.CalcMolarMass(MainCompound.name)
        MolInp = InputQuantity / molmass
        MolOut = MolInp / (getMoleMoleRat(MainCompound, DesiredOut))
        return BaseCode.MoleParticleCountCalc(MolOut, 3)


# MC = Compound("C6H14", 2)
# DO = Compound("O2", 19)
# TOR = "MoleToMole"
# InputQuantity = 7.2
#
# print(Stoichiometry(MC, DO, TOR, InputQuantity))

def CalculateLimitingCompound(ListOfReactants, ListOfMasses, DesiredProduct):
    LimitingMass = 10 ** 10
    LimitingIndex = 0
    for i, e in enumerate(ListOfReactants):
        out = Stoichiometry(e, DesiredProduct, "MassToMass", ListOfMasses[i])
        if out < LimitingMass:
            LimitingMass = out
            LimitingIndex = i
    return [LimitingMass, ListOfReactants[LimitingIndex]]


def CalculateExcessReactant(ListOfReactants, ListOfMasses, DesiredProduct):
    LimitingMass = 10 ** 10
    LimitingIndex = 0
    ListOfExcess = []
    for i, e in enumerate(ListOfReactants):
        out = Stoichiometry(e, DesiredProduct, "MassToMass", ListOfMasses[i])
        if out < LimitingMass:
            LimitingMass = out
            LimitingIndex = i
    for i, e in enumerate(ListOfReactants):
        if i != LimitingIndex:
            # if its not the limiting reactant determine how much reactants would you require
            MassOfR = Stoichiometry(DesiredProduct, e, "MassToMass", LimitingMass)
            ListOfExcess.append([e, MassOfR])
    # Output is a list of 2 item arrays with each subarray containing the data about the excess compound as the first element and its excess mass
    return ListOfExcess


def CalculateExcessReactant_ActualYield(Product, Reactant, ActualYield):
    return Stoichiometry(Reactant, Product, "MassToMass", ActualYield)


def reactionsolver(ListOfReactants, ListOfMasses, Product, ActualYield):
    LimitingReactant = CalculateLimitingCompound(ListOfReactants, ListOfMasses, Product)
    ExcessReactants = CalculateExcessReactant(ListOfReactants, ListOfMasses, Product)
    TheoreticalYield = (LimitingReactant[0])
    ListOfExcess = []
    PercentYeild = ActualYield / TheoreticalYield
    for i, e in enumerate(ListOfReactants):
        if e.name != LimitingReactant[1].name:
            Excess = ListOfMasses[i] - CalculateExcessReactant_ActualYield(e, Product, ActualYield)
            ListOfExcess.append(Excess)
    return [TheoreticalYield, PercentYeild, ListOfExcess]