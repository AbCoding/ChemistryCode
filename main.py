import BaseCode
from Stoichiometry import *
import  EmpiricalFormulaCode
import LightCode
import  HeatCurve
import GasLaws
import AcidBaseSolver
InputElement= "C6H12O6"
print("The mass of "+ InputElement+ " is " + str(BaseCode.CalcMolarMass(InputElement)))

MC = Compound("C6H14", 2)
DO = Compound("O2", 19)
TOR = "MoleToMole"
InputQuantity = 7.2

print(Stoichiometry(MC, DO, TOR, InputQuantity))



# def AskStoichiometry():
#   MainCompoundName= input("enter the compound for which you have a given measurement: ")
#   MainCompoundVal= int(input("Enter the coefficent for the known compound: "))
#   DesiredCompoundName= input("enter the compound which you want to calculate: ")
#   DesiredCompoundVal= int(input("Enter the coefficent for the desired compound: "))
#   TypeOfRatio= input("enter the type of ratio which you are converting between: ")
#   InputQuantity=float( input("enter the known measurement of the base compound in either moles or grams: "))
#   MC= Stoichiometry.Compound(MainCompoundName,MainCompoundVal)
#   DO= Stoichiometry.Compound(DesiredCompoundName,DesiredCompoundVal)
#   v= Stoichiometry.Stoichiometry(MC,DO,TypeOfRatio,InputQuantity)
#   print("The Amount of Desired Compound is:")
#   print(v)

# def LightUI():
#     Operation = int(input(
#         "What Operation would you like to do[1=getWavelength,2=getFreq,3=getPhoton,4=getPhotonCount]: "
#     ))
#     if Operation == 1:
#         inp = float(input("Whats the Frequency: "))
#         print(LightCode.getWavelength(inp))
#     elif Operation == 2:
#         inp = float(input("Whats the WaveLength: "))
#         print(LightCode.getFrequency(inp))
#     elif Operation == 3:
#         inp = float(input("Whats the Frequency: "))
#         print(LightCode.getPhotonEnergy(inp))
#     elif Operation == 4:
#         inp = float(input("Whats the Photon Energy: "))
#         inp2= float(input("Whats the Pulse Energy: "))
#         print(LightCode.getNumPhotons(inp,inp2))

# # LightUI()
# # AskStoichiometry()
# # # MC = Stoichiometry.Compound("NO2", 2)
# # # DO = Stoichiometry.Compound("HNO3", 2)
# # # TOR = "MassToMass"
# # # InputQuantity = 1.6*10**4
# # # print(BaseCode.CalcMolarMass(MC.name))
# # # print(BaseCode.CalcMolarMass(DO.name))
# # # print(Stoichiometry.Stoichiometry(MC, DO, TOR, InputQuantity))

# # molmass=BaseCode.CalcMolarMass("N2O4")
# # molmass1=BaseCode.CalcMolarMass("N2")
# # molmass2=BaseCode.CalcMolarMass("O4")
# # ans1=print(molmass1/molmass)
# # ans= print(molmass2/molmass)

# # listOfElements=[EmpiricalForm.Element("K",100*.287),EmpiricalForm.Element("H",100*(.015)),EmpiricalForm.Element("P",100*(.228)),EmpiricalForm.Element("O",100*(.47))]
# # em= EmpiricalForm.CalcEmpericalForm(listOfElements)
# # print(em)
# mass=.630
# CompoundsInMixture=["CaCO3","SiO2"]
# KnownElements=[BaseCode.Element("Co",.630)]
# for i in KnownElements:
#   print(i)

