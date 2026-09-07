from pydantic import BaseModel
from pydantic import BaseModel, Field
from typing import Literal
from configs.constants import maturities

class GetExchangeRateParams(BaseModel):
    currency: str
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")
    reference_currency: str = "EUR"
    variation: Literal["A", "E"] = "A"
    spot_rate:str = "SP00" 
    frequency: Literal["D", "M", "Q", "Y"] = "D"

class GetInterestRateParams(BaseModel):
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")
    frequency: Literal["D", "M"] = "D"
    area: Literal["U2","U3","PL"] = "U2"
    currency:str = "EUR"
    rate: Literal["DFR", "MRO", "MLF"] = "DFR"
    measure: Literal["LEV","PC_PA"] = "LEV"

class GetYieldCurveParams(BaseModel):
    area: Literal["U2", "U3", "PL"] = "U2"
    currency: str = "EUR"
    measure: Literal["SV_C_YM"] = "SV_C_YM"
    maturity: Literal["SR_3M","SR_6M","SR_1Y","SR_2Y","SR_5Y","SR_10Y","SR_30Y"] = "SR_3M"
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")

class GetBasicFinancialsParams(BaseModel):
    symbol: str
    metric: Literal["all","currentRatio","salesPerShare","netMargin","10DayAverageTradingVolume","52WeekHigh","52WeekLow","52WeekLowDate", "52WeekPriceReturnDaily"] = "all"