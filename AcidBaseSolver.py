import math

Kw = 1 * 10 ** -14


class AcidBase:
    def __init__(self, Molarity, Volume, strong):
        self.Molarity = Molarity
        self.Volume = Volume
        self.strong = strong

    def GetMoles(self):
        return self.Molarity * self.Volume


def AcidBaseSolver(Acid, Base, Ka=0, Kb=0):
    TotalVol = Acid.Volume + Base.Volume
    Acid.Molarity = Acid.GetMoles() / TotalVol
    Base.Molarity = Base.GetMoles() / TotalVol
    Acid.Volume = TotalVol
    Base.Volume = TotalVol

    if Acid.strong and Base.strong:
        limitingReactant = min(Acid.Molarity, Base.Molarity)
        Acid.Molarity = Acid.Molarity - limitingReactant
        Base.Molarity = Base.Molarity - limitingReactant
        if Base.Molarity == 0:
            Concentration_H3O = Acid.Molarity
            PH = -math.log10(Concentration_H3O)
            return PH
        else:

            Concentration_OH = Base.Molarity
            PH = 14 + math.log10(Concentration_OH)
            return PH

    if not (Acid.strong) and Base.strong:

        if Acid.Molarity == Base.Molarity:
            if Ka and not (Kb):
                Kb = Kw / Ka
            Concentration_OH = math.sqrt(Base.Molarity * Kb)
            PH = 14 + math.log10(Concentration_OH)
            return PH
        else:

            limitingReactant = min(Acid.Molarity, Base.Molarity)
            Acid.Molarity = Acid.Molarity - limitingReactant
            Base.Molarity = Base.Molarity - limitingReactant

            Concentration_H3O = (Ka * Acid.Molarity) / limitingReactant

            PH = -math.log10(Concentration_H3O)

            return PH

    if Acid.strong and not (Base.strong):

        if Acid.Molarity == Base.Molarity:
            if Kb and not (Ka):
                Ka = Kw / Kb
            Concentration_H3O = math.sqrt(Base.Molarity * Ka)
            PH = -math.log10(Concentration_H3O)
            return PH
        else:
            limitingReactant = min(Acid.Molarity, Base.Molarity)
            Acid.Molarity = Acid.Molarity - limitingReactant
            Base.Molarity = Base.Molarity - limitingReactant

            Concentration_OH = (Kb * Base.Molarity) / limitingReactant

            PH = 14 + math.log10(Concentration_OH)

            return PH


Acid = AcidBase(.05, .050, False)
Base = AcidBase(.05, .050, True)

print(AcidBaseSolver(Acid, Base, Kb=1.9 * 10 ** -5))