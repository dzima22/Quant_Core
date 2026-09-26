from datetime import date
from pydantic import BaseModel, Field, field_validator,model_validator
from typing import Literal
import re

class GetDailyExchangeRateParams(BaseModel):
    currency: str
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")
    reference_currency: str = "EUR"
    @field_validator("start_date", "end_date")
    @classmethod
    def validate_date_format(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError(
                "Date must be in YYYY-MM-DD format"
            )

        return value

class GetPeriodExchangeRateParams(BaseModel):
    currency: str
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")
    reference_currency: str = "EUR"
    variation: Literal["A", "E"] = "A"
    frequency: Literal["M", "Q", "A"]
    @model_validator(mode="after")
    def validate_period_format(self):
        patterns = {
            "M": r"^\d{4}-(0[1-9]|1[0-2])$",
            "Q": r"^\d{4}-Q[1-4]$",
            "A": r"^\d{4}$"}
        pattern = patterns[self.frequency]
        for field in ("start_date", "end_date"):
            value = getattr(self, field)

            if not re.fullmatch(pattern, value):
                raise ValueError(
                    f"{field} must be in the correct format for "
                    f"frequency '{self.frequency}'"
                )
        return self


class GetInterestRateParams(BaseModel):
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")
    frequency: Literal["D"] = "D"
    currency:str = "EUR"
    rate: Literal["DFR", "MLFR", "MRR_FR","MRR_RT","MRR_MBR"] = "DFR"
    measure: Literal["LEV","CHG"] = "LEV"
    @field_validator("start_date", "end_date")
    @classmethod
    def validate_date_format(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError(
                "Date must be in YYYY-MM-DD format"
            )

        return value
    @model_validator(mode="after")
    def validate_measure(self):
        if self.rate in {"MRR_FR", "MRR_RT", "MRR_MBR"} and self.measure == "CHG":
            raise ValueError(
                f"measure='CHG' is not available for rate='{self.rate}'"
            )

        return self

class GetYieldCurveParams(BaseModel):
    currency: str = "EUR"
    instrument: Literal["G_N_A", "G_N_C"] = "G_N_A"
    maturity: Literal["SR_3M","SR_6M","SR_1Y","SR_2Y","SR_5Y","SR_10Y","SR_30Y"] = "SR_3M"
    start_date: str = Field(alias="startPeriod")
    end_date: str = Field(alias="endPeriod")
    @field_validator("start_date", "end_date")
    @classmethod
    def validate_date_format(cls, value: str) -> str:
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError(
                "Date must be in YYYY-MM-DD format"
            )

        return value

class GetBasicFinancialsParams(BaseModel):
    symbol: str

class GetUSASpeandingPlusLobbingParams(BaseModel):
    symbol: str
    from_: str
    to: str 

class YachooSymbol(BaseModel):
    symbol: str

class YachooGetHistory(BaseModel):
    symbol: str
    period: str = "1y"
    interval: str = "1d"