from enum import Enum

class Variation(str, Enum):
    ANNUAL = "A"
    ENDOFYEAR = "E"

class Period(str,Enum):
    DAILY= "1d"
    FIVEDAYS="5d"
    MONTH="1mo" 
    THREEMONTH="3mo"
    HALFYEAR="6mo" 
    YEAR="1y"
    TWOYEAR="2y"
    FIVEYEAR="5y"
    TENYEAR="10y"  

class Interval(str,Enum):
    DAILY= "1d"
    MONTH="1mo" 
    HALFYEAR="6mo"

class Frequency(str, Enum):
    DAILY = "D"
    MONTH = "M"
    QUARTER = "Q"
    YEAR = "A"


class InterestRate(str, Enum):
    DFR = "DFR"
    MLFR = "MLFR"
    MRR_FR = "MRR_FR"
    MRR_RT = "MRR_RT"
    MRR_MBR = "MRR_MBR"


class Measure(str, Enum):
    LEVEL = "LEV"
    CHANGE = "CHG"


class YieldCurveInstrument(str, Enum):
    G_N_A = "G_N_A"
    G_N_C = "G_N_C"


class Maturity(str, Enum):
    SR_3M = "SR_3M"
    SR_6M = "SR_6M"
    SR_1Y = "SR_1Y"
    SR_2Y = "SR_2Y"
    SR_5Y = "SR_5Y"
    SR_10Y = "SR_10Y"
    SR_30Y = "SR_30Y"
