import BaseCode
import math


class Compound:
    def __init__(self, name, numInReaction):
        self.name = name
        self.num = numInReaction


def getMoleMoleRat(RCompound, PCompound):
    return RCompound.num / PCompound.num


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
