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


def LightUI():
    Operation = input(
        "What Operation would you like to do[1=getWavelength,2=getFreq,3=getPhoton,4=getPhotonCount]: "
    )
    if Operation == 1:
        inp = input("Whats the Frequency")
        print(getWavelength(inp))
    elif Operation == 2:
        inp = input("Whats the WaveLength")
        print(getFrequency(inp))

    return 2


LightUI()
