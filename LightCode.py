import math


def getWavelength(Freq):
    SpeedOfLight = 3 * (10 ** 8)
    return SpeedOfLight / Freq


def getFrequency(WaveLength):
    SpeedOfLight = 3 * (10 ** 8)
    return SpeedOfLight / WaveLength


def getPhotonEnergy(Frequency):
    PlanksConstnat = 6.62607004 * 10 ** (-34)

    return PlanksConstnat * Frequency


def getNumPhotons(PhotonEnergy, PulseEnergy):
    return PulseEnergy / PhotonEnergy


def ToScientificNotation(num, sigFigs):
    exp = math.floor(math.log10(num))
    tmpnum = num / (10 ** exp)
    tmpnum = round(tmpnum, (sigFigs - 1))
    return (str(tmpnum) + "*10^{}".format(exp))





