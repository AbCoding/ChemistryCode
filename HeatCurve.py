def MeltingandVapor(m, Cs):
    return m * Cs


def TempIncrease(m, Cs, Ti, Tf):
    DeltaT = Tf - Ti
    return m * Cs * DeltaT


# make the temp thing work properly
def SigmaQ(InitialTemp, FinalTemp, Mass, SpecificHeat_Solid=0, SpecificHeat_Liquid=0, SpecificHeat_Gas=0,
           SpecificHeat_Melt=0, SpecificHeat_Boil=0, MeltPoint=0, BoilPoint=0):
    seg1 = TempIncrease(m=Mass, Cs=SpecificHeat_Solid, Ti=InitialTemp, Tf=MeltPoint)
    seg2 = MeltingandVapor(m=Mass, Cs=SpecificHeat_Melt)
    seg3 = TempIncrease(m=Mass, Cs=SpecificHeat_Liquid, Ti=max(MeltPoint, InitialTemp), Tf=min(BoilPoint, FinalTemp))
    seg4 = MeltingandVapor(m=Mass, Cs=SpecificHeat_Boil)
    seg5 = TempIncrease(m=Mass, Cs=SpecificHeat_Gas, Ti=max(BoilPoint, InitialTemp), Tf=FinalTemp)

    return seg1 + seg2 + seg3 + seg4 + seg5


# v = SigmaQ(InitialTemp=99.999, FinalTemp=100, Mass=1000000, SpecificHeat_Liquid=4.187, MeltPoint=0, BoilPoint=100)
# print(v)

