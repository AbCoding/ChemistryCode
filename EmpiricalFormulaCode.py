import math
import BaseCode
from fractions import Fraction

class Element:
    def __init__(self, ElementName, mass):
        self.name = ElementName
        self.mass = mass
        self.AtomicMass = BaseCode.AtomicMass[ElementName]

    def numMoles(self):
        return self.mass / self.AtomicMass


def CalcEmpericalForm(ListOfElems):
    mcoeff = 1
    listofelem = []
    EmpiricalForm = ""
    m = ListOfElems[0].numMoles()
    for i in ListOfElems:
        m = min(m, i.numMoles())
    for i in ListOfElems:
        number = i.numMoles() / m

        coeff = Fraction(str(number)).limit_denominator(10)
        coeff = coeff.denominator

        if coeff > 1:
            mcoeff = coeff * mcoeff
        elem = [i.name, Fraction(str(number)).limit_denominator(10)]
        listofelem.append(elem)
    for i in listofelem:

        nm = i[0]
        num = int(i[1] * mcoeff)

        if num == 1:
            EmpiricalForm += nm
        else:
            EmpiricalForm += nm + str(num)

    return EmpiricalForm


def CalcChemForm(EmpiricalForm, atomicmass):
    mass = BaseCode.CalcMolarMass(EmpiricalForm)
    return atomicmass / mass


