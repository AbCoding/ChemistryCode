import math
import BaseCode


def CelsiusToKelvin(temp):
    return temp + 273


def GetPressure(area, force):
    return force / area


def GasLaws(P1=False, P2=False, V1=False, V2=False, T1=False, T2=False, n1=False, n2=False):
    if P1 == "out":
        if V1 and T2:
            return (P2 * V2 * T1) / (V1 * T2)
        elif V1 and V2:
            return (P2 * V2) / (V1)
        else:
            print("Error")
            return None
    if P2 == "out":
        if V1 and T2:
            return (P1 * V1 * T2) / (V2 * T1)
        elif V1 and V2:
            return (P1 * V1) / (V2)
        else:
            return None

    if V1 == "out":
        if P1 and T1:
            return (P2 * V2 * T1) / (T2 * P1)
        if T1 and T2:
            return (V2 * T1) / (T2)
        if P1 and P2:
            return (P2 * V2) / P1
        if n1 and n2:
            return (V2 * n1) / n2
    if V2 == "out":
        if P1 and T1:
            return (P1 * V1 * T2) / (T1 * P2)
        if T1 and T2:
            return (V1 * T2) / (T1)
        if P1 and P2:
            return (P1 * V1) / P2
        if n1 and n2:
            return (V1 * n2) / n1
